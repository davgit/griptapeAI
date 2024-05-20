from __future__ import annotations

from typing import Optional

from attr import define, field

from griptape.artifacts import BaseArtifact, TextArtifact
from griptape.mixins import SerializableMixin


@define(kw_only=True)
class ActionChunkArtifact(TextArtifact, SerializableMixin):
    value: Optional[str] = field(default=None, metadata={"serializable": True})
    tag: Optional[str] = field(default=None, metadata={"serializable": True})
    name: Optional[str] = field(default=None, metadata={"serializable": True})
    path: Optional[str] = field(default=None, metadata={"serializable": True})
    partial_input: Optional[str] = field(default=None, metadata={"serializable": True})
    index: Optional[int] = field(default=None, metadata={"serializable": True})

    def __add__(self, other: BaseArtifact) -> ActionChunkArtifact:
        if isinstance(other, ActionChunkArtifact):
            return ActionChunkArtifact(
                value=(self.value or "") + (other.value or ""),
                tag=(self.tag or "") + (other.tag or ""),
                name=(self.name or "") + (other.name or ""),
                path=(self.path or "") + (other.path or ""),
                partial_input=(self.partial_input or "") + (other.partial_input or ""),
                index=self.index,
            )
        else:
            return ActionChunkArtifact(value=(self.value or "") + (other.value or ""))
