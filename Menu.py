from linebot import LineBotApi, WebhookHandler
# 需要額外載入對應的函示庫
from linebot.models import PostbackAction, URIAction, MessageAction, FlexSendMessage, TemplateSendMessage, ButtonsTemplate

# line_bot_api = LineBotApi(const.TOKEN)
# line_bot_api.push_message('U732be8ffb0eaa17f376477cbbdc3efb4', TemplateSendMessage(
#     alt_text='ButtonsTemplate',
#     template=ButtonsTemplate(
#         thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
#         title='JasonHong',
#         text='這是按鈕測試',
#         actions=[
#             PostbackAction(
#                 label='postback',
#                 data='發送 postback'
#             ),
#             MessageAction(
#                 label='Hello',
#                 text='Hello'
#             ),
#             URIAction(
#                 label='派大星',
#                 uri='https://memeprod.ap-south-1.linodeobjects.com/user-template/3a35e7e8f145bce4c98a5d22646ff4e9.png'
#             )
#         ]
#     )
# ))



def main_menu(line_bot_api, ReplyToken):

    # 使用者進入連天室或輸入"選單"時回傳這張表單
    menu_template = TemplateSendMessage(
        alt_text='ButtonsTemplate',
        template=ButtonsTemplate(
            thumbnail_image_url='https://memeprod.ap-south-1.linodeobjects.com/user-template/3a35e7e8f145bce4c98a5d22646ff4e9.png',
            title='JasonHong',
            text='這是按鈕測試',
            actions=[
                MessageAction(
                    label='氣象選單',
                    text='氣象選單'
                ),
                MessageAction(
                    label='影片下載',
                    text='影片下載'
                ),
                MessageAction(
                    label='Hello',
                    text='Hello'
                ),
                URIAction(
                    label='派大星',
                    uri='https://memeprod.ap-south-1.linodeobjects.com/user-template/3a35e7e8f145bce4c98a5d22646ff4e9.png'
                )
            ]
        )
    )
    line_bot_api.reply_message(ReplyToken, menu_template)



def weather_menu(line_bot_api, ReplyToken):
        # 使用者進入連天室或輸入"選單"時回傳這張表單
    menu_template = TemplateSendMessage(
        alt_text='ButtonsTemplate',
        template=ButtonsTemplate(
            thumbnail_image_url='https://www.citypng.com/public/uploads/preview/hd-orange-storage-host-clouds-icon-png-31631696263tccmsna0eg.png',
            title='JasonHong',
            text='這是按鈕測試',
            actions=[
                MessageAction(
                    label='雷達回波圖',
                    text='雷達回波圖'
                ),
                MessageAction(
                    label='地震資訊',
                    text='地震資訊'
                ),
                URIAction(
                    label='派大星',
                    uri='https://memeprod.ap-south-1.linodeobjects.com/user-template/3a35e7e8f145bce4c98a5d22646ff4e9.png'
                )
            ]
        )
    )
    line_bot_api.reply_message(ReplyToken, menu_template)


def video_menu(line_bot_api, ReplyToken):
    flex_message = FlexSendMessage(
                alt_text="VideoMenu",
                contents={
                        "type": "bubble",
                        "hero": {
                        "type": "image",
                        "url": "https://th.bing.com/th/id/OIP.FOo5mn38UvUJQ9JbAEJv3AHaFx?pid=ImgDet&w=200&h=156&c=7&dpr=1.3",
                        "size": "full",
                        "aspectRatio": "20:15",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "uri": "http://linecorp.com/"
                        }
                        },
                        "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "text",
                            "text": "影片品質",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center"
                            },
                            {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                    "type": "text",
                                    "text": "提示 : ",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1,
                                    "align": "center"
                                    },
                                    {
                                    "type": "text",
                                    "text": "影片畫質，低畫質下載較快",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5,
                                    "align": "start"
                                    }
                                ]
                                }
                            ]
                            }
                        ]
                        },
                        "footer": {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "sm",
                        "contents": [
                            {
                            "type": "button",
                            "style": "primary",
                            "height": "md",
                            "action": {
                                "type": "message",
                                "label": "低畫質",
                                "text": "低畫質"
                            },
                            "position": "relative",
                            "margin": "none",
                            "color": "#87cefa",
                            "flex": 1,
                            "scaling": "false",
                            "offsetEnd": "sm"
                            },
                            {
                            "type": "button",
                            "style": "primary",
                            "height": "md",
                            "action": {
                                "type": "message",
                                "label": "高畫質",
                                "text": "高畫質"
                            },
                            "position": "relative",
                            "margin": "none",
                            "color": "#87cefa",
                            "offsetStart": "xs",
                            "offsetEnd": "none"
                            }
                        ],
                        "flex": 0
                        }
                    } #貼進來
    )
    line_bot_api.reply_message(ReplyToken, flex_message)


