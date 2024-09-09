import requests
from bs4 import BeautifulSoup
import re

# URL of the professor's page
url = "https://www.ratemyprofessors.com/professor/654997"

# Send an HTTP request to fetch the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the professor's name
    name_tag = soup.find('div', class_='NameTitle__Name-dowf0z-0 cfjPUG')
    
    if name_tag:
        # Get all span tags within name_tag
        name_spans = name_tag.find_all('span')
        # Combine the texts of the spans to form the full name
        full_name = ' '.join(span.text.strip() for span in name_spans)
        # Split the full name into first and last names
        name_parts = full_name.split()
        first_name = name_parts[0] if len(name_parts) > 0 else "N/A"
        last_name = name_parts[1] if len(name_parts) > 1 else "N/A"
    else:
        first_name = "N/A"
        last_name = "N/A"

    # Extract the department and university
    title_tag = soup.find('div', class_='NameTitle__Title-dowf0z-1 iLYGwn')
    
    if title_tag:
        department_tag = title_tag.find('a', class_='TeacherDepartment__StyledDepartmentLink-fl79e8-0 iMmVHb')
        department = department_tag.text.strip() if department_tag else "N/A"
        
        # Extract the university text
        university_tag = title_tag.find_all('a', href=True)[-1]
        university = university_tag.text.strip() if university_tag else "N/A"
    else:
        department = "N/A"
        university = "N/A"

    # Extract the numerator and denominator for the rating
    numerator_tag = soup.find('div', class_='RatingValue__Numerator-qw8sqy-2 liyUjw')
    denominator_tag = soup.find('div', class_='RatingValue__Denominator-qw8sqy-4 UqFtE')
    
    # Combine the numerator and denominator
    rating_numerator = numerator_tag.text.strip() if numerator_tag else "N/A"
    rating_denominator = denominator_tag.text.strip() if denominator_tag else "N/A"
    
    # Format the rating
    overall_rating = f"{rating_numerator}{rating_denominator}" if rating_numerator != "N/A" and rating_denominator != "N/A" else "N/A"

    # Extract the number of ratings
    num_ratings_tag = soup.find('div', class_='RatingValue__NumRatings-qw8sqy-0')
    num_ratings_text = num_ratings_tag.text.strip() if num_ratings_tag else "N/A"
    # Use regular expression to extract the numeric part
    num_ratings_match = re.search(r'\d+', num_ratings_text)
    num_ratings = num_ratings_match.group(0) if num_ratings_match else "N/A"

    # Extract the courses
    course_tags = soup.find_all('div', class_='RatingHeader__StyledClass-sc-1dlkqw1-3 eXfReS')
    courses = [course_tag.text.strip() for course_tag in course_tags]
    # Remove duplicates by converting to a set and back to a list
    unique_courses = list(set(courses))
    list_of_courses = ', '.join(unique_courses) if unique_courses else "N/A"

    #Extract the difficulty
    ease_levels = soup.find_all('div', class_='FeedbackItem__FeedbackNumber-uof32n-1 kkESWs')
    ease_checks = [ease_level.text.strip() for ease_level in ease_levels]
    take_again_text = ease_checks[0] if ease_checks[0] else "N/A"
    diff_level_text = ease_checks[1] if ease_checks[1] else "N/A"

    #Extract the reviews
    reviews_tags = soup.find_all('div', class_='Comments__StyledComments-dzzyvm-0 gRjWel')
    reviews = [review_tag.text.strip() for review_tag in reviews_tags]

    # Print the extracted information
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Department: {department}")
    print(f"University: {university}")
    print(f"Overall Rating: {overall_rating}")
    print(f"Number of Ratings: {num_ratings}")
    print(f"Courses: {list_of_courses}")
    print(f"Would take again: {take_again_text}")
    print(f"Difficulty level: {diff_level_text}")
    print(f"Reviews: {reviews}")
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
