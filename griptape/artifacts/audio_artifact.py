from __future__ import annotations

from attr import define

from griptape.artifacts import MediaArtifact


@define
class AudioArtifact(MediaArtifact):
    """AudioArtifact is a type of MediaArtifact representing audio."""

    media_type: str = "audio"
