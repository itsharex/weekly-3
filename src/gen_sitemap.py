"""
    Created by howie.hu at 2023-01-18.
    Description: 爬取周刊网站生成周刊
    Changelog: all notable changes to this file will be documented
"""

import os

from pysitemap import crawler

SM_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs/sitemap.xml")


def gen_sitemap():
    """
    生成 sitemap
    """
    root_url = "https://weekly.howie6879.cn/"
    crawler(
        root_url,
        out_file=SM_FILE,
        exclude_urls=[".pdf", ".jpg", ".db", ".css", ".js", ".ico"],
    )


if __name__ == "__main__":
    gen_sitemap()
