from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Customers(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]


class OrderStatusEnum(str, Enum):
    placed = "placed"
    shipped = "shipped"
    completed = "completed"
    return_pending = "return_pending"
    returned = "returned"


class Orders(BaseModel):
    id: int
    user_id: int
    order_date: date
    status: OrderStatusEnum


class PaymentMethodEnum(str, Enum):
    coupon = "coupon"
    gift_card = "gift_card"
    credit_card = "credit_card"
    bank_transfer = "bank_transfer"


class Payments(BaseModel):
    id: int
    order_id: int
    payment_method: PaymentMethodEnum
    amount: int
