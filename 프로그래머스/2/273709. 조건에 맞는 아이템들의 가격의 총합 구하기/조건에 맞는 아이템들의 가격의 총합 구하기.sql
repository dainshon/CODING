-- 코드를 작성해주세요

select sum(PRICE) AS TOTAL_PRICE
from ITEM_INFO
group by RARITY
having RARITY = 'LEGEND'