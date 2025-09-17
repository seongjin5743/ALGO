SELECT EMP.EMP_NO, 
        EMP.EMP_NAME, 
        GRADES.SCORE_GRADE AS GRADE, 
        CASE
            WHEN GRADES.SCORE_GRADE = 'S' THEN EMP.SAL * 0.2
            WHEN GRADES.SCORE_GRADE = 'A' THEN EMP.SAL * 0.15
            WHEN GRADES.SCORE_GRADE = 'B' THEN EMP.SAL * 0.1
            ELSE 0
        END AS BONUS
FROM HR_EMPLOYEES AS EMP
    JOIN (SELECT EMP_NO, 
                CASE
                    WHEN AVG(SCORE) >= 96 THEN 'S'
                    WHEN AVG(SCORE) >= 90 THEN 'A'
                    WHEN AVG(SCORE) >= 80 THEN 'B'
                    ELSE 'C'
                END AS SCORE_GRADE
            FROM HR_GRADE
            GROUP BY EMP_NO) AS GRADES
    ON EMP.EMP_NO = GRADES.EMP_NO
ORDER BY 1