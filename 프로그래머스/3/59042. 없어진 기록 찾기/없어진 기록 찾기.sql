-- 코드를 입력하세요

select ANIMAL_ID, NAME from ANIMAL_OUTS
where animal_id not in (SELECT ANIMAL_ID from ANIMAL_INS)