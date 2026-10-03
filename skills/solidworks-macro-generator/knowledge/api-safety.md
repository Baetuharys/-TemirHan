# SolidWorks API safety

## Generation rules
- Identify document type and active configuration before selecting API objects.
- Prefer the smallest API chain that accomplishes the task.
- Store object references explicitly and check for null/failed selections.
- Avoid relying on selection state when a direct object method is available.
- Mark version-sensitive API members for verification.
- Never silently save, overwrite, close, export, or modify production files in a macro without making that behavior explicit.
- For batch operations, add dry-run/report mode when practical.

## Debugging
Capture:
- SolidWorks version;
- document type;
- active configuration;
- failing line/member;
- error number/message;
- expected vs actual behavior.

The skill must distinguish generated code from code actually executed by the user.
