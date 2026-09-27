# Configuration File Hierarchy

Modern applications commonly combine:

```text
defaults
   ↓
configuration file
   ↓
environment variables
   ↓
runtime arguments
   ↓
secret manager
```

Example:

```text
config.yaml
      +
ENVIRONMENT
      +
DATABASE_URL
      +
secret manager
```

Do not place secrets in source-controlled configuration just because the configuration format is convenient.

## Common configuration formats

```text
.env
.yaml
.yml
.json
.toml
.ini
.properties
.conf
```

Choose based on tooling, schema needs, readability, and ecosystem conventions.
