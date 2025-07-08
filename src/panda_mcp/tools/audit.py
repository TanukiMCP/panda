"""
PandA Audit - Cognitive Audit Framework Enhancement for LLMs

This tool provides a single atomic interface that enhances LLM audit capabilities
by offering structured cognitive audit frameworks and systematic investigation guidance.
The LLM drives the audit process, and this tool provides the framework and structure.

Following MCP principles: LLM = DRIVER, Tool = VEHICLE
"""

from typing import Any, Dict, List, Optional
import re
import json
import os
import importlib.util
from pathlib import Path

class PandaAudit:
    """Single atomic audit tool that enhances LLM audit capabilities with cognitive frameworks."""
    
    def __init__(self):
        """Initialize the audit tool by dynamically loading cognitive audit frameworks."""
        self.frameworks = self._load_frameworks()
        # Keep legacy automated analysis for backward compatibility
        self.legacy_frameworks = self._load_legacy_frameworks()
    
    def _load_frameworks(self) -> Dict[str, Any]:
        """Dynamically load cognitive audit frameworks from the audit_frameworks directory."""
        frameworks = {}
        frameworks_dir = Path(__file__).parent.parent / "audit_frameworks"
        
        for file_path in frameworks_dir.glob("*.py"):
            if file_path.name.startswith("__") or file_path.name == "base.py":
                continue

            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(
                f"panda_mcp.audit_frameworks.{module_name}", file_path
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Framework name is the module name
                framework_name = module_name
                # The framework data is a variable with the same name
                if hasattr(module, framework_name):
                    frameworks[framework_name] = getattr(module, framework_name)

        return frameworks
    
    def _load_legacy_frameworks(self) -> Dict[str, Any]:
        """Load legacy pattern-based frameworks for backward compatibility."""
        legacy_frameworks = {}
        legacy_dir = Path(__file__).parent.parent / "auditing_frameworks"
        
        if legacy_dir.exists():
            for file_path in legacy_dir.glob("*.py"):
                if file_path.name.startswith("__") or file_path.name == "base.py":
                    continue

                module_name = file_path.stem
                try:
                    spec = importlib.util.spec_from_file_location(
                        f"panda_mcp.auditing_frameworks.{module_name}", file_path
                    )
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        
                        framework_name = module_name.replace("_framework", "")
                        if hasattr(module, f"{framework_name}_framework"):
                            legacy_frameworks[framework_name] = getattr(module, f"{framework_name}_framework")
                except Exception:
                    # Skip legacy frameworks that fail to load
                    pass
        
        return legacy_frameworks
    
    async def enhance_audit(
        self,
        audit_objective: str,
        framework: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        phase: Optional[str] = None,
        evidence_collected: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Enhance LLM audit capabilities with structured cognitive frameworks and investigation guidance.
        
        Args:
            audit_objective: The LLM's audit objective or investigation question
            framework: Optional framework to apply (security_audit, compliance_audit, etc.)
            context: Optional additional context about the audit scope and target
            phase: Optional current audit phase (planning, information_gathering, etc.)
            evidence_collected: Optional list of evidence collected in previous phases
            
        Returns:
            Dictionary with framework guidance, investigation questions, and progress tracking
        """
        try:
            result = {
                "status": "success",
                "objective_analysis": self._analyze_objective(audit_objective),
                "progress_tracking": self._track_audit_progress(phase, evidence_collected),
                "available_frameworks": list(self.frameworks.keys())
            }
            
            # Apply specific framework if requested
            if framework and framework in self.frameworks:
                result["framework_guidance"] = self._apply_framework(framework, audit_objective, context, phase)
            else:
                # Suggest appropriate framework based on audit objective
                result["framework_suggestions"] = self._suggest_frameworks(audit_objective)
            
            # Add context analysis if provided
            if context:
                result["context_analysis"] = self._analyze_audit_context(context)
            
            # Add evidence tracking if provided
            if evidence_collected:
                result["evidence_summary"] = self._summarize_evidence(evidence_collected)
            
            return result
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Audit enhancement failed: {str(e)}"
            }
    
    # Legacy method for backward compatibility
    async def analyze_content(
        self,
        content: str,
        analysis_type: str = "quality",
        context: Optional[Dict[str, Any]] = None,
        focus_areas: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Legacy content analysis method maintained for backward compatibility."""
        try:
            return {
                "status": "success",
                "analysis_type": analysis_type,
                "content_type": self._detect_content_type(content, context),
                "content_metrics": self._calculate_content_metrics(content),
                "findings": [],  # Legacy pattern matching disabled
                "summary": {
                    "total_findings": 0,
                    "by_category": {},
                    "by_severity": {},
                    "recommendations": [
                        "Consider using the new cognitive audit framework approach with enhance_audit method",
                        "Use structured investigation methodologies for professional auditing"
                    ]
                },
                "migration_notice": "This is a legacy method. Please use enhance_audit for cognitive audit frameworks."
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Legacy content analysis failed: {str(e)}"
            }
    
    def _analyze_objective(self, objective: str) -> Dict[str, Any]:
        """Analyze the audit objective to understand audit intent and scope."""
        analysis = {
            "length": len(objective),
            "audit_indicators": [],
            "audit_keywords": [],
            "scope_indicators": []
        }
        
        # Detect audit type indicators
        audit_patterns = [
            (r'\b(security|cyber|threat|vulnerability|breach)\b', "security_audit"),
            (r'\b(compliance|regulatory|policy|standard|requirement)\b', "compliance_audit"),
            (r'\b(quality|process|procedure|effectiveness|efficiency)\b', "quality_audit"),
            (r'\b(workflow|operation|business process|control)\b', "process_audit"),
            (r'\b(financial|accounting|transaction|revenue|expense)\b', "financial_audit"),
            (r'\b(IT|system|application|database|infrastructure)\b', "it_audit")
        ]
        
        for pattern, audit_type in audit_patterns:
            if re.search(pattern, objective, re.IGNORECASE):
                analysis["audit_indicators"].append(audit_type)
        
        # Detect audit keywords
        audit_keywords = [
            (r'\b(audit|assess|evaluate|review|examine|investigate)\b', "investigation"),
            (r'\b(risk|control|compliance|governance)\b', "risk_management"),
            (r'\b(finding|gap|deficiency|weakness|issue)\b', "finding_identification"),
            (r'\b(recommendation|improvement|remediation)\b', "improvement_focused")
        ]
        
        for pattern, keyword in audit_keywords:
            if re.search(pattern, objective, re.IGNORECASE):
                analysis["audit_keywords"].append(keyword)
        
        return analysis
    
    def _suggest_frameworks(self, objective: str) -> List[Dict[str, Any]]:
        """Suggest appropriate audit frameworks based on objective content."""
        suggestions = []
        
        # Framework suggestion logic based on content analysis
        framework_triggers = {
            "security_audit": [
                r'\b(security|cyber|threat|vulnerability|attack|breach|penetration)\b',
                r'\b(access control|authentication|authorization|encryption)\b',
                r'\b(firewall|malware|phishing|incident response)\b'
            ],
            "compliance_audit": [
                r'\b(compliance|regulatory|regulation|standard|requirement)\b',
                r'\b(policy|procedure|guideline|mandate|obligation)\b',
                r'\b(GDPR|SOX|HIPAA|PCI|ISO|NIST)\b'
            ],
            "quality_audit": [
                r'\b(quality|QMS|ISO 9001|six sigma|lean|improvement)\b',
                r'\b(process effectiveness|customer satisfaction|defect)\b',
                r'\b(standard|specification|requirement|criteria)\b'
            ],
            "process_audit": [
                r'\b(process|workflow|procedure|operation|business process)\b',
                r'\b(efficiency|effectiveness|optimization|automation)\b',
                r'\b(control|governance|risk management|performance)\b'
            ],
            "financial_audit": [
                r'\b(financial|accounting|transaction|revenue|expense|budget)\b',
                r'\b(internal control|GAAP|IFRS|SOX|materiality)\b',
                r'\b(reconciliation|journal entry|ledger|audit trail)\b'
            ],
            "it_audit": [
                r'\b(IT|system|application|database|infrastructure|network)\b',
                r'\b(change management|backup|recovery|availability)\b',
                r'\b(access control|data integrity|system security)\b'
            ]
        }
        
        for framework_name, patterns in framework_triggers.items():
            score = 0
            matched_patterns = []
            
            for pattern in patterns:
                if re.search(pattern, objective, re.IGNORECASE):
                    score += 1
                    matched_patterns.append(pattern)
            
            if score > 0:
                framework_info = self.frameworks[framework_name].copy()
                framework_info["relevance_score"] = score
                framework_info["matched_patterns"] = matched_patterns
                framework_info["name"] = framework_name
                suggestions.append(framework_info)
                
        # Sort by relevance score
        suggestions.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        return suggestions
    
    def _apply_framework(self, framework: str, objective: str, context: Optional[Dict[str, Any]], phase: Optional[str]) -> Dict[str, Any]:
        """Apply a specific cognitive audit framework to enhance the audit investigation."""
        framework_info = self.frameworks[framework].copy()
        
        # Add framework application guidance
        framework_info["application"] = {
            "current_objective": objective,
            "framework_lens": f"Conducting {framework.replace('_', ' ')} using professional methodology",
            "investigation_questions": framework_info["investigation_questions"],
            "methodology_guidance": framework_info["methodology"],
            "current_phase": phase or "planning",
            "next_steps": self._get_next_steps(framework, phase)
        }
        
        # Add context-specific guidance if available
        if context:
            framework_info["context_integration"] = self._integrate_context_with_framework(framework, context)
        
        return framework_info
    
    def _get_next_steps(self, framework: str, current_phase: Optional[str]) -> List[str]:
        """Get next steps based on current audit phase and framework methodology."""
        framework_info = self.frameworks[framework]
        methodology = framework_info["methodology"]
        
        if not current_phase:
            # Start with first phase
            first_phase = list(methodology.keys())[0]
            return methodology[first_phase]
        
        phase_keys = list(methodology.keys())
        if current_phase in phase_keys:
            current_index = phase_keys.index(current_phase)
            if current_index < len(phase_keys) - 1:
                next_phase = phase_keys[current_index + 1]
                return methodology[next_phase]
        
        return ["Complete current phase and proceed to next methodology phase"]
    
    def _integrate_context_with_framework(self, framework: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate context information with framework guidance."""
        integration = {
            "context_summary": context,
            "framework_context_fit": f"How {framework.replace('_', ' ')} applies to your audit context"
        }
        
        # Add context-specific guidance based on framework
        if framework == "security_audit" and "systems" in context:
            integration["system_focus"] = "Pay special attention to the system information for threat modeling"
        elif framework == "compliance_audit" and "regulations" in context:
            integration["regulatory_focus"] = "Focus on the specific regulatory requirements mentioned"
        elif framework == "financial_audit" and "materiality" in context:
            integration["materiality_consideration"] = "Consider materiality thresholds in audit testing"
        
        return integration
    
    def _track_audit_progress(self, phase: Optional[str], evidence: Optional[List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Track progress through audit phases with evidence collection."""
        progress = {
            "current_phase": phase or "planning",
            "has_evidence": bool(evidence),
            "evidence_count": len(evidence) if evidence else 0
        }
        
        if evidence:
            progress["evidence_summary"] = {
                "types": list(set(item.get("type", "unknown") for item in evidence)),
                "categories": list(set(item.get("category", "unknown") for item in evidence))
            }
        
        return progress
    
    def _analyze_audit_context(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze provided audit context for investigation planning."""
        analysis = {
            "context_keys": list(context.keys()),
            "context_complexity": len(context),
            "audit_relevant_elements": []
        }
        
        # Identify audit-relevant context elements
        relevant_keys = [
            "scope", "objectives", "timeline", "resources", "stakeholders",
            "systems", "processes", "regulations", "risks", "constraints"
        ]
        
        for key in context.keys():
            if any(relevant in key.lower() for relevant in relevant_keys):
                analysis["audit_relevant_elements"].append(key)
        
        return analysis
    
    def _summarize_evidence(self, evidence: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Summarize collected evidence for audit trail."""
        summary = {
            "total_items": len(evidence),
            "by_type": {},
            "by_category": {},
            "key_findings": []
        }
        
        for item in evidence:
            item_type = item.get("type", "unknown")
            category = item.get("category", "unknown")
            
            summary["by_type"][item_type] = summary["by_type"].get(item_type, 0) + 1
            summary["by_category"][category] = summary["by_category"].get(category, 0) + 1
            
            if item.get("significance") == "high":
                summary["key_findings"].append(item.get("description", "High significance finding"))
        
        return summary
    
    # Legacy helper methods for backward compatibility
    def _detect_content_type(self, content: str, context: Optional[Dict[str, Any]]) -> str:
        """Detect content type for legacy compatibility."""
        if context and "file_type" in context:
            return context["file_type"]
        return "text"
    
    def _calculate_content_metrics(self, content: str) -> Dict[str, Any]:
        """Calculate basic content metrics for legacy compatibility."""
        lines = content.split('\n')
        return {
            "total_lines": len(lines),
            "total_characters": len(content),
            "average_line_length": sum(len(line) for line in lines) / len(lines) if lines else 0
        }

# Tool class is ready for instantiation by the FastMCP server 