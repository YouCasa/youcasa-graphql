from typing import Any, TypeVar
from django.contrib.auth import get_user_model
import graphene
from graphql import GraphQLError

from users.models import CustomUser

from rental.models import Country, Landlord, State

T = TypeVar("T")
def get_landlord(landlord_id:str | int) -> Landlord:
    """
    Returns a landlord object with the specified landlor `id`
    or raises an error.
    """
    try:
        return Landlord.objects.get(pk=landlord_id)
    except Landlord.DoesNotExist:
        raise GraphQLError("Landlord with the specified `id` was not found.")


def ensure_exists(var: T) ->T:
    """
    ensures a specified object exists and returns that object, but raises an error otherwise
    """
    var_name = f"{var=}".split("=")[0]
    if not var:
        raise GraphQLError(f"{var_name} is required")
    return var


def get_country(country_id: str | int) -> Country:
    """
    Returns a country object with specified country `id`
    or raises an error
    """
    try:
        return Country.objects.get(pk=country_id)
    except Country.DoesNotExist:
        raise GraphQLError("Country with the specified `id` was not found.")


def get_state(state_id: str | int) -> State:
    """
    Returns a state object with the specified state `id`
    or raises an error
    """
    try:
        return State.objects.get(pk=state_id)
    except State.DoesNotExist:
        raise GraphQLError("State with the specified `id` was not found.")


def perform_state_create(info: graphene.ResolveInfo, **kwargs) -> State:
    """
    Performs state creation given the required arguments are passed
    """
    name = ensure_exists(kwargs.get("name", None))
    country_id = ensure_exists(kwargs.get("country_id", None))
    country = get_country(str(country_id))
    state = State.objects.create(name=name, country=country)
    return state


def perform_state_update(info: graphene.ResolveInfo, **kwargs) -> State:
    """
    Performs update on a state with the specified state_id
    """
    state_id = ensure_exists(kwargs.get("state_id", None))
    country_id = kwargs.get("country_id", None)
    state = get_state(str(state_id))
    state.name = kwargs.get("name", state.name)
    if country_id:
        state.country = get_country(str(country_id))
    state.save()
    return state


def perform_landlord_update(info: graphene.ResolveInfo, **kwargs) -> Landlord:
    """
    Performs landlord update activity on landlord object
    :param graphene.ResolveInfo: the graphql request info
    """
    landlord_id = kwargs.get("landlord_id", None)
    if not landlord_id:
        raise GraphQLError("landlord_id is reqiured")
    landlord = get_landlord(landlord_id)
    if not info.context.user != landlord.user:
        raise GraphQLError("You are not authorised to alter this landlord")
    email:str = kwargs.get("email", None)
    password: str = kwargs.get("password", None)
    if email:
        landlord.user.email = email
    if password:
        landlord.user.set_password(password)
    landlord.user.save()
    landlord.save()
    return landlord

def perform_landlord_create(info: graphene.ResolveInfo, **kwargs) -> Landlord:
    """
    Performs landlord update activity on landlord object
    :param graphene.ResolveInfo: the graphql request info
    """
    email: str = kwargs.get("email", None)
    password: str = kwargs.get("email", None)
    if not email:
        raise GraphQLError("email address is required")
    if not password:
        raise GraphQLError("password is required")
    user = CustomUser.objects.create_user(email=email, password=password)
    landlord = Landlord.objects.create(user=user)
