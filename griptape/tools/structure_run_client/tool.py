from __future__ import annotations

from attr import define, field
from schema import Literal, Schema

from griptape.artifacts import BaseArtifact, TextArtifact
from griptape.drivers import BaseStructureRunDriver
from griptape.tools.base_tool import BaseTool
from griptape.utils.decorators import activity


@define
class StructureRunClient(BaseTool):
    """
    Attributes:
        description: A description of what the Structure does.
        driver: Driver to run the Structure.
    """

    description: str = field(kw_only=True)
    driver: BaseStructureRunDriver = field(kw_only=True)

    @activity(
        config={
            "description": "Can be used to run a Griptape Structure with the following description: {{ self.description }}",
            "schema": Schema(
                {Literal("args", description="A list of string arguments to submit to the Structure Run"): list}
            ),
        }
    )
    def run_structure(self, params: dict) -> BaseArtifact:
        args: list[str] = params["values"]["args"]

        return self.driver.run(*[TextArtifact(arg) for arg in args])
