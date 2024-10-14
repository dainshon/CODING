-- 코드를 입력하세요
# SELECT cast(date_format(START_DATE, '%m') as unsigned) as MONTH, car_id-- , count(*) AS RECORDS

select cast(date_format(START_DATE, '%m') as unsigned) as MONTH, car_id, count(*) AS RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE, '%Y%m') between '202208' and '202210' 
    group by car_id
    having count(*) >= 5
    ) and date_format(START_DATE, '%Y%m') between '202208' and '202210'
group by car_id, MONTH
order by MONTH ASC, CAR_ID DESC

# order by MONTH ASC, CAR_ID DESC
#order by CAR_ID DESC