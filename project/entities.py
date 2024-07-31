from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.alias_generators import to_camel
from typing import Annotated
from typing import Generic
from typing import TypeVar


class Entity(BaseModel):
    """
    Base class for any entity.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        allow_inf_nan=False,
        arbitrary_types_allowed=True,
        extra="forbid",
        from_attributes=True,
        populate_by_name=True,
        revalidate_instances="always",
        ser_json_timedelta="float",
        strict=True,
        validate_assignment=True,
        validate_default=True,
        validate_return=True,
    )


T = TypeVar("T")


class DataEntity(Entity, Generic[T]):
    data: T


class ErrorEntity(Entity):
    errors: Annotated[list[str], Field(default_factory=list)]
