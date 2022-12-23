import graphene
from users.graphql.mutations import AuthMutations
from users.graphql.queries import UserQueries
from rental.graphql.mutations import RentalMutations

class Query(UserQueries, graphene.ObjectType):
    pass

class Mutation(
    AuthMutations,
    RentalMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
