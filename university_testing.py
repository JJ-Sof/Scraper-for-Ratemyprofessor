import time
import requests
import random
from bs4 import BeautifulSoup

universities = ["Abraham Baldwin Agricultural College", "Agnes Scott College", "Albany State University", "American InterContinental University-Atlanta", "Andrew College", "Atlanta Metropolitan State College", "Atlanta's John Marshall Law School", "Augusta University", "Berry College", "Beulah Heights University", "Brenau University", "Brewton-Parker College", "Chamberlain University-Georgia", "Clark Atlanta University", "Clayton  State University", "College of Coastal Georgia", "Columbia Theological Seminary", "Columbus State University", "Covenant College", "Dalton State College", "DeVry University-Georgia", "East Georgia State College", "Emmanuel College", "Emory University", "Fort Valley State University", "Georgia College & State University", "Georgia Gwinnett College", "Georgia Highlands College", "Georgia Institute of Technology-Main Campus", "Georgia Military College", "Georgia Southern University", "Georgia Southwestern State University", "Georgia State University", "Gordon State College", "Herzing University-Atlanta", "Interdenominational Theological Center", "Kennesaw State University", "LaGrange College", "Life University", "Luther Rice College & Seminary", "Mercer University", "Middle Georgia State University", "Morehouse College", "Morehouse School of Medicine", "National American University-Kings Bay", "Oglethorpe University", "Paine College", "Piedmont University", "Point University", "Reformed University", "Reinhardt University", "Savannah College of Art and Design", "Savannah State University", "Shorter University", "South Georgia State College", "South University-Savannah", "South University-Savannah Online", "Spelman College", "Strayer University-Georgia", "The Art Institute of Atlanta", "Thomas University", "Toccoa Falls College", "Truett McConnell University", "University of Georgia", "University of North Georgia", "University of Phoenix-Georgia", "University of West Georgia", "Valdosta State University", "Wesleyan College", "Young Harris College"]
university_ids = [0] * len(universities)

for uni_index, uni in enumerate(universities):
    for id in range(1, 10000):  
        url = f"https://www.ratemyprofessors.com/school/{id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title_tag = soup.find('div', class_='HeaderDescription__StyledTitleName-sc-1lt205f-1 eNxccF')
                if title_tag:
                    title = title_tag.text.strip()
                    if uni.lower() in title.lower():
                        university_ids[uni_index] = id  
                        break
        except requests.RequestException as e:
            print(f"Request failed for ID {id}: {e}")
        time.sleep(random.uniform(1, 5))

for i, uni in enumerate(universities):
    print(f"University: {uni}, ID: {university_ids[i]}")
