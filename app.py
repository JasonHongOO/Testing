from flask import Flask, request
import json
import time
import os
import requests

#其他程式
import Menu
import Weather.EarthQuake
import Weather.CurrentWeather
import Weather.WeatherForecast
import Weather.AirQuality
import Database
import VideoUrl

#第三方套件
import warnings
from linebot import LineBotSdkDeprecatedIn30
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, FollowEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage,TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction
# import whisper
import openai


new_path = r"./ffmpeg"
os.environ["PATH"] = new_path

from dotenv import load_dotenv # 載入 .env 檔案中的環境變數
load_dotenv()


app = Flask(__name__)

@app.route("/")
def home():
	return "HELLO POSTPOSTPOSTPOST "

@app.route("/about")
def about():
	return "HELLO about"

openai.api_key = os.getenv('OPENAI_API_KEY')
def GPT_response(text):
    print("Go GPT", text)
    try:
        # 接收回應
        # response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0.5, max_tokens=500)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=[
                                                        {"role": "user", "content": text},
                                                ],
                                                temperature=0.5, 
                                                max_tokens=500)
    except Exception as e:
        print("Error(GPT) : ",e)
    print("Go GPT", response)
    # 重組回應
    answer = response['choices'][0]['message']['content']
    print(answer)

    return answer

@app.route("/web", methods=['POST'])
def linebot():
    try:
        body = request.get_data(as_text=True)
        line_bot_api = LineBotApi(os.getenv('TOKEN'))
        handler = WebhookHandler(os.getenv('SECRET'))
        json_data = json.loads(body)
        print(json_data)
    except Exception as e:
        print("Error(基本物件) : ",e)

    try:
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)

        #event
        ReplyToken = json_data['events'][0]['replyToken']
        event_type = json_data['events'][0]['type']  # 取得事件類型
        UserID = json_data['events'][0]['source']['userId']

        #加入官方好友
        if event_type == 'follow':  # 判斷是否為 Follow Event (使用者加入好友)
            Menu.main_menu(line_bot_api, ReplyToken)
            Database.SaveData(line_bot_api.get_profile(UserID))

        #傳訊息
        if event_type == 'message':
            type = json_data['events'][0]['message']['type']
            MsgID = json_data['events'][0]['message']['id']

            #文字
            if type == 'text':
                msg = json_data['events'][0]['message']['text']
                print(f"msg = {msg}")

                #關鍵字
                if msg == "選單":
                    # line_bot_api.reply_message(ReplyToken, TextSendMessage(msg))
                    Menu.main_menu(line_bot_api, ReplyToken)  # 使用者輸入"選單"時，回傳選單給使用者
  
                elif msg == "氣象選單":
                    Menu.weather_menu(line_bot_api, ReplyToken)

                elif msg == "雷達回波圖":
                    RaderMsg = f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}'
                    line_bot_api.reply_message(ReplyToken, ImageSendMessage(original_content_url=RaderMsg, preview_image_url=RaderMsg))
                
                elif msg == "地震資訊":
                    EarthQuakeMsg = Weather.EarthQuake.earth_quake(os.getenv('WHEATHER_CODE'))
                    line_bot_api.push_message(UserID, TextSendMessage(text=EarthQuakeMsg[0]))       # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    line_bot_api.reply_message(ReplyToken, ImageSendMessage(original_content_url=EarthQuakeMsg[1], preview_image_url=EarthQuakeMsg[1]))

                elif msg == "影片下載":  
                    try:
                        # FlexMessage = json.load(open('VideoMenu.json','r',encoding='utf-8'))
                        # line_bot_api.reply_message(ReplyToken, FlexSendMessage(alt_text="VideoMenu",contents = FlexMessage))
                        Menu.video_menu(line_bot_api, ReplyToken)
                    except Exception as e:
                        print("Error(video) : ", e)

                elif msg == "高畫質" or msg == "低畫質":
                    try:
                        video_json = json.load(open('Config.json','r',encoding='utf-8'))
                    except:
                        print("video_json 不存在 : 新創建一個")
                        data = {"Video" : {}}
                        with open('Config.json', 'w') as file: json.dump(data, file)
                        video_json = json.load(open('Config.json','r',encoding='utf-8'))

                    video_json["Video"][UserID] = 1 if msg == "高畫質" else 0
                    with open('Config.json', 'w') as file:
                            json.dump(video_json, file)

                elif "youtube.com" in msg or "facebook.com" in msg:
                    if("youtube.com" in msg):
                        line_bot_api.push_message(UserID, TextSendMessage("youtube.com : " + "High Quality" if json.load(open('Config.json','r',encoding='utf-8'))["Video"][UserID] == 1 else "Low Quality"))
                    elif("facebook.com" in msg):
                        line_bot_api.push_message(UserID, TextSendMessage("facebook.com " + "High Quality" if json.load(open('Config.json','r',encoding='utf-8'))["Video"][UserID] == 1 else "Low Quality"))
                #     # print("(youtube) Mode = ", json.load(open('Config.json','r',encoding='utf-8'))["Video"][UserID])
                    reply = VideoUrl.VideoUrlDecoder(msg, 1)
                    line_bot_api.reply_message(ReplyToken, TextSendMessage(reply))
 
                else:
                    print("Messgae Context : ", msg)
                    reply = GPT_response(msg)
                    # reply = msg
                    print(f"reply : {reply}")
                    line_bot_api.reply_message(ReplyToken, TextSendMessage(reply))

            elif type == 'location' :
                address = json_data['events'][0]['message']['address'].replace('台','臺')
                print(address)
                
                reply = f"{address}\n\n{Weather.CurrentWeather.current_weather(os.getenv('WHEATHER_CODE'), address)}\n\n{Weather.AirQuality.aqi(address)}\n\n{Weather.WeatherForecast.forecast(os.getenv('WHEATHER_CODE'), address)}"
                line_bot_api.reply_message(ReplyToken, TextSendMessage(reply))

            elif type == 'audio':
                try:
                    print("Is Audio")
                    #寫入音訊檔
                    audio_content = line_bot_api.get_message_content(MsgID)
                    path='./Sound/sound.m4a'
                    with open(path, 'wb') as fd:
                        for chunk in audio_content.iter_content():
                            fd.write(chunk)

                    #進行語音轉文字處理
                    # model = whisper.load_model("base")
                    # result = model.transcribe(path)
                    # print("Audio Context : ", result["text"])
                    # reply = GPT_response(result["text"])
                    # reply = result["text"]

                    audio_file= open(path, "rb")
                    result = openai.Audio.transcribe("whisper-1", audio_file)
                    print("Audio Context : ", result["text"])
                    reply = result["text"]      
                    print("reply : ", reply)
                    #將轉換的文字回傳給用戶
                    line_bot_api.reply_message(ReplyToken, TextSendMessage(text=reply))
                except Exception as e:
                    print("ERROR (Audio) : ",e)

            else:
                reply = '你傳的不是文字呦～'
                print(f"reply : {reply}")
                line_bot_api.reply_message(ReplyToken, TextSendMessage(reply))
    except:
        print(body)
    return 'OK'



if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=LineBotSdkDeprecatedIn30)
    # port = int(os.environ.get('PORT', 6000))
    # app.run(host='0.0.0.0', port=port)
    app.run(port=6000)
    # app.run()