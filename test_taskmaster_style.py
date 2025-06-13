#!/usr/bin/env python3
"""
Test demonstrating PandA tools working like taskmaster with action-based interface
"""

import sys
import os
import asyncio

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_taskmaster_style():
    """Test PandA tools with taskmaster-style action interface."""
    print("🚀 Testing PandA Tools - Taskmaster Style Interface")
    print("=" * 60)
    
    try:
        from panda_mcp.tools.plan import PandaPlan
        from panda_mcp.tools.audit import PandaAudit
        
        # Initialize tools
        plan_tool = PandaPlan()
        audit_tool = PandaAudit()
        
        print("✅ Tools initialized successfully")
        
        # Test Planning Tool - Taskmaster Style
        print("\n📋 PLANNING TOOL - Taskmaster Style")
        print("-" * 40)
        
        # 1. Create session
        print("1. Creating planning session...")
        session_result = await plan_tool.execute(
            action="create_session",
            parameters={"session_name": "microservices_planning"}
        )
        print(f"   ✅ Session created: {session_result['session_id']}")
        session_id = session_result['session_id']
        
        # 2. Start planning
        print("\n2. Starting planning...")
        plan_result = await plan_tool.execute(
            action="plan",
            session_id=session_id,
            parameters={
                "task": "Design and implement a microservices architecture",
                "framework": "sequential",
                "mental_models": ["systems_thinking", "critical_path"],
                "context": {"domain": "e-commerce", "team_size": 8}
            }
        )
        print(f"   ✅ Planning started: {plan_result['total_steps']} steps generated")
        print(f"   📝 Current step: {plan_result['current_step']['name']}")
        
        # 3. Get status
        print("\n3. Getting status...")
        status_result = await plan_tool.execute(
            action="get_status",
            session_id=session_id
        )
        print(f"   ✅ Status: {status_result}")
        
        # 4. Execute step action
        print("\n4. Executing step action...")
        step_result = await plan_tool.execute(
            action="step_action",
            session_id=session_id,
            step_action="complete",
            result={"output": "System components mapped successfully"}
        )
        print(f"   ✅ Step action completed: {step_result['status']}")
        
        # 5. Advance step
        print("\n5. Advancing to next step...")
        advance_result = await plan_tool.execute(
            action="advance_step",
            session_id=session_id,
            result={"output": "Analysis complete, moving to next phase"}
        )
        print(f"   ✅ Advanced: {advance_result['status']}")
        
        # Test Auditing Tool - Taskmaster Style
        print("\n🔍 AUDITING TOOL - Taskmaster Style")
        print("-" * 40)
        
        # 1. Create audit session
        print("1. Creating audit session...")
        audit_session_result = await audit_tool.execute(
            action="create_session",
            parameters={"session_name": "codebase_security_audit"}
        )
        print(f"   ✅ Audit session created: {audit_session_result['session_id']}")
        audit_session_id = audit_session_result['session_id']
        
        # 2. Start audit
        print("\n2. Starting audit...")
        audit_result = await audit_tool.execute(
            action="audit",
            session_id=audit_session_id,
            parameters={
                "framework": "codebase",
                "checkers": ["security", "quality"],
                "path": "./src",
                "context": {"project_type": "python_mcp_server"}
            }
        )
        print(f"   ✅ Audit started: {audit_result['status']}")
        if audit_result['status'] == 'success':
            print(f"   📊 Findings: {len(audit_result.get('findings', []))} issues found")
        
        # 3. Get audit status
        print("\n3. Getting audit status...")
        audit_status = await audit_tool.execute(
            action="get_status",
            session_id=audit_session_id
        )
        print(f"   ✅ Audit status: {audit_status}")
        
        # 4. Get findings
        print("\n4. Getting findings...")
        findings_result = await audit_tool.execute(
            action="step_action",
            session_id=audit_session_id,
            step_action="get_findings"
        )
        print(f"   ✅ Retrieved {len(findings_result.get('findings', []))} findings")
        
        print("\n🎉 Taskmaster-Style Interface Test Complete!")
        print("=" * 60)
        print("✅ Both panda_plan and panda_audit work like taskmaster:")
        print("   • Single tool with action-based interface")
        print("   • LLM drives execution through actions")
        print("   • Session management handled internally")
        print("   • Step-by-step progression controlled by LLM")
        print("\n📋 Available Actions:")
        print("   panda_plan: create_session, plan, advance_step, step_action, get_status")
        print("   panda_audit: create_session, audit, advance_step, step_action, get_status")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_taskmaster_style())
    sys.exit(0 if success else 1) 