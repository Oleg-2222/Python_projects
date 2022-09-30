# pip install beatutifulsoup4, lxml
import re

from bs4 import BeautifulSoup

with open('C:\\Users\\User\\Desktop\\Python Jun\\pythonProject\\Parsing\\vk.html') as file:
    src = file.read()

# Создаем объект класса BS и передаем как параметры html-код и название парсера.
soup = BeautifulSoup(src, 'lxml')

# print(soup.find('div'))
# print(soup.findAll('div'))

# add_friend = soup.find('a', class_='friends_possible_link')
  # add_friend = soup.find('a', {'class': 'friends_possible_link'})
# print(add_friend.text.strip())

# friends = soup.findAll('a', class_='right_list_title right_list_title--name')
#
# for friend in friends:
#     print(friend.string)

# friends = soup.findAll('a', class_='right_list_title right_list_title--name')
#
# for friend in friends:
#     friend_name = friend.text
#     friend_url = friend.get('href')
#     print(f'{friend_name}: {friend_url}')

add_to_friend = soup.find_all(text=re.compile('([Дд]обавить в друзья)'))
add_to_friend_2 = soup.find_all(class_='right_list_field')

for add in add_to_friend_2:
    print(add.next_element.text.strip())
