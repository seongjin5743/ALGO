-- 코드를 작성해주세요
select b.SCORE, a.EMP_NO, a.EMP_NAME, a.POSITION, a.EMAIL from HR_EMPLOYEES a
join
(
    select EMP_NO, sum(SCORE) as SCORE from HR_GRADE
    group by EMP_NO
) b on a.EMP_NO = b.EMP_NO
where b.score = 
(
select max(score) from
    (
        SELECT SUM(SCORE) AS score
        FROM HR_GRADE
        GROUP BY EMP_NO
    ) x
)