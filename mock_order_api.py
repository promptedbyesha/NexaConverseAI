from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample in-memory fake database of orders and their status
fake_db = {
    "123": "shipped",
    "456": "processing",
    "789": "delivered"
}

@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    status = fake_db.get(order_id)
    if not status:
        raise HTTPException(status_code=404, detail="Order not found")
    return JSONResponse(content={"order_id": order_id, "status": status})
