# 🤖 AI / ML File Formats

AI systems use several different artifact classes.

## Dataset

```text
.csv
.json
.jsonl
.parquet
.arrow
.h5
```

## Model weights

```text
.pt
.pth
.ckpt
.safetensors
.bin
.gguf
```

## Model interchange

```text
.onnx
```

## TensorFlow ecosystem

```text
.pb
.h5
.keras
```

## NumPy

```text
.npy
.npz
```

## Format selection

| Need | Common choice |
|---|---|
| NumPy array | `.npy` |
| Multiple NumPy arrays | `.npz` |
| PyTorch weights | `.pt` / `.pth` |
| Safer tensor serialization | `.safetensors` |
| Cross-framework inference | `.onnx` |
| Local LLM distribution | `.gguf` |
| TensorFlow model | `.keras` / ecosystem-specific formats |

## Important security principle

Model files are executable-adjacent data from a trust perspective. Some serialization mechanisms can reconstruct arbitrary Python objects or otherwise create security risk.

Do not load untrusted model artifacts blindly.
