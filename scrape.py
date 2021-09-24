import requests
from bs4 import BeautifulSoup

URL = "https://ptable.com/?lang=en#Properties"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table_elements = soup.find(id="Ptable")
elements = table_elements.find_all("li")

elems = []
arr =   [None,[],[],[],[],[]]
lanths = []
acts = []

for element in elements[2:]:

    class_element = element.attrs.get("class")
    a_num_element = element.find("b").text.strip()
    abb_element = element.find("abbr").text.strip()
    name_element = element.find("em").text.strip()
    weight_element = element.find("data").text.strip()

    new_element = [a_num_element, abb_element, name_element, weight_element, class_element]
    elems.append(new_element)

for x in range(16):
    elems.insert(1, arr)
for x in range(10):
    elems.insert(20, arr)
for x in range(10):
    elems.insert(38, arr)
for x in range(14):
    lanths.append(elems.pop(92))
for x in range(2):
    lanths.insert(0, arr)
    lanths.append(arr)
for x in range(14):
    acts.append(elems.pop(110))
for x in range(2):
    acts.insert(0, arr)
    acts.append(arr)

if __name__=='__main__':
    print(elems)