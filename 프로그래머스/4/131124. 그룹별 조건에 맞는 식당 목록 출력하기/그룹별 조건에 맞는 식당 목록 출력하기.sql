-- 코드를 입력하세요
select MEMBER_NAME, b.REVIEW_TEXT, date_format(b.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE from MEMBER_PROFILE a
join REST_REVIEW b on a.MEMBER_ID = b.MEMBER_ID
where a.MEMBER_ID in(
    SELECT MEMBER_ID
    FROM (
        SELECT MEMBER_ID, COUNT(*) AS review_cnt
        FROM REST_REVIEW
        GROUP BY MEMBER_ID
    ) t
    WHERE review_cnt = (
        SELECT MAX(cnt)
        FROM (
            SELECT COUNT(*) AS cnt
            FROM REST_REVIEW
            GROUP BY MEMBER_ID
        ) sub
    )
)
order by REVIEW_DATE, b.REVIEW_TEXT