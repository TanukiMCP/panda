"""
Threat Modeling Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

threat_modeling: MentalModel = {
    "description": "Systematically identify, analyze, and mitigate potential threats, vulnerabilities, and attack vectors to protect valuable assets and systems",
    "questions": [
        "What are we trying to protect (assets, data, systems, processes)?",
        "Who are the potential threat actors and what motivates them?",
        "What attack vectors and methods could they use?",
        "What vulnerabilities exist in our current defenses?",
        "What would be the impact of successful attacks?",
        "What is the likelihood of each threat materializing?",
        "What countermeasures and controls can we implement?",
        "How will we monitor and detect threats in real-time?"
    ],
    "structure": {
        "asset_identification": "Catalog valuable assets that need protection",
        "threat_actor_analysis": "Profile potential attackers and their capabilities",
        "attack_vector_mapping": "Identify possible methods of compromise",
        "vulnerability_assessment": "Find weaknesses in current defenses",
        "impact_analysis": "Evaluate consequences of successful attacks",
        "risk_prioritization": "Rank threats by likelihood and impact",
        "mitigation_strategies": "Design countermeasures and controls",
        "monitoring_systems": "Establish detection and response capabilities"
    },
    "next_steps": "Implement highest priority mitigations, establish monitoring and incident response procedures, and regularly update threat model"
} 