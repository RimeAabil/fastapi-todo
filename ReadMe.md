# FastAPI Todo Application

This is a simple **Todo API** built with [FastAPI](https://fastapi.tiangolo.com/).
It demonstrates how to create, read, update, and delete tasks using a modern, high-performance Python web framework.

---

## What is FastAPI?

**FastAPI** is a modern web framework for building APIs with Python 3.6+ based on standard type hints.

Key features:

* **High performance** – built on top of *Starlette* (for the web layer) and *Pydantic* (for data validation).
* **Data validation** – automatic request validation and parsing thanks to Pydantic.
* **Interactive documentation** – generates API docs automatically with **Swagger UI** and **ReDoc**.
* **Asynchronous support** – designed to work seamlessly with `async/await`.
* **Standards-based** – follows OpenAPI and JSON Schema standards.

---

### Synchronous vs Asynchronous APIs

* **Synchronous API**: The client sends a request and waits for the server to respond before continuing.
  *Example: ordering a coffee and waiting at the counter until it’s ready.*

* **Asynchronous API**: The client sends a request but does not wait; it continues doing other work until notified that the response is ready.
  *Example: ordering a coffee, sitting down, and being notified when it’s ready.*

FastAPI supports both approaches, depending on your use case.

---

## Project Overview

This project is a **Todo Management API**. It supports:

* Getting all todos
* Getting a todo by ID
* Adding a new todo
* Updating an existing todo
* Deleting a todo

Each todo also has a **priority level**: Low, Medium, or High.

---

## Architecture Overview

Here’s a simplified view of how FastAPI handles requests:

```mermaid
flowchart TD
    A[Client (Browser / API Client)] --> B[FastAPI Application]
    B --> C[Request Validation<br/>(Pydantic)]
    B --> D[Routing (Endpoints)]
    B --> E[Business Logic<br/>(Python Code)]
    C --> F[Response (JSON)]
    D --> F
    E --> F


---

## Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-todo.git
   cd fastapi-todo
   ```

2. Install dependencies:

   ```bash
   pip install "fastapi[standard]" uvicorn
   ```

3. Run the FastAPI app:

   ```bash
   uvicorn main:api --reload
   ```

4. Open your browser at:

   * Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * ReDoc docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Recommendations for Running and Testing

* If you just want to **explore and test the API quickly**, you don’t need any external API testing tool.
  When the server is running locally, simply go to:

  ```
  http://127.0.0.1:8000/docs
  ```

  You’ll get an **interactive interface** (Swagger UI) to test all endpoints directly from your browser.

* Use `/redoc` for a clean, automatically generated API reference.

* For production deployments, running with **Uvicorn** or **Gunicorn** is recommended to ensure scalability and performance.

---

## Example Endpoints

### Get all todos

```http
GET /todos
```

### Get a todo by ID

```http
GET /todos/{todo_id}
```

### Create a todo

```http
POST /todos
Content-Type: application/json

{
  "todo_name": "Finish project",
  "todo_description": "Complete the FastAPI project for GitHub",
  "priority": 1
}
```

### Update a todo

```http
PUT /todos/{todo_id}
Content-Type: application/json

{
  "todo_description": "Updated description",
  "priority": 2
}
```

### Delete a todo

```http
DELETE /todos/{todo_id}
```

---

## References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://docs.pydantic.dev/)
* [Starlette Documentation](https://www.starlette.io/)

---

This serves as a practice project for learning FastAPI.

---
