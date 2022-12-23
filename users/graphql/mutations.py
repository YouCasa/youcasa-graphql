import graphene
import graphql_jwt

from users.graphql.types import UserType

class ObtainJSONWebToken(graphql_jwt.ObtainJSONWebToken):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, _, info: graphene.ResolveInfo, **kwargs):
        return cls(user=info.context.user)

class AuthMutations(graphene.ObjectType):
    """
    Contains all authentication related mutations for a user.
    """
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
