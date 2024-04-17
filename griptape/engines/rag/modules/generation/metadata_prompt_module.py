from attr import define, field
from griptape.engines.rag import RagContext
from griptape.engines.rag.modules import BaseGenerationModule
from griptape.utils import J2


@define
class MetadataPromptModule(BaseGenerationModule):
    metadata: str = field(kw_only=True)

    def generate(self, context: RagContext) -> RagContext:
        context.before_query.append(
            J2("data/modules/metadata/system.j2").render(metadata=self.metadata)
        )

        return context
