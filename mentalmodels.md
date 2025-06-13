# Mental Models Framework

This document provides a comprehensive list of mental models that can be integrated into the PandA planning and auditing framework. Each model includes a description, use cases, implementation status, and integration guidance.

## Currently Implemented Mental Models

### Core Planning Models

#### [x] 1. Default Mental Model
**Description:** General-purpose planning model for any knowledge domain that provides a structured approach to problem-solving.

**Use Cases:**
- General project planning
- Task breakdown and analysis
- Basic problem-solving workflows
- Initial planning when domain expertise is limited

**Implementation:** Fully implemented in `src/panda_mcp/core/planning/mental_models.py`

#### [x] 2. First Principles Thinking
**Description:** Breaking down complex problems into fundamental truths and building up from there.

**Use Cases:**
- Innovation and product development
- Challenging assumptions
- Problem-solving in new domains
- Strategic planning

**Implementation:** Fully implemented in `src/panda_mcp/core/planning/mental_models.py`

#### [x] 3. Systems Thinking
**Description:** Understanding how different parts of a system interact and influence each other.

**Use Cases:**
- Complex system analysis
- Organizational design
- Process optimization
- Understanding feedback loops

**Implementation:** Fully implemented in `src/panda_mcp/core/planning/mental_models.py`

#### [x] 4. Critical Path Analysis
**Description:** Identifying the sequence of activities that determines the minimum project duration.

**Use Cases:**
- Project management
- Resource allocation
- Timeline optimization
- Risk assessment

**Implementation:** Fully implemented in `src/panda_mcp/core/planning/mental_models.py`

#### [x] 5. Decision Tree Analysis
**Description:** Visual representation of decisions and their possible consequences.

**Use Cases:**
- Strategic decision making
- Risk analysis
- Option evaluation
- Probability assessment

**Implementation:** Fully implemented in `src/panda_mcp/core/planning/mental_models.py`

## Mental Models to Implement

### Cognitive and Decision-Making Models

#### [ ] 6. Occam's Razor
**Description:** The simplest explanation is usually the correct one.

**Use Cases:**
- Problem diagnosis
- Hypothesis selection
- Design decisions
- Debugging

**Integration:** Add to mental_models.py with simplicity-focused planning steps

#### [ ] 7. Hanlon's Razor
**Description:** Never attribute to malice that which can be adequately explained by stupidity.

**Use Cases:**
- Conflict resolution
- Team management
- Customer service
- Incident analysis

**Integration:** Add assumption-checking steps in planning framework

#### [ ] 8. Confirmation Bias Awareness
**Description:** Recognizing the tendency to search for information that confirms existing beliefs.

**Use Cases:**
- Research methodology
- Data analysis
- Strategic planning
- Peer review

**Integration:** Add bias-checking steps in audit framework

#### [ ] 9. Anchoring Bias
**Description:** Over-relying on the first piece of information encountered.

**Use Cases:**
- Negotiation
- Estimation
- Pricing decisions
- Performance evaluation

**Integration:** Add multiple reference point generation in planning

#### [ ] 10. Availability Heuristic
**Description:** Judging probability by how easily examples come to mind.

**Use Cases:**
- Risk assessment
- Decision making
- Resource allocation
- Priority setting

**Integration:** Add systematic data gathering steps

### Strategic Thinking Models

#### [ ] 11. SWOT Analysis
**Description:** Analyzing Strengths, Weaknesses, Opportunities, and Threats.

**Use Cases:**
- Strategic planning
- Competitive analysis
- Project assessment
- Personal development

**Integration:** Add structured analysis template to planning framework

#### [ ] 12. Porter's Five Forces
**Description:** Framework for analyzing competitive forces in an industry.

**Use Cases:**
- Market analysis
- Competitive strategy
- Industry assessment
- Investment decisions

**Integration:** Add competitive analysis module

#### [ ] 13. Blue Ocean Strategy
**Description:** Creating uncontested market space rather than competing in existing markets.

