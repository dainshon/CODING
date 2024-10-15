-- 코드를 입력하세요
SELECT concat('/home/grep/src/',B.BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
from USED_GOODS_FILE F left outer join USED_GOODS_BOARD B
on F.BOARD_ID = B.BOARD_ID
where B.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by FILE_ID DESC

