# Insurance Policy Management System

## Overview

This project is an Insurance Policy Management System that manages policyholders, products, and payments. The system allows policy managers to perform various tasks, such as adding and suspending policyholders, registering new members, and managing policy products.

## Setup Instructions

1. **Clone the Repository**:
    ```
    git clone <repository-link>
    ```
2. **Navigate to the Project Directory**:
    ```
    cd policy-management-system
    ```
3. **Run the Demonstration Script**:
    ```
    python main.py
    ```

## Classes and Methods

### Policyholder
- **Attributes**:
    - `policyholder_id`
    - `name`
    - `active`
    - `products`
- **Methods**:
    - `register(product)`
    - `suspend()`
    - `reactivate()`
    - `display_details()`

### Product
- **Attributes**:
    - `product_id`
    - `name`
    - `price`
- **Methods**:
    - `update(name, price)`
    - `suspend()`

### Payment
- **Attributes**:
    - `policyholder`
    - `product`
    - `paid`
- **Methods**:
    - `process_payment()`
    - `send_reminder()`
    - `apply_penalty()`

## Demonstration

The `main.py` script demonstrates the functionality of the system by creating two policyholders, assigning them products, processing their payments, and displaying their account details.
