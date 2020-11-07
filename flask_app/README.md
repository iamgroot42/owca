## On windows (PowerShell)

`$env:FLASK_APP = "backend"`
`$env:FLASK_ENV = "development"`
`flask init-db`
`flask run`

=====================
SCHEMA

course: 

"id": "hci",
"instructor": "tomato",
"tas": ["avocado"],
"description": "dummy HCI course go brr   --- add days of the week ",
"days of week" : " < eg mon, tue "
"time": "" 
"meetings": "< upcoming class zoom link> "
"schedule": < link to schedule page >
"syllabus": "" - link to syllabus page
"course_site": "www.hci.com"

instructor_office_hour_link : " < zoom link > "

- Authentation: 
"id": ""
"password: ""

- UserInfo: 

"id": ""
"name": ""
"courseList": [] # list of course ids

-Resources 
""

- assignments

assignment id 
course id
title
description
due date
max score
submission link
attachements

- announcements
course id: 
Annoucement id:
Announcement title
announcement description
link: 

notification ?? 
