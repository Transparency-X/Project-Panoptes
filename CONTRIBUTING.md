# Contributing to Project Panoptes

Thank you for helping build the definitive open resource on surveillance cults.  
Please read this guide and the safety disclaimer before contributing.

## Ways to Contribute

- **Add a new group** – Submit a JSON file under `data/groups/`.
- **Improve an existing group** – Fill in missing fields, add sources, update active status.
- **Enhance schemas** – Propose changes to `schema/` to capture new patterns.
- **Write documentation** – Fix typos, add glossary terms, translate content.
- **Develop tools** – Build software under `tools/` that uses the structured data.

## Adding or Updating a Group

1. Read the schema: [`schema/group.schema.json`](./schema/group.schema.json).
2. Create a JSON file named with a slug of the group’s name (e.g., `nxium.json`).
3. Fill in **all required fields** (id, name, active_status, surveillance_pillars, sources).
4. Validate locally:
   ```bash
   python scripts/validate_data.py


Open a Pull Request. The CI workflow will also validate automatically.

Data Guidelines
Sources are mandatory. Every factual claim must be backed by a citation (news report, court document, academic paper, or survivor account).

Respect survivors. Do not include personally identifying information without explicit consent.

Stay objective. Present documented facts; avoid editorialising.

Proposing Schema Changes
Open an issue describing the use case. The schema should remain stable, but we welcome careful extensions (e.g., new pillar types, additional recruitment methods).

Community Standards
This project adheres to a Code of Conduct. We expect all contributors to create a safe, welcoming environment.

Questions?
Start a Discussion or open an issue.




