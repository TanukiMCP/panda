"""
Auditing patterns implementation for PandA auditing
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Type
from enum import Enum

class AuditingPatternType(Enum):
    """Types of auditing patterns available."""
    # Security Auditing Patterns
    VULNERABILITY_ASSESSMENT = "vulnerability_assessment"
    ACCESS_CONTROL_AUDIT = "access_control_audit"
    ENCRYPTION_COMPLIANCE = "encryption_compliance"
    SECURITY_CONFIGURATION_REVIEW = "security_configuration_review"
    INCIDENT_RESPONSE_AUDIT = "incident_response_audit"
    DATA_LOSS_PREVENTION = "data_loss_prevention"
    NETWORK_SECURITY_AUDIT = "network_security_audit"
    APPLICATION_SECURITY = "application_security"
    
    # Quality Assurance Patterns
    CODE_QUALITY_ASSESSMENT = "code_quality_assessment"
    TEST_COVERAGE_ANALYSIS = "test_coverage_analysis"
    DOCUMENTATION_QUALITY = "documentation_quality"
    DEPENDENCY_MANAGEMENT = "dependency_management"
    PERFORMANCE_QUALITY = "performance_quality"
    USER_EXPERIENCE_AUDIT = "user_experience_audit"
    DATA_QUALITY_ASSESSMENT = "data_quality_assessment"
    API_QUALITY = "api_quality"
    
    # Compliance and Governance Patterns
    REGULATORY_COMPLIANCE = "regulatory_compliance"
    POLICY_ADHERENCE = "policy_adherence"
    CHANGE_MANAGEMENT_AUDIT = "change_management_audit"
    RISK_MANAGEMENT = "risk_management"
    AUDIT_TRAIL = "audit_trail"
    BUSINESS_CONTINUITY = "business_continuity"
    VENDOR_MANAGEMENT = "vendor_management"
    DATA_GOVERNANCE = "data_governance"
    
    # Performance and Operational Patterns
    SYSTEM_PERFORMANCE = "system_performance"
    RESOURCE_UTILIZATION = "resource_utilization"
    AVAILABILITY_RELIABILITY = "availability_reliability"
    MONITORING_ALERTING = "monitoring_alerting"
    BACKUP_RECOVERY = "backup_recovery"
    OPERATIONAL_EXCELLENCE = "operational_excellence"
    INFRASTRUCTURE_AUDIT = "infrastructure_audit"
    CLOUD_SECURITY = "cloud_security"
    
    # Process and Workflow Patterns
    DEVOPS_PIPELINE = "devops_pipeline"
    PROJECT_MANAGEMENT = "project_management"
    COMMUNICATION_AUDIT = "communication_audit"
    TRAINING_COMPETENCY = "training_competency"
    
    # Financial and Business Patterns
    COST_MANAGEMENT = "cost_management"
    REVENUE_ASSURANCE = "revenue_assurance"
    CONTRACT_MANAGEMENT = "contract_management"
    
    # Environmental and Sustainability Patterns
    ENVIRONMENTAL_IMPACT = "environmental_impact"
    WASTE_MANAGEMENT = "waste_management"
    SOCIAL_RESPONSIBILITY = "social_responsibility"

class AuditingPattern(ABC):
    """Base class for auditing patterns."""
    
    def __init__(self, name: str, description: str):
        """Initialize an auditing pattern."""
        self.name = name
        self.description = description
    
    @abstractmethod
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate auditing steps using this pattern."""
        pass

# Security Auditing Pattern Implementations

