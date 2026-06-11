"""Order workflow helpers for the café service layer."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from services.order import Order, OrderItem


DEFAULT_PRODUCTS_PATH = Path(__file__).resolve().parent.parent / "data" / "products.json"


class OrderServiceError(Exception):
	"""Base error for order service failures."""


class ProductNotFoundError(OrderServiceError):
	"""Raised when a product cannot be located in the catalog."""


class InvalidQuantityError(OrderServiceError):
	"""Raised when the requested quantity is not valid."""


class OrderService:
	def __init__(self, products: Iterable[dict[str, Any]] | None = None, products_path: str | Path | None = None):
		self.products_path = Path(products_path) if products_path is not None else DEFAULT_PRODUCTS_PATH
		self._products = list(products) if products is not None else self._load_products()

	def _load_products(self) -> list[dict[str, Any]]:
		import json

		with self.products_path.open("r", encoding="utf-8") as file:
			data = json.load(file)

		if not isinstance(data, list):
			raise OrderServiceError("Product catalog must be a list of product records.")

		return [self._normalize_product(product) for product in data]

	def _normalize_product(self, product: Any) -> dict[str, Any]:
		if isinstance(product, dict):
			return {
				"productId": int(product["productId"]),
				"name": str(product["name"]),
				"price": float(product["price"]),
				"stock": int(product["stock"]),
				"category": str(product.get("category", "")),
			}

		return {
			"productId": int(getattr(product, "productId", getattr(product, "id"))),
			"name": str(getattr(product, "name")),
			"price": float(getattr(product, "price")),
			"stock": int(getattr(product, "stock")),
			"category": str(getattr(product, "category", "")),
		}

	@property
	def products(self) -> list[dict[str, Any]]:
		return [dict(product) for product in self._products]

	def list_products(self, category: str | None = None) -> list[dict[str, Any]]:
		if category is None:
			return self.products

		normalized_category = category.strip().lower()
		return [product for product in self.products if product["category"].strip().lower() == normalized_category]

	def find_product(self, identifier: int | str) -> dict[str, Any]:
		for product in self._products:
			if self._matches_identifier(product, identifier):
				return dict(product)

		raise ProductNotFoundError(f"Product '{identifier}' was not found.")

	def _matches_identifier(self, product: dict[str, Any], identifier: int | str) -> bool:
		if isinstance(identifier, int):
			return product["productId"] == identifier

		candidate = str(identifier).strip().lower()
		return candidate in {
			str(product["productId"]).lower(),
			product["name"].strip().lower(),
		}

	def create_order(self, customer_name: str, product_identifier: int | str, quantity: int) -> Order:
		quantity = self._validate_quantity(quantity)
		product = self.find_product(product_identifier)

		if quantity > product["stock"]:
			raise InvalidQuantityError(
				f"Requested quantity {quantity} exceeds available stock of {product['stock']} for {product['name']}."
			)

		order = Order(customer_name=customer_name.strip())
		order.add_item(
			OrderItem(
				product_id=product["productId"],
				name=product["name"],
				unit_price=product["price"],
				quantity=quantity,
			)
		)
		return order

	def create_order_from_items(self, customer_name: str, items: Iterable[dict[str, Any]]) -> Order:
		order = Order(customer_name=customer_name.strip())

		for item in items:
			product = self.find_product(item["product_id"])
			quantity = self._validate_quantity(item["quantity"])

			if quantity > product["stock"]:
				raise InvalidQuantityError(
					f"Requested quantity {quantity} exceeds available stock of {product['stock']} for {product['name']}."
				)

			order.add_item(
				OrderItem(
					product_id=product["productId"],
					name=product["name"],
					unit_price=product["price"],
					quantity=quantity,
				)
			)

		return order

	def build_receipt_lines(self, order: Order) -> list[str]:
		lines = [
			"===== PYTHON CAFÉ RECEIPT =====",
			f"Order ID: {order.order_id}",
			f"Customer: {order.customer_name}",
			f"Created: {order.created_at.isoformat()}",
			"",
		]

		for item in order.items:
			lines.append(
				f"{item.name} x{item.quantity} @ KES {item.unit_price:.2f} = KES {item.line_total:.2f}"
			)

		lines.extend([
			"",
			f"Subtotal: KES {order.subtotal:.2f}",
			f"Total: KES {order.total:.2f}",
		])

		if order.payment_status == "paid":
			lines.extend([
				f"Payment Method: {order.payment_method}",
				f"Amount Paid: KES {order.amount_paid:.2f}",
				f"Change: KES {order.change_due:.2f}",
			])

		return lines

	def render_receipt(self, order: Order) -> str:
		return "\n".join(self.build_receipt_lines(order))

	def _validate_quantity(self, quantity: int) -> int:
		try:
			numeric_quantity = int(quantity)
		except (TypeError, ValueError) as error:
			raise InvalidQuantityError("Quantity must be a whole number.") from error

		if numeric_quantity <= 0:
			raise InvalidQuantityError("Quantity must be greater than zero.")

		return numeric_quantity

