from pydantic import BaseModel

from schema.product import Product

class Order(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    status: str = "pending"


class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]

orders = order = Order(id=1, customer_id=1, items=[1, 2], product_id=123, quantity=2)
