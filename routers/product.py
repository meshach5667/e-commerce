from fastapi import APIRouter, HTTPException, Depends,status
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
@product_router.get("/products/")
async def read_products():
    return {"products": list(products.values())}


@product_router.get("/{product_id}", response_model=Product)
def get_single_product(product_id: int,  
                       qty: Optional[int]=None,  
                       available: bool=True):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        product = products[product_id]
        
        # Checking if the fields are optional or not
        if qty is None and available is False:
            return {"id": product.id, "name": product.name, "price": product}["id"]+ \
                f"- {f'Quantity: {qty}' if qty is not None else ''}"\
                f"+ Available: {('Yes' if available else 'No')}"
        elif qty is not None:
            product.quantity_available -= qty
            return product
        else:
            return product

@product_router.put("/update-product-info/{product_id}")
def edit_product_info(product_id: int, payload: Product):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product does not exist")
    else:
        products[product_id].set_fields(**payload.dict())
        return {"message": "The information of  the product was updated", "data": products[product_id]}
    
        
@product_router.delete("/delete-product/{product_id}")
def delete(id:int):
    if id  not in products:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"There is no product with the id {id}")
    del  products[id]
    return{"message":"The product has been deleted successfully"}

   

