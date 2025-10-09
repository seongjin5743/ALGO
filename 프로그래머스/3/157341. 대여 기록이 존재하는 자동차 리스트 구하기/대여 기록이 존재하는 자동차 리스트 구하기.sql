-- 코드를 입력하세요
SELECT distinct((a.car_id)) from CAR_RENTAL_COMPANY_CAR a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
on a.CAR_ID = b.CAR_ID
where month(b.start_date) = 10 and a.car_type = '세단'
order by a.car_id desc