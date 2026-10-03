# Usage Guide

## 1. Select the task
Start with the smallest skill that directly matches the request. For a multi-stage job, use an end-to-end workflow and invoke specialist skills at the relevant gates.

## 2. Load the skill
The reusable core is the relevant `skills/<slug>/SKILL.md` plus only the knowledge/workflow files needed for the task.

## 3. Keep the provider separate
The engineering method does not depend on the AI provider. The provider adapter only describes how to supply the core skill to a runtime.

## 4. For a normal engineering task
```text
Task intake
→ Context audit
→ Specialist analysis
→ Verification
→ Output contract
```

## 5. For a manufacturing release
```text
Model
→ Sheet metal validation
→ Flat pattern
→ Drawing review
→ DXF release
→ Cut/mark process mapping
→ Bending review
→ Weld/fastener review
→ Assembly review
→ Cost/documentation
→ Release gate
```

## 6. Do not overclaim
If the repository contains a workflow but the user's actual SolidWorks version, CAM system, laser controller, material certificate, drawing standard, or shop capability is unknown, report that dependency instead of inventing a tool-specific answer.
