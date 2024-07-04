
# drop null: 크롤링해왔을 때 운영시간/url null값이면 drop
def drop_null(df):
    # url 컬럼 빈값 제거
    drop_url = df.dropna(subset=['url'], inplace=False).reset_index(drop=True, inplace=False)
    # 운영시간 빈 리스트 제거
    drop_time = drop_url[drop_url['운영시간'] != '[]']

    return drop_time