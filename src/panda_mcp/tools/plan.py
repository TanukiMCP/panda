"""
PandA Plan - Planning Framework Enhancement for LLMs

This tool provides a single atomic interface that enhances LLM planning capabilities
by offering structured frameworks and progress tracking. The LLM drives the process,
and this tool provides the structure and guidance.

Following MCP principles: LLM = DRIVER, Tool = VEHICLE
"""

from typing import Any, Dict, List, Optional
import re
import json
import os
import importlib.util
from pathlib import Path

class PandaPlan:
    """Single atomic planning tool that enhances LLM reasoning with structured frameworks."""
    
    def __init__(self):
        """Initialize the planning tool by dynamically loading frameworks."""
        self.frameworks = self._load_frameworks()
    
    def _load_frameworks(self) -> Dict[str, Any]:
        """Dynamically load planning frameworks from the mental_models directory."""
        frameworks = {}
        models_dir = Path(__file__).parent.parent / "mental_models"
        
        for file_path in models_dir.glob("*.py"):
            if file_path.name.startswith("__") or file_path.name == "base.py":
                continue

            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(
                f"panda_mcp.mental_models.{module_name}", file_path
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
    
    async def enhance_planning(
        self,
        thought: str,
        framework: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        step_number: Optional[int] = None,
        previous_steps: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Enhance LLM planning with structured frameworks and progress tracking.
        
        Args:
            thought: The LLM's current planning thought or question
            framework: Optional framework to apply (first_principles, systems_thinking, etc.)
            context: Optional additional context about the planning task
            step_number: Optional current step number in a sequence
            previous_steps: Optional list of previous planning steps
            
        Returns:
            Dictionary with framework guidance, structure, and progress tracking
        """
        try:
            result = {
                "status": "success",
                "thought_analysis": self._analyze_thought(thought),
                "progress_tracking": self._track_progress(step_number, previous_steps),
                "available_frameworks": list(self.frameworks.keys())
            }
            
            # Apply specific framework if requested
            if framework and framework in self.frameworks:
                result["framework_guidance"] = self._apply_framework(framework, thought, context)
            else:
                # Suggest appropriate framework based on thought content
                result["framework_suggestions"] = self._suggest_frameworks(thought)
            
            # Add context analysis if provided
            if context:
                result["context_analysis"] = self._analyze_context(context)
            
            return result
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Planning enhancement failed: {str(e)}"
            }
    
    def _analyze_thought(self, thought: str) -> Dict[str, Any]:
        """Analyze the LLM's thought to understand planning intent."""
        analysis = {
            "length": len(thought),
            "complexity_indicators": [],
            "planning_keywords": [],
            "question_count": len(re.findall(r'\?', thought))
        }
        
        # Detect complexity indicators
        complexity_patterns = [
            (r'\b(complex|complicated|difficult|challenging)\b', "complexity_mentioned"),
            (r'\b(multiple|several|various|many)\b', "multiple_elements"),
            (r'\b(depend|require|need|prerequisite)\b', "dependencies_mentioned"),
            (r'\b(system|network|interconnect|relationship)\b', "systems_thinking_relevant"),
            (r'\b(user|customer|stakeholder|people)\b', "human_centered"),
            (r'\b(step|phase|stage|sequence)\b', "sequential_thinking")
        ]
        
        for pattern, indicator in complexity_patterns:
            if re.search(pattern, thought, re.IGNORECASE):
                analysis["complexity_indicators"].append(indicator)
        
        # Detect planning keywords
        planning_patterns = [
            (r'\b(plan|strategy|approach|method)\b', "planning"),
            (r'\b(goal|objective|target|aim)\b', "goal_oriented"),
            (r'\b(problem|issue|challenge|obstacle)\b', "problem_solving"),
            (r'\b(analyze|understand|explore|investigate)\b', "analytical"),
            (r'\b(create|build|develop|design)\b', "creative"),
            (r'\b(improve|optimize|enhance|better)\b', "improvement")
        ]
        
        for pattern, keyword in planning_patterns:
            if re.search(pattern, thought, re.IGNORECASE):
                analysis["planning_keywords"].append(keyword)
        
        return analysis
    
    def _suggest_frameworks(self, thought: str) -> List[Dict[str, Any]]:
        """Suggest appropriate frameworks based on thought content."""
        suggestions = []
        
        # Framework suggestion logic based on content analysis
        framework_triggers = {
            "first_principles": [
                r'\b(fundamental|basic|core|essential|simple)\b',
                r'\b(assumption|given|premise)\b',
                r'\b(why|how|what if)\b'
            ],
            "systems_thinking": [
                r'\b(system|network|interconnect|relationship|feedback)\b',
                r'\b(stakeholder|component|element)\b',
                r'\b(impact|effect|consequence|ripple)\b'
            ],
            "design_thinking": [
                r'\b(user|customer|people|human|experience)\b',
                r'\b(need|want|pain|problem|solution)\b',
                r'\b(prototype|test|iterate|feedback)\b'
            ],
            "critical_path": [
                r'\b(task|step|sequence|order|timeline)\b',
                r'\b(depend|prerequisite|before|after)\b',
                r'\b(bottleneck|constraint|limit)\b'
            ],
            "swot_analysis": [
                r'\b(strength|weakness|opportunity|threat)\b',
                r'\b(advantage|disadvantage|risk|benefit)\b',
                r'\b(internal|external|competitive)\b'
            ]
        }
        
        for framework_name, patterns in framework_triggers.items():
            score = 0
            matched_patterns = []
            
            for pattern in patterns:
                if re.search(pattern, thought, re.IGNORECASE):
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
    
    def _apply_framework(self, framework: str, thought: str, context: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Apply a specific framework to enhance the planning thought."""
        framework_info = self.frameworks[framework].copy()
        
        # Add framework application guidance
        framework_info["application"] = {
            "current_thought": thought,
            "framework_lens": f"Viewing your thought through the {framework} framework",
            "guided_questions": framework_info["questions"],
            "structure_template": framework_info["structure"],
            "next_steps_guidance": framework_info["next_steps"]
        }
        
        # Add context-specific guidance if available
        if context:
            framework_info["context_integration"] = self._integrate_context_with_framework(framework, context)
        
        return framework_info
    
    def _integrate_context_with_framework(self, framework: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate context information with framework guidance."""
        integration = {
            "context_summary": context,
            "framework_context_fit": f"How {framework} applies to your specific context"
        }
        
        # Add context-specific guidance based on framework
        if framework == "design_thinking" and "users" in context:
            integration["user_focus"] = "Pay special attention to the user information in your context"
        elif framework == "systems_thinking" and "stakeholders" in context:
            integration["stakeholder_mapping"] = "Use the stakeholder information to map system relationships"
        elif framework == "critical_path" and "timeline" in context:
            integration["timeline_integration"] = "Consider the timeline constraints in your critical path analysis"
        
        return integration
    
    def _track_progress(self, step_number: Optional[int], previous_steps: Optional[List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Track progress through a planning sequence."""
        progress = {
            "current_step": step_number or 1,
            "has_previous_steps": bool(previous_steps),
            "step_count": len(previous_steps) if previous_steps else 0
        }
        
        if previous_steps:
            progress["previous_steps_summary"] = [
                {
                    "step": i + 1,
                    "framework_used": step.get("framework"),
                    "key_insight": step.get("insight", "No insight recorded")[:100]
                }
                for i, step in enumerate(previous_steps[-5:])  # Last 5 steps
            ]
            
            # Analyze progress patterns
            frameworks_used = [step.get("framework") for step in previous_steps if step.get("framework")]
            if frameworks_used:
                progress["framework_diversity"] = len(set(frameworks_used))
                progress["most_used_framework"] = max(set(frameworks_used), key=frameworks_used.count)
        
        return progress
    
    def _analyze_context(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze provided context for planning relevance."""
        analysis = {
            "context_keys": list(context.keys()),
            "context_complexity": len(context),
            "planning_relevant_elements": []
        }
        
        # Identify planning-relevant context elements
        relevant_keys = [
            "goals", "objectives", "constraints", "timeline", "resources",
            "stakeholders", "users", "requirements", "dependencies", "risks"
        ]
        
        for key in context.keys():
            if any(relevant in key.lower() for relevant in relevant_keys):
                analysis["planning_relevant_elements"].append(key)
        
        return analysis

# Tool class is ready for instantiation by the FastMCP server 