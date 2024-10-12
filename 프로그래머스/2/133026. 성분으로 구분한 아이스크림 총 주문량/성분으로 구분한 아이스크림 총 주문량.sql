-- 코드를 입력하세요
SELECT B.INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
from FIRST_HALF A left outer join ICECREAM_INFO B on A.FLAVOR = B.FLAVOR
group by INGREDIENT_TYPE
order by TOTAL_ORDER ASC