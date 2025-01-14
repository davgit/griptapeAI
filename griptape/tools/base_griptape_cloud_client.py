from __future__ import annotations
from abc import ABC
from attr import Factory, define, field
from griptape.tools import BaseTool


@define
class BaseGriptapeCloudClient(BaseTool, ABC):
    """
    Attributes:
        base_url: Base URL for the Griptape Cloud Knowledge Base API.
        api_key: API key for Griptape Cloud.
        headers: Headers for the Griptape Cloud Knowledge Base API.
    """

    base_url: str = field(default="https://cloud.griptape.ai", kw_only=True)
    api_key: str = field(kw_only=True)
    headers: dict = field(
        default=Factory(lambda self: {"Authorization": f"Bearer {self.api_key}"}, takes_self=True), kw_only=True
    )
