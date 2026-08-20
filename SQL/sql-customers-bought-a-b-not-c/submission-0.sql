WITH cte AS (
    SELECT
        c.customer_id,
        c.customer_name,
        COUNT(DISTINCT CASE 
            WHEN o.product_name IN ('A', 'B') 
            THEN o.product_name 
        END) AS ab_count,
        COUNT(CASE 
            WHEN o.product_name = 'C' 
            THEN 1 
        END) AS c_count
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT customer_id, customer_name
FROM cte
WHERE ab_count = 2
  AND c_count = 0
ORDER BY customer_name;