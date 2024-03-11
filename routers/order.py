from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Optional
from schema.order import Order
from schema.order import OrderPayload 


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

@order_router.post('/', status_code=201)
def create_order(payload: OrderPayload):
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=payload.customer_id,
        product_id=payload.product_id,
        quantity=payload.quantity,
        status="pending"
    )
    orders[order_id] = new_order
    return {'message': 'Order created successfully', 'data': new_order}

@order_router.get('/', status_code=200)
def list_orders():
    return {'message': 'success', 'data': orders}

@order_router.get('/{order_id}', status_code=200, dependencies=[get_order_dependency])
def get_order_by_id(order_id: int):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {'message': 'success', 'data': order}

@order_router.put('/{order_id}/checkout', status_code=200)
def checkout_order_by_id(order_id: int):
    order = checkout_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {'message': 'Order checked out successfully', 'data': order}
