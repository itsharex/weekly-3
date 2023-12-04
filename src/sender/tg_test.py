"""
    Created by howie.hu at 2023-12-04.
    Description: 有时候发送失败，单独测试
    export http_proxy=http://0.0.0.0:1090;export https_proxy=http://0.0.0.0:1090;
    PIPENV_DOTENV_LOCATION=./dev.env pipenv run python ./src/sender/tg_test.py
    Changelog: all notable changes to this file will be documented
"""
import asyncio
import os

from src.sender.tg_utils import send_to_tg

data = {
    "text": "\n👉 名称：[weekly.fre123.com](https://weekly.fre123.com/)\n🤖 类型：🕸网站\n👏 介绍：\n",
    "image_link": "https://images-1252557999.file.myqcloud.com/uPic/weekly_fre123.jpg",
}


result = asyncio.run(
    send_to_tg(
        chat_id=os.getenv("TG_CHAT_ID"),
        text=data["text"],
        image_link=data["image_link"],
    )
)

if result["status"]:
    print("发送成功！")
