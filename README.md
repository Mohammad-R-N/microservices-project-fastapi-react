# 🧩 FastAPI Event-Driven Microservices

A learning-focused backend project built with **FastAPI**, demonstrating a **two-microservice architecture** using **event-driven communication** via **Redis Streams**.

This project simulates a simple store and warehouse system where services communicate asynchronously to handle orders, inventory, and refunds.

---

## 🚀 Key Concepts Covered

- Microservices architecture
- Event-driven communication
- Redis Streams & Consumer Groups
- Background workers (consumers)
- Service-to-service decoupling
- FastAPI for API services

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Redis (Streams)**
- **Uvicorn**
- **Async workers / consumers**

---

## 🧱 Architecture Overview

The system consists of **two independent microservices**:

### 1️⃣ Store Service
Responsible for:
- Receiving refund events
- Updating order status after payment issues

### 2️⃣ Warehouse Service
Responsible for:
- Handling completed orders
- Managing product inventory
- Triggering refunds when stock is insufficient

### 🔁 Communication Pattern

Services do **not** call each other directly.  
Instead, they communicate via **Redis Streams** using events.
```bash
Order Completed
|
v
Warehouse Service
|
| (if inventory insufficient)
v
Refund Event
|
v
Store Service
```
---
## 📁 Project Structure

```text
back-end/
├── store/
│   ├── main.py
│   └── refund_consumer.py
│
├── warehouse/
│   ├── main.py
│   └── inventory_consumer.py
│
└── README.md
```

---
## 📦 Services Explained

## 🟢 Store Service

**Purpose**
Handles refund-related events and updates order status accordingly.

Key File
```text
store/refund_consumer.py
```

**Responsibilities**

- Listens to `refund-order` Redis stream

- Part of `payment-group` consumer group

- Marks orders as `refunded`

## 🟢 Warehouse Service

**Purpose**
Handles order fulfillment and inventory logic.

Key File
```text
warehouse/inventory_consumer.py
```

**Responsibilities**

- Listens to `order-completed` Redis stream

- Part of `warehouse-group` consumer group

- Decreases product stock

- Emits `refund-order` event if inventory is insufficient

---
🔄 Event Definitions

`order-completed`

Triggered when an order is successfully placed and paid.

**Consumed by**

- Warehouse Service
---
`refund-order`

Triggered when an order cannot be fulfilled due to inventory issues.

**Consumed by**

- Store Service

---
## 🧪 Running the Project

**1️⃣ Requirements**

- Python 3.10+

- Redis (local or Docker)

---
**2️⃣ Start Redis (Docker)**
```bash
docker run -p 6379:6379 redis
```

---
**3️⃣ Run Services**
Store Service
```bash
cd store
uvicorn main:app --reload
```

Warehouse Service
```bash
cd warehouse
uvicorn main:app --reload
```
Each service runs independently.

---
## 🧠 Why Event-Driven?

**This architecture helps you learn:**

- Loose coupling between services

- Scalability without direct dependencies

- Real-world microservice patterns

- Async processing and eventual consistency

**This pattern is widely used in:**

- E-commerce platforms

- Payment systems

- Order processing pipelines

---
## 🎯 Learning Goals

This project is ideal for learning:

- How microservices communicate

- How background consumers work

- How to model real-world workflows

- How to structure FastAPI beyond CRUD

---
## 🚧 Possible Improvements

- Add database persistence

- Add retry & dead-letter queues

- Add logging & monitoring

- Add Dockerfiles per service

- Add API Gateway

- Add tests

---
## 🤝 Contributing

This is a learning project.
Feel free to fork, experiment, and improve.

---
## 📄 License

**MIT** License
