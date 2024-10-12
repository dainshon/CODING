SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE
where cast(substring(DATE_OF_BIRTH, 6, 2) as unsigned)=3 and TLNO is not null and GENDER = 'W'
order by MEMBER_ID ASC