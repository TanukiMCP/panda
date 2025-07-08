"""
Compliance Audit Cognitive Framework

This framework guides systematic compliance auditing through regulatory requirement
assessment, policy adherence evaluation, documentation review, and gap analysis.
"""
from typing import Dict, Any

# Type definition for audit framework structure
AuditFramework = Dict[str, Any]

compliance_audit: AuditFramework = {
    "description": "Systematic compliance audit framework focusing on regulatory requirement assessment, policy adherence evaluation, documentation review, and compliance gap analysis through professional auditing methodologies",
    
    "investigation_questions": [
        "What regulatory requirements apply to this organization?",
        "How are compliance requirements documented and communicated?",
        "What policies and procedures support compliance requirements?",
        "How is compliance monitoring and measurement performed?",
        "What compliance training and awareness programs exist?",
        "How are compliance violations identified and addressed?",
        "What documentation supports compliance claims?",
        "How are regulatory changes identified and implemented?",
        "What are the consequences of non-compliance?",
        "How is compliance effectiveness measured and reported?"
    ],
    
    "methodology": {
        "planning": [
            "Identify applicable regulations and standards",
            "Define compliance audit scope and objectives", 
            "Map regulatory requirements to business processes",
            "Develop compliance testing approach",
            "Establish sampling methodology"
        ],
        "requirement_analysis": [
            "Review applicable laws and regulations",
            "Analyze industry standards and guidelines",
            "Examine contractual compliance obligations",
            "Document compliance requirement matrix",
            "Identify compliance risk areas",
            "Review regulatory change management process"
        ],
        "compliance_testing": [
            "Test policy implementation and adherence",
            "Evaluate control effectiveness",
            "Review compliance monitoring procedures",
            "Assess training and awareness programs",
            "Examine compliance reporting processes",
            "Test exception handling and remediation"
        ],
        "gap_analysis_and_reporting": [
            "Identify compliance gaps and deficiencies",
            "Assess risk level of non-compliance",
            "Develop remediation recommendations",
            "Create compliance improvement roadmap",
            "Prepare compliance audit report",
            "Present findings to compliance committee"
        ]
    },
    
    "evidence_requirements": [
        "Regulatory requirement documentation and updates",
        "Compliance policies and procedures",
        "Compliance training materials and attendance records",
        "Compliance monitoring reports and metrics",
        "Regulatory correspondence and communications",
        "Compliance violation reports and remediation actions",
        "Internal audit reports and management responses",
        "External compliance assessments and certifications",
        "Legal opinions and compliance guidance",
        "Board and committee meeting minutes related to compliance"
    ],
    
    "evaluation_criteria": [
        "Completeness of regulatory requirement identification",
        "Adequacy of compliance policies and procedures",
        "Effectiveness of compliance monitoring and testing",
        "Quality of compliance training and awareness programs",
        "Timeliness of regulatory change implementation",
        "Adequacy of compliance violation response",
        "Quality of compliance documentation and records",
        "Effectiveness of compliance reporting and governance",
        "Maturity of compliance risk management",
        "Overall compliance program effectiveness"
    ],
    
    "reporting_structure": {
        "executive_summary": "High-level overview of compliance posture and critical gaps",
        "regulatory_landscape": "Summary of applicable regulations and requirements",
        "compliance_findings": "Specific compliance gaps, violations, and control weaknesses",
        "risk_assessment": "Analysis of compliance risks and potential regulatory impact",
        "recommendations": "Specific actions to address compliance deficiencies",
        "implementation_roadmap": "Timeline and priorities for compliance improvements",
        "appendices": "Detailed requirement mappings, test results, and supporting documentation"
    },
    
    "risk_assessment_approach": "Risk-based approach prioritizing high-impact regulatory requirements, focusing on areas with severe penalties, regulatory scrutiny, or business impact. Consider likelihood of regulatory examination, materiality of violations, and reputational risk to the organization."
} 