# Write your MySQL query statement below
SELECT id, movie, description, rating From Cinema Where id%2=1 and description <> 'boring' order by rating desc