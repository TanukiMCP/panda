"""
Evidence Synthesis Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

evidence_synthesis: MentalModel = {
    "description": "Systematically collect, evaluate, and integrate diverse sources of evidence to form well-supported conclusions and decisions",
    "questions": [
        "What evidence sources are available to inform this decision?",
        "How reliable and credible is each source of evidence?",
        "What patterns or themes emerge across different evidence sources?",
        "Where do evidence sources contradict each other and why?",
        "What gaps exist in our evidence base?",
        "How strong is the overall evidence for each conclusion?",
        "What assumptions are we making about the evidence?",
        "What additional evidence would strengthen our conclusions?"
    ],
    "structure": {
        "evidence_collection": "Gather diverse, relevant information sources",
        "credibility_assessment": "Evaluate reliability and quality of sources",
        "pattern_recognition": "Identify themes and convergent findings",
        "contradiction_analysis": "Examine conflicting evidence and explanations",
        "gap_identification": "Find missing information and blind spots",
        "strength_evaluation": "Assess confidence levels in conclusions",
        "assumption_testing": "Challenge underlying assumptions about evidence",
        "evidence_triangulation": "Cross-validate findings across sources"
    },
    "next_steps": "Integrate synthesized evidence into actionable insights, identify areas needing additional research, and document confidence levels"
} 