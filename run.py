# from pyscript import display, document
import pandas as pd
import subprocess
import os
import time

def file_exists(filename):
    return os.path.exists(os.path.join('data', filename)) # 존재하면 True

if __name__ =="__main__":

    # INPUTS: 들어올것으로 예상
    filename = 'test'
    result_filename = 'result'
    dong = '종로1.2.3.4가동'
    search_lat = '37.571006515132865' 
    search_lng = '126.99251768504305' 
    search_radius = '0.5' # km
    search_date = ['2024','07','06'] 
    search_time = '08:00' # 궁금한 시간

    # Define file paths
    csv_file = f'{filename}.csv'
    crawled_file = f'{filename}_crawled.csv'
    sorted_file = f'{filename}_sorted.csv'

    if not os.path.exists('data'):
        os.makedirs('data')

    # 1) 데이터 정리: f'{filename}.csv'가 없으면 만들어
    if not file_exists(csv_file):
        if file_exists('original_data.csv'):
            print('1) cleaning_script.py 실행')
            print('original_data.csv을 불러옵니다..')
            starttime = time.time()
            subprocess.run(['python', 'data_cleaning/cleaning_script.py', filename])
            endtime = time.time()
            print(f'1) cleaning_script.py 완료!, {endtime - starttime} seconds {"="*20}\n')
        else:
            print("데이터를 로드할 수 없습니다 ㅠ ...(1)")

    # 2) 데이터 크롤링: f'{filename}_crawled.csv'가 없으면 만들어
    if file_exists(csv_file) and not file_exists(crawled_file):
        print('2) crawler_script.py 실행')
        print(f'{csv_file}.csv을 불러옵니다..')
        starttime = time.time()
        subprocess.run(['python', 'data_crawling/crawler_script.py', filename])
        endtime = time.time()
        print(f'2) crawling_script.py 완료!, {endtime - starttime} seconds {"="*20}\n')
    else:
        print("데이터를 로드할 수 없습니다 ㅠ ...(2)")

    # 3) 거리순 정렬: f'{filename}_sorted.csv'가 없으면 만들어
    if file_exists(crawled_file) and not file_exists(sorted_file):
        print('3) sorting_script.py 실행')
        print(f'{crawled_file}을 불러옵니다..')
        starttime = time.time()
        subprocess.run(['python', 'data_cleaning/sorting_script.py', filename, search_lat, search_lng, search_radius])
        endtime = time.time()
        print(f'3) sorting_script.py 완료, {endtime - starttime} seconds {"="*20}\n')
    else:
        print("데이터를 로드할 수 없습니다 ㅠ ...(3)")
    
    # 4) 운영시간 필터링: f'{filename}_sorted.csv'가 있으면 실행
    if file_exists(sorted_file):
        print('4) filter_script.py 실행')
        print(f'{sorted_file}을 불러옵니다..')

        year, mon, day = search_date
        time_ = ''.join(search_time.split(':'))
        result_filename = f'{result_filename}_{year + mon + day}_{time_}.csv'

        starttime = time.time()
        subprocess.run(['python', 'data_filtering/filter_script.py', filename, year, mon, day, search_time, result_filename])
        endtime = time.time()
        print(f'4) filtering_script.py 완료!, {endtime - starttime} seconds {"="*20}\n')

        # 확인
        result_path = os.path.join('result/', result_filename)
        df = pd.read_csv(result_path)
        print(df)

    else:
        print("4) 데이터를 로드할 수 없습니다 ㅠ ...(4)")

    # web
    # def function(evt):  
    #     lat_value = document.querySelector("#latValue")
    #     lng_value = document.querySelector("#lngValue")
    #     radius_value = document.querySelector("#radiusValue")
    #     date_value = document.querySelector("#dateValue")
    #     time_value = document.querySelector("#timeValue")
    #     result= document.querySelector("#result")
    #     # 입력값 확인
    #     # result.innerText = f'{lat_value.value, lng_value.value, radius_value.value, date_value.value.split('-'), time_value.value}'
        
    #     ## 입력값
    #     search_lat = lat_value.value    # 위도
    #     search_lng = lng_value.value    # 경도
    #     search_radius = radius_value.value  # 반경
    #     search_date = date_value.value.split('-')
    #     search_time = time_value.value
    #     '''
    #     '37.57035764261156', <class 'str'>
    #     '126.99036702755654', <class 'str'> 
    #     '0.3', <class 'str'>
    #     ['2024', '07', '31'], <class 'list'>
    #     '00:45', <class 'str'>
    #     '''

    #     ## 필터링 진행 함수 
    #     if float(search_radius) > 10:
    #         result.innerText = "반경을 10 이하로 입력해주세요."
    #     else:
    #         # 필터링
    #         result.innerText = "=========검색결과==========="
    #         pass
