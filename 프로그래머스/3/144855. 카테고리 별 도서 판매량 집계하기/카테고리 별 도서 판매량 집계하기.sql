-- 코드를 입력하세요
SELECT a.CATEGORY, sum(b.sales) as TOTAL_SALES from book a
join book_sales b on a.book_id = b.book_id
where date_format(b.sales_date, '%Y-%m') = '2022-01'
group by a.category
order by a.category asc