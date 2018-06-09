from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://internshala.com/internships/computer%20science-internship"
furl = urlopen(url)
html = furl.read()
furl.close()

filename = 'internships.csv'
f = open(filename,'w')

headers = "Internship_Name, Company, Location, Start_Date, Duration, Stipend, Posted_On, Last_Date\n"
f.write(headers)

soup = BeautifulSoup(html,'html.parser')

containers =  soup.findAll('div',{'class':'container-fluid individual_internship '})
for container in containers:
    info = container.findAll('a')
    Internship_Name = info[0].text.strip()
    Company = info[1].text.strip()
    Location = info[2].text.strip()
    info = container.findAll('td')
    start_date = info[0].text.strip()
    duaration = info[1].text.strip()
    stipend = info[2].text.strip()
    posted_on = info[3].text.strip()
    last_date = info[4].text.strip()
    #print(Internship_Name)
    #print(Company)
    #print(Location)
    #print(start_date)
    #print(duaration)
    #print(stipend)
    #print(posted_on)
    #print(last_date)
    #print()
    #print()
    f.write (Internship_Name + "," + Company.replace(',','|') + "," +  Location.replace(',','|') + "," + start_date + "," +  duaration + "," + stipend + "," + posted_on + "," + last_date + "\n")
