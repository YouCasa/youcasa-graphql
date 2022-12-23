from typing import Callable, NamedTuple
import graphene
from graphene_django.types import ErrorType

from rental.decorators import validate_staff, custom_login_required

class SerializerMutationType(NamedTuple):
    get_serializer_kwargs: Callable

class StaffRequiredMixin(SerializerMutationType):
    @classmethod
    @custom_login_required
    @validate_staff
    def get_serializer_kwargs(cls, root, info: graphene.ResolveInfo, **input):
        return super().get_serializer_kwargs(root, info, **input)

class GenericMutationMixin():
    success = graphene.Boolean()
    errors = graphene.List(ErrorType)
