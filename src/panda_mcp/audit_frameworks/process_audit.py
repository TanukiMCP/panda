"""
Process Audit Cognitive Framework

This framework guides systematic process auditing through workflow efficiency analysis,
control effectiveness evaluation, operational risk assessment, and performance measurement.
"""
from typing import Dict, Any

# Type definition for audit framework structure
AuditFramework = Dict[str, Any]

process_audit: AuditFramework = {
    "description": "Systematic process audit framework focusing on workflow efficiency analysis, control effectiveness evaluation, operational risk assessment, and performance measurement through professional process auditing methodologies",
    
    "investigation_questions": [
        "What are the key business processes and their objectives?",
        "How are processes documented and controlled?",
        "What are the process performance indicators and targets?",
        "How are process risks identified and managed?",
        "What controls are embedded within processes?",
        "How is process efficiency measured and improved?",
        "What automation and technology support processes?",
        "How are process exceptions handled?",
        "What training and competency requirements exist?",
        "How are processes monitored and reviewed?"
    ],
    
    "methodology": {
        "planning": [
            "Define process audit scope and objectives",
            "Identify critical business processes",
            "Map process flows and dependencies",
            "Assess process risk factors",
            "Establish performance evaluation criteria"
        ],
        "process_mapping": [
            "Document current process flows",
            "Identify process inputs, outputs, and controls",
            "Map process roles and responsibilities",
            "Analyze process handoffs and interfaces",
            "Review process documentation and procedures",
            "Assess process automation and technology"
        ],
        "control_evaluation": [
            "Test process controls effectiveness",
            "Evaluate segregation of duties",
            "Assess authorization and approval controls",
            "Review exception handling procedures",
            "Analyze process monitoring mechanisms",
            "Test data integrity and validation controls"
        ],
        "performance_assessment": [
            "Measure process efficiency and effectiveness",
            "Identify process bottlenecks and delays",
            "Assess resource utilization and capacity",
            "Evaluate process quality and accuracy",
            "Analyze process improvement opportunities",
            "Prepare process audit findings and recommendations"
        ]
    },
    
    "evidence_requirements": [
        "Process documentation and flowcharts",
        "Process performance metrics and reports",
        "Process control matrices and testing results",
        "Process exception reports and resolution logs",
        "Process training materials and records",
        "Process improvement project documentation",
        "System and application process configurations",
        "Process monitoring and review reports",
        "Process risk assessments and mitigation plans",
        "Process stakeholder interviews and feedback"
    ],
    
    "evaluation_criteria": [
        "Adequacy of process design and documentation",
        "Effectiveness of process controls and governance",
        "Efficiency of process execution and cycle times",
        "Accuracy and quality of process outputs",
        "Adequacy of process risk management",
        "Effectiveness of process monitoring and reporting",
        "Maturity of process improvement capabilities",
        "Adequacy of process training and competency",
        "Effectiveness of process exception handling",
        "Overall process optimization and value creation"
    ],
    
    "reporting_structure": {
        "executive_summary": "High-level overview of process performance and key findings",
        "process_landscape": "Summary of audited processes and their criticality",
        "control_assessment": "Evaluation of process controls and governance effectiveness",
        "efficiency_analysis": "Process performance metrics and improvement opportunities",
        "risk_findings": "Process risks and control deficiencies identified",
        "recommendations": "Specific actions to optimize process performance",
        "appendices": "Detailed process maps, control testing results, and supporting evidence"
    },
    
    "risk_assessment_approach": "Risk-based approach prioritizing high-volume, high-value, and customer-facing processes. Focus on processes with regulatory requirements, significant manual intervention, complex handoffs, or history of errors and exceptions."
} 