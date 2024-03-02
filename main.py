from fastapi import FastAPI

from routers.customer import customer_router
from routers.product import product_router
from routers.order import order_router

app = FastAPI()

app.include_router(customer_router, prefix='/customers', tags=['Customer'])
app.include_router(product_router, prefix='/products', tags=['Product'])
app.include_router(order_router, prefix='/orders', tags=['Order'])

@app.get('/')
def index():
    return {'message': 'Welcome to our store'}