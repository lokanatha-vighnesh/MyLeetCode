# Write your MySQL query statement below
SELECT name,bonus 
FROM Employee AS a
LEFT JOIN Bonus AS b ON a.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000 

