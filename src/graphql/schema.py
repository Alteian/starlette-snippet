import strawberry

from strawberry import Schema
from strawberry.extensions import QueryDepthLimiter, ValidationCache
from strawberry.tools import merge_types
from strawberry.types import Info


@strawberry.type
class PingQuery:
    @strawberry.field
    def ping(self) -> str:
        return "pong"


@strawberry.type
class ContextGreetingQuery:
    @strawberry.field
    def greeting(self, info: Info) -> str:
        return info.context.greeting_from_context


Query = merge_types(
    name="Query",
    types=(
        PingQuery,
        ContextGreetingQuery,
    ),
)


schema = Schema(
    query=Query,
    extensions=[QueryDepthLimiter(max_depth=10), ValidationCache(maxsize=100)],
)
