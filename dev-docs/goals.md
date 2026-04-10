# Project Goals

FastReader is a Python middleware that sits between an AI agent and raw documents. It pre-processes document structure using code-based heuristics (no LLM calls), producing a JSON manifest of structural markers. The agent receives a compact summary of what's in the document and requests only the sections it needs, reducing token usage and cost.
