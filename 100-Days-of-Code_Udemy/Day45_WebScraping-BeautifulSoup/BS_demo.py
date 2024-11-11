from bs4 import BeautifulSoup
import requests

# # Beautiful Soup demo
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")  # CSS Selector, a tag inside a p tag
# print(company_url)
#
# name = soup.select_one(selector="#name")  # CSS Selector, id
# print(name)
#
# headings = soup.select(".heading")  # CSS Selector, class
# print(headings)


# Scraping Y Combinator Hacker News (https://news.ycombinator.com)
response = requests.get("https://news.ycombinator.com")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

articles = soup.select(selector=".titleline a")
article_texts = [x.getText() for x in articles]
article_links = [x.get("href") for x in articles if x.find(class_="sitestr") is None]
article_upvotes = [int(x.getText().split()[0]) for x in soup.select(selector=".score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvotes_index = article_upvotes.index(max(article_upvotes))

print(article_texts[max_upvotes_index])
print(article_links[max_upvotes_index])
print(article_upvotes[max_upvotes_index])
