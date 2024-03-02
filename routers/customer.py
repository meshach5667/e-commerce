from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional

from schema.customer import Customer, CustomerCreate

customer_router = APIRouter()
customers: List[Customer] = []

# Create customer 
# List customer
# edit customer

# create customer
@customer_router.post('/', status_code=201)
def create_customer(payload: CustomerCreate):
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id, 
        username=payload.username, 
        address=payload.address
    )
    customers.append(new_customer)
    return {'message': 'customer created successfully', 'data': new_customer}

@customer_router.get('/', status_code=200)
def list_customers():
    return {'message': 'success', 'data': customers}

@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    curr_customer = None
    # get the customer
    for customer in customers:
        if customer.id == customer_id:
            curr_customer = customer
            break
    if not curr_customer:
        raise HTTPException(status_code=404, detail="customer not found")
    curr_customer.username = payload.username
    curr_customer.address = payload.address
    return {'message': 'customer edited successfully', 'data': curr_customer}
def check_username_exists(username: str) -> Optional[Customer]:
    return next((customer for customer in customers if customer.username == username), None)

check_username_dependency = Depends(check_username_exists)


# edit customer
@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    curr_customer = None
    # get the customer
    for customer in customers:
        if customer.id == customer_id:
            curr_customer = customer
            break
    if not curr_customer:
        raise HTTPException(status_code=404, detail="customer not found")
    curr_customer.username = payload.username
    curr_customer.address = payload.address
    return {'message': 'customer edited successfully', 'data': curr_customer}