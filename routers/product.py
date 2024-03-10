from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Optional

from schema.product import Product, ProductCreate

product_router = APIRouter()
products: Dict[int, Product] = {}


@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
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
    return {'message': 'Success', 'data': list(products.values())}


@product_router.put("/update-product-info/{product_id}")
def edit_product_info(product_id: int, payload: Product):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product does not exist")
    else:
        products[product_id].set_fields(**payload.dict())
        return {"message": "The information of  the product was updated", "data": products[product_id]}
    
        

# @product_router.get('/{product_id}', status_code=200)
# def get_product_by_id(product_id: int, product: Product = Depends(get_product_dependency)):
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return {'message': 'Success', 'data': product}
