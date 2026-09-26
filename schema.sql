CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(100),
    customer_id VARCHAR(100),
    order_date DATE,
    product_id VARCHAR(100),
    category VARCHAR(150),
    quantity INT,
    unit_price DECIMAL(12,2),
    discount DECIMAL(6,2),
    payment_type VARCHAR(50),
    customer_location VARCHAR(150),
    rating DECIMAL(3,2),
    delivery_days INT,
    revenue DECIMAL(14,2)
);
