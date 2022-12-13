import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Country(models.Model):
    """
    Refers to the country where an apartment is found.
    """
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class State(models.Model):
    """
    Refers to the state where an apartment is found.
    """
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class LGA(models.Model):
    """
    Refers to the local government area where an apartment is found.
    """
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class City(models.Model):
    """
    Refers to the city where an apartment is found.
    """
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Landlord(models.Model):
    """
    Refers to the owner of an apartment.
    """
    # Has fields that determine whether the landlord can_change_price or can_change_vacancy of an apartment
    # this is intended to be used as services that can be taken away if the landlord owes us money.
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    can_change_price = models.BooleanField(default=True)
    can_change_vacancy = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.email


class Agent(models.Model):
    """
    Refers to an agent that a landlord can assign to take care of an apartment.
    They should have the necessary permisions that can also be revoked if needed
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    can_change_price = models.BooleanField(default=False)
    can_change_vacancy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email
