-- Write your query below
SELECT employee_id,
CASE WHEN employee_id%2!=0 AND name NOT LIKE 'M%'
THEN salary
ELSE 0
END AS bonus
FROM employees
GROUP BY employee_id
ORDER BY employee_id
