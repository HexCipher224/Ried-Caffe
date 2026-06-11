"""Order domain objects for the café service layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class OrderItem:
	product_id: int
	name: str
	unit_price: float
	quantity: int

	@property
	def line_total(self) -> float:
		return float(self.unit_price) * int(self.quantity)

	def to_dict(self) -> dict[str, Any]:
		return {
			"product_id": self.product_id,
			"name": self.name,
			"unit_price": float(self.unit_price),
			"quantity": int(self.quantity),
			"line_total": self.line_total,
		}


@dataclass(slots=True)
class Order:
	customer_name: str
	items: list[OrderItem] = field(default_factory=list)
	order_id: str = field(default_factory=lambda: uuid4().hex[:10])
	created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
	status: str = "pending"
	payment_status: str = "unpaid"
	payment_method: str | None = None
	amount_paid: float = 0.0
	change_due: float = 0.0

	def add_item(self, item: OrderItem) -> None:
		self.items.append(item)

	@property
	def subtotal(self) -> float:
		return sum(item.line_total for item in self.items)

	@property
	def total(self) -> float:
		return self.subtotal

	def mark_paid(self, payment_method: str, amount_paid: float) -> None:
		self.payment_method = payment_method
		self.amount_paid = float(amount_paid)
		self.change_due = round(self.amount_paid - self.total, 2)
		self.payment_status = "paid"
		self.status = "completed"

	def to_dict(self) -> dict[str, Any]:
		return {
			"order_id": self.order_id,
			"customer_name": self.customer_name,
			"created_at": self.created_at.isoformat(),
			"status": self.status,
			"payment_status": self.payment_status,
			"payment_method": self.payment_method,
			"amount_paid": self.amount_paid,
			"change_due": self.change_due,
			"subtotal": self.subtotal,
			"total": self.total,
			"items": [item.to_dict() for item in self.items],
		}

	def summary(self) -> str:
		lines = [
			f"Order {self.order_id}",
			f"Customer: {self.customer_name}",
			f"Status: {self.status} / {self.payment_status}",
		]

		for item in self.items:
			lines.append(
				f"- {item.name} x{item.quantity} @ KES {item.unit_price:.2f} = KES {item.line_total:.2f}"
			)

		lines.append(f"Total: KES {self.total:.2f}")
		return "\n".join(lines)

