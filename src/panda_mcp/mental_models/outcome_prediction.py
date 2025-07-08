"""
Outcome Prediction Mental Model
"""
from typing import Dict, Any, List

# Type definition for mental model structure
MentalModel = Dict[str, Any]

outcome_prediction: MentalModel = {
    "description": "Anticipate likely results and consequences of decisions and actions using systematic forecasting methods and probabilistic thinking",
    "questions": [
        "What outcomes are we trying to predict and why?",
        "What historical data or patterns can inform our predictions?",
        "What are the key variables that will influence outcomes?",
        "What range of possible outcomes could occur?",
        "What is the probability distribution of different outcomes?",
        "What leading indicators can help us track prediction accuracy?",
        "How confident are we in our predictions and what creates uncertainty?",
        "How should predictions influence our current decisions and actions?"
    ],
    "structure": {
        "prediction_targets": "Define specific outcomes to forecast",
        "historical_analysis": "Extract patterns from past data and experience",
        "variable_identification": "Map key factors influencing outcomes",
        "outcome_scenarios": "Develop range of possible result scenarios",
        "probability_assessment": "Estimate likelihood of different outcomes",
        "leading_indicators": "Identify early signals for prediction validation",
        "uncertainty_quantification": "Assess confidence levels and error ranges",
        "decision_integration": "Use predictions to inform current choices"
    },
    "next_steps": "Generate probability-weighted forecasts, establish prediction tracking systems, and integrate forecasts into decision processes"
} 