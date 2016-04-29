#!/usr/bin/python
# -*- coding: utf-8 -*-

# Wikipediaから記事をパースする

import argparse
import bz2
import xml.etree.ElementTree as ET


def get_page(wiki_file):
    u'''ファイルから<page>〜</page>の文字列を取り出す

    Wikipediaのページの形式
    <page>
        <title>記事のタイトル</title>
        ...
    </page>
    '''
    page_lines = []
    page_started, page_ended = False, False

    while not page_started:
        line = wiki_file.readline()
        if line == '':
            # readline()が空文字を返したら終了
            return False
        if line.find('<page>') != -1:
            page_started = True
            page_lines.append(line)

    while not page_ended:
        line = wiki_file.readline()
        if line.find('</page>') != -1:
            page_ended = True
        page_lines.append(line)

    return '\n'.join(page_lines)


def parse_wiki(input_path):
    u'''Wikipediaの圧縮ファイルをパースする'''
    # bz2形式の圧縮ファイルをオープン
    wiki_file = bz2.BZ2File(input_path)

    while True:
        # ページ単位でXML形式の文字列取得
        page_str = get_page(wiki_file)
        if not page_str:
            break

        # XMLをパースする
        root = ET.fromstring(page_str)

        # 例えば記事のタイトルを取得する場合
        # <title>記事のタイトル</title>
        title = root.find('title').text.encode('utf-8')
        print ("##")
        print title


if __name__ == '__main__':
    # コマンドライン引数をパース
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_path',
        help=u'Wikipediaの記事の圧縮ファイルのパス (例:jawiki-YYYYMMDD-pages-articles.xml.bz2'
    )
    args = parser.parse_args()
    # ファイルを読みだして記事ごとにパース
    parse_wiki(args.input_path)
