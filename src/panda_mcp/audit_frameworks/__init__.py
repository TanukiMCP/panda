"""
Cognitive Audit Frameworks for PandA MCP Server

This module provides structured cognitive auditing frameworks that guide systematic
investigation processes similar to how mental models guide planning.

Each framework provides:
- Investigation questions for systematic inquiry
- Methodology phases for progressive audit
- Evidence requirements and collection guidance
- Evaluation criteria and standards
- Reporting structure for professional audit reports
"""

from .base import AuditFramework
from .security_audit import security_audit
from .compliance_audit import compliance_audit
from .quality_audit import quality_audit
from .process_audit import process_audit
from .financial_audit import financial_audit
from .it_audit import it_audit

__all__ = [
    "AuditFramework",
    "security_audit",
    "compliance_audit", 
    "quality_audit",
    "process_audit",
    "financial_audit",
    "it_audit"
] 