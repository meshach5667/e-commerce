from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Optional

from pydantic import BaseModel

class Order(BaseModel):
    id: int
    customer_id: int
    product_id: int
    quantity: int
    status: str = "pending"

order_router = APIRouter()
orders: Dict[int, Order] = {}

def get_order(order_id: int) -> Optional[Order]:
    return orders.get(order_id)

def checkout_order(order_id: int) -> Optional[Order]:
    order = get_order(order_id)
    if not order or order.status != "pending":
        raise HTTPException(status_code=404, detail="Order not found or not in pending status")
    order.status = "completed"
    return order

get_order_dependency = Depends(get_order)
checkout_order_dependency = Depends(checkout_order)

@order_router.post('/', status_code=201)
def create_order(payload: dict):
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        **payload,
        status="pending"
    )
    orders[order_id] = new_order
    return {'message': 'Order created successfully', 'data': new_order}

@order_router.get('/', status_code=200)
def list_orders():
    return {'message': 'success', 'data': orders}

@order_router.get('/{order_id}', status_code=200, dependencies=[get_order_dependency])
def get_order_by_id(order: Order = Depends(get_order_dependency)):
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {'message': 'success', 'data': order}

@order_router.put('/{order_id}/checkout', status_code=200, dependencies=[checkout_order_dependency])
def checkout_order_by_id(order: Order = Depends(checkout_order_dependency)):
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {'message': 'Order checked out successfully', 'data': order}