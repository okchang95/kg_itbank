# 1. 데이터 정리
# ------------------------------------------------------------------------
# 오리지날데이터(약 47만개)를 받아서 원하는 구역, 원하는 업종(일단은 카페만)으로 데이터 축소, 
# input: 원본 csv 파일, 행정동  (+ 법정동, 업종)
# output: 선택된 데이터 csv파일

import pandas as pd
import os, sys

## INPUTS ================================================================
filename = sys.argv[1]

## =======================================================================

# 데이터 포털 원본 데이터
original_filename = 'original_data.csv' # sys.argv[2]

# 행정동명 (필요하면 법정동명도 포함시켜서 필터링)
dong = '종로1.2.3.4가동' # sys.argv[3]

# data path
abs_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(abs_root_path, 'data/')
original_data_path = os.path.join(data_dir, original_filename)
df = pd.read_csv(original_data_path)

# 1) 불필요한 컬럼 제거
columns_to_keep = ['상호명', '지점명', '상권업종소분류명', '표준산업분류명', '행정동명', '법정동명', '지번주소', '도로명주소', '경도', '위도']
df_filtered = df[columns_to_keep]
print('1) 컬럼 정리')

# 2) 업종 필터링
cafe_df = df_filtered[(df_filtered['표준산업분류명'] == '커피 전문점') | (df_filtered['상권업종소분류명'] == '카페')]
print('2) 업종 필터링')

# 3) 결측치 제거
drop_df = cafe_df.dropna(subset=['표준산업분류명'], inplace=False)
print('3) 결측치 제거')

# 4) 행정동명으로 필터링
dong_df = drop_df[drop_df['행정동명'] == dong] # 법정동 포함: " | (df['법정동명'] == b_dong)] "
print('4) 행정동 필터링')

# 인덱스 초기화
reidx_df = dong_df.reset_index(drop=True, inplace=False)
print('5) 인덱스 초기화')

# 저장
reidx_df.to_csv(os.path.join(data_dir, f'{filename}.csv'), index=False, encoding='utf-8-sig')
print('6) 저장 완료 =================================================')


