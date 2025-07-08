"""
Value Stream Mapping Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

value_stream_mapping: MentalModel = {
    "description": "Visualize and optimize the flow of value through processes by identifying waste, bottlenecks, and improvement opportunities",
    "questions": [
        "What value are we trying to deliver to the end customer?",
        "What are all the steps in our current value delivery process?",
        "Which steps add value and which create waste?",
        "Where do delays, bottlenecks, and inefficiencies occur?",
        "How much time does each step take and what causes variation?",
        "What information flows are needed to support the value stream?",
        "Where can we eliminate waste and streamline the process?",
        "What would the ideal future state value stream look like?"
    ],
    "structure": {
        "value_definition": "Clearly define customer value and outcomes",
        "process_mapping": "Document all steps in value delivery",
        "value_analysis": "Distinguish value-adding from wasteful activities",
        "bottleneck_identification": "Find constraints and delay points",
        "time_analysis": "Measure duration and variation in each step",
        "information_flows": "Map supporting data and communication needs",
        "waste_elimination": "Remove non-value-adding activities",
        "future_state_design": "Create optimized value stream vision"
    },
    "next_steps": "Implement value stream improvements, eliminate identified waste, and establish continuous monitoring of flow efficiency"
} 