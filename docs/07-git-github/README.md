# 🐙 Git & GitHub Files

Important repository-level files:

```text
.gitignore
.gitattributes
.gitmodules
.gitkeep
README.md
LICENSE
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
CHANGELOG.md
CODEOWNERS
```

## Git internals

The `.git/` directory stores repository metadata, references, objects, and configuration.

It should normally not be manually edited.

## GitHub automation

```text
.github/
└── workflows/
    └── ci.yml
```

Workflow files describe automated jobs such as:

- tests
- linting
- packaging
- releases
- deployments

## Important repository hygiene

Do not commit:

```text
.env
credentials
private keys
large generated binaries
local virtual environments
IDE caches
database dumps
```
