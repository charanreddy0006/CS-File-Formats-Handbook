# Repository Architecture

```text
                    ┌────────────────────────┐
                    │       README.md         │
                    │  Human entry point      │
                    └───────────┬────────────┘
                                │
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
       Documentation        Catalogs            Examples
             │                  │                  │
       domain guides       CSV / JSON        safe samples
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ↓
                         Validation scripts
                                │
                                ↓
                          GitHub Actions
```

## Design principle

The repository separates:

- **knowledge** → `docs/`
- **machine-readable metadata** → `catalogs/`
- **safe demonstrations** → `examples/`
- **automation** → `scripts/` and `.github/`

This makes the project both readable and programmable.
