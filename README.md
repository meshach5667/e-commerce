# FastAPI E-Commerce API

This project is a simple e-commerce API built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.

## Overview

This API provides basic functionalities for managing orders in an e-commerce system. It allows users to:

- Create new orders
- List existing orders
- Retrieve specific orders by ID
- Checkout orders

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic (for data validation)
- HTTPx (for HTTP client)
- Docker (optional, for containerization)

## Installation

1. Clone this repository:

    ```bash
    git clone [https://github.com/your_username/fastapi-ecommerce-api.git](https://github.com/meshach5667/e-commerce)
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-ecommerce-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## API Endpoints

- **POST /orders/**: Create a new order.
- **GET /orders/**: List all existing orders.
- **GET /orders/{order_id}**: Retrieve a specific order by ID.
- **PUT /orders/{order_id}/checkout**: Checkout an order.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.


