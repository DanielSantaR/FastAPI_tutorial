from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_name: str = None
    user_surname: str = None
    user_nationality: str = 'colombian'
    user_age: Optional[int]


class UserIn(User):
    user_password: str = None


class UserOut(User):
    pass


class Item(BaseModel):
    item_name: str = None
    item_description: Optional[str]
    item_price: float = None
    item_tax: Optional[float]

# TODO: 
# muy buen uso de los modelos pydantic y de la herencia
# tambien debes tener en cuenta que no siempre es necesario
# darle un valor por defecto a los atributos

# por ejemplo en Item el atributo item_price podria ser
# un valor obligatorio y quedaria item_price: float
# y de esta forma ese atributo va a ser obligatorio

# tambien puedes evitar usar nombre redundantes como
# user_username quedaria mejor solo username

# este seria una forma en la que se podria reescribir,
# aun se entiende pero tiene una escritura mas ligera
# y de esta forma al usar los atributos en otra parte
# del codigo uno se evita el poner nombres tan largos

# class Item(BaseModel):
#     name: str
#     description: Optional[str]
#     price: float
#     tax: Optional[float]

# TODO