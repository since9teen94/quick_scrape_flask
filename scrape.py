import requests
from bs4 import BeautifulSoup

URL = "https://ptable.com/?lang=en#Properties"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table_elements = soup.find(id="Ptable")
elements = table_elements.find_all("li")

elems = []

for element in elements[2:]:

    class_element = element.attrs.get("class")
    a_num_element = element.find("b").text.strip()
    abb_element = element.find("abbr").text.strip()
    name_element = element.find("em").text.strip()
    weight_element = element.find("data").text.strip()

    new_element = [a_num_element, abb_element, name_element, weight_element, class_element]
    elems.append(new_element)

if __name__=='__main__':
    print(elems)