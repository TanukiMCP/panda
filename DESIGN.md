# PandA MCP Refactoring Design

This document outlines the design for refactoring the PandA MCP to support multi-step, sequential reasoning for LLMs.

## 1. Core Objective

The primary goal is to empower an LLM to perform complex tasks by breaking them down into a sequence of steps. At each step, the LLM can leverage specialized "mental models" for planning and "auditing frameworks" for analysis.

## 2. New Components

### 2.1. `SequentialExecutor`

-   **Purpose**: Manages the execution of a sequence of tasks defined by the LLM.
-   **Location**: `src/panda_mcp/core/sequencer.py`
-   **Class**: `SequentialExecutor`
-   **Data Structures**:
    -   `steps`: A list of dictionaries, where each step defines the `tool` to use (`panda_plan` or `panda_audit`) and the `parameters` for that tool.
    -   `context`: A dictionary for sharing state and data across steps.
-   **Methods**:
    -   `__init__(self, steps, initial_context={})`: Initializes with steps and context.
    -   `run(self)`: Executes the full sequence of steps.
    -   `step(self)`: Executes one step at a time for interactive control.

### 2.2. Modular Mental Models (`PandaPlan`)

-   **Purpose**: To make the `PandaPlan` tool extensible with new planning frameworks (mental models) without modifying the core code.
-   **Directory**: `src/panda_mcp/mental_models/`
-   **Structure**:
    -   Each mental model (e.g., "first principles") will be in its own Python file.
    -   A base class, `MentalModel`, in `src/panda_mcp/mental_models/base.py` will define a common interface.
-   **Refactoring `PandaPlan`**:
    -   `PandaPlan` will be updated to dynamically load all mental models from the `mental_models` directory.

### 2.3. Modular Auditing Frameworks (`PandaAudit`)

-   **Purpose**: To make the `PandaAudit` tool extensible with new sets of auditing patterns.
-   **Directory**: `src/panda_mcp/auditing_frameworks/`
-   **Structure**:
    -   Each auditing framework (e.g., "security") will be in its own file, defining the relevant patterns.
    -   A base class, `AuditingFramework`, in `src/panda_mcp/auditing_frameworks/base.py` will provide a common structure.
-   **Refactoring `PandaAudit`**:
    -   `PandaAudit` will be updated to dynamically load all auditing frameworks from the `auditing_frameworks` directory.

## 3. New High-Level Tool

### 3.1. `panda_reason`

-   **Purpose**: A single, powerful tool for the LLM to initiate sequential reasoning tasks.
-   **Function Signature**: `panda_reason(steps: List[Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]`
-   **Functionality**:
    -   Instantiates the `SequentialExecutor`.
    -   Runs the defined sequence of steps.
    -   Returns the aggregated results from all steps.

## 4. Project Structure Changes

The following new directories will be created:

-   `src/panda_mcp/core/sequencer/`
-   `src/panda_mcp/mental_models/`
-   `src/panda_mcp/auditing_frameworks/`

This design provides a clear path to achieving the desired multi-step reasoning capabilities in a modular and extensible way. 