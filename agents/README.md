# Engineering Agent Layer

Agents are **routing contracts**, not independent sources of truth. They tell an AI runtime which skill/tool/knowledge to use and when to stop. The core stays provider-agnostic; runtime-specific wiring belongs in `adapters/`.

Default flow: `orchestrator` → `intake` → specialist(s) → `verification` → deliverable/release state.

Never run every specialist for every question. Route the smallest set that covers the task.
