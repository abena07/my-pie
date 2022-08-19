from cgitb import text
from bs4 import BeautifulSoup
import requests

url ='https://www.ug.edu.gh/announcements/vacancies-national-service-personnel-20222023-academic-year'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
for length in soup.find_all("strong" ):
    print(length.get_text())


# def get_paragraphs(first_paragraph):
#     current_paragraph = first_paragraph
#     while True:
#         yield current_paragraph

#         current_paragraph = current_paragraph.find_next('p')
#         if not current_paragraph or (current_paragraph.strong and current_paragraph.strong.text.strip() != ''):
#             break

# for p in get_paragraphs(soup.select_one('strong:contains("Deadline")')):
#     print(p)