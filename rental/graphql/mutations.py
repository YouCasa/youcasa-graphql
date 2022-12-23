import graphene
from graphene_django.types import ErrorType
from graphene_django.rest_framework.mutation import SerializerMutation
from rental.decorators import custom_login_required, validate_staff
from rental.graphql.types import StateType

from rental.graphql.utils.mutations import perform_landlord_update, perform_state_create, perform_state_update
from rental.mixins import GenericMutationMixin, StaffRequiredMixin
from rental.serializers import CitySerializer, CountrySerializer, LGASerializer, StateSerializer

class CountryCreateUpdateMutation(StaffRequiredMixin, SerializerMutation):
    """
    Performs create and update mutation on a country.
    To perform an update, all you need to do is pass the country `id`.
    """
    class Meta:
        serializer_class = CountrySerializer
        model_operation = ["create", "update"]
        lookup_field = "id"


class StateCreateMutation(GenericMutationMixin, graphene.Mutation):
    """
    Performs create mutation on a state.
    """
    state = graphene.Field(StateType)
        
    class Arguments:
        name = graphene.String(required=True)
        country_id = graphene.ID(required=True)

    @classmethod
    @custom_login_required
    @validate_staff
    def mutate(cls, root, info: graphene.ResolveInfo, **kwargs):
        state = perform_state_create(info, **kwargs)
        return StateCreateMutation(success=True, state=state)


class StateUpdateMutation(GenericMutationMixin, graphene.Mutation):
    """
    Perform update mutation on a state.
    """
    state = graphene.Field(StateType)
    class Arguments:
        name = graphene.String()
        country_id = graphene.ID()
        state_id = graphene.ID(required=True)

    @classmethod
    @custom_login_required
    @validate_staff
    def mutate(cls, root, info: graphene.ResolveInfo, **kwargs):
        state = perform_state_update(info, **kwargs)
        return StateUpdateMutation(success=True, state=state)


class RentalMutations(graphene.ObjectType):
    country_create_and_update = CountryCreateUpdateMutation.Field()
    create_state = StateCreateMutation.Field()
    update_state = StateUpdateMutation.Field()
    # lga_create_and_update = LGACreateUpdateMutation.Field()
    # city_create_and_update = CityCreateUpdateMutation.Field()
