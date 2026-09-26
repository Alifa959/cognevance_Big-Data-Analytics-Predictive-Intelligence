USE ecommerce_analytics;

-- 1. Revenue by category
SELECT category, SUM(revenue) AS total_revenue
FROM orders
GROUP BY category
ORDER BY total_revenue DESC;

-- 2. Monthly revenue
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(revenue) AS revenue
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- 3. Top customers
SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(revenue) AS total_spending
FROM orders
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 20;

-- 4. Average order value
SELECT SUM(revenue) / COUNT(DISTINCT order_id) AS average_order_value
FROM orders;

-- 5. Revenue by location
SELECT customer_location, SUM(revenue) AS revenue
FROM orders
GROUP BY customer_location
ORDER BY revenue DESC;

-- 6. Repeat customers
SELECT customer_id, COUNT(DISTINCT order_id) AS orders_count
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT order_id) > 1
ORDER BY orders_count DESC;
