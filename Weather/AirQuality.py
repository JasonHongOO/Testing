import requests
import statistics

# 空氣品質函式
def aqi(address):
    city_list, site_list ={}, {}
    msg = '找不到空氣品質資訊。'
    try:
        # 2022/12 時氣象局有修改了 API 內容，將部份大小寫混合全改成小寫，因此程式碼也跟著修正
        url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
        a_data = requests.get(url)             # 使用 get 方法透過空氣品質指標 API 取得內容
        a_data_json = a_data.json()            # json 格式化訊息內容
        for i in a_data_json['records']:       # 依序取出 records 內容的每個項目
            try :
                city = i['county']                 # 取出縣市名稱
                if city not in city_list:
                    city_list[city]=[]             # 以縣市名稱為 key，準備存入串列資料
                site = i['sitename']               # 取出鄉鎮區域名稱
                if(i['aqi']):
                    aqi = int(i['aqi'])                # 取得 AQI 數值      (可能會是空的)
                else :
                    aqi = -1
                status = i['status']               # 取得空氣品質狀態
                if status == "" : status = '(未檢測到)'
                site_list[site] = {'aqi':aqi, 'status':status}  # 記錄鄉鎮區域空氣品質
                city_list[city].append(aqi)        # 將各個縣市裡的鄉鎮區域空氣 aqi 數值，以串列方式放入縣市名稱的變數裡

            except Exception as e:
                print("Error : ",e)
                print("City : ", city)
                print("site : ", site)
                print("aqi : ", i['aqi'])

        for i in city_list:
            if i in address: # 如果地址裡包含縣市名稱的 key，就直接使用對應的內容
                # 參考 https://airtw.epa.gov.tw/cht/Information/Standard/AirQualityIndicator.aspx
                aqi_val = round(statistics.mean(city_list[i]),0)  # 計算平均數值，如果找不到鄉鎮區域，就使用縣市的平均值
                aqi_status = ''  # 手動判斷對應的空氣品質說明文字
                if aqi_val == -1: aqi_status = '(未檢測到)'
                elif aqi_val>0 and aqi_val<=50: aqi_status = '良好'
                elif aqi_val>50 and aqi_val<=100: aqi_status = '普通'
                elif aqi_val>100 and aqi_val<=150: aqi_status = '對敏感族群不健康'
                elif aqi_val>150 and aqi_val<=200: aqi_status = '對所有族群不健康'
                elif aqi_val>200 and aqi_val<=300: aqi_status = '非常不健康'
                else: aqi_status = '危害'
                msg = f'空氣品質{aqi_status} ( AQI {aqi_val} )。' # 定義回傳的訊息
                break

        for i in site_list:
            if i in address:  # 如果地址裡包含鄉鎮區域名稱的 key，就直接使用對應的內容
                msg = f'空氣品質{site_list[i]["status"]} ( AQI {site_list[i]["aqi"]} )。'
                break
        return msg    # 回傳 msg
    except Exception as e:
        print(f"Error : {e}")
        return msg    # 如果取資料有發生錯誤，直接回傳 msg