import requests

def earth_quake(WHEATHER_CODE):
    msg = ['找不到地震資訊','https://example.com/demo.jpg']            # 預設回傳的訊息
    try:
        url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={WHEATHER_CODE}'
        e_data = requests.get(url)                                   # 爬取地震資訊網址
        e_data_json = e_data.json()                                  # json 格式化訊息內容
        eq = e_data_json['records']['Earthquake'][0]                    # 取出地震資訊

        loc = eq['EarthquakeInfo']['Epicenter']['Location']       # 地震地點
        val = eq['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'] # 地震規模
        dep = eq['EarthquakeInfo']['FocalDepth']                 # 地震深度
        eq_time = eq['EarthquakeInfo']['OriginTime']              # 地震時間
        img = eq['ReportImageURI']                                # 地震圖
        msg = [f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。', img]

        # print(f"weather, {msg}")
        return msg    # 回傳 msg
    except Exception as e:
        print(f"weather : {msg} \n error : {e}")
        return msg    # 如果取資料有發生錯誤，直接回傳 msg