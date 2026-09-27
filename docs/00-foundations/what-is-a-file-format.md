# What Is a File Format?

A **file format** is a defined way of organizing information inside a file so software can interpret the stored bytes correctly.

A filename such as:

```text
report.pdf
```

contains two different ideas:

- `report` → filename
- `.pdf` → filename extension

The extension is a hint. The actual structure is defined by the format specification and encoded bytes.

## A useful abstraction

```text
Physical storage
      ↓
Bytes
      ↓
Encoding / binary structure
      ↓
Format specification
      ↓
Parser / reader
      ↓
Application data
```

## Format dimensions

A format can be:

- human-readable or machine-oriented
- text-based or binary
- schema-less, schema-flexible, or schema-defined
- compressed or uncompressed
- streaming-friendly or random-access friendly
- open, standardized, or proprietary
- single-purpose or general-purpose

## Example

JSON:

```json
{
  "name": "Charan",
  "skills": ["Python", "SQL"]
}
```

The file is text-based and easy for humans to inspect.

Parquet stores structured data differently. It is binary, column-oriented, and designed for analytical workloads.

## Important distinction

> **Extension ≠ format ≠ MIME type ≠ encoding**

These concepts are related but not interchangeable.
