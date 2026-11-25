
import strawberry

from starlette.concurrency import run_in_threadpool
from strawberry.fastapi import GraphQLRouter

from database import SessionLocal
from models import User


@strawberry.type
class UserGraphQL:
    id: int
    role: str
    is_admin: bool


def find_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)

        if user is None:
            return None

        return UserGraphQL(
            id=user.id,
            role=user.role,
            is_admin=user.role == "admin"
        )


@strawberry.type
class Query:

    @strawberry.field
    async def user(self, id: int) -> UserGraphQL | None:
        return await run_in_threadpool(find_user, id)


schema = strawberry.Schema(query=Query)

graphql_router = GraphQLRouter(schema)