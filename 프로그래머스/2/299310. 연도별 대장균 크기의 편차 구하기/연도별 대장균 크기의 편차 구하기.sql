# select YEAR,(MAX_SIZE-SIZE_OF_COLONY) AS YEAR_DEV, ID
# from ECOLI_DATA A left outer join (
#     select date_format(DIFFERENTIATION_DATE,"%Y") as YEAR, MAX(SIZE_OF_COLONY) as MAX_SIZE
#     from ECOLI_DATA
#     group by date_format(DIFFERENTIATION_DATE,"%Y")
#     ) B 
#     on date_format(A.DIFFERENTIATION_DATE,"%Y") = B.YEAR
-- ORDER BY YEAR ASC, YEAR_DEV ASC
select YEAR, (max_size - SIZE_OF_COLONY) as YEAR_DEV, ID
from ECOLI_DATA A left outer join (
select year(DIFFERENTIATION_DATE) as YEAR, MAX(SIZE_OF_COLONY) as max_size
from ECOLI_DATA
group by YEAR) B 
on year(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC