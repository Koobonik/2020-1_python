import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import warnings
from konlpy.tag import Okt
import pytagcloud
from collections import Counter

warnings.filterwarnings("ignore")
columns = ['title', 'category', 'content_text']
df = pd.DataFrame(columns=columns)
req = requests.get("https://namu.wiki/w/GTA%205/%EC%9D%B4%EB%8F%99%20%EC%88%98%EB%8B%A8")
html = req.content
soup = BeautifulSoup(html, 'lxml')
contents_table = soup.find(name="article")
title = contents_table.find_all('h1')[0]
category = contents_table.find_all('ul')[0]
content_paragraphs = contents_table.find_all(name="div", attrs={"class": "wiki-paragraph"})
content_corpus_list = []
if title is not None:
    row_title = title.text.replace("\n", " ")
else:
    row_title = ""

if content_paragraphs is not None:
    for paragraphs in content_paragraphs:
        if paragraphs is not None:
            content_corpus_list.append(paragraphs.text.replace("\n", " "))
        else:
            content_corpus_list.append("")
else:
    content_corpus_list.append("")

if category is not None:
    row_category = category.text.replace("\n", " ")
else:
    row_category = ""

row = [row_title, row_category, "".join(content_corpus_list)]
series = pd.Series(row, index=df.columns)
df = df.append(series, ignore_index=True)
print(df)

# asd
# df['title'] = df['title'].apply(lambda x: text_cleaning(x))
# df['category'] = df['category'].apply(lambda x: text_cleaning(x))
# df['content_text'] = df['content_text'].apply(lambda x: text_cleaning(x))
# df.head(5)
title_corpus = "".join(df['title'].tolist())
category_corpus = "".join(df['category'].tolist())
content_corpus = "".join(df['content_text'].tolist())
print("-----------------")
print(title_corpus)
nouns_tagger = Okt()
nouns = nouns_tagger.nouns(content_corpus)
count = Counter(nouns)
# print(count)

koean_stopwords_path = "./korean_stopwords.txt"
with open(koean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readline()
stopwords = [x.strip() for x in stopwords]
# print(stopwords[:10])
namu_wiki_stopwords = ['상위', '문서', '내용', '누설', '아래', '해당', '설명', '표기', '추가', '모든', '사용', '매우', '가장', '줄거리', '요소',
                       '상황', '편집', '틀', '경우', '때문', '모습', '정도',
                       '이후', '사실', '생각', '인물', '이름', '년월', '마냥', '마저', '양병', '것', '무려', '여기']
for stopword in namu_wiki_stopwords:
    stopwords.append(stopword)

remove_char_counter = Counter({x: count[x] for x in count if len(x) > 1})
print(remove_char_counter)



# 가장 출현 빈도수가 높은 40개의 단어를 선정합니다.
ranked_tags = remove_char_counter.most_common(40)
# pytagcloud로 출력할 40개의 단어를 입력합니다. 단어 출력의 최대 크기는 80으로 제한합니다.
taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
# print(taglist)
# # pytagcloud 이미지를 생성합니다. 폰트는 나눔 고딕을 사용합니다.
pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='NanumGothic', rectangular=False)
#
from IPython.display import Image

Image(filename='wordcloud.jpg')


def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    return result
