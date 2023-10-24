from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float = 0.0

item1 = Item(name="Widget")
print(item1)  # Output: Item(name='Widget', price=0.0)

item2 = Item(name="Gadget", price=10.99)
print(item2)  # Output: Item(name='Gadget', price=10.99)

