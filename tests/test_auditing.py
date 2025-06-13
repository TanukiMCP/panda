"""
Tests for PandA auditing framework
"""

import pytest
from typing import Dict, Any

from panda_mcp.core.auditing import (
    AuditSession,
    CodebaseAuditor,
    TextAuditor,
    GeneralAuditor,
    SecurityChecker,
    QualityChecker
)

@pytest.fixture
def session() -> AuditSession:
    """Create a test audit session."""
    return AuditSession("test_session")

@pytest.fixture
def codebase_auditor() -> CodebaseAuditor:
    """Create a test codebase auditor."""
    return CodebaseAuditor()

@pytest.fixture
def text_auditor() -> TextAuditor:
    """Create a test text auditor."""
    return TextAuditor()

@pytest.fixture
def general_auditor() -> GeneralAuditor:
    """Create a test general auditor."""
    return GeneralAuditor()

def test_audit_session_initialization(session: AuditSession):
    """Test audit session initialization."""
    assert session.session_id == "test_session"
    assert session.state["findings"] == []
    assert isinstance(session.state["checkers"], set)
    assert session.state["status"] == "initialized"
    assert all(
        metric in session.state["metrics"]
        for metric in ["total_checks", "passed_checks", "failed_checks", "warnings"]
    )

def test_audit_session_findings(session: AuditSession):
    """Test audit session finding management."""
    # Add findings
    error_finding = {
        "type": "security",
        "severity": "error",
        "message": "Security issue found"
    }
    warning_finding = {
        "type": "quality",
        "severity": "warning",
        "message": "Quality issue found"
    }
    
    session.add_finding(error_finding)
    session.add_finding(warning_finding)
    
    # Check findings
    assert len(session.get_findings()) == 2
    assert len(session.get_findings("error")) == 1
    assert len(session.get_findings("warning")) == 1
    
    # Check metrics
    metrics = session.get_metrics()
    assert metrics["total_checks"] == 2
    assert metrics["failed_checks"] == 1
    assert metrics["warnings"] == 1

def test_audit_session_checkers(session: AuditSession):
    """Test audit session checker management."""
    session.add_checker("security")
    session.add_checker("quality")
    
    assert "security" in session.state["checkers"]
    assert "quality" in session.state["checkers"]
    
    # Test duplicate addition
    session.add_checker("security")
    assert len(session.state["checkers"]) == 2

@pytest.mark.asyncio
async def test_codebase_auditor_validation(codebase_auditor: CodebaseAuditor):
    """Test codebase auditor parameter validation."""
    # Test with valid parameters
    assert codebase_auditor.validate_parameters({
        "path": "/test/path",
        "checkers": ["security", "quality"]
    })
    
    # Test with missing parameters
    assert not codebase_auditor.validate_parameters({
        "path": "/test/path"
    })
    
    # Test with invalid checkers
    assert not codebase_auditor.validate_parameters({
        "path": "/test/path",
        "checkers": ["invalid_checker"]
    })

@pytest.mark.asyncio
async def test_text_auditor_validation(text_auditor: TextAuditor):
    """Test text auditor parameter validation."""
    # Test with valid parameters
    assert text_auditor.validate_parameters({
        "content": "Test content",
        "checkers": ["quality", "consistency"]
    })
    
    # Test with missing parameters
    assert not text_auditor.validate_parameters({
        "content": "Test content"
    })
    
    # Test with invalid checkers
    assert not text_auditor.validate_parameters({
        "content": "Test content",
        "checkers": ["security"]  # Not supported by text auditor
    })

@pytest.mark.asyncio
async def test_general_auditor_validation(general_auditor: GeneralAuditor):
    """Test general auditor parameter validation."""
    # Test with valid parameters
    assert general_auditor.validate_parameters({
        "content": "Test content",
        "checkers": ["security", "quality"],
        "content_type": "text"
    })
    
    # Test with missing parameters
    assert not general_auditor.validate_parameters({
        "content": "Test content",
        "checkers": ["security"]
    })

@pytest.mark.asyncio
async def test_security_checker():
    """Test security checker functionality."""
    checker = SecurityChecker()
    content = """
    api_key = "secret123"
    result = eval("1 + 1")
    """
    
    findings = await checker.check(content, {"location": "test.py"})
    assert len(findings) == 2  # Should find API key and eval usage
    assert any("api key" in finding["message"].lower() for finding in findings)
    assert any("eval" in finding["message"].lower() for finding in findings)

@pytest.mark.asyncio
async def test_quality_checker():
    """Test quality checker functionality."""
    checker = QualityChecker()
    content = "x" * 120 + "\n# TODO: Fix this"
    
    findings = await checker.check(content, {"location": "test.py"})
    assert len(findings) == 2  # Should find line length and TODO
    assert any("line" in finding["message"].lower() for finding in findings)
    assert any("todo" in finding["message"].lower() for finding in findings) 