# Text vs Binary Files

## Text

Text files represent information using character encodings.

Examples:

```text
.txt
.md
.json
.csv
.yaml
.xml
.py
.sql
.html
.css
```

Advantages:

- easy to inspect
- easy to diff
- easy to generate
- generally portable

## Binary

Binary formats represent data using byte structures that are not intended to be read directly as text.

Examples:

```text
.png
.parquet
.sqlite
.exe
.pdf
.mp4
.onnx
```

Binary does **not** automatically mean compressed.

## Engineering trade-off

| Property | Text | Binary |
|---|---:|---:|
| Human readability | High | Low |
| Compactness | Usually lower | Often higher |
| Schema richness | Variable | Often strong |
| Random access | Variable | Format-dependent |
| Debugging | Easy | Requires tools |
| Interoperability | Often high | Format-dependent |

The right choice depends on the workload.
