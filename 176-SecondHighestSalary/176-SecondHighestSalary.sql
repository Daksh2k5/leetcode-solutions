# Last updated: 9/19/2026, 1:10:09 PM
SELECT (SELECT DISTINCT salary as SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1)
as SecondHighestSalary
