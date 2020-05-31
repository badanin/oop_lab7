from parse import Parse
# Исходная страница
url = "http://yandex.ru"

# получаем ссылки первого уровня
links = Parse.get_content(None, url)
for link in links:
    print("=================================")
    print("- " + link[1] + " - " + link[0])

    # Получаем ссылки второго уровня
    l2 = Parse.get_content(None, link[0])
    for lnk in l2:
        print("--- " + lnk[1] + " - " + lnk[0])
