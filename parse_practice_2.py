import requests
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://www.weblancer.net/jobs/'
#
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('index.html', 'w') as file:
#     file.write(src)

# with open('index.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_tasks_hrefs = soup.find_all(class_='text-bold')
#
# all_tasks_dict = {}
# for item in all_tasks_hrefs:
#     item_text = item.text
#     item_href = 'https://www.weblancer.net' + item.get('href')
#     all_tasks_dict[item_text] = item_href
#
# with open('all_tasks_dict.json', 'w') as file:
#     json.dump(all_tasks_dict, file, indent=4, ensure_ascii=False)

with open('all_tasks_dict.json') as file:
    all_tasks = json.load(file)


count = 0
for task_name, task_href in all_tasks.items():

    rep = ['-', ' ', '\'', ',']
    for item in rep:
        if item in task_name:
            task_name = task_name.replace(item, '_')

    req = requests.get(url=task_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{task_name}.html', 'w') as file:
        file.write(src)

    with open(f'data/{count}_{task_name}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # Проверка на наличие страницы.
    attr_error_block = soup.find(class_='page_content landing')
    if attr_error_block is None:
        continue

    customer_name = soup.find(class_='page_content landing').find('span', class_='name')
    customer_text = soup.find('div', class_='col-12 text_field').find('p')

    with open(f'data/{count}_{task_name}.csv', 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                'Задание',
                'Имя'
            )
        )

    task_info = []
    task_info.append(
        {
            'name': customer_name.text,
            'text': customer_text.text
        }
    )


    with open(f'data/{count}_{task_name}.csv', 'a', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                customer_text.text,
                customer_name.text
            )
        )

    with open(f'data/{count}_{customer_name.text}.json', 'a', encoding='utf-8') as file:
        json.dump(task_info, file, indent=4, ensure_ascii=False)

    count += 1