-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH from member_profile
where GENDER = 'W' and TLNO is not null and date_format(DATE_OF_BIRTH, '%m') = 3
order by MEMBER_ID asc