import requests
from bs4 import BeautifulSoup

# Quick scrape from ptable.com to find the basic information (atomic number, weight, name and abbreviation)
# so that we can render a basic periodic table

URL = "https://ptable.com/?lang=en#Properties"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table_elements = soup.find(id="Ptable")
# The needed information was stored in list items inside of the #Ptable element
elements = table_elements.find_all("li")

# arr is a list of None and empty lists for spacing the periodic table
arr =   [None,[],[],[],[],[]]
# separating out the lanthanides and actinides
elems = []
lanths = []
acts = []

# A for loop to attain the information we are seeking followed by some manipulations to
# make our grid spacing more like that of an actual periodic table
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

# Used for checking that desired information is being scraped
if __name__=='__main__':
    print(elems)