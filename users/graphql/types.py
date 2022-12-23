from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
# import graphene

User = get_user_model()

class UserType(DjangoObjectType):
    """
    CustomUser GraphQL object type.
    """
    class Meta:
        model = User
        exclude = ("password", "last_login", "is_superuser", "is_staff", "is_active")
