from pyscript import display, document
import subprocess

if __name__ =="__main__":

    def function(evt):  
        lat_value = document.querySelector("#latValue")
        lng_value = document.querySelector("#lngValue")
        radius_value = document.querySelector("#radiusValue")
        date_value = document.querySelector("#dateValue")
        time_value = document.querySelector("#timeValue")
        result= document.querySelector("#result")
        # 입력값 확인
        # result.innerText = f'{lat_value.value, lng_value.value, radius_value.value, date_value.value.split('-'), time_value.value}'
        
        ## 입력값
        search_lat = lat_value.value    # 위도
        search_lng = lng_value.value    # 경도
        search_radius = radius_value.value  # 반경
        search_date = date_value.value.split('-')
        search_time = time_value.value
        '''
        '37.57035764261156', <class 'str'>
        '126.99036702755654', <class 'str'> 
        '0.3', <class 'str'>
        ['2024', '07', '31'], <class 'list'>
        '00:45', <class 'str'>
        '''

        ## 필터링 진행 함수 
        if float(search_radius) > 10:
            result.innerText = "반경을 10 이하로 입력해주세요."
        else:
            # 필터링
            result.innerText = "=========검색결과==========="
            pass

    # INPUTS
    filename = 'cafe_jongro'
    # data_dir = 'data/'
    # result_dir = 'result/'

    # search_date = ['2024','07','06'] # 원하는 날짜
    # search_date = '2024','07','06'
    year = '2024'
    mon = '07'
    day = '06'
    # search_time = '01:00' # 궁금한 시간

    # # PATHS
    # save_filename = 'cafe_jongro'
    # result_path = '/Users/okchang/mainbiz/project/p1_final/result'
    date = year + mon + day
    time = ''.join(search_time.split(':'))
    result_filename = f'카페리스트검색결과_{date}_{time}.csv'


    # subprocess.run(['python', 'data_load.py'])
    # subprocess.run(['python', 'crawl.py'])
    subprocess.run(['python', 'sort_distance.py', str(latitude), str(longitude), str(radius)])
    subprocess.run(['python', 'get_time.py', year, mon, day, search_time])
            