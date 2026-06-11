"""Payment helpers for the café service layer."""

from __future__ import annotations

from dataclasses import dataclass

from services.order import Order


class PaymentError(Exception):
	"""Base error for payment failures."""


class InsufficientPaymentError(PaymentError):
	"""Raised when the amount paid does not cover the order total."""


@dataclass(slots=True)
class PaymentResult:
	success: bool
	amount_due: float
	amount_paid: float
	change_due: float
	payment_method: str
	message: str


class PaymentService:
	def process_payment(self, order: Order, amount_paid: float, payment_method: str = "cash") -> PaymentResult:
		amount_paid = float(amount_paid)
		amount_due = round(order.total, 2)

		if amount_paid < amount_due:
			raise InsufficientPaymentError(
				f"Payment of KES {amount_paid:.2f} is not enough for KES {amount_due:.2f}."
			)

		order.mark_paid(payment_method=payment_method, amount_paid=amount_paid)
		change_due = round(amount_paid - amount_due, 2)

		return PaymentResult(
			success=True,
			amount_due=amount_due,
			amount_paid=amount_paid,
			change_due=change_due,
			payment_method=payment_method,
			message="Payment accepted.",
		)

	def format_payment_summary(self, order: Order, result: PaymentResult) -> str:
		lines = [
			"===== PAYMENT SUMMARY =====",
			f"Order ID: {order.order_id}",
			f"Customer: {order.customer_name}",
			f"Amount Due: KES {result.amount_due:.2f}",
			f"Amount Paid: KES {result.amount_paid:.2f}",
			f"Change Due: KES {result.change_due:.2f}",
			f"Method: {result.payment_method}",
			result.message,
		]
		return "\n".join(lines)

