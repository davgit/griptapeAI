from abc import ABC, abstractmethod
from attr import define
from griptape.engines.rag import RagContext
from griptape.engines.rag.modules import BaseModule


@define(kw_only=True)
class BaseBeforeGenerationModule(BaseModule, ABC):
    @abstractmethod
    def run(self, context: RagContext) -> RagContext:
        ...
