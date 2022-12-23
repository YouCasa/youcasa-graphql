import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from users.graphql.types import UserType

class UserQueries(graphene.ObjectType):
    get_user = graphene.Field(UserType)

    @login_required
    def resolve_get_user(self, info: graphene.ResolveInfo, **_):
        print(info.context)
        if info.context.user.is_authenticated:
            return info.context.user
        raise GraphQLError("User must be authenticated")
