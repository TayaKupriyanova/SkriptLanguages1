import requests
from bs4 import BeautifulSoup

"""
****************************************************************************
Это скрипт, который извлекает новости с ленты сайта "Томского времени",    *                                    *
а затем сохраняет в файл статьи конкретного автора:                        *
Загловок:                                                                  *
Аннотация:                                                                 *
Автор:                                                                     *
****************************************************************************
"""

f = open("articles_text.txt", 'w')

for p in range(1,10):
    url = f'https://tomsk-time.ru/news/page/{p}/'
    response = requests.get(url)
    print(response.ok)

    soup = BeautifulSoup(response.text, 'lxml')
    all_hrefs_articles = soup.find_all(class_='shortstory')
    for article in all_hrefs_articles:

        article_name = article.find(class_='link-style link-black')['title']
        print("Заголовок статьи: ",article_name)
        #f.write("Заголовок статьи: " + article_name + '\n')

        article_text = article.find("div",class_='shortstory__content-text').contents[1].text
        print("Аннотация: ", article_text)
        #f.write("Аннотация: " + article_text+ '\n')

        article_author = article.find(class_='shortstorytagsauthor').text.strip()
        if len(article_author)>1:
            print("Автор: ", article_author)
        else:
            print("Автор не указан")
        if article_author == "Павел Соловьёв":
            f.write("Заголовок статьи: " + article_name + '\n')
            f.write("Аннотация: " + article_text + '\n')
            f.write("Автор: "+ article_author+ '\n'+ '\n')
        print()

f.close()

