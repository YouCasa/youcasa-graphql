import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Country(models.Model):
    """
    Refers to the country where an apartment is found.
    """
    name = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=3, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name


class State(models.Model):
    """
    Refers to the state where an apartment is found.
    """
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class LGA(models.Model):
    """
    Refers to the local government area where an apartment is found.
    """
    name = models.CharField(max_length=255, unique=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    """
    Refers to the city where an apartment is found.
    """
    name = models.CharField(max_length=255, unique=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Landlord(models.Model):
    """
    Refers to the owner of an apartment.
    """
    # Has fields that determine whether the landlord can_change_price or can_change_vacancy of an apartment
    # this is intended to be used as services that can be taken away if the landlord owes us money.
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    can_change_price = models.BooleanField(default=True)
    can_change_vacancy = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    """
    Refers to an agent that a landlord can assign to take care of an apartment.
    They should have the necessary permisions that can also be revoked if needed
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    can_change_price = models.BooleanField(default=False)
    can_change_vacancy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Apartment(models.Model):
    """
    Represents an an apartment. Currently of all kinds.
    """
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    lga = models.ForeignKey(LGA, on_delete=models.PROTECT, help_text="local government area")
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.TextField(max_length=500)
    description = models.TextField(max_length=700, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    landlord = models.ForeignKey(Landlord, on_delete=models.PROTECT, null=True, blank=True)
    price_is_negotiable = models.BooleanField(default=True, help_text="can this price be negotiated")
    number_of_rooms = models.PositiveIntegerField()
    is_vacant = models.BooleanField(default=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    lattitude = models.CharField(max_length=255, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        address = str(self.address)[:15]
        return f"{self.city} {address}"
