from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from typing import Annotated


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'        # não aceita campos extras
        from_attributes = True  # conversoes de models para schemas e de schemas p/ models
        
        
class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]