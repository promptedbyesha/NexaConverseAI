import requests

def get_order_status(order_id: str) -> str:
    try:
        response = requests.get(f"http://localhost:8001/orders/{order_id}")
        response.raise_for_status()
        data = response.json()
        return data.get("status", "Status unknown")
    except requests.RequestException:
        return "Could not retrieve order status at the moment."
