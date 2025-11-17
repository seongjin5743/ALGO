-- 코드를 작성해주세요
SELECT 
    ID,
    (SELECT COUNT(*) 
     FROM ECOLI_DATA child 
     WHERE child.PARENT_ID = parent.ID) AS CHILD_COUNT
FROM ECOLI_DATA parent
ORDER BY ID;