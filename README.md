# 2020 COVID-19 HealthHack Submission: CrowdCount

### Authors:
- Jordan Phillips -- jmp2291@columbia.edu
- Shomik Ghose -- sg3789@columbia.edu
- Austin Tao -- alt2177@columbia.edu

### Project Details:
- DevPost submission to the COVID Hackathon II can be found here: [Insert URL Here]
- A video demonstration of the project can be found here: [Insert YouTube URL Here]
- If you wish to demo the project, please view the requirements.txt

### Project Overview:
CrowdCount is a brand-new project created for the COVID Hackathon II hosted by the Stevens
Venture Center. This site utilizes state-of-the-art computer vision to track the number of
people entering and exiting an establishment and updates a database in real-time, allowing business
owners to get a live feed of how busy their location is. Not only would this enable earlier
re-opening for businesses, but it would also create an environment that is safe for owners,
workers, and patrons alike. Additionally, CrowdCount offers an easy-to-use, search-based
website that allows members of the public to see both real-time and daily average data for
crowd sizes at establishments of their choice.

Our team developed CrowdCount over the course of 9 days, including frontend development with HTML/CSS, backend development with Django, SQLite databases, and our own custom API, and open-source computer vision software using OpenCV. Even though our team members were spread out across the continental U.S., we used collaborative tools such as GitHub and Slack in order to effectively communicate and produce a polished, working product.

Though we're extremely proud of the work we've done, we understand that CrowdCount, in its current state, is only the beginning of adjusting to life post-COVID-19. For the future, we hope to make our website more interactive and include robust visualizations of our data in order to provide even more to the public. We hope to create a weekly reporting system that we can provide to businesses so that they can track changes in their crowd size over time and plan for days of the week that are busier on average.

Additionally, we hope to begin integrating CrowdCount into our daily lives. One important area of us students’ lives that we feel that CrowdCount can specifically impact is university buildings — if universities can carefully monitor the number of people in a lecture hall or library, they will be more confident in their ability to protect students from COVID-19 and can accelerate the timeline of students returning to campus and receiving a high-quality education.

### Directory Setup
## compvis
Contains computer vision code allowing for remote cameras to update the data in our databases.
## Frontend
Contains the raw html/css/js that was ported into the Django templates under HealthHack
## HealthHack
Contains the django web application for this Project.
To run this project, make sure that django, and python are installed on your system.
Then, navigate to the HealthHack folder in your commandline and run python manage.py runserver
