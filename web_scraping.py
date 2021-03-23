# 1st step install and import modules
    #-- pip/pip3 install lxml
    #-- pip/pip3 install requests
    #-- pip/pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_title = []
company_name = []
location_name = []
skills = []
links = []
salary = []

# 2st step use request to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# 3st step save page content/markup
src = result.content
# print(src)

# 4st step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# print(soup)

# 5st step find the elements containing info we need
#-- jop titles, jop skills, company names, location names
jop_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
location_names = soup.find_all("span", {"class":"css-5wys0k"})
jop_skills = soup.find_all("div", {"class":"css-y4udm8"})
s = soup.find_all("div", {"class":"css-1o5ybe7 e1581u7e0"})
print(s)
# 6st step loop over returned lists to extract needed info into other lists
for i in range(len(jop_titles)):
    jop_title.append(jop_titles[i].text)
    links.append(jop_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(jop_skills[i].text)

for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    salaries = soup.find("section", {"class":"css-3kx5e2"})
    salary.append(salaries)
    # print(salaries)

# 7st step create csv file and fill it with values
file_list = [jop_title, company_name, location_name, skills, links, salary]
exported = zip_longest(*file_list)
with open("/home/mahmoudaboelnaga/Desktop/developer/jop_tutorial.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Jop title", "Company name", "Location name", "Skills", "links", "Salary"])
    wr.writerows(exported)
# 8st step to fetch the link of the jop and fetch in page details