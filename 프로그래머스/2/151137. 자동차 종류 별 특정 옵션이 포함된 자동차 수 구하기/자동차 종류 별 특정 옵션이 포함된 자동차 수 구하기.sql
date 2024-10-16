-- 코드를 입력하세요
select CAR_TYPE, count(*) as CARS
from
    (SELECT *
    from CAR_RENTAL_COMPANY_CAR
    where OPTIONS REGEXP '통풍시트|열선시트|가죽시트') A
group by CAR_TYPE
order by CAR_TYPE ASC

-- SUBSTRING_INDEX(OPTIONS,',',-7)