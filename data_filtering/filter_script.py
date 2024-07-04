# 4. 운영시간 정리, result.csv
# ------------------------------------------------------------------------
from ast import literal_eval
import pandas as pd
import os, sys

import filter

## INPUTS ================================================================
# filename = 'cafe_jongro'
# search_date = ['2024','07','06'] # 원하는 날짜
# search_time = '01:00' # 궁금한 시간s

filename = sys.argv[1]          # 'cafe_jongro'
year = sys.argv[2]              # ['2024','07','06'][0]
mon = sys.argv[3]               # ['2024','07','06'][1]
day = sys.argv[4]               # ['2024','07','06'][2]
search_time = sys.argv[5]       # '01:00'
result_filename = sys.argv[6]   # f'카페리스트검색결과_{date}_{time}.csv'
## =======================================================================

# data path
abs_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(abs_root_path, 'data/')

# csv 불러와서 편집
crawled_df = pd.read_csv(os.path.join(data_dir, f'{filename}_sorted.csv'),
                            converters={"운영시간":literal_eval, "운영시간":literal_eval})

# 최종 결과 저장
abs_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_path = os.path.join(abs_root_path, 'result/')

result_path = os.path.join(save_path, result_filename)
result_df = filter.checked_cafe_df(crawled_df, result_path, [year, mon, day], search_time)

