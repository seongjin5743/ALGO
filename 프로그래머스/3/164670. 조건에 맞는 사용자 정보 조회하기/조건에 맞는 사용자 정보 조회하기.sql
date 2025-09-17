SELECT a.USER_ID, a.NICKNAME,
       concat(a.CITY, ' ', a.STREET_ADDRESS1, ' ', a.STREET_ADDRESS2) AS 전체주소,
       concat(substr(a.TLNO,1,3), '-', substr(a.TLNO,4,4), '-', substr(a.TLNO,8,4)) AS 전화번호
FROM USED_GOODS_USER a
WHERE a.USER_ID IN (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
)
order by a.USER_ID desc;