**Use Cases:**
- Innovation strategy
- Product development
- Market positioning
- Differentiation

**Integration:** Add innovation-focused planning template

#### [ ] 14. Jobs-to-be-Done Framework
**Description:** Understanding what customers are trying to accomplish.

**Use Cases:**
- Product development
- Customer research
- Market segmentation
- Innovation

**Integration:** Add customer-centric planning approach

#### [ ] 15. Lean Startup Methodology
**Description:** Build-Measure-Learn cycle for rapid iteration and validation.

**Use Cases:**
- Product development
- Startup planning
- Innovation projects
- Hypothesis testing

**Integration:** Add iterative planning with validation checkpoints

### Mathematical and Analytical Models

#### [ ] 16. Pareto Principle (80/20 Rule)
**Description:** 80% of effects come from 20% of causes.

**Use Cases:**
- Priority setting
- Resource allocation
- Problem solving
- Optimization

**Integration:** Add impact/effort analysis to planning steps

#### [ ] 17. Expected Value Calculation
**Description:** Calculating the average outcome when the future includes scenarios with different probabilities.

**Use Cases:**
- Investment decisions
- Risk assessment
- Strategic planning
- Resource allocation

**Integration:** Add probability-weighted outcome analysis

#### [ ] 18. Monte Carlo Simulation
**Description:** Using random sampling to understand the impact of risk and uncertainty.

**Use Cases:**
- Risk analysis
- Project planning
- Financial modeling
- Decision making

**Integration:** Add uncertainty modeling to planning framework

#### [ ] 19. Regression to the Mean
**Description:** Extreme measurements tend to be closer to the average on subsequent measurements.

**Use Cases:**
- Performance evaluation
- Forecasting
- Quality control
- Investment analysis

**Integration:** Add trend analysis with mean reversion awareness

#### [ ] 20. Compound Interest
**Description:** Interest calculated on initial principal and accumulated interest.

**Use Cases:**
- Financial planning
- Investment strategy
- Growth planning
- Resource accumulation

**Integration:** Add exponential growth modeling

### Systems and Process Models

#### [ ] 21. Feedback Loops
**Description:** Outputs of a system are routed back as inputs, creating a loop.

**Use Cases:**
- System design
- Process improvement
- Organizational behavior
- Product development

**Integration:** Add feedback mechanism identification in systems thinking

#### [ ] 22. Network Effects
**Description:** Value of a product/service increases as more people use it.

**Use Cases:**
- Platform strategy
- Product planning
- Market analysis
- Growth strategy

**Integration:** Add network value analysis to strategic planning

#### [ ] 23. Economies of Scale
**Description:** Cost advantages obtained due to size, output, or scale of operation.

**Use Cases:**
- Business strategy
- Operations planning
- Cost analysis
- Capacity planning

**Integration:** Add scale analysis to resource planning

#### [ ] 24. Bottleneck Theory (Theory of Constraints)
**Description:** System performance is limited by its weakest component.

**Use Cases:**
- Process optimization
- Performance improvement
- Resource allocation
- System design

**Integration:** Add constraint identification to critical path analysis

#### [ ] 25. Minimum Viable Product (MVP)
**Description:** Product with minimum features to satisfy early customers and provide feedback.

**Use Cases:**
- Product development
- Startup strategy
- Feature prioritization
- Risk reduction

**Integration:** Add MVP planning template

### Psychological and Behavioral Models

#### [ ] 26. Loss Aversion
**Description:** People prefer avoiding losses over acquiring equivalent gains.

**Use Cases:**
- Change management
- Product positioning
- Negotiation
- Risk communication

**Integration:** Add loss/gain framing in decision analysis

#### [ ] 27. Social Proof
**Description:** People follow the actions of others in uncertain situations.

**Use Cases:**
- Marketing strategy
- Change management
- Product adoption
- Team dynamics

**Integration:** Add social validation steps in implementation planning

