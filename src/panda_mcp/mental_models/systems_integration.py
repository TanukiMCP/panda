"""
Systems Integration Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

systems_integration: MentalModel = {
    "description": "Coordinate multiple interconnected systems, processes, and stakeholders to create seamless end-to-end functionality and value",
    "questions": [
        "What different systems need to work together harmoniously?",
        "How do these systems currently interact and where are the gaps?",
        "What are the key integration points and interfaces?",
        "What data, information, or resources need to flow between systems?",
        "Where do conflicts or incompatibilities exist between systems?",
        "How can we ensure reliable and resilient integration?",
        "What governance and coordination mechanisms are needed?",
        "How will we test and validate the integrated system performance?"
    ],
    "structure": {
        "system_mapping": "Identify all systems requiring integration",
        "interaction_analysis": "Understand current connections and gaps",
        "interface_design": "Define integration points and protocols",
        "flow_optimization": "Enable smooth data and resource exchange",
        "conflict_resolution": "Address incompatibilities and tensions",
        "reliability_engineering": "Build robust and resilient integrations",
        "governance_frameworks": "Establish coordination and control mechanisms",
        "validation_testing": "Verify integrated system performance"
    },
    "next_steps": "Implement integration architecture, establish governance processes, and monitor integrated system performance continuously"
} 