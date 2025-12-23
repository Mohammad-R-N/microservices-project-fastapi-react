from fastapi import APIRouter
from models.products import Product
from db.services import product_services

router = APIRouter(prefix="/product", tags=["products"])


@router.post("/")
def create_product(product: Product):
    return product.save()


@router.get("/{pk}")
def get_product(pk: str):
    return Product.get(pk)


@router.get("/all")
def get_all_products():
    return [product_services.product_format(pk) for pk in Product.all_pks()]


@router.delete("/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)