#### [ ] 28. Reciprocity Principle
**Description:** People feel obligated to return favors.

**Use Cases:**
- Relationship building
- Negotiation
- Team collaboration
- Customer relations

**Integration:** Add reciprocity considerations in stakeholder planning

#### [ ] 29. Commitment and Consistency
**Description:** People want to be consistent with previous commitments.

**Use Cases:**
- Goal setting
- Change management
- Team alignment
- Customer retention

**Integration:** Add commitment tracking in planning framework

#### [ ] 30. Scarcity Principle
**Description:** People value things more when they are rare or limited.

**Use Cases:**
- Product positioning
- Resource allocation
- Priority setting
- Motivation

**Integration:** Add scarcity analysis to strategic planning

### Problem-Solving Models

#### [ ] 31. Root Cause Analysis
**Description:** Method of problem solving to identify the root causes of problems.

**Use Cases:**
- Problem diagnosis
- Quality improvement
- Incident investigation
- Process optimization

**Integration:** Add systematic root cause investigation steps

#### [ ] 32. Five Whys Technique
**Description:** Asking "why" five times to get to the root of a problem.

**Use Cases:**
- Problem solving
- Process improvement
- Debugging
- Understanding causation

**Integration:** Add iterative questioning framework

#### [ ] 33. Fishbone Diagram (Ishikawa)
**Description:** Visual tool to systematically identify potential causes of a problem.

**Use Cases:**
- Problem analysis
- Quality control
- Team brainstorming
- Process improvement

**Integration:** Add cause categorization framework

#### [ ] 34. Design Thinking
**Description:** Human-centered approach to innovation and problem-solving.

**Use Cases:**
- Product development
- Service design
- Innovation projects
- User experience

**Integration:** Add empathy-driven planning approach

#### [ ] 35. Lateral Thinking
**Description:** Solving problems through indirect and creative approaches.

**Use Cases:**
- Innovation
- Creative problem solving
- Breakthrough thinking
- Alternative solutions

**Integration:** Add creative ideation steps to planning

### Economic and Financial Models

#### [ ] 36. Opportunity Cost
**Description:** The value of the best alternative foregone when making a choice.

**Use Cases:**
- Resource allocation
- Investment decisions
- Strategic planning
- Priority setting

**Integration:** Add alternative analysis to decision framework

#### [ ] 37. Sunk Cost Fallacy
**Description:** Continuing investment based on previously invested resources rather than future value.

**Use Cases:**
- Project management
- Investment decisions
- Strategic planning
- Resource allocation

**Integration:** Add sunk cost awareness in decision checkpoints

#### [ ] 38. Time Value of Money
**Description:** Money available now is worth more than the same amount in the future.

**Use Cases:**
- Financial planning
- Investment analysis
- Project evaluation
- Resource allocation

**Integration:** Add present value calculations to financial planning

#### [ ] 39. Risk-Return Tradeoff
**Description:** Higher potential returns come with higher risk.

**Use Cases:**
- Investment strategy
- Project planning
- Resource allocation
- Strategic decisions

**Integration:** Add risk-return analysis to decision framework

#### [ ] 40. Diversification
**Description:** Spreading investments or efforts to reduce risk.

**Use Cases:**
- Portfolio management
- Strategic planning
- Risk management
- Resource allocation

**Integration:** Add diversification analysis to risk planning

### Communication and Influence Models

#### [ ] 41. Pyramid Principle
**Description:** Structuring communication with conclusion first, then supporting arguments.

**Use Cases:**
- Presentation design
- Report writing
- Strategic communication
- Executive briefings

**Integration:** Add structured communication templates

#### [ ] 42. Storytelling Framework
**Description:** Using narrative structure to communicate ideas effectively.

**Use Cases:**
- Stakeholder communication
- Change management
- Product marketing
- Team alignment

**Integration:** Add narrative planning to communication strategy

#### [ ] 43. Active Listening
**Description:** Fully concentrating on, understanding, and responding to the speaker.

