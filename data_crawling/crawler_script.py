# 2. 크롤링
# ------------------------------------------------------------------------
# cleaning_script.py로부터 만들어진 csv사용
# 크롤링해서 데이터에 url, time컬럼 추가 =====> 시간 오래걸림(에러나면 한줄씩 try해서 실패하면 다시하는걸로)
# 시간이 오래걸리니 중간 에러를 대비해서 나눠서 처리, 저장
# 1) filename_url.csv, 
# 2) filename_crawled.csv

import pandas as pd
import os, sys

import crawl

## INPUTS ================================================================
filename = sys.argv[1] # 'cafe_jongro'

## =======================================================================

# 데이터 저장 경로
abs_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(abs_root_path, 'data')

data_path = os.path.join(data_dir, f'{filename}.csv') # 정리만 된 data: cafe_jongro.csv

## 1) url 컬럼 추가, 저장
df_url = crawl.get_urls(data_path)
df_url.to_csv(os.path.join(data_dir, f'{filename}_url.csv'), index=False, encoding='utf-8-sig')
print('1) URL 크롤링 완료!!!!!!!!!!!!!!')

## 2) 운영시간 컬럼 추가, 저장
loaded_df_url = pd.read_csv(os.path.join(data_dir, f'{filename}_url.csv')) # url포함해서 저장된 csv파일 load

save_path = os.path.join(data_dir, f'{filename}_crawled.csv') # 크롤링 포함된 data 저장
crawl.get_time_n_dropna(loaded_df_url, save_path) # save csv
print('2) 운영시간 크롤링 + 결측치 제거 완료')