class VulnerabilityAssessmentPattern(AuditingPattern):
    """Vulnerability Assessment auditing pattern."""
    
    def __init__(self):
        """Initialize the vulnerability assessment pattern."""
        super().__init__(
            name=AuditingPatternType.VULNERABILITY_ASSESSMENT.value,
            description="Systematic identification and evaluation of security vulnerabilities"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate vulnerability assessment audit steps."""
        return [
            {
                "type": "scope_definition",
                "name": "Define Assessment Scope",
                "description": f"Define the scope and boundaries for vulnerability assessment of {scope}",
                "expected_output": "Detailed scope document with systems, applications, and networks to be assessed"
            },
            {
                "type": "asset_inventory",
                "name": "Create Asset Inventory",
                "description": "Identify and catalog all assets within the assessment scope",
                "expected_output": "Comprehensive asset inventory with system details, versions, and configurations"
            },
            {
                "type": "threat_modeling",
                "name": "Conduct Threat Modeling",
                "description": "Identify potential threats and attack vectors relevant to the assets",
                "expected_output": "Threat model documenting potential attack scenarios and threat actors"
            },
            {
                "type": "automated_scanning",
                "name": "Perform Automated Vulnerability Scanning",
                "description": "Execute automated vulnerability scans using appropriate tools",
                "expected_output": "Raw scan results from vulnerability scanners with identified vulnerabilities"
            },
            {
                "type": "manual_testing",
                "name": "Conduct Manual Security Testing",
                "description": "Perform manual testing to identify vulnerabilities missed by automated tools",
                "expected_output": "Manual testing results with detailed findings and proof-of-concept exploits"
            },
            {
                "type": "vulnerability_analysis",
                "name": "Analyze and Validate Vulnerabilities",
                "description": "Analyze scan results, validate findings, and eliminate false positives",
                "expected_output": "Validated vulnerability list with severity ratings and impact assessments"
            },
            {
                "type": "risk_assessment",
                "name": "Assess Risk and Impact",
                "description": "Evaluate the risk and potential business impact of identified vulnerabilities",
                "expected_output": "Risk assessment matrix with vulnerability prioritization based on business impact"
            },
            {
                "type": "remediation_planning",
                "name": "Develop Remediation Plan",
                "description": "Create detailed remediation plans for identified vulnerabilities",
                "expected_output": "Remediation roadmap with timelines, resources, and implementation strategies"
            },
            {
                "type": "reporting",
                "name": "Generate Assessment Report",
                "description": "Compile comprehensive vulnerability assessment report with findings and recommendations",
                "expected_output": "Executive and technical reports with vulnerability findings, risk ratings, and remediation guidance"
            }
        ]

class AccessControlAuditPattern(AuditingPattern):
    """Access Control Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the access control audit pattern."""
        super().__init__(
            name=AuditingPatternType.ACCESS_CONTROL_AUDIT.value,
            description="Comprehensive review of user access rights, permissions, and authentication mechanisms"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate access control audit steps."""
        return [
            {
                "type": "access_inventory",
                "name": "Inventory Access Controls",
                "description": f"Catalog all access control systems and mechanisms within {scope}",
                "expected_output": "Complete inventory of access control systems, user directories, and authentication mechanisms"
            },
            {
                "type": "user_account_review",
                "name": "Review User Accounts",
                "description": "Examine all user accounts for appropriateness and current status",
                "expected_output": "User account analysis with active, inactive, and privileged account classifications"
            },
            {
                "type": "permission_analysis",
                "name": "Analyze User Permissions",
                "description": "Review user permissions and access rights against job requirements",
                "expected_output": "Permission matrix showing user access rights and alignment with role requirements"
            },
            {
                "type": "privileged_access_review",
                "name": "Review Privileged Access",
                "description": "Examine privileged accounts and administrative access controls",
                "expected_output": "Privileged access inventory with justification and monitoring controls assessment"
            },
            {
                "type": "authentication_assessment",
                "name": "Assess Authentication Mechanisms",
                "description": "Evaluate authentication methods, password policies, and multi-factor authentication",
                "expected_output": "Authentication strength assessment with policy compliance evaluation"
            },
            {
                "type": "segregation_duties",
                "name": "Verify Segregation of Duties",
                "description": "Check for proper segregation of duties and prevention of conflicting access",
                "expected_output": "Segregation of duties analysis with identified conflicts and recommendations"
            },
            {
                "type": "access_provisioning",
                "name": "Review Access Provisioning Process",
                "description": "Examine user access provisioning, modification, and deprovisioning processes",
                "expected_output": "Access lifecycle process assessment with control effectiveness evaluation"
            },
            {
                "type": "access_monitoring",
                "name": "Evaluate Access Monitoring",
                "description": "Assess monitoring and logging of access activities and suspicious behavior",
                "expected_output": "Access monitoring capability assessment with logging and alerting effectiveness"
            },
            {
                "type": "compliance_verification",
                "name": "Verify Regulatory Compliance",
                "description": "Check access controls against applicable regulatory requirements",
                "expected_output": "Compliance assessment report with gaps and remediation requirements"
            }
        ]

class EncryptionCompliancePattern(AuditingPattern):
    """Encryption Compliance auditing pattern."""
    
    def __init__(self):
        """Initialize the encryption compliance pattern."""
        super().__init__(
            name=AuditingPatternType.ENCRYPTION_COMPLIANCE.value,
            description="Verification of encryption implementation, key management, and cryptographic standards compliance"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate encryption compliance audit steps."""
        return [
            {
                "type": "encryption_inventory",
                "name": "Inventory Encryption Usage",
                "description": f"Identify all encryption implementations and cryptographic controls in {scope}",
                "expected_output": "Comprehensive encryption inventory with algorithms, key lengths, and usage contexts"
            },
            {
                "type": "data_classification",
                "name": "Review Data Classification",
                "description": "Assess data classification and encryption requirements for different data types",
                "expected_output": "Data classification matrix with encryption requirements and current protection status"
            },
            {
                "type": "encryption_standards",
                "name": "Verify Encryption Standards",
                "description": "Check compliance with approved cryptographic standards and algorithms",
                "expected_output": "Standards compliance assessment with approved vs. implemented encryption methods"
            },
            {
                "type": "key_management",
                "name": "Audit Key Management",
                "description": "Review key generation, distribution, storage, rotation, and destruction processes",
                "expected_output": "Key management lifecycle assessment with process effectiveness and security evaluation"
            },
            {
                "type": "data_at_rest",
                "name": "Assess Data-at-Rest Encryption",
                "description": "Verify encryption of sensitive data stored in databases, files, and storage systems",
                "expected_output": "Data-at-rest encryption coverage analysis with gaps and implementation recommendations"
            },
            {
                "type": "data_in_transit",
                "name": "Assess Data-in-Transit Encryption",
                "description": "Verify encryption of data transmitted over networks and communication channels",
                "expected_output": "Data-in-transit encryption assessment with protocol analysis and security evaluation"
            },
            {
                "type": "certificate_management",
                "name": "Review Certificate Management",
                "description": "Audit digital certificate lifecycle management and PKI infrastructure",
                "expected_output": "Certificate management assessment with expiration tracking and renewal processes"
            },
            {
                "type": "encryption_performance",
                "name": "Evaluate Encryption Performance",
                "description": "Assess the performance impact of encryption implementations",
                "expected_output": "Performance impact analysis with optimization recommendations and resource utilization"
            },
            {
                "type": "regulatory_compliance",
                "name": "Verify Regulatory Compliance",
                "description": "Check encryption implementations against regulatory requirements (GDPR, HIPAA, etc.)",
                "expected_output": "Regulatory compliance assessment with specific requirement mapping and gap analysis"
            }
        ]

class SecurityConfigurationReviewPattern(AuditingPattern):
    """Security Configuration Review auditing pattern."""
    
    def __init__(self):
        """Initialize the security configuration review pattern."""
        super().__init__(
            name=AuditingPatternType.SECURITY_CONFIGURATION_REVIEW.value,
            description="Assessment of security configurations across systems, networks, and applications"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate security configuration review audit steps."""
        return [
            {
                "type": "baseline_establishment",
                "name": "Establish Security Baselines",
                "description": f"Define security configuration baselines for systems within {scope}",
                "expected_output": "Security baseline documentation with approved configurations and standards"
            },
            {
                "type": "configuration_inventory",
                "name": "Inventory Current Configurations",
                "description": "Document current security configurations across all systems and applications",
                "expected_output": "Configuration inventory with current settings, versions, and security parameters"
            },
            {
                "type": "hardening_assessment",
                "name": "Assess System Hardening",
                "description": "Evaluate system hardening measures against security best practices",
                "expected_output": "Hardening assessment report with compliance to security benchmarks and standards"
            },
            {
                "type": "default_settings_review",
                "name": "Review Default Settings",
                "description": "Identify and assess systems still using default or insecure configurations",
                "expected_output": "Default settings analysis with security risks and remediation recommendations"
            },
            {
                "type": "access_control_config",
                "name": "Review Access Control Configurations",
                "description": "Examine access control settings, permissions, and authentication configurations",
                "expected_output": "Access control configuration assessment with security posture evaluation"
            },
            {
                "type": "network_security_config",
                "name": "Assess Network Security Configurations",
                "description": "Review firewall rules, network segmentation, and security device configurations",
                "expected_output": "Network security configuration analysis with rule effectiveness and gap identification"
            },
            {
                "type": "logging_monitoring_config",
                "name": "Review Logging and Monitoring Configurations",
                "description": "Assess security logging, monitoring, and alerting configurations",
                "expected_output": "Logging and monitoring configuration assessment with coverage and effectiveness analysis"
            },
            {
                "type": "configuration_drift",
                "name": "Detect Configuration Drift",
                "description": "Identify deviations from approved security configurations over time",
                "expected_output": "Configuration drift analysis with unauthorized changes and compliance deviations"
            },
            {
                "type": "remediation_prioritization",
                "name": "Prioritize Configuration Remediation",
                "description": "Prioritize configuration issues based on risk and business impact",
                "expected_output": "Remediation priority matrix with risk-based configuration improvement roadmap"
            }
        ]

class IncidentResponseAuditPattern(AuditingPattern):
    """Incident Response Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the incident response audit pattern."""
        super().__init__(
            name=AuditingPatternType.INCIDENT_RESPONSE_AUDIT.value,
            description="Evaluation of incident response procedures, capabilities, and effectiveness"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate incident response audit steps."""
        return [
            {
                "type": "policy_review",
                "name": "Review Incident Response Policies",
                "description": f"Examine incident response policies and procedures for {scope}",
                "expected_output": "Policy assessment with completeness, currency, and alignment with best practices"
            },
            {
                "type": "team_assessment",
                "name": "Assess Incident Response Team",
                "description": "Evaluate incident response team structure, roles, and responsibilities",
                "expected_output": "Team capability assessment with role definitions, skills, and availability analysis"
            },
            {
                "type": "detection_capabilities",
                "name": "Evaluate Detection Capabilities",
                "description": "Assess incident detection mechanisms, monitoring, and alerting systems",
                "expected_output": "Detection capability analysis with coverage, accuracy, and response time metrics"
            },
            {
                "type": "response_procedures",
                "name": "Review Response Procedures",
                "description": "Examine incident classification, escalation, and response procedures",
                "expected_output": "Response procedure assessment with workflow effectiveness and decision criteria"
            },
            {
                "type": "communication_protocols",
                "name": "Assess Communication Protocols",
                "description": "Review internal and external communication procedures during incidents",
                "expected_output": "Communication protocol evaluation with stakeholder notification and coordination processes"
            },
            {
                "type": "forensic_capabilities",
                "name": "Evaluate Forensic Capabilities",
                "description": "Assess digital forensics capabilities and evidence preservation procedures",
                "expected_output": "Forensic capability assessment with evidence handling and chain of custody procedures"
            },
            {
                "type": "recovery_procedures",
                "name": "Review Recovery Procedures",
                "description": "Examine system recovery, business continuity, and restoration procedures",
                "expected_output": "Recovery procedure assessment with restoration timelines and business impact analysis"
            },
            {
                "type": "training_exercises",
                "name": "Assess Training and Exercises",
                "description": "Evaluate incident response training programs and tabletop exercises",
                "expected_output": "Training effectiveness assessment with exercise results and skill development analysis"
            },
            {
                "type": "lessons_learned",
                "name": "Review Lessons Learned Process",
                "description": "Assess post-incident review processes and continuous improvement mechanisms",
                "expected_output": "Lessons learned process evaluation with improvement implementation and knowledge retention"
            }
        ]

class DataLossPreventionPattern(AuditingPattern):
    """Data Loss Prevention auditing pattern."""
    
    def __init__(self):
        """Initialize the data loss prevention pattern."""
        super().__init__(
            name=AuditingPatternType.DATA_LOSS_PREVENTION.value,
            description="Assessment of data protection mechanisms and data leakage prevention controls"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate data loss prevention audit steps."""
        return [
            {
                "type": "data_discovery",
                "name": "Discover and Classify Data",
                "description": f"Identify and classify sensitive data within {scope}",
                "expected_output": "Data inventory with classification levels, locations, and sensitivity ratings"
            },
            {
                "type": "dlp_policy_review",
                "name": "Review DLP Policies",
                "description": "Examine data loss prevention policies and rules configuration",
                "expected_output": "DLP policy assessment with rule effectiveness and coverage analysis"
            },
            {
                "type": "data_flow_analysis",
                "name": "Analyze Data Flows",
                "description": "Map data flows and identify potential leakage points",
                "expected_output": "Data flow diagram with risk assessment and control point identification"
            },
            {
                "type": "endpoint_protection",
                "name": "Assess Endpoint Protection",
                "description": "Evaluate data protection controls on endpoints and mobile devices",
                "expected_output": "Endpoint protection assessment with device security and data handling controls"
            },
            {
                "type": "network_monitoring",
                "name": "Review Network Monitoring",
                "description": "Assess network-based data loss prevention monitoring and controls",
                "expected_output": "Network DLP effectiveness analysis with traffic monitoring and blocking capabilities"
            },
            {
                "type": "email_security",
                "name": "Evaluate Email Security",
                "description": "Review email data loss prevention and content filtering controls",
                "expected_output": "Email security assessment with content inspection and policy enforcement evaluation"
            },
            {
                "type": "cloud_data_protection",
                "name": "Assess Cloud Data Protection",
                "description": "Evaluate data protection controls for cloud services and applications",
                "expected_output": "Cloud data protection analysis with service-specific controls and compliance assessment"
            },
            {
                "type": "incident_response_dlp",
                "name": "Review DLP Incident Response",
                "description": "Assess data loss incident detection, response, and remediation procedures",
                "expected_output": "DLP incident response capability assessment with detection accuracy and response effectiveness"
            },
            {
                "type": "user_awareness",
                "name": "Evaluate User Awareness",
                "description": "Assess user training and awareness programs for data protection",
                "expected_output": "User awareness assessment with training effectiveness and behavioral compliance analysis"
            }
        ]

class NetworkSecurityAuditPattern(AuditingPattern):
    """Network Security Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the network security audit pattern."""
        super().__init__(
            name=AuditingPatternType.NETWORK_SECURITY_AUDIT.value,
            description="Comprehensive review of network security controls, segmentation, and monitoring"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate network security audit steps."""
        return [
            {
                "type": "network_architecture",
                "name": "Review Network Architecture",
                "description": f"Analyze network architecture and topology for {scope}",
                "expected_output": "Network architecture documentation with security zones and trust boundaries"
            },
            {
                "type": "firewall_assessment",
                "name": "Assess Firewall Configuration",
                "description": "Review firewall rules, policies, and configuration effectiveness",
                "expected_output": "Firewall assessment with rule analysis, policy effectiveness, and security gaps"
            },
            {
                "type": "network_segmentation",
                "name": "Evaluate Network Segmentation",
                "description": "Assess network segmentation implementation and effectiveness",
                "expected_output": "Segmentation analysis with isolation effectiveness and lateral movement prevention"
            },
            {
                "type": "intrusion_detection",
                "name": "Review Intrusion Detection Systems",
                "description": "Evaluate IDS/IPS deployment, configuration, and effectiveness",
                "expected_output": "IDS/IPS assessment with detection capability, rule tuning, and alert management"
            },
            {
                "type": "wireless_security",
                "name": "Assess Wireless Security",
                "description": "Review wireless network security controls and access management",
                "expected_output": "Wireless security assessment with encryption, authentication, and access control evaluation"
            },
            {
                "type": "network_monitoring",
                "name": "Evaluate Network Monitoring",
                "description": "Assess network monitoring capabilities and traffic analysis",
                "expected_output": "Network monitoring assessment with visibility, logging, and anomaly detection capabilities"
            },
            {
                "type": "remote_access",
                "name": "Review Remote Access Security",
                "description": "Evaluate VPN, remote access controls, and secure connectivity",
                "expected_output": "Remote access security assessment with authentication, encryption, and access control analysis"
            },
            {
                "type": "network_devices",
                "name": "Assess Network Device Security",
                "description": "Review security configuration of routers, switches, and network appliances",
                "expected_output": "Network device security assessment with configuration hardening and management security"
            },
            {
                "type": "vulnerability_scanning",
                "name": "Conduct Network Vulnerability Scanning",
                "description": "Perform network vulnerability assessment and penetration testing",
                "expected_output": "Network vulnerability assessment with identified weaknesses and exploitation risks"
            }
        ]

class ApplicationSecurityPattern(AuditingPattern):
    """Application Security auditing pattern."""
    
    def __init__(self):
        """Initialize the application security pattern."""
        super().__init__(
            name=AuditingPatternType.APPLICATION_SECURITY.value,
            description="Security assessment of applications including code review, dependency analysis, and runtime security"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate application security audit steps."""
        return [
            {
                "type": "application_inventory",
                "name": "Inventory Applications",
                "description": f"Catalog all applications within {scope} and their security characteristics",
                "expected_output": "Application inventory with technology stack, criticality, and security requirements"
            },
            {
                "type": "secure_development",
                "name": "Assess Secure Development Practices",
                "description": "Review secure coding practices and development lifecycle security",
                "expected_output": "Secure development assessment with SDLC security integration and practice effectiveness"
            },
            {
                "type": "code_review",
                "name": "Conduct Security Code Review",
                "description": "Perform static analysis and manual code review for security vulnerabilities",
                "expected_output": "Code security assessment with vulnerability identification and remediation recommendations"
            },
            {
                "type": "dependency_analysis",
                "name": "Analyze Dependencies and Libraries",
                "description": "Review third-party components, libraries, and dependency security",
                "expected_output": "Dependency security analysis with vulnerability assessment and update recommendations"
            },
            {
                "type": "authentication_authorization",
                "name": "Assess Authentication and Authorization",
                "description": "Review application authentication mechanisms and access controls",
                "expected_output": "Authentication and authorization assessment with security strength and implementation analysis"
            },
            {
                "type": "input_validation",
                "name": "Evaluate Input Validation",
                "description": "Assess input validation, sanitization, and injection attack prevention",
                "expected_output": "Input validation assessment with injection vulnerability analysis and prevention controls"
            },
            {
                "type": "session_management",
                "name": "Review Session Management",
                "description": "Evaluate session handling, token management, and session security",
                "expected_output": "Session management assessment with security controls and vulnerability analysis"
            },
            {
                "type": "api_security",
                "name": "Assess API Security",
                "description": "Review API security controls, authentication, and data protection",
                "expected_output": "API security assessment with endpoint protection, rate limiting, and data exposure analysis"
            },
            {
                "type": "runtime_protection",
                "name": "Evaluate Runtime Protection",
                "description": "Assess runtime application security monitoring and protection mechanisms",
                "expected_output": "Runtime security assessment with monitoring capabilities and threat detection effectiveness"
            }
        ]

# Quality Assurance Pattern Implementations

class CodeQualityAssessmentPattern(AuditingPattern):
    """Code Quality Assessment auditing pattern."""
    
    def __init__(self):
        """Initialize the code quality assessment pattern."""
        super().__init__(
            name=AuditingPatternType.CODE_QUALITY_ASSESSMENT.value,
            description="Comprehensive evaluation of code quality metrics, standards compliance, and maintainability"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate code quality assessment audit steps."""
        return [
            {
                "type": "codebase_analysis",
                "name": "Analyze Codebase Structure",
                "description": f"Examine the overall structure and organization of {scope} codebase",
                "expected_output": "Codebase structure analysis with architecture assessment and organization metrics"
            },
            {
                "type": "coding_standards",
                "name": "Assess Coding Standards Compliance",
                "description": "Evaluate adherence to coding standards, style guides, and best practices",
                "expected_output": "Coding standards compliance report with violations and improvement recommendations"
            },
            {
                "type": "complexity_analysis",
                "name": "Analyze Code Complexity",
                "description": "Measure cyclomatic complexity, cognitive complexity, and maintainability metrics",
                "expected_output": "Code complexity analysis with hotspots identification and refactoring recommendations"
            },
            {
                "type": "duplication_detection",
                "name": "Detect Code Duplication",
                "description": "Identify duplicated code blocks and assess code reuse opportunities",
                "expected_output": "Code duplication report with consolidation opportunities and refactoring suggestions"
            },
            {
                "type": "technical_debt",
                "name": "Assess Technical Debt",
                "description": "Evaluate technical debt accumulation and maintenance burden",
                "expected_output": "Technical debt assessment with prioritized remediation roadmap and impact analysis"
            },
            {
                "type": "code_coverage",
                "name": "Analyze Code Coverage",
                "description": "Review test coverage metrics and identify untested code areas",
                "expected_output": "Code coverage analysis with gap identification and testing recommendations"
            },
            {
                "type": "security_analysis",
                "name": "Conduct Security Code Analysis",
                "description": "Perform static analysis for security vulnerabilities and unsafe patterns",
                "expected_output": "Security code analysis with vulnerability identification and remediation guidance"
            },
            {
                "type": "performance_analysis",
                "name": "Analyze Performance Patterns",
                "description": "Identify performance anti-patterns and optimization opportunities",
                "expected_output": "Performance analysis with bottleneck identification and optimization recommendations"
            },
            {
                "type": "maintainability_assessment",
                "name": "Assess Code Maintainability",
                "description": "Evaluate code maintainability, readability, and long-term sustainability",
                "expected_output": "Maintainability assessment with improvement strategies and best practice recommendations"
            }
        ]

class TestCoverageAnalysisPattern(AuditingPattern):
    """Test Coverage Analysis auditing pattern."""
    
    def __init__(self):
        """Initialize the test coverage analysis pattern."""
        super().__init__(
            name=AuditingPatternType.TEST_COVERAGE_ANALYSIS.value,
            description="Assessment of test coverage, test quality, and testing strategy effectiveness"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate test coverage analysis audit steps."""
        return [
            {
                "type": "test_inventory",
                "name": "Inventory Test Suite",
                "description": f"Catalog all tests and testing frameworks within {scope}",
                "expected_output": "Test suite inventory with test types, frameworks, and coverage scope"
            },
            {
                "type": "coverage_metrics",
                "name": "Analyze Coverage Metrics",
                "description": "Measure line, branch, and function coverage across the codebase",
                "expected_output": "Coverage metrics report with detailed coverage percentages and gap analysis"
            },
            {
                "type": "test_quality",
                "name": "Assess Test Quality",
                "description": "Evaluate test effectiveness, maintainability, and reliability",
                "expected_output": "Test quality assessment with test effectiveness metrics and improvement recommendations"
            },
            {
                "type": "test_strategy",
                "name": "Review Testing Strategy",
                "description": "Examine testing strategy, test pyramid, and testing approach alignment",
                "expected_output": "Testing strategy evaluation with approach effectiveness and optimization recommendations"
            },
            {
                "type": "critical_path_coverage",
                "name": "Analyze Critical Path Coverage",
                "description": "Assess test coverage of critical business logic and high-risk areas",
                "expected_output": "Critical path coverage analysis with risk-based testing recommendations"
            },
            {
                "type": "test_automation",
                "name": "Evaluate Test Automation",
                "description": "Review test automation coverage, CI/CD integration, and automation effectiveness",
                "expected_output": "Test automation assessment with automation gaps and improvement opportunities"
            },
            {
                "type": "performance_testing",
                "name": "Assess Performance Testing",
                "description": "Evaluate performance testing coverage and load testing strategies",
                "expected_output": "Performance testing assessment with coverage gaps and testing strategy recommendations"
            },
            {
                "type": "security_testing",
                "name": "Review Security Testing",
                "description": "Assess security testing coverage and vulnerability testing practices",
                "expected_output": "Security testing evaluation with coverage assessment and testing enhancement recommendations"
            },
            {
                "type": "test_maintenance",
                "name": "Evaluate Test Maintenance",
                "description": "Assess test maintenance burden, flaky tests, and test suite health",
                "expected_output": "Test maintenance analysis with test suite optimization and reliability improvement recommendations"
            }
        ]

class DocumentationQualityPattern(AuditingPattern):
    """Documentation Quality auditing pattern."""
    
    def __init__(self):
        """Initialize the documentation quality pattern."""
        super().__init__(
            name=AuditingPatternType.DOCUMENTATION_QUALITY.value,
            description="Evaluation of documentation completeness, accuracy, and accessibility"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate documentation quality audit steps."""
        return [
            {
                "type": "documentation_inventory",
                "name": "Inventory Documentation Assets",
                "description": f"Catalog all documentation types and assets within {scope}",
                "expected_output": "Documentation inventory with types, locations, and ownership mapping"
            },
            {
                "type": "completeness_assessment",
                "name": "Assess Documentation Completeness",
                "description": "Evaluate coverage of required documentation areas and identify gaps",
                "expected_output": "Completeness assessment with gap analysis and coverage recommendations"
            },
            {
                "type": "accuracy_verification",
                "name": "Verify Documentation Accuracy",
                "description": "Check documentation accuracy against current system state and requirements",
                "expected_output": "Accuracy verification report with outdated content identification and update requirements"
            },
            {
                "type": "accessibility_review",
                "name": "Review Documentation Accessibility",
                "description": "Assess documentation accessibility, searchability, and user experience",
                "expected_output": "Accessibility assessment with usability improvements and navigation enhancements"
            },
            {
                "type": "standards_compliance",
                "name": "Evaluate Standards Compliance",
                "description": "Check adherence to documentation standards, templates, and style guides",
                "expected_output": "Standards compliance evaluation with consistency improvements and template recommendations"
            },
            {
                "type": "maintenance_process",
                "name": "Assess Maintenance Processes",
                "description": "Review documentation maintenance workflows and update procedures",
                "expected_output": "Maintenance process assessment with workflow optimization and responsibility clarification"
            },
            {
                "type": "user_feedback",
                "name": "Analyze User Feedback",
                "description": "Evaluate user feedback, usage analytics, and documentation effectiveness",
                "expected_output": "User feedback analysis with improvement priorities and user experience enhancements"
            },
            {
                "type": "technical_documentation",
                "name": "Review Technical Documentation",
                "description": "Assess API documentation, code comments, and technical specifications",
                "expected_output": "Technical documentation review with clarity improvements and completeness recommendations"
            },
            {
                "type": "knowledge_management",
                "name": "Evaluate Knowledge Management",
                "description": "Assess knowledge capture, sharing, and retention processes",
                "expected_output": "Knowledge management evaluation with process improvements and knowledge preservation strategies"
            }
        ]

class DependencyManagementPattern(AuditingPattern):
    """Dependency Management auditing pattern."""
    
    def __init__(self):
        """Initialize the dependency management pattern."""
        super().__init__(
            name=AuditingPatternType.DEPENDENCY_MANAGEMENT.value,
            description="Assessment of third-party dependencies, licensing, and security implications"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate dependency management audit steps."""
        return [
            {
                "type": "dependency_inventory",
                "name": "Inventory Dependencies",
                "description": f"Catalog all third-party dependencies and libraries in {scope}",
                "expected_output": "Comprehensive dependency inventory with versions, sources, and usage mapping"
            },
            {
                "type": "vulnerability_scanning",
                "name": "Scan for Vulnerabilities",
                "description": "Identify known security vulnerabilities in dependencies",
                "expected_output": "Vulnerability scan results with severity ratings and remediation recommendations"
            },
            {
                "type": "license_compliance",
                "name": "Assess License Compliance",
                "description": "Review dependency licenses for compliance and compatibility",
                "expected_output": "License compliance assessment with risk analysis and policy adherence verification"
            },
            {
                "type": "version_management",
                "name": "Evaluate Version Management",
                "description": "Assess dependency versioning strategy and update practices",
                "expected_output": "Version management evaluation with update policies and maintenance recommendations"
            },
            {
                "type": "supply_chain_security",
                "name": "Assess Supply Chain Security",
                "description": "Evaluate dependency sources, integrity verification, and supply chain risks",
                "expected_output": "Supply chain security assessment with risk mitigation and verification improvements"
            },
            {
                "type": "dependency_health",
                "name": "Analyze Dependency Health",
                "description": "Assess dependency maintenance status, community support, and longevity",
                "expected_output": "Dependency health analysis with sustainability assessment and replacement recommendations"
            },
            {
                "type": "usage_optimization",
                "name": "Optimize Dependency Usage",
                "description": "Identify unused dependencies and optimization opportunities",
                "expected_output": "Usage optimization report with cleanup recommendations and dependency reduction strategies"
            },
            {
                "type": "update_strategy",
                "name": "Review Update Strategy",
                "description": "Evaluate dependency update processes and automation",
                "expected_output": "Update strategy assessment with automation recommendations and maintenance workflow improvements"
            },
            {
                "type": "risk_assessment",
                "name": "Conduct Risk Assessment",
                "description": "Assess overall dependency risk profile and mitigation strategies",
                "expected_output": "Dependency risk assessment with mitigation strategies and monitoring recommendations"
            }
        ]

class PerformanceQualityPattern(AuditingPattern):
    """Performance Quality auditing pattern."""
    
    def __init__(self):
        """Initialize the performance quality pattern."""
        super().__init__(
            name=AuditingPatternType.PERFORMANCE_QUALITY.value,
            description="Evaluation of system performance characteristics, bottlenecks, and optimization opportunities"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate performance quality audit steps."""
        return [
            {
                "type": "performance_baseline",
                "name": "Establish Performance Baseline",
                "description": f"Define performance baselines and benchmarks for {scope}",
                "expected_output": "Performance baseline documentation with key metrics and acceptable thresholds"
            },
            {
                "type": "load_testing",
                "name": "Conduct Load Testing",
                "description": "Perform load testing to assess system performance under various conditions",
                "expected_output": "Load testing results with performance metrics and capacity analysis"
            },
            {
                "type": "bottleneck_analysis",
                "name": "Identify Performance Bottlenecks",
                "description": "Analyze system components to identify performance bottlenecks and constraints",
                "expected_output": "Bottleneck analysis with root cause identification and optimization priorities"
            },
            {
                "type": "resource_utilization",
                "name": "Analyze Resource Utilization",
                "description": "Assess CPU, memory, disk, and network resource utilization patterns",
                "expected_output": "Resource utilization analysis with optimization recommendations and capacity planning"
            },
            {
                "type": "response_time_analysis",
                "name": "Analyze Response Times",
                "description": "Evaluate system response times and latency characteristics",
                "expected_output": "Response time analysis with latency distribution and improvement recommendations"
            },
            {
                "type": "scalability_assessment",
                "name": "Assess Scalability",
                "description": "Evaluate system scalability and performance under increasing load",
                "expected_output": "Scalability assessment with scaling limitations and architecture recommendations"
            },
            {
                "type": "caching_strategy",
                "name": "Review Caching Strategy",
                "description": "Assess caching implementation and effectiveness",
                "expected_output": "Caching strategy evaluation with optimization opportunities and implementation improvements"
            },
            {
                "type": "database_performance",
                "name": "Analyze Database Performance",
                "description": "Evaluate database query performance and optimization opportunities",
                "expected_output": "Database performance analysis with query optimization and indexing recommendations"
            },
            {
                "type": "monitoring_alerting",
                "name": "Review Performance Monitoring",
                "description": "Assess performance monitoring and alerting capabilities",
                "expected_output": "Performance monitoring evaluation with alerting improvements and observability enhancements"
            }
        ]

class UserExperienceAuditPattern(AuditingPattern):
    """User Experience Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the user experience audit pattern."""
        super().__init__(
            name=AuditingPatternType.USER_EXPERIENCE_AUDIT.value,
            description="Assessment of user interface design, usability, and accessibility compliance"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate user experience audit steps."""
        return [
            {
                "type": "usability_assessment",
                "name": "Conduct Usability Assessment",
                "description": f"Evaluate user interface usability and user experience for {scope}",
                "expected_output": "Usability assessment with user journey analysis and improvement recommendations"
            },
            {
                "type": "accessibility_compliance",
                "name": "Assess Accessibility Compliance",
                "description": "Evaluate compliance with accessibility standards (WCAG, ADA)",
                "expected_output": "Accessibility compliance report with violations and remediation requirements"
            },
            {
                "type": "design_consistency",
                "name": "Review Design Consistency",
                "description": "Assess design system adherence and visual consistency",
                "expected_output": "Design consistency evaluation with style guide compliance and standardization recommendations"
            },
            {
                "type": "user_feedback_analysis",
                "name": "Analyze User Feedback",
                "description": "Review user feedback, support tickets, and satisfaction metrics",
                "expected_output": "User feedback analysis with pain point identification and improvement priorities"
            },
            {
                "type": "navigation_assessment",
                "name": "Assess Navigation and Information Architecture",
                "description": "Evaluate site navigation, information architecture, and findability",
                "expected_output": "Navigation assessment with information architecture improvements and user flow optimization"
            },
            {
                "type": "mobile_responsiveness",
                "name": "Review Mobile Responsiveness",
                "description": "Assess mobile and responsive design implementation",
                "expected_output": "Mobile responsiveness evaluation with cross-device compatibility and optimization recommendations"
            },
            {
                "type": "performance_ux",
                "name": "Evaluate Performance Impact on UX",
                "description": "Assess how performance affects user experience and satisfaction",
                "expected_output": "Performance UX analysis with loading time optimization and user experience improvements"
            },
            {
                "type": "conversion_optimization",
                "name": "Analyze Conversion Optimization",
                "description": "Evaluate conversion funnels and user engagement metrics",
                "expected_output": "Conversion analysis with optimization opportunities and user engagement improvements"
            },
            {
                "type": "user_testing",
                "name": "Review User Testing Practices",
                "description": "Assess user testing methodologies and feedback incorporation",
                "expected_output": "User testing evaluation with methodology improvements and feedback integration recommendations"
            }
        ]

class DataQualityAssessmentPattern(AuditingPattern):
    """Data Quality Assessment auditing pattern."""
    
    def __init__(self):
        """Initialize the data quality assessment pattern."""
        super().__init__(
            name=AuditingPatternType.DATA_QUALITY_ASSESSMENT.value,
            description="Evaluation of data accuracy, completeness, consistency, and integrity"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate data quality assessment audit steps."""
        return [
            {
                "type": "data_profiling",
                "name": "Conduct Data Profiling",
                "description": f"Profile data sources and analyze data characteristics within {scope}",
                "expected_output": "Data profiling report with data distribution, patterns, and quality metrics"
            },
            {
                "type": "accuracy_assessment",
                "name": "Assess Data Accuracy",
                "description": "Evaluate data accuracy against source systems and business rules",
                "expected_output": "Data accuracy assessment with error identification and correction recommendations"
            },
            {
                "type": "completeness_analysis",
                "name": "Analyze Data Completeness",
                "description": "Assess data completeness and identify missing or null values",
                "expected_output": "Data completeness analysis with gap identification and data collection improvements"
            },
            {
                "type": "consistency_validation",
                "name": "Validate Data Consistency",
                "description": "Check data consistency across systems and validate referential integrity",
                "expected_output": "Data consistency validation with inconsistency identification and harmonization recommendations"
            },
            {
                "type": "timeliness_evaluation",
                "name": "Evaluate Data Timeliness",
                "description": "Assess data freshness, update frequency, and temporal accuracy",
                "expected_output": "Data timeliness evaluation with latency analysis and refresh optimization recommendations"
            },
            {
                "type": "validity_verification",
                "name": "Verify Data Validity",
                "description": "Validate data against business rules, formats, and constraints",
                "expected_output": "Data validity verification with rule violations and validation improvement recommendations"
            },
            {
                "type": "uniqueness_analysis",
                "name": "Analyze Data Uniqueness",
                "description": "Identify duplicate records and assess data deduplication needs",
                "expected_output": "Data uniqueness analysis with duplicate identification and deduplication strategies"
            },
            {
                "type": "lineage_tracking",
                "name": "Track Data Lineage",
                "description": "Map data lineage and transformation processes",
                "expected_output": "Data lineage documentation with transformation tracking and impact analysis"
            },
            {
                "type": "quality_monitoring",
                "name": "Evaluate Quality Monitoring",
                "description": "Assess data quality monitoring processes and alerting mechanisms",
                "expected_output": "Data quality monitoring evaluation with process improvements and automation recommendations"
            }
        ]

class APIQualityPattern(AuditingPattern):
    """API Quality auditing pattern."""
    
    def __init__(self):
        """Initialize the API quality pattern."""
        super().__init__(
            name=AuditingPatternType.API_QUALITY.value,
            description="Assessment of API design, documentation, security, and performance standards"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate API quality audit steps."""
        return [
            {
                "type": "api_inventory",
                "name": "Inventory API Endpoints",
                "description": f"Catalog all API endpoints and services within {scope}",
                "expected_output": "API inventory with endpoint documentation, versions, and usage patterns"
            },
            {
                "type": "design_standards",
                "name": "Assess API Design Standards",
                "description": "Evaluate API design consistency and adherence to REST/GraphQL standards",
                "expected_output": "API design assessment with standards compliance and consistency recommendations"
            },
            {
                "type": "documentation_quality",
                "name": "Review API Documentation",
                "description": "Assess API documentation completeness, accuracy, and usability",
                "expected_output": "API documentation evaluation with completeness gaps and usability improvements"
            },
            {
                "type": "versioning_strategy",
                "name": "Evaluate Versioning Strategy",
                "description": "Review API versioning approach and backward compatibility",
                "expected_output": "API versioning assessment with strategy improvements and compatibility recommendations"
            },
            {
                "type": "security_assessment",
                "name": "Assess API Security",
                "description": "Evaluate API authentication, authorization, and security controls",
                "expected_output": "API security assessment with vulnerability identification and security enhancement recommendations"
            },
            {
                "type": "performance_testing",
                "name": "Conduct API Performance Testing",
                "description": "Test API performance, throughput, and response times",
                "expected_output": "API performance analysis with bottleneck identification and optimization recommendations"
            },
            {
                "type": "error_handling",
                "name": "Review Error Handling",
                "description": "Assess API error handling, status codes, and error message quality",
                "expected_output": "Error handling evaluation with consistency improvements and user experience enhancements"
            },
            {
                "type": "rate_limiting",
                "name": "Evaluate Rate Limiting",
                "description": "Assess rate limiting implementation and API usage controls",
                "expected_output": "Rate limiting assessment with policy optimization and abuse prevention recommendations"
            },
            {
                "type": "monitoring_analytics",
                "name": "Review API Monitoring and Analytics",
                "description": "Evaluate API monitoring, logging, and usage analytics",
                "expected_output": "API monitoring evaluation with observability improvements and analytics enhancement recommendations"
            }
        ]

class RegulatoryCompliancePattern(AuditingPattern):
    """Regulatory Compliance auditing pattern."""
    
    def __init__(self):
        """Initialize the regulatory compliance pattern."""
        super().__init__(
            name=AuditingPatternType.REGULATORY_COMPLIANCE.value,
            description="Systematic assessment of compliance with industry regulations and standards"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate regulatory compliance audit steps."""
        return [
            {
                "type": "regulation_inventory",
                "name": "Inventory Applicable Regulations",
                "description": f"Identify all regulations applicable to {scope}",
                "expected_output": "Comprehensive regulation inventory with applicability assessment and compliance requirements"
            },
            {
                "type": "compliance_framework",
                "name": "Assess Compliance Framework",
                "description": "Evaluate existing compliance management framework and governance structure",
                "expected_output": "Compliance framework assessment with governance effectiveness and structural recommendations"
            },
            {
                "type": "policy_alignment",
                "name": "Review Policy Alignment",
                "description": "Assess alignment of organizational policies with regulatory requirements",
                "expected_output": "Policy alignment analysis with gap identification and alignment recommendations"
            },
            {
                "type": "control_effectiveness",
                "name": "Evaluate Control Effectiveness",
                "description": "Assess effectiveness of compliance controls and monitoring mechanisms",
                "expected_output": "Control effectiveness evaluation with performance metrics and improvement recommendations"
            },
            {
                "type": "documentation_review",
                "name": "Review Compliance Documentation",
                "description": "Evaluate completeness and accuracy of compliance documentation",
                "expected_output": "Documentation assessment with completeness gaps and quality improvement recommendations"
            },
            {
                "type": "training_awareness",
                "name": "Assess Training and Awareness",
                "description": "Evaluate compliance training programs and staff awareness levels",
                "expected_output": "Training effectiveness assessment with awareness gaps and program enhancement recommendations"
            },
            {
                "type": "monitoring_reporting",
                "name": "Review Monitoring and Reporting",
                "description": "Assess compliance monitoring processes and regulatory reporting mechanisms",
                "expected_output": "Monitoring and reporting evaluation with process improvements and automation opportunities"
            },
            {
                "type": "incident_management",
                "name": "Evaluate Compliance Incident Management",
                "description": "Review processes for managing compliance violations and regulatory incidents",
                "expected_output": "Incident management assessment with response effectiveness and process optimization recommendations"
            },
            {
                "type": "continuous_improvement",
                "name": "Assess Continuous Improvement",
                "description": "Evaluate mechanisms for ongoing compliance improvement and adaptation",
                "expected_output": "Continuous improvement evaluation with maturity assessment and enhancement strategies"
            }
        ]

class PolicyAdherencePattern(AuditingPattern):
    """Policy Adherence auditing pattern."""
    
    def __init__(self):
        """Initialize the policy adherence pattern."""
        super().__init__(
            name=AuditingPatternType.POLICY_ADHERENCE.value,
            description="Evaluation of organizational policy compliance and enforcement effectiveness"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate policy adherence audit steps."""
        return [
            {
                "type": "policy_inventory",
                "name": "Inventory Organizational Policies",
                "description": f"Catalog all policies applicable to {scope}",
                "expected_output": "Policy inventory with categorization, ownership, and applicability mapping"
            },
            {
                "type": "policy_currency",
                "name": "Assess Policy Currency",
                "description": "Evaluate policy update frequency, version control, and relevance",
                "expected_output": "Policy currency assessment with outdated policy identification and update recommendations"
            },
            {
                "type": "communication_effectiveness",
                "name": "Review Policy Communication",
                "description": "Assess policy communication methods and staff awareness levels",
                "expected_output": "Communication effectiveness evaluation with awareness gaps and dissemination improvements"
            },
            {
                "type": "compliance_monitoring",
                "name": "Evaluate Compliance Monitoring",
                "description": "Review mechanisms for monitoring policy adherence and violations",
                "expected_output": "Monitoring mechanism assessment with detection capability and reporting effectiveness"
            },
            {
                "type": "enforcement_consistency",
                "name": "Assess Enforcement Consistency",
                "description": "Evaluate consistency of policy enforcement across the organization",
                "expected_output": "Enforcement consistency analysis with variation identification and standardization recommendations"
            },
            {
                "type": "exception_management",
                "name": "Review Exception Management",
                "description": "Assess processes for managing policy exceptions and waivers",
                "expected_output": "Exception management evaluation with approval processes and risk assessment procedures"
            },
            {
                "type": "training_compliance",
                "name": "Evaluate Training Compliance",
                "description": "Review policy training requirements and completion rates",
                "expected_output": "Training compliance assessment with completion gaps and effectiveness improvements"
            },
            {
                "type": "violation_response",
                "name": "Assess Violation Response",
                "description": "Evaluate processes for responding to policy violations and corrective actions",
                "expected_output": "Violation response assessment with response effectiveness and corrective action tracking"
            },
            {
                "type": "policy_effectiveness",
                "name": "Measure Policy Effectiveness",
                "description": "Assess overall effectiveness of policies in achieving intended outcomes",
                "expected_output": "Policy effectiveness measurement with outcome analysis and optimization recommendations"
            }
        ]

class ChangeManagementAuditPattern(AuditingPattern):
    """Change Management Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the change management audit pattern."""
        super().__init__(
            name=AuditingPatternType.CHANGE_MANAGEMENT_AUDIT.value,
            description="Assessment of change management processes, controls, and documentation"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate change management audit steps."""
        return [
            {
                "type": "process_documentation",
                "name": "Review Change Process Documentation",
                "description": f"Evaluate change management process documentation for {scope}",
                "expected_output": "Process documentation assessment with completeness evaluation and standardization recommendations"
            },
            {
                "type": "approval_workflows",
                "name": "Assess Approval Workflows",
                "description": "Review change approval workflows and authorization mechanisms",
                "expected_output": "Approval workflow evaluation with efficiency analysis and control effectiveness assessment"
            },
            {
                "type": "risk_assessment",
                "name": "Evaluate Change Risk Assessment",
                "description": "Assess risk assessment processes for proposed changes",
                "expected_output": "Risk assessment evaluation with methodology effectiveness and impact analysis quality"
            },
            {
                "type": "testing_validation",
                "name": "Review Testing and Validation",
                "description": "Evaluate change testing procedures and validation requirements",
                "expected_output": "Testing and validation assessment with coverage analysis and quality assurance effectiveness"
            },
            {
                "type": "rollback_procedures",
                "name": "Assess Rollback Procedures",
                "description": "Review rollback and recovery procedures for failed changes",
                "expected_output": "Rollback procedure evaluation with recovery capability and contingency planning assessment"
            },
            {
                "type": "communication_coordination",
                "name": "Evaluate Communication and Coordination",
                "description": "Assess change communication processes and stakeholder coordination",
                "expected_output": "Communication effectiveness evaluation with stakeholder engagement and coordination improvements"
            },
            {
                "type": "change_tracking",
                "name": "Review Change Tracking",
                "description": "Evaluate change tracking systems and audit trail maintenance",
                "expected_output": "Change tracking assessment with audit trail completeness and traceability analysis"
            },
            {
                "type": "post_implementation",
                "name": "Assess Post-Implementation Review",
                "description": "Review post-implementation review processes and lessons learned capture",
                "expected_output": "Post-implementation review evaluation with effectiveness measurement and improvement identification"
            },
            {
                "type": "emergency_changes",
                "name": "Evaluate Emergency Change Procedures",
                "description": "Assess emergency change procedures and expedited approval processes",
                "expected_output": "Emergency change evaluation with risk management and control effectiveness in urgent situations"
            }
        ]

class RiskManagementPattern(AuditingPattern):
    """Risk Management auditing pattern."""
    
    def __init__(self):
        """Initialize the risk management pattern."""
        super().__init__(
            name=AuditingPatternType.RISK_MANAGEMENT.value,
            description="Evaluation of risk identification, assessment, and mitigation processes"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate risk management audit steps."""
        return [
            {
                "type": "risk_framework",
                "name": "Assess Risk Management Framework",
                "description": f"Evaluate risk management framework and governance structure for {scope}",
                "expected_output": "Risk framework assessment with governance effectiveness and structural adequacy evaluation"
            },
            {
                "type": "risk_identification",
                "name": "Review Risk Identification Processes",
                "description": "Assess risk identification methodologies and coverage completeness",
                "expected_output": "Risk identification evaluation with methodology effectiveness and coverage gap analysis"
            },
            {
                "type": "risk_assessment",
                "name": "Evaluate Risk Assessment Methods",
                "description": "Review risk assessment techniques, scoring, and prioritization methods",
                "expected_output": "Risk assessment methodology evaluation with scoring consistency and prioritization effectiveness"
            },
            {
                "type": "risk_register",
                "name": "Review Risk Register Management",
                "description": "Assess risk register maintenance, updates, and information quality",
                "expected_output": "Risk register evaluation with data quality assessment and maintenance process effectiveness"
            },
            {
                "type": "mitigation_strategies",
                "name": "Assess Mitigation Strategies",
                "description": "Evaluate risk mitigation strategies and control implementation",
                "expected_output": "Mitigation strategy assessment with control effectiveness and implementation adequacy"
            },
            {
                "type": "monitoring_reporting",
                "name": "Review Risk Monitoring and Reporting",
                "description": "Assess risk monitoring processes and reporting mechanisms",
                "expected_output": "Monitoring and reporting evaluation with frequency adequacy and stakeholder communication effectiveness"
            },
            {
                "type": "risk_appetite",
                "name": "Evaluate Risk Appetite and Tolerance",
                "description": "Review risk appetite statements and tolerance level definitions",
                "expected_output": "Risk appetite evaluation with tolerance alignment and decision-making guidance assessment"
            },
            {
                "type": "incident_correlation",
                "name": "Assess Risk-Incident Correlation",
                "description": "Evaluate correlation between identified risks and actual incidents",
                "expected_output": "Risk-incident correlation analysis with predictive accuracy and identification improvement recommendations"
            },
            {
                "type": "continuous_improvement",
                "name": "Review Risk Management Maturity",
                "description": "Assess risk management maturity and continuous improvement processes",
                "expected_output": "Risk management maturity evaluation with improvement opportunities and capability enhancement recommendations"
            }
        ]

class AuditTrailPattern(AuditingPattern):
    """Audit Trail auditing pattern."""
    
    def __init__(self):
        """Initialize the audit trail pattern."""
        super().__init__(
            name=AuditingPatternType.AUDIT_TRAIL.value,
            description="Assessment of audit logging, trail completeness, and forensic capabilities"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate audit trail audit steps."""
        return [
            {
                "type": "logging_coverage",
                "name": "Assess Logging Coverage",
                "description": f"Evaluate audit logging coverage across {scope}",
                "expected_output": "Logging coverage assessment with gap identification and completeness evaluation"
            },
            {
                "type": "log_integrity",
                "name": "Review Log Integrity Controls",
                "description": "Assess log integrity protection mechanisms and tamper detection",
                "expected_output": "Log integrity evaluation with protection mechanism effectiveness and tamper detection capabilities"
            },
            {
                "type": "retention_policies",
                "name": "Evaluate Log Retention Policies",
                "description": "Review log retention policies and compliance with regulatory requirements",
                "expected_output": "Retention policy assessment with regulatory compliance and storage optimization recommendations"
            },
            {
                "type": "access_controls",
                "name": "Assess Log Access Controls",
                "description": "Evaluate access controls for audit logs and segregation of duties",
                "expected_output": "Log access control evaluation with privilege management and segregation effectiveness"
            },
            {
                "type": "log_analysis",
                "name": "Review Log Analysis Capabilities",
                "description": "Assess log analysis tools, techniques, and automated monitoring",
                "expected_output": "Log analysis capability assessment with tool effectiveness and automation opportunities"
            },
            {
                "type": "forensic_readiness",
                "name": "Evaluate Forensic Readiness",
                "description": "Assess forensic investigation capabilities and evidence preservation",
                "expected_output": "Forensic readiness evaluation with investigation capability and evidence handling procedures"
            },
            {
                "type": "compliance_reporting",
                "name": "Review Compliance Reporting",
                "description": "Evaluate audit trail reporting for compliance and regulatory requirements",
                "expected_output": "Compliance reporting assessment with regulatory alignment and reporting effectiveness"
            },
            {
                "type": "performance_impact",
                "name": "Assess Performance Impact",
                "description": "Evaluate performance impact of audit logging on system operations",
                "expected_output": "Performance impact analysis with optimization recommendations and resource utilization assessment"
            },
            {
                "type": "alerting_monitoring",
                "name": "Review Alerting and Monitoring",
                "description": "Assess real-time monitoring and alerting based on audit trail analysis",
                "expected_output": "Alerting and monitoring evaluation with detection effectiveness and response time optimization"
            }
        ]

class BusinessContinuityPattern(AuditingPattern):
    """Business Continuity auditing pattern."""
    
    def __init__(self):
        """Initialize the business continuity pattern."""
        super().__init__(
            name=AuditingPatternType.BUSINESS_CONTINUITY.value,
            description="Evaluation of business continuity planning, disaster recovery, and resilience capabilities"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate business continuity audit steps."""
        return [
            {
                "type": "bcp_documentation",
                "name": "Review BCP Documentation",
                "description": f"Evaluate business continuity plan documentation for {scope}",
                "expected_output": "BCP documentation assessment with completeness evaluation and currency verification"
            },
            {
                "type": "risk_assessment",
                "name": "Assess Business Impact Analysis",
                "description": "Review business impact analysis and risk assessment methodologies",
                "expected_output": "Business impact analysis evaluation with risk identification completeness and impact assessment accuracy"
            },
            {
                "type": "recovery_strategies",
                "name": "Evaluate Recovery Strategies",
                "description": "Assess recovery strategies and alternative operating procedures",
                "expected_output": "Recovery strategy evaluation with feasibility assessment and resource requirement analysis"
            },
            {
                "type": "testing_exercises",
                "name": "Review Testing and Exercises",
                "description": "Evaluate BCP testing frequency, scenarios, and exercise effectiveness",
                "expected_output": "Testing and exercise assessment with scenario coverage and improvement identification"
            },
            {
                "type": "communication_plans",
                "name": "Assess Communication Plans",
                "description": "Review crisis communication plans and stakeholder notification procedures",
                "expected_output": "Communication plan evaluation with stakeholder coverage and notification effectiveness"
            },
            {
                "type": "resource_allocation",
                "name": "Evaluate Resource Allocation",
                "description": "Assess resource allocation for business continuity and recovery operations",
                "expected_output": "Resource allocation assessment with adequacy evaluation and optimization recommendations"
            },
            {
                "type": "vendor_dependencies",
                "name": "Review Vendor Dependencies",
                "description": "Evaluate third-party vendor continuity plans and dependency management",
                "expected_output": "Vendor dependency evaluation with continuity assurance and alternative supplier identification"
            },
            {
                "type": "recovery_objectives",
                "name": "Assess Recovery Objectives",
                "description": "Review recovery time objectives (RTO) and recovery point objectives (RPO)",
                "expected_output": "Recovery objective assessment with achievability evaluation and optimization recommendations"
            },
            {
                "type": "plan_maintenance",
                "name": "Evaluate Plan Maintenance",
                "description": "Assess BCP maintenance processes and update procedures",
                "expected_output": "Plan maintenance evaluation with update frequency and change management effectiveness"
            }
        ]

class VendorManagementPattern(AuditingPattern):
    """Vendor Management auditing pattern."""
    
    def __init__(self):
        """Initialize the vendor management pattern."""
        super().__init__(
            name=AuditingPatternType.VENDOR_MANAGEMENT.value,
            description="Assessment of third-party vendor relationships, contracts, and risk management"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate vendor management audit steps."""
        return [
            {
                "type": "vendor_inventory",
                "name": "Inventory Vendor Relationships",
                "description": f"Catalog all vendor relationships and dependencies within {scope}",
                "expected_output": "Vendor inventory with relationship categorization, criticality assessment, and dependency mapping"
            },
            {
                "type": "due_diligence",
                "name": "Assess Vendor Due Diligence",
                "description": "Review vendor selection and due diligence processes",
                "expected_output": "Due diligence evaluation with selection criteria effectiveness and risk assessment adequacy"
            },
            {
                "type": "contract_management",
                "name": "Evaluate Contract Management",
                "description": "Assess vendor contract terms, conditions, and lifecycle management",
                "expected_output": "Contract management assessment with terms adequacy and lifecycle process effectiveness"
            },
            {
                "type": "performance_monitoring",
                "name": "Review Performance Monitoring",
                "description": "Evaluate vendor performance monitoring and SLA compliance tracking",
                "expected_output": "Performance monitoring evaluation with SLA effectiveness and compliance measurement accuracy"
            },
            {
                "type": "risk_assessment",
                "name": "Assess Vendor Risk Management",
                "description": "Review vendor risk assessment and ongoing risk monitoring processes",
                "expected_output": "Vendor risk management evaluation with risk identification completeness and mitigation effectiveness"
            },
            {
                "type": "security_compliance",
                "name": "Evaluate Security and Compliance",
                "description": "Assess vendor security controls and regulatory compliance requirements",
                "expected_output": "Security and compliance evaluation with control adequacy and regulatory alignment assessment"
            },
            {
                "type": "data_protection",
                "name": "Review Data Protection",
                "description": "Evaluate vendor data handling, protection, and privacy compliance",
                "expected_output": "Data protection assessment with handling procedures and privacy compliance verification"
            },
            {
                "type": "business_continuity",
                "name": "Assess Vendor Business Continuity",
                "description": "Review vendor business continuity capabilities and disaster recovery plans",
                "expected_output": "Vendor business continuity evaluation with resilience assessment and recovery capability verification"
            },
            {
                "type": "termination_procedures",
                "name": "Evaluate Termination Procedures",
                "description": "Assess vendor termination procedures and data/asset recovery processes",
                "expected_output": "Termination procedure evaluation with data recovery effectiveness and transition planning adequacy"
            }
        ]

class DataGovernancePattern(AuditingPattern):
    """Data Governance auditing pattern."""
    
    def __init__(self):
        """Initialize the data governance pattern."""
        super().__init__(
            name=AuditingPatternType.DATA_GOVERNANCE.value,
            description="Evaluation of data governance frameworks, stewardship, and lifecycle management"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate data governance audit steps."""
        return [
            {
                "type": "governance_framework",
                "name": "Assess Data Governance Framework",
                "description": f"Evaluate data governance framework and organizational structure for {scope}",
                "expected_output": "Governance framework assessment with organizational effectiveness and role clarity evaluation"
            },
            {
                "type": "data_stewardship",
                "name": "Review Data Stewardship",
                "description": "Assess data stewardship roles, responsibilities, and accountability mechanisms",
                "expected_output": "Data stewardship evaluation with role effectiveness and accountability mechanism assessment"
            },
            {
                "type": "data_classification",
                "name": "Evaluate Data Classification",
                "description": "Review data classification schemes and sensitivity labeling processes",
                "expected_output": "Data classification assessment with scheme adequacy and labeling process effectiveness"
            },
            {
                "type": "lifecycle_management",
                "name": "Assess Data Lifecycle Management",
                "description": "Evaluate data lifecycle management processes from creation to disposal",
                "expected_output": "Lifecycle management evaluation with process completeness and stage transition effectiveness"
            },
            {
                "type": "quality_management",
                "name": "Review Data Quality Management",
                "description": "Assess data quality standards, monitoring, and improvement processes",
                "expected_output": "Data quality management evaluation with standards effectiveness and improvement process adequacy"
            },
            {
                "type": "privacy_protection",
                "name": "Evaluate Privacy Protection",
                "description": "Review data privacy controls and personal data protection mechanisms",
                "expected_output": "Privacy protection assessment with control effectiveness and regulatory compliance verification"
            },
            {
                "type": "access_controls",
                "name": "Assess Data Access Controls",
                "description": "Evaluate data access controls and authorization mechanisms",
                "expected_output": "Data access control evaluation with authorization effectiveness and principle of least privilege compliance"
            },
            {
                "type": "retention_disposal",
                "name": "Review Retention and Disposal",
                "description": "Assess data retention policies and secure disposal procedures",
                "expected_output": "Retention and disposal evaluation with policy compliance and disposal security effectiveness"
            },
            {
                "type": "compliance_monitoring",
                "name": "Evaluate Compliance Monitoring",
                "description": "Review data governance compliance monitoring and reporting mechanisms",
                "expected_output": "Compliance monitoring evaluation with detection effectiveness and reporting adequacy assessment"
            }
        ]

class SystemPerformancePattern(AuditingPattern):
    """System Performance auditing pattern."""
    
    def __init__(self):
        """Initialize the system performance pattern."""
        super().__init__(
            name=AuditingPatternType.SYSTEM_PERFORMANCE.value,
            description="Comprehensive assessment of system performance, capacity, and scalability"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate system performance audit steps."""
        return [
            {
                "type": "performance_baseline",
                "name": "Establish Performance Baseline",
                "description": f"Establish performance baselines and benchmarks for {scope}",
                "expected_output": "Performance baseline documentation with key metrics, thresholds, and historical trends"
            },
            {
                "type": "capacity_analysis",
                "name": "Conduct Capacity Analysis",
                "description": "Analyze system capacity utilization and growth projections",
                "expected_output": "Capacity analysis with utilization patterns, bottlenecks, and scaling recommendations"
            },
            {
                "type": "scalability_assessment",
                "name": "Assess Scalability Architecture",
                "description": "Evaluate system scalability design and horizontal/vertical scaling capabilities",
                "expected_output": "Scalability assessment with architecture evaluation and scaling strategy recommendations"
            },
            {
                "type": "load_testing",
                "name": "Review Load Testing Results",
                "description": "Analyze load testing methodologies and performance under stress conditions",
                "expected_output": "Load testing evaluation with stress test results and performance degradation analysis"
            },
            {
                "type": "response_time_analysis",
                "name": "Analyze Response Times",
                "description": "Evaluate system response times and latency across different components",
                "expected_output": "Response time analysis with latency measurements and optimization opportunities"
            },
            {
                "type": "throughput_evaluation",
                "name": "Evaluate System Throughput",
                "description": "Assess system throughput capabilities and transaction processing rates",
                "expected_output": "Throughput evaluation with processing capacity and performance optimization recommendations"
            },
            {
                "type": "resource_contention",
                "name": "Identify Resource Contention",
                "description": "Analyze resource contention issues and performance bottlenecks",
                "expected_output": "Resource contention analysis with bottleneck identification and resolution strategies"
            },
            {
                "type": "performance_monitoring",
                "name": "Review Performance Monitoring",
                "description": "Evaluate performance monitoring tools and alerting mechanisms",
                "expected_output": "Performance monitoring assessment with tool effectiveness and alerting optimization"
            },
            {
                "type": "optimization_opportunities",
                "name": "Identify Optimization Opportunities",
                "description": "Identify performance optimization opportunities and improvement strategies",
                "expected_output": "Optimization roadmap with prioritized improvements and expected performance gains"
            }
        ]

class ResourceUtilizationPattern(AuditingPattern):
    """Resource Utilization auditing pattern."""
    
    def __init__(self):
        """Initialize the resource utilization pattern."""
        super().__init__(
            name=AuditingPatternType.RESOURCE_UTILIZATION.value,
            description="Evaluation of resource usage efficiency, optimization opportunities, and cost management"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate resource utilization audit steps."""
        return [
            {
                "type": "resource_inventory",
                "name": "Inventory Resource Assets",
                "description": f"Catalog all resource assets and their utilization within {scope}",
                "expected_output": "Resource inventory with asset categorization, utilization rates, and cost allocation"
            },
            {
                "type": "utilization_analysis",
                "name": "Analyze Utilization Patterns",
                "description": "Analyze resource utilization patterns and identify underutilized assets",
                "expected_output": "Utilization analysis with usage patterns, peak/off-peak trends, and efficiency metrics"
            },
            {
                "type": "cost_efficiency",
                "name": "Assess Cost Efficiency",
                "description": "Evaluate cost efficiency of resource allocation and spending patterns",
                "expected_output": "Cost efficiency assessment with spending analysis and optimization recommendations"
            },
            {
                "type": "rightsizing_opportunities",
                "name": "Identify Rightsizing Opportunities",
                "description": "Identify opportunities for resource rightsizing and capacity optimization",
                "expected_output": "Rightsizing analysis with over/under-provisioned resources and optimization strategies"
            },
            {
                "type": "allocation_policies",
                "name": "Review Allocation Policies",
                "description": "Evaluate resource allocation policies and governance mechanisms",
                "expected_output": "Allocation policy assessment with governance effectiveness and policy optimization"
            },
            {
                "type": "waste_identification",
                "name": "Identify Resource Waste",
                "description": "Identify resource waste, redundancies, and elimination opportunities",
                "expected_output": "Waste analysis with redundancy identification and elimination strategies"
            },
            {
                "type": "automation_opportunities",
                "name": "Assess Automation Opportunities",
                "description": "Evaluate opportunities for resource management automation",
                "expected_output": "Automation assessment with implementation opportunities and efficiency gains"
            },
            {
                "type": "forecasting_planning",
                "name": "Review Forecasting and Planning",
                "description": "Assess resource forecasting accuracy and capacity planning processes",
                "expected_output": "Forecasting evaluation with planning accuracy and methodology improvements"
            },
            {
                "type": "sustainability_impact",
                "name": "Evaluate Sustainability Impact",
                "description": "Assess environmental impact and sustainability of resource utilization",
                "expected_output": "Sustainability assessment with environmental impact and green optimization opportunities"
            }
        ]

class AvailabilityReliabilityPattern(AuditingPattern):
    """Availability and Reliability auditing pattern."""
    
    def __init__(self):
        """Initialize the availability and reliability pattern."""
        super().__init__(
            name=AuditingPatternType.AVAILABILITY_RELIABILITY.value,
            description="Assessment of system availability, reliability metrics, and uptime performance"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate availability and reliability audit steps."""
        return [
            {
                "type": "sla_compliance",
                "name": "Assess SLA Compliance",
                "description": f"Evaluate service level agreement compliance and availability targets for {scope}",
                "expected_output": "SLA compliance assessment with availability metrics and target achievement analysis"
            },
            {
                "type": "uptime_analysis",
                "name": "Analyze Uptime Performance",
                "description": "Analyze system uptime performance and downtime patterns",
                "expected_output": "Uptime analysis with availability statistics, downtime trends, and improvement opportunities"
            },
            {
                "type": "reliability_metrics",
                "name": "Review Reliability Metrics",
                "description": "Evaluate reliability metrics including MTBF, MTTR, and failure rates",
                "expected_output": "Reliability metrics assessment with performance indicators and benchmark comparisons"
            },
            {
                "type": "fault_tolerance",
                "name": "Assess Fault Tolerance",
                "description": "Evaluate fault tolerance mechanisms and system resilience capabilities",
                "expected_output": "Fault tolerance evaluation with resilience assessment and single point of failure identification"
            },
            {
                "type": "redundancy_analysis",
                "name": "Analyze Redundancy Implementation",
                "description": "Assess redundancy implementation and failover capabilities",
                "expected_output": "Redundancy analysis with failover effectiveness and redundancy optimization recommendations"
            },
            {
                "type": "incident_impact",
                "name": "Evaluate Incident Impact",
                "description": "Analyze incident impact on availability and service delivery",
                "expected_output": "Incident impact analysis with availability correlation and impact reduction strategies"
            },
            {
                "type": "maintenance_windows",
                "name": "Review Maintenance Windows",
                "description": "Evaluate planned maintenance impact and scheduling optimization",
                "expected_output": "Maintenance window assessment with scheduling effectiveness and availability impact minimization"
            },
            {
                "type": "monitoring_alerting",
                "name": "Assess Monitoring and Alerting",
                "description": "Evaluate availability monitoring and proactive alerting mechanisms",
                "expected_output": "Monitoring and alerting evaluation with detection effectiveness and response time optimization"
            },
            {
                "type": "improvement_strategies",
                "name": "Identify Improvement Strategies",
                "description": "Identify strategies for improving availability and reliability performance",
                "expected_output": "Improvement strategy roadmap with prioritized initiatives and expected availability gains"
            }
        ]

class MonitoringAlertingPattern(AuditingPattern):
    """Monitoring and Alerting auditing pattern."""
    
    def __init__(self):
        """Initialize the monitoring and alerting pattern."""
        super().__init__(
            name=AuditingPatternType.MONITORING_ALERTING.value,
            description="Evaluation of monitoring systems, alerting mechanisms, and observability practices"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate monitoring and alerting audit steps."""
        return [
            {
                "type": "monitoring_coverage",
                "name": "Assess Monitoring Coverage",
                "description": f"Evaluate monitoring coverage across all components within {scope}",
                "expected_output": "Monitoring coverage assessment with gap identification and completeness evaluation"
            },
            {
                "type": "metrics_collection",
                "name": "Review Metrics Collection",
                "description": "Assess metrics collection strategies and data quality",
                "expected_output": "Metrics collection evaluation with data quality assessment and collection optimization"
            },
            {
                "type": "alerting_rules",
                "name": "Evaluate Alerting Rules",
                "description": "Review alerting rules, thresholds, and notification mechanisms",
                "expected_output": "Alerting rules assessment with threshold optimization and false positive reduction"
            },
            {
                "type": "dashboard_effectiveness",
                "name": "Assess Dashboard Effectiveness",
                "description": "Evaluate monitoring dashboards and visualization effectiveness",
                "expected_output": "Dashboard effectiveness evaluation with usability assessment and visualization improvements"
            },
            {
                "type": "incident_correlation",
                "name": "Review Incident Correlation",
                "description": "Assess incident correlation capabilities and root cause analysis support",
                "expected_output": "Incident correlation evaluation with analysis capability and correlation accuracy assessment"
            },
            {
                "type": "response_automation",
                "name": "Evaluate Response Automation",
                "description": "Assess automated response capabilities and self-healing mechanisms",
                "expected_output": "Response automation evaluation with automation effectiveness and self-healing capability assessment"
            },
            {
                "type": "observability_maturity",
                "name": "Assess Observability Maturity",
                "description": "Evaluate overall observability maturity and monitoring strategy",
                "expected_output": "Observability maturity assessment with capability evaluation and strategic improvement recommendations"
            },
            {
                "type": "tool_integration",
                "name": "Review Tool Integration",
                "description": "Assess monitoring tool integration and data correlation capabilities",
                "expected_output": "Tool integration evaluation with interoperability assessment and integration optimization"
            },
            {
                "type": "performance_impact",
                "name": "Evaluate Performance Impact",
                "description": "Assess performance impact of monitoring systems on production environments",
                "expected_output": "Performance impact analysis with monitoring overhead assessment and optimization recommendations"
            }
        ]

class BackupRecoveryPattern(AuditingPattern):
    """Backup and Recovery auditing pattern."""
    
    def __init__(self):
        """Initialize the backup and recovery pattern."""
        super().__init__(
            name=AuditingPatternType.BACKUP_RECOVERY.value,
            description="Assessment of backup strategies, recovery procedures, and data protection effectiveness"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate backup and recovery audit steps."""
        return [
            {
                "type": "backup_strategy",
                "name": "Assess Backup Strategy",
                "description": f"Evaluate backup strategy and data protection approach for {scope}",
                "expected_output": "Backup strategy assessment with approach evaluation and coverage completeness"
            },
            {
                "type": "backup_frequency",
                "name": "Review Backup Frequency",
                "description": "Assess backup frequency and scheduling optimization",
                "expected_output": "Backup frequency evaluation with scheduling effectiveness and RPO alignment"
            },
            {
                "type": "recovery_procedures",
                "name": "Evaluate Recovery Procedures",
                "description": "Review recovery procedures and restoration processes",
                "expected_output": "Recovery procedure assessment with process effectiveness and RTO compliance"
            },
            {
                "type": "backup_integrity",
                "name": "Assess Backup Integrity",
                "description": "Evaluate backup integrity verification and validation processes",
                "expected_output": "Backup integrity assessment with validation effectiveness and data corruption detection"
            },
            {
                "type": "recovery_testing",
                "name": "Review Recovery Testing",
                "description": "Assess recovery testing frequency and test scenario coverage",
                "expected_output": "Recovery testing evaluation with test coverage and restoration success rates"
            },
            {
                "type": "storage_management",
                "name": "Evaluate Storage Management",
                "description": "Review backup storage management and retention policies",
                "expected_output": "Storage management assessment with retention policy compliance and storage optimization"
            },
            {
                "type": "security_controls",
                "name": "Assess Backup Security",
                "description": "Evaluate backup security controls and encryption implementation",
                "expected_output": "Backup security assessment with encryption effectiveness and access control evaluation"
            },
            {
                "type": "disaster_recovery",
                "name": "Review Disaster Recovery Integration",
                "description": "Assess integration with disaster recovery plans and procedures",
                "expected_output": "Disaster recovery integration evaluation with plan alignment and recovery coordination"
            },
            {
                "type": "automation_monitoring",
                "name": "Evaluate Automation and Monitoring",
                "description": "Assess backup automation and monitoring capabilities",
                "expected_output": "Automation and monitoring evaluation with process efficiency and failure detection capabilities"
            }
        ]

class OperationalExcellencePattern(AuditingPattern):
    """Operational Excellence auditing pattern."""
    
    def __init__(self):
        """Initialize the operational excellence pattern."""
        super().__init__(
            name=AuditingPatternType.OPERATIONAL_EXCELLENCE.value,
            description="Evaluation of operational processes, automation, and continuous improvement practices"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate operational excellence audit steps."""
        return [
            {
                "type": "process_maturity",
                "name": "Assess Process Maturity",
                "description": f"Evaluate operational process maturity and standardization within {scope}",
                "expected_output": "Process maturity assessment with standardization evaluation and maturity level analysis"
            },
            {
                "type": "automation_coverage",
                "name": "Review Automation Coverage",
                "description": "Assess automation coverage and manual process elimination opportunities",
                "expected_output": "Automation coverage evaluation with manual process identification and automation opportunities"
            },
            {
                "type": "efficiency_metrics",
                "name": "Evaluate Efficiency Metrics",
                "description": "Review operational efficiency metrics and performance indicators",
                "expected_output": "Efficiency metrics assessment with performance indicator analysis and benchmark comparisons"
            },
            {
                "type": "continuous_improvement",
                "name": "Assess Continuous Improvement",
                "description": "Evaluate continuous improvement processes and innovation practices",
                "expected_output": "Continuous improvement evaluation with process effectiveness and innovation capability assessment"
            },
            {
                "type": "knowledge_management",
                "name": "Review Knowledge Management",
                "description": "Assess knowledge management practices and documentation quality",
                "expected_output": "Knowledge management assessment with documentation quality and knowledge sharing effectiveness"
            },
            {
                "type": "skill_development",
                "name": "Evaluate Skill Development",
                "description": "Review staff skill development and competency management programs",
                "expected_output": "Skill development evaluation with competency assessment and training effectiveness"
            },
            {
                "type": "quality_assurance",
                "name": "Assess Quality Assurance",
                "description": "Evaluate quality assurance processes and error prevention mechanisms",
                "expected_output": "Quality assurance assessment with error prevention effectiveness and quality improvement strategies"
            },
            {
                "type": "collaboration_tools",
                "name": "Review Collaboration Tools",
                "description": "Assess collaboration tools and communication effectiveness",
                "expected_output": "Collaboration tools evaluation with communication effectiveness and tool optimization"
            },
            {
                "type": "performance_culture",
                "name": "Evaluate Performance Culture",
                "description": "Assess performance culture and operational excellence mindset",
                "expected_output": "Performance culture evaluation with cultural assessment and excellence mindset development"
            }
        ]

class InfrastructureAuditPattern(AuditingPattern):
    """Infrastructure Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the infrastructure audit pattern."""
        super().__init__(
            name=AuditingPatternType.INFRASTRUCTURE_AUDIT.value,
            description="Comprehensive assessment of infrastructure components, configurations, and lifecycle management"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate infrastructure audit steps."""
        return [
            {
                "type": "infrastructure_inventory",
                "name": "Inventory Infrastructure Components",
                "description": f"Catalog all infrastructure components and dependencies within {scope}",
                "expected_output": "Infrastructure inventory with component categorization, dependencies, and lifecycle status"
            },
            {
                "type": "configuration_management",
                "name": "Assess Configuration Management",
                "description": "Evaluate configuration management practices and standardization",
                "expected_output": "Configuration management assessment with standardization evaluation and drift detection"
            },
            {
                "type": "lifecycle_management",
                "name": "Review Lifecycle Management",
                "description": "Assess infrastructure lifecycle management and refresh planning",
                "expected_output": "Lifecycle management evaluation with refresh planning and end-of-life risk assessment"
            },
            {
                "type": "capacity_planning",
                "name": "Evaluate Capacity Planning",
                "description": "Review infrastructure capacity planning and growth management",
                "expected_output": "Capacity planning assessment with growth projections and scaling strategy evaluation"
            },
            {
                "type": "security_hardening",
                "name": "Assess Security Hardening",
                "description": "Evaluate infrastructure security hardening and baseline compliance",
                "expected_output": "Security hardening assessment with baseline compliance and vulnerability identification"
            },
            {
                "type": "patch_management",
                "name": "Review Patch Management",
                "description": "Assess patch management processes and vulnerability remediation",
                "expected_output": "Patch management evaluation with remediation effectiveness and compliance assessment"
            },
            {
                "type": "monitoring_instrumentation",
                "name": "Evaluate Monitoring Instrumentation",
                "description": "Review infrastructure monitoring and instrumentation coverage",
                "expected_output": "Monitoring instrumentation assessment with coverage evaluation and visibility optimization"
            },
            {
                "type": "automation_orchestration",
                "name": "Assess Automation and Orchestration",
                "description": "Evaluate infrastructure automation and orchestration capabilities",
                "expected_output": "Automation and orchestration evaluation with capability assessment and efficiency improvements"
            },
            {
                "type": "documentation_standards",
                "name": "Review Documentation Standards",
                "description": "Assess infrastructure documentation quality and maintenance standards",
                "expected_output": "Documentation standards assessment with quality evaluation and maintenance process effectiveness"
            }
        ]

class CloudSecurityPattern(AuditingPattern):
    """Cloud Security auditing pattern."""
    
    def __init__(self):
        """Initialize the cloud security pattern."""
        super().__init__(
            name=AuditingPatternType.CLOUD_SECURITY.value,
            description="Assessment of cloud infrastructure security, configuration, and compliance"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate cloud security audit steps."""
        return [
            {
                "type": "cloud_posture",
                "name": "Assess Cloud Security Posture",
                "description": f"Evaluate overall cloud security posture and configuration for {scope}",
                "expected_output": "Cloud security posture assessment with configuration evaluation and security gap identification"
            },
            {
                "type": "identity_access",
                "name": "Review Cloud Identity and Access",
                "description": "Assess cloud identity and access management implementation",
                "expected_output": "Cloud IAM assessment with access control evaluation and privilege management analysis"
            },
            {
                "type": "data_protection",
                "name": "Evaluate Cloud Data Protection",
                "description": "Review cloud data protection mechanisms and encryption implementation",
                "expected_output": "Cloud data protection assessment with encryption effectiveness and data security evaluation"
            },
            {
                "type": "network_security",
                "name": "Assess Cloud Network Security",
                "description": "Evaluate cloud network security controls and segmentation",
                "expected_output": "Cloud network security assessment with segmentation effectiveness and traffic control evaluation"
            },
            {
                "type": "compliance_governance",
                "name": "Review Compliance and Governance",
                "description": "Assess cloud compliance frameworks and governance implementation",
                "expected_output": "Cloud compliance assessment with governance effectiveness and regulatory alignment"
            },
            {
                "type": "monitoring_logging",
                "name": "Evaluate Cloud Monitoring and Logging",
                "description": "Review cloud monitoring, logging, and audit trail capabilities",
                "expected_output": "Cloud monitoring evaluation with logging effectiveness and audit trail completeness"
            },
            {
                "type": "incident_response",
                "name": "Assess Cloud Incident Response",
                "description": "Evaluate cloud-specific incident response capabilities and procedures",
                "expected_output": "Cloud incident response assessment with capability evaluation and response effectiveness"
            },
            {
                "type": "shared_responsibility",
                "name": "Review Shared Responsibility Model",
                "description": "Assess understanding and implementation of cloud shared responsibility model",
                "expected_output": "Shared responsibility assessment with model understanding and responsibility allocation clarity"
            },
            {
                "type": "cost_security_optimization",
                "name": "Evaluate Cost and Security Optimization",
                "description": "Assess balance between cloud security controls and cost optimization",
                "expected_output": "Cost-security optimization assessment with balance evaluation and optimization recommendations"
            }
        ]

class DevOpsPipelinePattern(AuditingPattern):
    """DevOps Pipeline auditing pattern."""
    
    def __init__(self):
        """Initialize the DevOps pipeline pattern."""
        super().__init__(
            name=AuditingPatternType.DEVOPS_PIPELINE.value,
            description="Assessment of CI/CD pipelines, deployment processes, and DevOps maturity"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate DevOps pipeline audit steps."""
        return [
            {
                "type": "pipeline_architecture",
                "name": "Assess Pipeline Architecture",
                "description": f"Evaluate CI/CD pipeline architecture and design for {scope}",
                "expected_output": "Pipeline architecture assessment with design evaluation and scalability analysis"
            },
            {
                "type": "security_integration",
                "name": "Review Security Integration",
                "description": "Assess security controls integration throughout the pipeline",
                "expected_output": "Security integration evaluation with control effectiveness and vulnerability management"
            },
            {
                "type": "automation_coverage",
                "name": "Evaluate Automation Coverage",
                "description": "Review automation coverage and manual intervention requirements",
                "expected_output": "Automation coverage assessment with manual process identification and optimization opportunities"
            },
            {
                "type": "testing_strategy",
                "name": "Assess Testing Strategy",
                "description": "Evaluate testing strategy integration and quality gates",
                "expected_output": "Testing strategy evaluation with quality gate effectiveness and coverage analysis"
            },
            {
                "type": "deployment_practices",
                "name": "Review Deployment Practices",
                "description": "Assess deployment practices and release management processes",
                "expected_output": "Deployment practices assessment with release management effectiveness and rollback capabilities"
            },
            {
                "type": "monitoring_observability",
                "name": "Evaluate Monitoring and Observability",
                "description": "Review pipeline monitoring and observability implementation",
                "expected_output": "Monitoring and observability evaluation with visibility assessment and alerting effectiveness"
            },
            {
                "type": "compliance_governance",
                "name": "Assess Compliance and Governance",
                "description": "Evaluate compliance controls and governance implementation in pipelines",
                "expected_output": "Compliance and governance assessment with control effectiveness and regulatory alignment"
            },
            {
                "type": "performance_optimization",
                "name": "Review Performance Optimization",
                "description": "Assess pipeline performance and optimization opportunities",
                "expected_output": "Performance optimization evaluation with bottleneck identification and efficiency improvements"
            },
            {
                "type": "maturity_assessment",
                "name": "Evaluate DevOps Maturity",
                "description": "Assess overall DevOps maturity and continuous improvement practices",
                "expected_output": "DevOps maturity assessment with capability evaluation and improvement roadmap"
            }
        ]

class ProjectManagementPattern(AuditingPattern):
    """Project Management auditing pattern."""
    
    def __init__(self):
        """Initialize the project management pattern."""
        super().__init__(
            name=AuditingPatternType.PROJECT_MANAGEMENT.value,
            description="Evaluation of project management processes, methodologies, and delivery effectiveness"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate project management audit steps."""
        return [
            {
                "type": "methodology_compliance",
                "name": "Assess Methodology Compliance",
                "description": f"Evaluate project management methodology compliance within {scope}",
                "expected_output": "Methodology compliance assessment with adherence evaluation and process standardization"
            },
            {
                "type": "planning_execution",
                "name": "Review Planning and Execution",
                "description": "Assess project planning processes and execution effectiveness",
                "expected_output": "Planning and execution evaluation with process effectiveness and delivery performance"
            },
            {
                "type": "resource_management",
                "name": "Evaluate Resource Management",
                "description": "Review resource allocation, utilization, and management practices",
                "expected_output": "Resource management assessment with allocation efficiency and utilization optimization"
            },
            {
                "type": "risk_management",
                "name": "Assess Project Risk Management",
                "description": "Evaluate project risk identification, assessment, and mitigation processes",
                "expected_output": "Project risk management evaluation with risk identification completeness and mitigation effectiveness"
            },
            {
                "type": "stakeholder_engagement",
                "name": "Review Stakeholder Engagement",
                "description": "Assess stakeholder engagement and communication effectiveness",
                "expected_output": "Stakeholder engagement evaluation with communication effectiveness and satisfaction assessment"
            },
            {
                "type": "quality_management",
                "name": "Evaluate Quality Management",
                "description": "Review project quality management processes and deliverable quality",
                "expected_output": "Quality management assessment with process effectiveness and deliverable quality evaluation"
            },
            {
                "type": "change_management",
                "name": "Assess Change Management",
                "description": "Evaluate project change management processes and impact assessment",
                "expected_output": "Change management evaluation with process effectiveness and impact assessment accuracy"
            },
            {
                "type": "performance_metrics",
                "name": "Review Performance Metrics",
                "description": "Assess project performance metrics and KPI tracking",
                "expected_output": "Performance metrics evaluation with KPI effectiveness and measurement accuracy"
            },
            {
                "type": "lessons_learned",
                "name": "Evaluate Lessons Learned",
                "description": "Review lessons learned processes and knowledge capture effectiveness",
                "expected_output": "Lessons learned evaluation with knowledge capture effectiveness and improvement implementation"
            }
        ]

class CommunicationAuditPattern(AuditingPattern):
    """Communication Audit auditing pattern."""
    
    def __init__(self):
        """Initialize the communication audit pattern."""
        super().__init__(
            name=AuditingPatternType.COMMUNICATION_AUDIT.value,
            description="Assessment of communication processes, channels, and effectiveness across teams"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate communication audit steps."""
        return [
            {
                "type": "channel_effectiveness",
                "name": "Assess Communication Channels",
                "description": f"Evaluate communication channel effectiveness within {scope}",
                "expected_output": "Communication channel assessment with effectiveness evaluation and optimization recommendations"
            },
            {
                "type": "information_flow",
                "name": "Review Information Flow",
                "description": "Assess information flow patterns and bottleneck identification",
                "expected_output": "Information flow analysis with bottleneck identification and flow optimization strategies"
            },
            {
                "type": "stakeholder_engagement",
                "name": "Evaluate Stakeholder Engagement",
                "description": "Review stakeholder engagement strategies and satisfaction levels",
                "expected_output": "Stakeholder engagement evaluation with satisfaction assessment and engagement improvement strategies"
            },
            {
                "type": "meeting_effectiveness",
                "name": "Assess Meeting Effectiveness",
                "description": "Evaluate meeting processes, outcomes, and efficiency",
                "expected_output": "Meeting effectiveness assessment with efficiency evaluation and process optimization recommendations"
            },
            {
                "type": "documentation_standards",
                "name": "Review Documentation Standards",
                "description": "Assess communication documentation standards and quality",
                "expected_output": "Documentation standards evaluation with quality assessment and standardization improvements"
            },
            {
                "type": "feedback_mechanisms",
                "name": "Evaluate Feedback Mechanisms",
                "description": "Review feedback collection and response mechanisms",
                "expected_output": "Feedback mechanism evaluation with collection effectiveness and response quality assessment"
            },
            {
                "type": "crisis_communication",
                "name": "Assess Crisis Communication",
                "description": "Evaluate crisis communication preparedness and response capabilities",
                "expected_output": "Crisis communication assessment with preparedness evaluation and response effectiveness"
            },
            {
                "type": "cultural_alignment",
                "name": "Review Cultural Alignment",
                "description": "Assess communication cultural alignment and inclusivity",
                "expected_output": "Cultural alignment evaluation with inclusivity assessment and cultural sensitivity improvements"
            },
            {
                "type": "technology_utilization",
                "name": "Evaluate Technology Utilization",
                "description": "Review communication technology utilization and effectiveness",
                "expected_output": "Technology utilization assessment with tool effectiveness and optimization opportunities"
            }
        ]

class TrainingCompetencyPattern(AuditingPattern):
    """Training and Competency auditing pattern."""
    
    def __init__(self):
        """Initialize the training and competency pattern."""
        super().__init__(
            name=AuditingPatternType.TRAINING_COMPETENCY.value,
            description="Evaluation of training programs, skill development, and competency management"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate training and competency audit steps."""
        return [
            {
                "type": "competency_framework",
                "name": "Assess Competency Framework",
                "description": f"Evaluate competency framework and skill requirements for {scope}",
                "expected_output": "Competency framework assessment with skill requirement evaluation and framework effectiveness"
            },
            {
                "type": "training_programs",
                "name": "Review Training Programs",
                "description": "Assess training program effectiveness and curriculum quality",
                "expected_output": "Training program evaluation with curriculum assessment and effectiveness measurement"
            },
            {
                "type": "skill_gap_analysis",
                "name": "Conduct Skill Gap Analysis",
                "description": "Identify skill gaps and development needs across the organization",
                "expected_output": "Skill gap analysis with development needs identification and prioritization recommendations"
            },
            {
                "type": "learning_delivery",
                "name": "Evaluate Learning Delivery",
                "description": "Assess learning delivery methods and accessibility",
                "expected_output": "Learning delivery evaluation with method effectiveness and accessibility assessment"
            },
            {
                "type": "performance_measurement",
                "name": "Review Performance Measurement",
                "description": "Evaluate training performance measurement and assessment methods",
                "expected_output": "Performance measurement evaluation with assessment method effectiveness and outcome tracking"
            },
            {
                "type": "certification_compliance",
                "name": "Assess Certification Compliance",
                "description": "Review certification requirements and compliance tracking",
                "expected_output": "Certification compliance assessment with requirement tracking and compliance gap identification"
            },
            {
                "type": "continuous_learning",
                "name": "Evaluate Continuous Learning",
                "description": "Assess continuous learning culture and professional development support",
                "expected_output": "Continuous learning evaluation with culture assessment and development support effectiveness"
            },
            {
                "type": "knowledge_retention",
                "name": "Review Knowledge Retention",
                "description": "Evaluate knowledge retention strategies and organizational learning",
                "expected_output": "Knowledge retention assessment with strategy effectiveness and organizational learning evaluation"
            },
            {
                "type": "roi_measurement",
                "name": "Assess Training ROI",
                "description": "Evaluate training return on investment and business impact",
                "expected_output": "Training ROI assessment with business impact measurement and investment optimization recommendations"
            }
        ]

class CostManagementPattern(AuditingPattern):
    """Cost Management auditing pattern."""
    
    def __init__(self):
        """Initialize the cost management pattern."""
        super().__init__(
            name=AuditingPatternType.COST_MANAGEMENT.value,
            description="Assessment of cost allocation, budget management, and financial efficiency"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate cost management audit steps."""
        return [
            {
                "type": "budget_planning",
                "name": "Assess Budget Planning",
                "description": f"Evaluate budget planning processes and accuracy for {scope}",
                "expected_output": "Budget planning assessment with process effectiveness and forecasting accuracy evaluation"
            },
            {
                "type": "cost_allocation",
                "name": "Review Cost Allocation",
                "description": "Assess cost allocation methodologies and accuracy",
                "expected_output": "Cost allocation evaluation with methodology assessment and allocation accuracy verification"
            },
            {
                "type": "variance_analysis",
                "name": "Conduct Variance Analysis",
                "description": "Analyze budget variances and identify root causes",
                "expected_output": "Variance analysis with root cause identification and corrective action recommendations"
            },
            {
                "type": "cost_controls",
                "name": "Evaluate Cost Controls",
                "description": "Assess cost control mechanisms and approval processes",
                "expected_output": "Cost control evaluation with mechanism effectiveness and approval process assessment"
            },
            {
                "type": "financial_reporting",
                "name": "Review Financial Reporting",
                "description": "Evaluate financial reporting accuracy and timeliness",
                "expected_output": "Financial reporting assessment with accuracy verification and timeliness evaluation"
            },
            {
                "type": "procurement_efficiency",
                "name": "Assess Procurement Efficiency",
                "description": "Review procurement processes and cost optimization opportunities",
                "expected_output": "Procurement efficiency evaluation with process optimization and cost reduction opportunities"
            },
            {
                "type": "roi_analysis",
                "name": "Conduct ROI Analysis",
                "description": "Evaluate return on investment for major expenditures",
                "expected_output": "ROI analysis with investment effectiveness and value realization assessment"
            },
            {
                "type": "cost_optimization",
                "name": "Identify Cost Optimization",
                "description": "Identify cost optimization opportunities and efficiency improvements",
                "expected_output": "Cost optimization assessment with opportunity identification and implementation strategies"
            },
            {
                "type": "financial_governance",
                "name": "Evaluate Financial Governance",
                "description": "Assess financial governance framework and oversight mechanisms",
                "expected_output": "Financial governance evaluation with framework effectiveness and oversight adequacy assessment"
            }
        ]

class RevenueAssurancePattern(AuditingPattern):
    """Revenue Assurance auditing pattern."""
    
    def __init__(self):
        """Initialize the revenue assurance pattern."""
        super().__init__(
            name=AuditingPatternType.REVENUE_ASSURANCE.value,
            description="Evaluation of revenue recognition, billing accuracy, and financial controls"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate revenue assurance audit steps."""
        return [
            {
                "type": "revenue_recognition",
                "name": "Assess Revenue Recognition",
                "description": f"Evaluate revenue recognition processes and compliance for {scope}",
                "expected_output": "Revenue recognition assessment with process compliance and accuracy verification"
            },
            {
                "type": "billing_accuracy",
                "name": "Review Billing Accuracy",
                "description": "Assess billing processes and accuracy controls",
                "expected_output": "Billing accuracy evaluation with process assessment and error rate analysis"
            },
            {
                "type": "revenue_leakage",
                "name": "Identify Revenue Leakage",
                "description": "Identify potential revenue leakage points and prevention mechanisms",
                "expected_output": "Revenue leakage analysis with leakage point identification and prevention strategies"
            },
            {
                "type": "pricing_controls",
                "name": "Evaluate Pricing Controls",
                "description": "Assess pricing controls and discount approval processes",
                "expected_output": "Pricing controls evaluation with approval process effectiveness and control adequacy"
            },
            {
                "type": "contract_compliance",
                "name": "Review Contract Compliance",
                "description": "Evaluate contract compliance and revenue terms adherence",
                "expected_output": "Contract compliance assessment with terms adherence and compliance gap identification"
            },
            {
                "type": "reconciliation_processes",
                "name": "Assess Reconciliation Processes",
                "description": "Review revenue reconciliation processes and accuracy",
                "expected_output": "Reconciliation process evaluation with accuracy assessment and process improvement recommendations"
            },
            {
                "type": "fraud_prevention",
                "name": "Evaluate Fraud Prevention",
                "description": "Assess fraud prevention controls and detection mechanisms",
                "expected_output": "Fraud prevention evaluation with control effectiveness and detection capability assessment"
            },
            {
                "type": "reporting_accuracy",
                "name": "Review Reporting Accuracy",
                "description": "Evaluate revenue reporting accuracy and regulatory compliance",
                "expected_output": "Reporting accuracy assessment with compliance verification and accuracy improvement recommendations"
            },
            {
                "type": "performance_monitoring",
                "name": "Assess Performance Monitoring",
                "description": "Review revenue performance monitoring and KPI tracking",
                "expected_output": "Performance monitoring evaluation with KPI effectiveness and tracking accuracy assessment"
            }
        ]

class ContractManagementPattern(AuditingPattern):
    """Contract Management auditing pattern."""
    
    def __init__(self):
        """Initialize the contract management pattern."""
        super().__init__(
            name=AuditingPatternType.CONTRACT_MANAGEMENT.value,
            description="Assessment of contract lifecycle management, compliance, and performance tracking"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate contract management audit steps."""
        return [
            {
                "type": "lifecycle_management",
                "name": "Assess Lifecycle Management",
                "description": f"Evaluate contract lifecycle management processes for {scope}",
                "expected_output": "Lifecycle management assessment with process effectiveness and stage transition evaluation"
            },
            {
                "type": "compliance_monitoring",
                "name": "Review Compliance Monitoring",
                "description": "Assess contract compliance monitoring and tracking mechanisms",
                "expected_output": "Compliance monitoring evaluation with tracking effectiveness and violation detection capabilities"
            },
            {
                "type": "performance_tracking",
                "name": "Evaluate Performance Tracking",
                "description": "Review contract performance tracking and SLA monitoring",
                "expected_output": "Performance tracking assessment with SLA monitoring effectiveness and performance measurement accuracy"
            },
            {
                "type": "risk_assessment",
                "name": "Assess Contract Risk",
                "description": "Evaluate contract risk assessment and mitigation strategies",
                "expected_output": "Contract risk assessment with risk identification completeness and mitigation strategy effectiveness"
            },
            {
                "type": "approval_processes",
                "name": "Review Approval Processes",
                "description": "Assess contract approval workflows and authorization controls",
                "expected_output": "Approval process evaluation with workflow efficiency and authorization control effectiveness"
            },
            {
                "type": "renewal_management",
                "name": "Evaluate Renewal Management",
                "description": "Review contract renewal processes and optimization opportunities",
                "expected_output": "Renewal management assessment with process effectiveness and optimization opportunity identification"
            },
            {
                "type": "financial_controls",
                "name": "Assess Financial Controls",
                "description": "Evaluate contract financial controls and payment processes",
                "expected_output": "Financial controls evaluation with payment process effectiveness and control adequacy assessment"
            },
            {
                "type": "documentation_standards",
                "name": "Review Documentation Standards",
                "description": "Assess contract documentation standards and record keeping",
                "expected_output": "Documentation standards evaluation with record keeping effectiveness and standardization assessment"
            },
            {
                "type": "termination_procedures",
                "name": "Evaluate Termination Procedures",
                "description": "Review contract termination procedures and exit strategies",
                "expected_output": "Termination procedure evaluation with exit strategy effectiveness and transition planning assessment"
            }
        ]

class EnvironmentalImpactPattern(AuditingPattern):
    """Environmental Impact auditing pattern."""
    
    def __init__(self):
        """Initialize the environmental impact pattern."""
        super().__init__(
            name=AuditingPatternType.ENVIRONMENTAL_IMPACT.value,
            description="Assessment of environmental impact, sustainability practices, and green computing initiatives"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate environmental impact audit steps."""
        return [
            {
                "type": "carbon_footprint",
                "name": "Assess Carbon Footprint",
                "description": f"Evaluate carbon footprint and greenhouse gas emissions for {scope}",
                "expected_output": "Carbon footprint assessment with emission measurement and reduction opportunity identification"
            },
            {
                "type": "energy_efficiency",
                "name": "Review Energy Efficiency",
                "description": "Assess energy consumption patterns and efficiency improvements",
                "expected_output": "Energy efficiency evaluation with consumption analysis and optimization recommendations"
            },
            {
                "type": "resource_consumption",
                "name": "Evaluate Resource Consumption",
                "description": "Review resource consumption and conservation practices",
                "expected_output": "Resource consumption assessment with conservation effectiveness and reduction strategies"
            },
            {
                "type": "waste_generation",
                "name": "Assess Waste Generation",
                "description": "Evaluate waste generation patterns and reduction initiatives",
                "expected_output": "Waste generation analysis with reduction initiative effectiveness and improvement opportunities"
            },
            {
                "type": "green_technology",
                "name": "Review Green Technology",
                "description": "Assess green technology adoption and sustainable computing practices",
                "expected_output": "Green technology evaluation with adoption effectiveness and sustainable computing assessment"
            },
            {
                "type": "compliance_standards",
                "name": "Evaluate Environmental Compliance",
                "description": "Review compliance with environmental standards and regulations",
                "expected_output": "Environmental compliance assessment with standards adherence and regulatory alignment"
            },
            {
                "type": "supply_chain_impact",
                "name": "Assess Supply Chain Impact",
                "description": "Evaluate environmental impact of supply chain and vendor practices",
                "expected_output": "Supply chain impact assessment with vendor sustainability evaluation and improvement strategies"
            },
            {
                "type": "reporting_transparency",
                "name": "Review Environmental Reporting",
                "description": "Assess environmental reporting accuracy and transparency",
                "expected_output": "Environmental reporting evaluation with accuracy assessment and transparency improvement recommendations"
            },
            {
                "type": "improvement_initiatives",
                "name": "Evaluate Improvement Initiatives",
                "description": "Review environmental improvement initiatives and their effectiveness",
                "expected_output": "Improvement initiative evaluation with effectiveness measurement and enhancement strategies"
            }
        ]

class WasteManagementPattern(AuditingPattern):
    """Waste Management auditing pattern."""
    
    def __init__(self):
        """Initialize the waste management pattern."""
        super().__init__(
            name=AuditingPatternType.WASTE_MANAGEMENT.value,
            description="Evaluation of waste reduction, recycling programs, and resource conservation practices"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate waste management audit steps."""
        return [
            {
                "type": "waste_assessment",
                "name": "Conduct Waste Assessment",
                "description": f"Assess waste generation and categorization within {scope}",
                "expected_output": "Waste assessment with generation analysis and categorization effectiveness"
            },
            {
                "type": "reduction_programs",
                "name": "Review Reduction Programs",
                "description": "Evaluate waste reduction programs and their effectiveness",
                "expected_output": "Reduction program evaluation with effectiveness measurement and improvement opportunities"
            },
            {
                "type": "recycling_initiatives",
                "name": "Assess Recycling Initiatives",
                "description": "Review recycling programs and material recovery processes",
                "expected_output": "Recycling initiative assessment with program effectiveness and recovery rate optimization"
            },
            {
                "type": "disposal_practices",
                "name": "Evaluate Disposal Practices",
                "description": "Assess waste disposal practices and environmental compliance",
                "expected_output": "Disposal practice evaluation with compliance assessment and environmental impact analysis"
            },
            {
                "type": "circular_economy",
                "name": "Review Circular Economy Practices",
                "description": "Evaluate circular economy implementation and resource reuse",
                "expected_output": "Circular economy assessment with implementation effectiveness and reuse optimization"
            },
            {
                "type": "vendor_management",
                "name": "Assess Waste Vendor Management",
                "description": "Review waste management vendor relationships and performance",
                "expected_output": "Vendor management evaluation with performance assessment and relationship optimization"
            },
            {
                "type": "cost_efficiency",
                "name": "Evaluate Cost Efficiency",
                "description": "Assess waste management cost efficiency and optimization opportunities",
                "expected_output": "Cost efficiency evaluation with optimization opportunities and budget effectiveness"
            },
            {
                "type": "employee_engagement",
                "name": "Review Employee Engagement",
                "description": "Evaluate employee engagement in waste management initiatives",
                "expected_output": "Employee engagement assessment with participation effectiveness and awareness improvement"
            },
            {
                "type": "performance_metrics",
                "name": "Assess Performance Metrics",
                "description": "Review waste management performance metrics and tracking",
                "expected_output": "Performance metrics evaluation with tracking effectiveness and measurement optimization"
            }
        ]

class SocialResponsibilityPattern(AuditingPattern):
    """Social Responsibility auditing pattern."""
    
    def __init__(self):
        """Initialize the social responsibility pattern."""
        super().__init__(
            name=AuditingPatternType.SOCIAL_RESPONSIBILITY.value,
            description="Assessment of corporate social responsibility initiatives, ethical practices, and community impact"
        )
    
    async def generate_audit_steps(
        self,
        scope: str,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate social responsibility audit steps."""
        return [
            {
                "type": "csr_strategy",
                "name": "Assess CSR Strategy",
                "description": f"Evaluate corporate social responsibility strategy and alignment for {scope}",
                "expected_output": "CSR strategy assessment with alignment evaluation and strategic effectiveness"
            },
            {
                "type": "ethical_practices",
                "name": "Review Ethical Practices",
                "description": "Assess ethical practices and code of conduct implementation",
                "expected_output": "Ethical practices evaluation with code implementation and compliance assessment"
            },
            {
                "type": "community_impact",
                "name": "Evaluate Community Impact",
                "description": "Review community impact initiatives and stakeholder engagement",
                "expected_output": "Community impact assessment with initiative effectiveness and stakeholder engagement evaluation"
            },
            {
                "type": "diversity_inclusion",
                "name": "Assess Diversity and Inclusion",
                "description": "Evaluate diversity and inclusion programs and outcomes",
                "expected_output": "Diversity and inclusion assessment with program effectiveness and outcome measurement"
            },
            {
                "type": "employee_wellbeing",
                "name": "Review Employee Wellbeing",
                "description": "Assess employee wellbeing programs and workplace culture",
                "expected_output": "Employee wellbeing evaluation with program effectiveness and culture assessment"
            },
            {
                "type": "supply_chain_ethics",
                "name": "Evaluate Supply Chain Ethics",
                "description": "Review supply chain ethical practices and vendor compliance",
                "expected_output": "Supply chain ethics assessment with vendor compliance and ethical practice evaluation"
            },
            {
                "type": "transparency_reporting",
                "name": "Assess Transparency and Reporting",
                "description": "Evaluate transparency in CSR reporting and stakeholder communication",
                "expected_output": "Transparency and reporting evaluation with communication effectiveness and disclosure adequacy"
            },
            {
                "type": "impact_measurement",
                "name": "Review Impact Measurement",
                "description": "Assess social impact measurement and outcome tracking",
                "expected_output": "Impact measurement evaluation with tracking effectiveness and outcome assessment"
            },
            {
                "type": "continuous_improvement",
                "name": "Evaluate Continuous Improvement",
                "description": "Review continuous improvement in social responsibility practices",
                "expected_output": "Continuous improvement evaluation with practice enhancement and strategic development"
            }
        ]

# Registry of available auditing patterns
_AUDITING_PATTERNS: Dict[str, Type[AuditingPattern]] = {
    AuditingPatternType.VULNERABILITY_ASSESSMENT.value: VulnerabilityAssessmentPattern,
    AuditingPatternType.ACCESS_CONTROL_AUDIT.value: AccessControlAuditPattern,
    AuditingPatternType.ENCRYPTION_COMPLIANCE.value: EncryptionCompliancePattern,
    AuditingPatternType.SECURITY_CONFIGURATION_REVIEW.value: SecurityConfigurationReviewPattern,
    AuditingPatternType.INCIDENT_RESPONSE_AUDIT.value: IncidentResponseAuditPattern,
    AuditingPatternType.DATA_LOSS_PREVENTION.value: DataLossPreventionPattern,
    AuditingPatternType.NETWORK_SECURITY_AUDIT.value: NetworkSecurityAuditPattern,
    AuditingPatternType.APPLICATION_SECURITY.value: ApplicationSecurityPattern,
    AuditingPatternType.CODE_QUALITY_ASSESSMENT.value: CodeQualityAssessmentPattern,
    AuditingPatternType.TEST_COVERAGE_ANALYSIS.value: TestCoverageAnalysisPattern,
    AuditingPatternType.DOCUMENTATION_QUALITY.value: DocumentationQualityPattern,
    AuditingPatternType.DEPENDENCY_MANAGEMENT.value: DependencyManagementPattern,
    AuditingPatternType.PERFORMANCE_QUALITY.value: PerformanceQualityPattern,
    AuditingPatternType.USER_EXPERIENCE_AUDIT.value: UserExperienceAuditPattern,
    AuditingPatternType.DATA_QUALITY_ASSESSMENT.value: DataQualityAssessmentPattern,
    AuditingPatternType.API_QUALITY.value: APIQualityPattern,
    AuditingPatternType.REGULATORY_COMPLIANCE.value: RegulatoryCompliancePattern,
    AuditingPatternType.POLICY_ADHERENCE.value: PolicyAdherencePattern,
    AuditingPatternType.CHANGE_MANAGEMENT_AUDIT.value: ChangeManagementAuditPattern,
    AuditingPatternType.RISK_MANAGEMENT.value: RiskManagementPattern,
    AuditingPatternType.AUDIT_TRAIL.value: AuditTrailPattern,
    AuditingPatternType.BUSINESS_CONTINUITY.value: BusinessContinuityPattern,
    AuditingPatternType.VENDOR_MANAGEMENT.value: VendorManagementPattern,
    AuditingPatternType.DATA_GOVERNANCE.value: DataGovernancePattern,
    AuditingPatternType.SYSTEM_PERFORMANCE.value: SystemPerformancePattern,
    AuditingPatternType.RESOURCE_UTILIZATION.value: ResourceUtilizationPattern,
    AuditingPatternType.AVAILABILITY_RELIABILITY.value: AvailabilityReliabilityPattern,
    AuditingPatternType.MONITORING_ALERTING.value: MonitoringAlertingPattern,
    AuditingPatternType.BACKUP_RECOVERY.value: BackupRecoveryPattern,
    AuditingPatternType.OPERATIONAL_EXCELLENCE.value: OperationalExcellencePattern,
    AuditingPatternType.INFRASTRUCTURE_AUDIT.value: InfrastructureAuditPattern,
    AuditingPatternType.CLOUD_SECURITY.value: CloudSecurityPattern,
    AuditingPatternType.DEVOPS_PIPELINE.value: DevOpsPipelinePattern,
    AuditingPatternType.PROJECT_MANAGEMENT.value: ProjectManagementPattern,
    AuditingPatternType.COMMUNICATION_AUDIT.value: CommunicationAuditPattern,
    AuditingPatternType.TRAINING_COMPETENCY.value: TrainingCompetencyPattern,
    AuditingPatternType.COST_MANAGEMENT.value: CostManagementPattern,
    AuditingPatternType.REVENUE_ASSURANCE.value: RevenueAssurancePattern,
    AuditingPatternType.CONTRACT_MANAGEMENT.value: ContractManagementPattern,
    AuditingPatternType.ENVIRONMENTAL_IMPACT.value: EnvironmentalImpactPattern,
    AuditingPatternType.WASTE_MANAGEMENT.value: WasteManagementPattern,
    AuditingPatternType.SOCIAL_RESPONSIBILITY.value: SocialResponsibilityPattern,
}

def get_auditing_pattern(name: str) -> Optional[AuditingPattern]:
    """Get an auditing pattern by name."""
    pattern_class = _AUDITING_PATTERNS.get(name)
    if pattern_class:
        return pattern_class()
    return None

def register_auditing_pattern(name: str, pattern_class: Type[AuditingPattern]) -> None:
    """Register a new auditing pattern."""
    _AUDITING_PATTERNS[name] = pattern_class

def get_available_patterns() -> List[str]:
    """Get list of available auditing pattern names."""
    return list(_AUDITING_PATTERNS.keys())

def get_patterns_by_category() -> Dict[str, List[str]]:
    """Get auditing patterns organized by category."""
    categories = {
        "Security": [
            AuditingPatternType.VULNERABILITY_ASSESSMENT.value,
            AuditingPatternType.ACCESS_CONTROL_AUDIT.value,
            AuditingPatternType.ENCRYPTION_COMPLIANCE.value,
            AuditingPatternType.SECURITY_CONFIGURATION_REVIEW.value,
            AuditingPatternType.INCIDENT_RESPONSE_AUDIT.value,
            AuditingPatternType.DATA_LOSS_PREVENTION.value,
            AuditingPatternType.NETWORK_SECURITY_AUDIT.value,
            AuditingPatternType.APPLICATION_SECURITY.value,
        ],
        "Quality": [
            AuditingPatternType.CODE_QUALITY_ASSESSMENT.value,
            AuditingPatternType.TEST_COVERAGE_ANALYSIS.value,
            AuditingPatternType.DOCUMENTATION_QUALITY.value,
            AuditingPatternType.DEPENDENCY_MANAGEMENT.value,
            AuditingPatternType.PERFORMANCE_QUALITY.value,
            AuditingPatternType.USER_EXPERIENCE_AUDIT.value,
            AuditingPatternType.DATA_QUALITY_ASSESSMENT.value,
            AuditingPatternType.API_QUALITY.value,
        ],
        "Compliance": [
            AuditingPatternType.REGULATORY_COMPLIANCE.value,
            AuditingPatternType.POLICY_ADHERENCE.value,
            AuditingPatternType.CHANGE_MANAGEMENT_AUDIT.value,
            AuditingPatternType.RISK_MANAGEMENT.value,
            AuditingPatternType.AUDIT_TRAIL.value,
            AuditingPatternType.BUSINESS_CONTINUITY.value,
            AuditingPatternType.VENDOR_MANAGEMENT.value,
            AuditingPatternType.DATA_GOVERNANCE.value,
        ],
        "Performance": [
            AuditingPatternType.SYSTEM_PERFORMANCE.value,
            AuditingPatternType.RESOURCE_UTILIZATION.value,
            AuditingPatternType.AVAILABILITY_RELIABILITY.value,
            AuditingPatternType.MONITORING_ALERTING.value,
            AuditingPatternType.BACKUP_RECOVERY.value,
            AuditingPatternType.OPERATIONAL_EXCELLENCE.value,
            AuditingPatternType.INFRASTRUCTURE_AUDIT.value,
            AuditingPatternType.CLOUD_SECURITY.value,
        ],
        "Process": [
            AuditingPatternType.DEVOPS_PIPELINE.value,
            AuditingPatternType.PROJECT_MANAGEMENT.value,
            AuditingPatternType.COMMUNICATION_AUDIT.value,
            AuditingPatternType.TRAINING_COMPETENCY.value,
        ],
        "Business": [
            AuditingPatternType.COST_MANAGEMENT.value,
            AuditingPatternType.REVENUE_ASSURANCE.value,
            AuditingPatternType.CONTRACT_MANAGEMENT.value,
        ],
        "Sustainability": [
            AuditingPatternType.ENVIRONMENTAL_IMPACT.value,
            AuditingPatternType.WASTE_MANAGEMENT.value,
            AuditingPatternType.SOCIAL_RESPONSIBILITY.value,
        ]
    }
    return categories 