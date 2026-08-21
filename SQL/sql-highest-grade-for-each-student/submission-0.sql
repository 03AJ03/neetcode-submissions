-- Write your query below
WITH cte AS
(SELECT student_id,exam_id,score,
DENSE_RANK() OVER (PARTITION BY student_id ORDER BY score desc,exam_id asc) AS rnk 
FROM exam_results)
SELECT student_id,exam_id,score
FROM cte 
WHERE rnk=1
ORDER BY student_id