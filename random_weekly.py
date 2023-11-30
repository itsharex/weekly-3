"""
    Created by howie.hu at 2022-05-10.
    Description: 根据历史数据生成周刊
    Changelog: all notable changes to this file will be documented
"""
import os
import sqlite3

W_HEADER = """# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。

"""
W_FOOTER = """
## ✍️ 说明

- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[weekly.howie6879.com](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)
- [FRE123-Free Resource for Everyone](https://www.fre123.com/)：利用周刊收集的资源，为非极客用户群体减少信息差👉 [FRE123|老胡周刊免费资源之启动篇](https://mp.weixin.qq.com/s/6El2AW93K4RiEHhma3vVPg)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。
"""


def gen_weekly():
    """
    基于历史数据，生成回顾周刊
    """
    db_file = os.path.join(os.path.dirname(__file__), "weekly.db")
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # 查询
    full_content = W_HEADER
    for each in ["🎯 项目", "🤖 软件", "👀 资料", "🕸 网站"]:
        full_content += f"\n## {each} \n"
        res = cursor.execute(
            f"SELECT item_content FROM 'items' WHERE item_type='{each}' ORDER BY random() LIMIT 3 ;"
        )
        for item in res.fetchall():
            item_content = item[0]
            full_content += f"\n### {item_content} \n"
    full_content += W_FOOTER
    with open("./docs/recommend/index.md", "w", encoding="utf-8") as f:
        f.write(full_content)
    # 退出
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    gen_weekly()
