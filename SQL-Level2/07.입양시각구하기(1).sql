SELECT HOUR(DATETIME), COUNT(DATETIME) FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= "9" and HOUR(DATETIME) <= "19"
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME) asc;