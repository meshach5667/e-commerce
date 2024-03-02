from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Optional

from schema.product import Product, ProductCreate

product_router = APIRouter()
products: Dict[int, Product] = {}

# create product
# list all products
# get product by id

def get_product(product_id: int) -> Optional[Product]:
    return products.get(product_id)

get_product_dependency = Depends(get_product)

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}

@product_router.get('/{product_id}', status_code=200, dependencies=[get_product_dependency])
def get_product_by_id(product: Product = Depends(get_product_dependency)):
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {'message': 'success', 'data': product}