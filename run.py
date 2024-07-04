from pyscript import display, document

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
        search_lat = lat_value.value
        search_lng = lng_value.value
        search_radius = radius_value.value
        search_date = date_value.value
        search_time = time_value.value

        ## 필터링 진행 함수 
        if float(search_radius) > 10:
            result.innerText = "반경을 10 이하로 입력해주세요."
        else:
            # 필터링
            result.innerText = "=========검색결과==========="
            pass
