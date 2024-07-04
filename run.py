import sort_distance, get_time
import subprocess
# import Element

if __name__ =="__main__":

    # def function(): 
    #     lat_value = Element("latValue")
    #     lng_value = Element("lngValue")
    #     radius_value = Element("radiusValue")
    #     date_value = Element("dateValue")
    #     time_value = Element("timeValue")
        
    #     result= Element("result")
    #     result.element.innerText = f'{lat_value, lng_value, radius_value, date_value, time_value}'
    
    # # INPUTS - sort_distance.py
    latitude = 37.571006515132865
    longitude = 126.99251768504305
    radius = 0.5 # km

    # # INPUTS - get_time.py
    # search_date = ['2024','07','06'] # 원하는 날짜
    # search_date = '2024','07','06'
    year = '2024'
    mon = '07'
    day = '06'
    search_time = '01:00' # 궁금한 시간

    # # PATHS
    # data_path = '/Users/okchang/mainbiz/project/p1_final/data'
    # save_filename = 'cafe_jongro'
    # result_path = '/Users/okchang/mainbiz/project/p1_final/result'
    
    date = year + mon + day
    time = ''.join(search_time.split(':'))
    result_filename = f'카페리스트검색결과_{date}_{time}.csv'


    # subprocess.run(['python', 'data_load.py'])
    # subprocess.run(['python', 'crawl.py'])
    subprocess.run(['python', 'sort_distance.py', str(latitude), str(longitude), str(radius)])
    subprocess.run(['python', 'get_time.py', year, mon, day, search_time])
                    



    pass