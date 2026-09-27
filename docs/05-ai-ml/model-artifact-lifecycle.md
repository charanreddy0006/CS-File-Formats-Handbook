# ML Model Artifact Lifecycle

```text
Training
   ↓
Checkpoint
   ↓
Validation
   ↓
Serialization
   ↓
Artifact registry
   ↓
Deployment
   ↓
Inference
   ↓
Monitoring
```

Potential artifacts:

```text
dataset.parquet
model.safetensors
model.onnx
tokenizer.json
config.json
metrics.json
```

A production model is often a **bundle of related artifacts**, not one file.

## Provenance matters

Record:

- model version
- source repository
- training data version
- framework version
- conversion step
- checksum
- evaluation results
- intended runtime
