from models.orders import Order


def order_format(pk: str):
    order = Order.get(pk)
    return {
        "id": order.pk,
        "product_id": order.product_id,
        "price": order.price,
        "fee": order.fee,
        "total": order.total,
        "quantity": order.quantity,
        "status": order.status,
    }
