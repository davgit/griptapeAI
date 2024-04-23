from __future__ import annotations

from attr import define, field

from griptape.artifacts import MediaArtifact


@define
class AudioArtifact(MediaArtifact):
    """AudioArtifact is a type of MediaArtifact representing audio.

    Attributes:
        value: Raw bytes representing media data.
        media_type: The type of media, defaults to "image".
        format: The format of the media, like png, jpeg, or gif.
        name: Artifact name, generated using creation time and a random string.
        model: Optionally specify the model used to generate the media.
        prompt: Optionally specify the prompt used to generate the media.
    """

    media_type: str = "audio"