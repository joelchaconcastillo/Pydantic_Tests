from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

# Serialize to JSON
item = Item(name="Widget", price=9.99)
item_json = item.model_dump_json()
#item_json = item.model_dump(mode='json')
print(item_json)

# Deserialize from JSON
#item_from_json = Item.model_dump('{"name": "Gadget", "price": 19.99}')
item_from_json = Item.model_validate_json(item_json)
#item_from_json = Item.model_dump_json(item_json)
#print(item_from_json)

