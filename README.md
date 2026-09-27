# 📂 CS File Formats Handbook

> **A structured, practical knowledge base for understanding the files behind modern computing.**

Most developers learn programming languages. Far fewer build a mental model of the **files those languages, tools, platforms, databases, pipelines, operating systems, and AI systems actually produce and consume**.

This repository is designed to close that gap.

It is not just a list of extensions. It is a **living file-format reference** covering what a format means, where it belongs in a software system, how it behaves, what tools use it, what can go wrong, and when one format should be preferred over another.

---

## 🎯 What this repository covers

| Domain | What you'll find |
|---|---|
| 🧠 Foundations | text vs binary, encoding, MIME types, magic bytes, serialization |
| 💻 Programming | source, bytecode, binaries, libraries, package manifests |
| 🌐 Web | HTML, CSS, JS/TS, WebAssembly, manifests, API payloads |
| 📊 Data Engineering | CSV, JSONL, Parquet, Avro, ORC, Arrow, NDJSON |
| 🗄️ Databases | SQL dumps, SQLite, database files, migrations, backups |
| 🤖 AI / ML | ONNX, PyTorch, TensorFlow, SafeTensors, GGUF, checkpoints |
| ☁️ Cloud / DevOps | Docker, Kubernetes, Terraform, CI/CD, Helm, env files |
| 🔐 Security | PEM, certificates, keys, CSRs, signatures, hashes |
| 📚 Documents | Markdown, PDF, DOCX, LaTeX, EPUB |
| 🖼️ Images | PNG, JPEG, SVG, WebP, TIFF, ICO |
| 🎬 Media | MP4, MKV, WebM, WAV, FLAC, AAC, containers/codecs |
| 📦 Archives | ZIP, TAR, GZIP, 7z, Zstandard, layered archives |
| 🖥️ Systems | EXE, DLL, ELF, SO, DMG, DEB, RPM, services |
| 📱 Mobile | APK, AAB, DEX, AAR, IPA, Xcode artifacts |
| 🔬 Scientific | MAT, HDF5, NetCDF, FITS, GRIB |
| 🗺️ GIS / 3D | GeoJSON, Shapefile, KML, OBJ, STL, GLTF |
| 🧪 Testing / Observability | JUnit XML, coverage, logs, traces, reports |

---

## 🧭 The mental model

A file extension alone does **not** tell the whole story.

Think of a file as:

```text
FILE
 ├── Name
 ├── Extension
 ├── MIME type
 ├── Encoding
 ├── Container / format
 ├── Schema
 ├── Compression
 ├── Metadata
 ├── Payload
 └── Integrity / security properties
```

For example:

```text
data.parquet
    ↓
Columnar storage format
    ↓
Schema + columns + statistics
    ↓
Optional compression
    ↓
Optimized for analytical workloads
```

Whereas:

```text
model.safetensors
    ↓
Tensor serialization format
    ↓
Tensor metadata + tensor data
    ↓
Designed for safer model-weight loading
```

---

## 🗺️ Repository map

```text
CS-File-Formats-Handbook/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── ROADMAP.md
├── Makefile
│
├── catalogs/
│   ├── master-catalog.csv
│   ├── master-catalog.json
│   ├── extension-index.json
│   ├── mime-types.json
│   └── format-families.json
│
├── docs/
│   ├── 00-foundations/
│   ├── 01-programming-languages/
│   ├── 02-web-development/
│   ├── 03-data-engineering/
│   ├── 04-databases/
│   ├── 05-ai-ml/
│   ├── 06-cloud-devops/
│   ├── 07-git-github/
│   ├── 08-security/
│   ├── 09-documents/
│   ├── 10-images/
│   ├── 11-audio-video/
│   ├── 12-archives-compression/
│   ├── 13-operating-systems/
│   ├── 14-mobile/
│   ├── 15-scientific-engineering/
│   ├── 16-gis-3d-specialized/
│   ├── 17-testing-observability/
│   └── 18-decision-guides/
│
├── examples/
│   ├── text/
│   ├── config/
│   ├── data/
│   ├── code/
│   └── metadata/
│
└── scripts/
    ├── validate_catalog.py
    ├── find_extension.py
    └── stats.py
```

---

## 🔎 How to use it

### If you know the extension

Start with:

```text
catalogs/master-catalog.csv
```

or use:

```bash
python scripts/find_extension.py parquet
```

### If you know the problem

Use the decision guides:

- [Choosing a data format](docs/18-decision-guides/choosing-data-format.md)
- [Choosing an API format](docs/18-decision-guides/choosing-api-format.md)
- [Choosing an image format](docs/18-decision-guides/choosing-image-format.md)
- [Choosing an archive](docs/18-decision-guides/choosing-archive.md)
- [Choosing a model format](docs/18-decision-guides/choosing-model-format.md)

### If you are learning fundamentals

Start with:

- [What is a file format?](docs/00-foundations/what-is-a-file-format.md)
- [Extension vs format](docs/00-foundations/extension-vs-format.md)
- [Text vs binary](docs/00-foundations/text-vs-binary.md)
- [Encoding](docs/00-foundations/encoding.md)
- [Serialization](docs/00-foundations/serialization.md)
- [Containers vs codecs](docs/00-foundations/containers-vs-codecs.md)

---

## ⭐ Why this is different

This handbook organizes formats by **engineering role**, not alphabetically.

A format entry is evaluated across dimensions such as:

```text
Purpose
Storage model
Human readability
Schema support
Compression
Streaming
Random access
Interoperability
Typical scale
Tooling
Security considerations
Common mistakes
```

That makes the repository useful for:

- students
- software engineers
- backend developers
- data engineers
- ML engineers
- DevOps engineers
- cloud engineers
- security learners
- technical interview preparation

---

## 📈 Scope

The catalog intentionally includes:

- common formats every CS student should recognize
- formats frequently encountered in professional engineering
- specialized scientific and engineering formats
- configuration and infrastructure files
- package and dependency manifests
- model and dataset formats
- system and executable formats
- files with **no conventional extension**

This is a reference, not a claim that every obscure proprietary format is included.

---

## 🔐 Security principle

Never commit:

```text
.env
private keys
production database dumps
credentials
access tokens
customer data
personal documents
unapproved model weights
```

Use `.gitignore`, secret managers, and environment variables appropriately.

---

## 🧪 Validation

Run:

```bash
python scripts/validate_catalog.py
python scripts/stats.py
```

Search the catalog:

```bash
python scripts/find_extension.py json
python scripts/find_extension.py parquet
python scripts/find_extension.py safetensors
```

---

## 🤝 Contributing

New formats are welcome.

Every catalog entry should answer:

1. What is it?
2. What problem does it solve?
3. Is it text or binary?
4. What systems use it?
5. What are its strengths?
6. What are its limitations?
7. What alternatives exist?
8. What security considerations matter?

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

