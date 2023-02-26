"""
    Created by howie.hu at 2023-02-26.
    Description: 周刊工具函数模块
    Changelog: all notable changes to this file will be documented
"""

import requests
import os


def get_lxgwwenkai_font():
    """
    获取霞鹜文楷：https://github.com/lxgw/LxgwWenKai
    """
    file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "docs/statics/css/files"
    )

    base_url = "https://gw.alipayobjects.com/os/k/font/"
    for i in range(4, 120):
        full_url = f"{base_url}./files/lxgwwenkaiscreenr-subset-{i}.woff2"
        full_path = f"{file_path}/lxgwwenkaiscreenr-subset-{i}.woff2"
        content = requests.get(full_url).content

        if isinstance(content, str):
            continue
        else:
            print(full_url + "持久化成功!")
            with open(full_path, "wb") as fp:
                fp.write(content)


if __name__ == "__main__":
    get_lxgwwenkai_font()
