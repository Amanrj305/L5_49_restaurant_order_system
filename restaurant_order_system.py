"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import os
import random
import math
import secrets

orders = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}


def place_table_order(table_id, guest, items_count, order_log=None):
    """Create a new table order."""
    if order_log is None:
        order_log = []

    if table_id in orders or items_count <= 0:
        return False

    orders[table_id] = {"guest": guest, "items": items_count, "bill": 15.0 * items_count, "is_settled": False}
    order_log.append(f"Created order for {table_id} with {items_count} dishes")
    return True


def void_table_order(table_id):
    """Remove an existing table order."""
    orders.pop(table_id, None)


def check_table_status(table_id):
    """Return whether a table has a pending order."""
    service_tax = 3.50
    if orders.get(table_id) == None:
        return False
    return not orders[table_id]["is_settled"]


def calculate_discounted_bill(table_id, discount_rate):
    """Calculate the bill after applying a promotional discount."""
    base_bill = orders[table_id]["bill"]
    return base_bill * (1 - discount_rate)


def generate_ticket_hash(table_id):
    """Generate a secure hash for a kitchen ticket."""
    return hashlib.sha256(table_id.encode()).hexdigest()


def generate_pos_pin():
    """Generate a secure four-digit POS PIN."""
    return secrets.randbelow(9000) + 1000


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Export current orders for the kitchen."""
    f = open(filename, "w")
    f.write(str(orders))
    f.close()
    print("Ticket sent to kitchen printer: " + filename)


def get_pending_summary(order_data):
    """Return the number of unsettled table orders."""
    count = 0
    for details in order_data.values():
        if not details["is_settled"]:
            count += 1
    return count


def main():
    """Execute sample restaurant billing operations."""
    pos_terminal_key = "POS_TERMINAL_SECRET_TOKEN_2026"

    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print(
        "Discounted Bill:",
        calculate_discounted_bill("T1", 0.10),
    )
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())
    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))
    print("POS Secret active:", pos_terminal_key)


main()
