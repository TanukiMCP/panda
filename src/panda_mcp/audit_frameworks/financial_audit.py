"""
Financial Audit Cognitive Framework

This framework guides systematic financial auditing through internal control evaluation,
accuracy verification procedures, risk assessment methodology, and authorization control testing.
"""
from typing import Dict, Any

# Type definition for audit framework structure
AuditFramework = Dict[str, Any]

financial_audit: AuditFramework = {
    "description": "Systematic financial audit framework focusing on internal control evaluation, accuracy verification procedures, risk assessment methodology, and authorization control testing through professional financial auditing methodologies",
    
    "investigation_questions": [
        "What are the key financial processes and controls?",
        "How are financial transactions authorized and recorded?",
        "What are the segregation of duties in financial processes?",
        "How is financial data validated and reconciled?",
        "What are the financial reporting processes and controls?",
        "How are financial risks identified and mitigated?",
        "What are the budgeting and forecasting processes?",
        "How is access to financial systems controlled?",
        "What are the month-end and year-end closing procedures?",
        "How are financial policies and procedures maintained?"
    ],
    
    "methodology": {
        "planning": [
            "Define financial audit scope and materiality",
            "Assess financial statement risk areas",
            "Identify key financial processes and controls",
            "Develop audit testing approach",
            "Establish sampling methodology for testing"
        ],
        "controls_assessment": [
            "Evaluate design of financial controls",
            "Test operating effectiveness of controls",
            "Assess segregation of duties",
            "Review authorization and approval controls",
            "Analyze access controls to financial systems",
            "Evaluate management review controls"
        ],
        "substantive_testing": [
            "Perform detailed transaction testing",
            "Conduct analytical procedures and variance analysis",
            "Verify account balances and reconciliations",
            "Test journal entries and adjustments",
            "Review supporting documentation",
            "Perform cut-off and completeness testing"
        ],
        "reporting_and_recommendations": [
            "Summarize control deficiencies and findings",
            "Assess financial reporting accuracy",
            "Evaluate compliance with accounting standards",
            "Develop management letter recommendations",
            "Prepare financial audit report",
            "Present findings to audit committee"
        ]
    },
    
    "evidence_requirements": [
        "Financial policies and procedures documentation",
        "General ledger and trial balance reports",
        "Account reconciliations and supporting schedules",
        "Journal entries and posting documentation",
        "Bank statements and confirmations",
        "Accounts receivable aging and confirmations",
        "Inventory count sheets and supporting records",
        "Fixed asset registers and depreciation schedules",
        "Accounts payable confirmations and supporting invoices",
        "Financial statement preparation and review documentation"
    ],
    
    "evaluation_criteria": [
        "Adequacy of financial controls design and implementation",
        "Effectiveness of authorization and approval processes",
        "Accuracy of financial recording and reporting",
        "Completeness of financial transaction capture",
        "Timeliness of financial closing and reporting",
        "Compliance with accounting standards and policies",
        "Adequacy of financial risk management",
        "Effectiveness of financial system access controls",
        "Quality of financial documentation and support",
        "Overall financial control environment strength"
    ],
    
    "reporting_structure": {
        "executive_summary": "High-level overview of financial control environment and key findings",
        "controls_assessment": "Evaluation of internal controls design and operating effectiveness",
        "financial_findings": "Specific control deficiencies and compliance issues",
        "materiality_assessment": "Analysis of financial impact and significance of findings",
        "recommendations": "Specific actions to strengthen financial controls and processes",
        "management_responses": "Management's planned corrective actions and timelines",
        "appendices": "Detailed testing results, samples, and supporting documentation"
    },
    
    "risk_assessment_approach": "Risk-based approach focusing on material account balances, complex transactions, and high-risk processes. Prioritize areas with history of errors, significant estimates and judgments, regulatory requirements, and fraud risk indicators."
} 