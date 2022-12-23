from typing import Callable, TypeVar, TypedDict
from functools import wraps
from graphql_auth.decorators import login_required

import graphene
from graphql import GraphQLError

T = TypeVar("T")

class ErrorType(TypedDict):
    field: str
    message: str

class GQLErrors:
    """
    Defines a list of error messages for various graphql violations
    """
    unauthorized_entry: str = "You are not authorised to perform this action"

def custom_login_required(func: Callable[..., T]) -> Callable[..., T]:
    """
    Ensures user is loged in for serializer mutations
    """
    @wraps(func)
    def wrapper(cls, root, info: graphene.ResolveInfo, **kwargs):
        if not info.context.user.is_authenticated:
            raise GraphQLError(GQLErrors.unauthorized_entry)
        return func(cls, root, info, **kwargs)
    return wrapper


def validate_staff(func: Callable[..., T]) -> Callable[..., T]:
    """
    Ensures that request user is a staff
    """
    @wraps(func)
    def wrapper(cls, root, info:graphene.ResolveInfo, **kwargs):
        if not info.context.user.is_staff:
            raise GraphQLError(GQLErrors.unauthorized_entry)
        return func(cls, root, info, **kwargs)
    return wrapper
