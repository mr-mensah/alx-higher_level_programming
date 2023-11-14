-- script that import in hbtn_0c_0 database this table dump
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=8 OR month=7 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
