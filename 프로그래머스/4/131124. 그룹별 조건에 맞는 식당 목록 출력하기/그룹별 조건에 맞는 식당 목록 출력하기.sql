# -- 코드를 입력하세요
select MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW A left outer join MEMBER_PROFILE B
on A.MEMBER_ID = B.MEMBER_ID
where A.MEMBER_ID IN
(
SELECT MEMBER_ID -- , count(*) as review_cnt
from REST_REVIEW
group by MEMBER_ID
having count(*) = 
    (SELECT count(*) as cnt
    from REST_REVIEW
    group by MEMBER_ID
    order by cnt DESC
    limit 1)
)
order by REVIEW_DATE ASC
 
 