# Usage Guide

## Create a prompt

```bash
python scripts/new_prompt.py master my-master
python scripts/new_prompt.py module my-module --category capability
python scripts/new_prompt.py blueprint my-skill
```

## Regenerate catalog

```bash
python scripts/generate_catalog.py
```

## Validate

```bash
python scripts/validate_metadata.py
python scripts/validate_catalog.py
python scripts/check_missing_links.py
python scripts/validate_localization.py
```

## Development rule

A reusable behavior starts as a module. A multi-module workflow starts as a master or blueprint. Only after representative test cases and stable input/output contracts should a blueprint become a packaged skill.
