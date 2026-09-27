# Containers vs Codecs

This distinction matters especially for multimedia.

## Container

A container packages one or more streams plus metadata.

Examples:

```text
MP4
MKV
WebM
AVI
MOV
```

## Codec

A codec encodes or decodes the actual media stream.

Examples:

```text
H.264
H.265 / HEVC
AV1
VP9
AAC
Opus
FLAC
```

So:

```text
video.mp4
   └── MP4 container
         ├── H.264 video stream
         └── AAC audio stream
```

Changing the container does not necessarily re-encode the media.
