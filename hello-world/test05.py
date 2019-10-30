# モジュールのインポート
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

# 決まった文字入力で指定の返信をする
app = Flask(__name__)

Meat_List = {

    "にく" : "",
    "ニク" : "",
    "肉" : "",

    "おにく":"",
    "オニク":"",
    "お肉" : "",

    "やきにく" : "【肉屋の台所】\n＠都内某所\n黒毛和牛の食べ放題を堪能できるお店。\n" + "公式：https://nikuyanodaidokoro.com/\n" + "ホットペッパー：https://www.hotpepper.jp/gstr01224/SA11/",
    "ヤキニク" : "【肉屋の台所】\n＠都内某所\n黒毛和牛の食べ放題を堪能できるお店。\n" + "公式：https://nikuyanodaidokoro.com/\n" + "ホットペッパー：https://www.hotpepper.jp/gstr01224/SA11/",
    "焼肉": "【肉屋の台所】\n＠都内某所\n黒毛和牛の食べ放題を堪能できるお店。\n" + "公式：https://nikuyanodaidokoro.com/\n" + "ホットペッパー：https://www.hotpepper.jp/gstr01224/SA11/\n\n" +
            "【ホルモンまさる】\n＠東京：田町\nコスパ良く美味しい焼肉を堪能できるお店。\n" + "https://tabelog.com/tokyo/A1314/A131402/13150755/"

}

Seafood_List = {

    "さかな": "",
    "サカナ": "",
    "魚":"",

    "おさかな":"",
    "オサカナ":"",
    "お魚": "",

    "さしみ": "",
    "サシミ": "",
    "刺身":"",

    "おさしみ":"",
    "オサシミ":"",
    "お刺身":"",

    "かいせん":"",
    "カイセン":"",
    "海鮮":"",

    "すし":"",
    "スシ":"",
    "寿司":"",

    "おすし":"",
    "オスシ":"",
    "お寿司":""

}

Sweets_List = {

    "すいーつ":"",
    "スイーツ":"",
    "でざーと":"",
    "デザート":"",

    "あいす": "",
    "アイス": "",

    "かきごおり": "",
    "カキゴオリ": "",
    "かき氷": "",
    "カキ氷": "",

    "たぴおか": "",
    "タピオカ": "",

    "けーき": "",
    "ケーキ": "",

    "海鮮": "",
    "すし": "",
    "おすし": "",
    "スシ": "",
    "オスシ": "",
    "寿司": "",
    "お寿司": ""

}

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# データの受け渡し
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# text入力の条件分岐
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text in Meat_List:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Meat_List[event.message.text]))

    elif event.message.text in Seafood_List:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Seafood_List[event.message.text]))

    elif event.message.text in Sweets_List:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Sweets_List[event.message.text]))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="新しいお店かな？！リストに追加をお願いしよう！"))

# ここからスタート portの指定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)