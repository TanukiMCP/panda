"""
IT Audit Cognitive Framework

This framework guides systematic IT auditing through system security assessment,
data integrity verification, technology governance evaluation, and change management review.
"""
from typing import Dict, Any

# Type definition for audit framework structure
AuditFramework = Dict[str, Any]

it_audit: AuditFramework = {
    "description": "Systematic IT audit framework focusing on system security assessment, data integrity verification, technology governance evaluation, and change management review through professional IT auditing methodologies",
    
    "investigation_questions": [
        "What are the critical IT systems and infrastructure components?",
        "How are IT systems secured and access controlled?",
        "What are the data backup and recovery procedures?",
        "How is change management implemented across IT systems?",
        "What are the IT governance policies and procedures?",
        "How is system availability and performance monitored?",
        "What are the disaster recovery and business continuity plans?",
        "How is data integrity and accuracy ensured?",
        "What are the IT compliance requirements and controls?",
        "How are IT risks identified and managed?"
    ],
    
    "methodology": {
        "planning": [
            "Define IT audit scope and objectives",
            "Identify critical systems and applications",
            "Assess IT risk landscape and priorities",
            "Map IT governance structure and processes",
            "Establish technical testing approach"
        ],
        "systems_assessment": [
            "Review IT architecture and infrastructure",
            "Assess system security configurations",
            "Evaluate access control implementations",
            "Analyze system integration and interfaces",
            "Review system documentation and procedures",
            "Test system availability and performance"
        ],
        "controls_evaluation": [
            "Test IT general controls effectiveness",
            "Evaluate change management controls",
            "Assess data backup and recovery controls",
            "Review incident response procedures",
            "Analyze monitoring and logging controls",
            "Test disaster recovery capabilities"
        ],
        "governance_review": [
            "Assess IT governance framework",
            "Evaluate IT risk management processes",
            "Review IT compliance monitoring",
            "Analyze IT performance management",
            "Assess IT resource management",
            "Prepare IT audit findings and recommendations"
        ]
    },
    
    "evidence_requirements": [
        "IT governance policies and procedures",
        "System architecture and network diagrams",
        "Access control matrices and user privilege reports",
        "Change management logs and approval records",
        "System backup and recovery test results",
        "Incident response logs and resolution documentation",
        "System monitoring and performance reports",
        "Disaster recovery test plans and results",
        "IT compliance assessment reports",
        "Vendor contracts and service level agreements"
    ],
    
    "evaluation_criteria": [
        "Adequacy of IT governance and oversight",
        "Effectiveness of system security controls",
        "Robustness of access control mechanisms",
        "Reliability of data backup and recovery processes",
        "Effectiveness of change management controls",
        "Adequacy of system monitoring and alerting",
        "Maturity of incident response capabilities",
        "Effectiveness of disaster recovery planning",
        "Compliance with IT policies and standards",
        "Overall IT risk management effectiveness"
    ],
    
    "reporting_structure": {
        "executive_summary": "High-level overview of IT control environment and critical findings",
        "governance_assessment": "Evaluation of IT governance framework and processes",
        "systems_findings": "Specific system security and control deficiencies",
        "risk_analysis": "IT risks and their potential business impact",
        "recommendations": "Specific actions to strengthen IT controls and governance",
        "implementation_roadmap": "Prioritized IT improvement initiatives and timelines",
        "appendices": "Technical testing results, configurations, and supporting evidence"
    },
    
    "risk_assessment_approach": "Risk-based approach prioritizing business-critical systems, external-facing applications, and high-risk IT processes. Focus on systems processing sensitive data, financially material applications, regulatory compliance systems, and areas with history of security incidents."
} 