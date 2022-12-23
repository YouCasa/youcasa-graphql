import graphene
from graphene_django import DjangoObjectType

from rental.models import LGA, Agent, Apartment, Country, Landlord, State, City


class CountryType(DjangoObjectType):
    """
    Country GraphQL object type.
    """
    country_id = graphene.ID()
    class Meta:
        model = Country
        field = ("name",)
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"]
        }
        interfaces = (graphene.relay.Node, )

    def resolve_country_id(self, _):
        if isinstance(self, Country):
            return getattr(self, "id")
        return None


class StateType(DjangoObjectType):
    """
    State GraphQL object type.
    """
    state_id = graphene.ID()
    class Meta:
        model = State
        field = ("name",)
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"]
        }
        interfaces = (graphene.relay.Node, )

    def resolve_state_id(self, _):
        if isinstance(self, State):
            return getattr(self, "id")
        return None


class LGAType(DjangoObjectType):
    """
    LGA GraphQL object type.
    """
    class Meta:
        model = LGA
        field = ("name",)
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"]
        }
        interfaces = (graphene.relay.Node, )

class CityType(DjangoObjectType):
    """
    City GraphQL object type.
    """
    class Meta:
        model = City
        field = ("name",)
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"]
        }
        interfaces = (graphene.relay.Node, )


class LandlordType(DjangoObjectType):
    """
    Landlord GraphQL object type.
    """
    class Meta:
        model = Landlord
        field = ("user", "can_change_price", "can_change_vacancy")

class AgentType(DjangoObjectType):
    """
    Agent GraphQL object type.
    """
    class Meta:
        model = Agent
        field = ("user", "can_change_price", "can_change_vacancy")

class ApartmentType(DjangoObjectType):
    """
    Apartment GraphQL object type.
    """
    class Meta:
        model = Apartment
        fields = (
            "country", "state",
            "lga", "city", "address",
            "description", "price", "landlord",
            "price_is_negotiable", "number_of_rooms",
            "is_vacant", "agent", "longitude", "lattitude"
        )
        filetr_fields = {
            "country__id": ["exact"],
            "is_vacant": ["exact"],
            "price_is_negotiable": ["exact"],
            "country__name": ["exact", "istartswith", "icontains"],
            "state__id": ["exact"],
            "state__name": ["exact", "istartswith", "icontains"],
            "lga__id": ["exact"],
            "lga__name": ["exact", "istartswith", "icontains"],
            "address": ["exact", "istartswith", "icontains"],
            "price": ["exact", "istartswith", "icontains"],
            "description": ["exact", "istartswith", "icontains"],
        }
        interfaces = (graphene.relay.Node, )
