SELECT 
    ID,
    CASE 
        WHEN per_rank <= 0.25 THEN 'CRITICAL'
        WHEN per_rank <= 0.5 THEN 'HIGH'
        WHEN per_rank <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS colony_name
FROM(SELECT
        id,
        size_of_colony,
        PERCENT_RANK()OVER(ORDER BY size_of_colony DESC) AS per_rank
    FROM ECOLI_DATA) AS PER_RANK_DATA
ORDER BY ID ASC;