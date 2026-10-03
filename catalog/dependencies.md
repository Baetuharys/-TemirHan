# Dependency Policy

Dependencies express reusable behavior that must be available for a prompt or blueprint to work as intended.

- Prefer small reusable modules over duplicated instructions.
- Keep domain knowledge separate from runtime-specific adapter behavior.
- Avoid circular dependencies.
- Do not add a dependency merely because it is related; add it when the target actually relies on its behavior.
