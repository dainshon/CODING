-- 코드를 입력하세요
select ANIMAL_ID, NAME
from ANIMAL_OUTS -- A left outer join ANIMAL_INS B
-- on A.ANIMAL_ID NOT IN ()
where ANIMAL_ID NOT IN (select ANIMAL_ID from ANIMAL_INS)
order by ANIMAL_ID ASC

