-- 코드를 입력하세요
SELECT category, sum(sales) as TOTAL_SALES
from BOOK_SALES A left outer join BOOK B on A.BOOK_ID = B.BOOK_ID
where date_format(SALES_DATE, "%Y%m") = '202201'
group by category
order by category asc
