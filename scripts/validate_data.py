#!/usr/bin/env python3
"""Validate all group JSON files against the schema."""
import json
import os
from jsonschema import validate, RefResolver, Draft202012Validator

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "..", "schema")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "groups")

def load_schema(name):
    path = os.path.join(SCHEMA_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    group_schema = load_schema("group.schema.json")
    source_schema = load_schema("source.schema.json")

    # Build a resolver that knows about sibling schemas
    resolver = RefResolver(
        base_uri=f"file://{SCHEMA_DIR}/",
        referrer=group_schema,
        store={
            "source.schema.json": source_schema
        }
    )
    Validator = Draft202012Validator
    validator = Validator(group_schema, resolver=resolver)

    for filename in sorted(os.listdir(DATA_DIR)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            instance = json.load(f)
        print(f"Validating {filename}...", end=" ")
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        if errors:
            print("FAIL")
            for error in errors:
                print(f"  - {error.message} at {'/'.join(str(p) for p in error.absolute_path)}")
        else:
            print("OK")

if __name__ == "__main__":
    main()