**Use Cases:**
- Team collaboration
- Customer research
- Conflict resolution
- Stakeholder management

**Integration:** Add listening checkpoints in stakeholder planning

#### [ ] 44. Nonviolent Communication
**Description:** Communication approach based on empathy and honest expression.

**Use Cases:**
- Conflict resolution
- Team management
- Customer service
- Change management

**Integration:** Add empathetic communication framework

#### [ ] 45. Influence Mapping
**Description:** Identifying and understanding stakeholder influence relationships.

**Use Cases:**
- Stakeholder management
- Change management
- Political navigation
- Coalition building

**Integration:** Add stakeholder influence analysis

### Learning and Adaptation Models

#### [ ] 46. Growth Mindset
**Description:** Belief that abilities can be developed through dedication and hard work.

**Use Cases:**
- Personal development
- Team building
- Learning culture
- Innovation

**Integration:** Add learning-oriented planning approach

#### [ ] 47. Deliberate Practice
**Description:** Purposeful practice with immediate feedback and repetition.

**Use Cases:**
- Skill development
- Performance improvement
- Training programs
- Expertise building

**Integration:** Add practice planning framework

#### [ ] 48. Double-Loop Learning
**Description:** Questioning underlying assumptions and mental models, not just actions.

**Use Cases:**
- Organizational learning
- Strategic planning
- Process improvement
- Innovation

**Integration:** Add assumption questioning in audit framework

#### [ ] 49. Antifragility
**Description:** Systems that gain from disorder and stress.

**Use Cases:**
- System design
- Risk management
- Strategic planning
- Resilience building

**Integration:** Add stress-testing and adaptation planning

#### [ ] 50. Black Swan Events
**Description:** Rare, unpredictable events with major impact.

**Use Cases:**
- Risk planning
- Scenario analysis
- Strategic planning
- Crisis preparation

**Integration:** Add extreme scenario planning

### Meta-Cognitive Models

#### [ ] 51. Metacognition
**Description:** Thinking about thinking; awareness of one's own thought processes.

**Use Cases:**
- Learning optimization
- Decision quality
- Problem solving
- Self-improvement

**Integration:** Add reflection steps in planning framework

#### [ ] 52. Dunning-Kruger Effect
**Description:** People with limited knowledge overestimate their competence.

**Use Cases:**
- Team management
- Skill assessment
- Learning planning
- Quality control

**Integration:** Add competence assessment in planning

#### [ ] 53. Impostor Syndrome
**Description:** Feeling like a fraud despite evidence of competence.

**Use Cases:**
- Personal development
- Team management
- Performance evaluation
- Confidence building

**Integration:** Add confidence-building steps in personal planning

#### [ ] 54. Beginner's Mind
**Description:** Approaching situations with openness and lack of preconceptions.

**Use Cases:**
- Learning
- Innovation
- Problem solving
- Adaptation

**Integration:** Add fresh perspective steps in planning

## Integration Guidelines

### Adding New Mental Models

1. **Define the Model:** Create a clear description and use cases
2. **Implement Logic:** Add to `src/panda_mcp/core/planning/mental_models.py`
3. **Create Templates:** Add planning step templates
4. **Add Tests:** Create validation tests
5. **Update Documentation:** Add to this file with [x] status

### Usage in Planning

Mental models can be specified in planning requests:
```python
context = {
    "mental_models": ["first_principles", "systems_thinking"],
    "domain": "software_development"
}
```

### Combining Models

Multiple mental models can be combined for comprehensive analysis:
- **Strategic + Analytical:** SWOT + Expected Value
- **Creative + Systematic:** Design Thinking + First Principles
- **Risk + Decision:** Monte Carlo + Decision Trees

### Framework Extension

The mental models framework is designed to be extensible. New models should follow the established pattern of:
1. Clear problem identification
2. Structured analysis steps
3. Decision support
4. Implementation guidance
5. Validation criteria 