# 4. 운영시간 정리, result.csv

from py import filter
import pandas as pd
import os
from ast import literal_eval
import sys

## INPUTS ==========================================
# filename = 'cafe_jongro'
# search_date = ['2024','07','06'] # 원하는 날짜
# search_time = '01:00' # 궁금한 시간

# search_date = sys.argv[1]

filename = sys.argv[1]
year = sys.argv[2]
mon = sys.argv[3]
day = sys.argv[4]
search_time = sys.argv[5]
result_filename = sys.argv[6]

search_date = [year, mon, day]


## INPUTS ==========================================
data_dir = 'data/'

# csv 불러와서 편집
crawled_df = pd.read_csv(os.path.join(data_dir, f'{filename}_sorted.csv'),
                            converters={"운영시간":literal_eval, "운영시간":literal_eval})

# 최종 결과 저장
save_path = 'result/'
result_path = os.path.join(save_path, result_filename)
result_df = filter.checked_cafe_df(crawled_df, result_path, search_date, search_time)

# 확인
# print(result_df)
