### How to run the app. 

<<<<<<< HEAD
1. move to the src folder in mail_server. 
2. Run the flask app -- python app.py


### Example rest call to the end point exposed
curl -X POST -H "Content-Type: application/json" -d '{"recipient": "abcdexample@virginia.edu", "title": "Reading Response 9 based on Topic Presentation List T9 or T10", "content": "Reading response for Nov 9 topic presentations Choose one from the following four papers"}' http://0.0.0.0:5050/send-mail
=======
1. Run the flask app -- python app.py


### Example rest call to the end point exposed
curl -X POST -H "Content-Type: application/json" -d '{"recipient": "abcdex@virginia.edu", "title": "Reading Response 9 based on Topic Presentation List T9 or T10", "content": "Reading response for Nov 9 topic presentations Choose one from the following four papers"}' http://0.0.0.0:5050/send-mail
>>>>>>> 5b23d2031e2b28eb21cdee983774819fee7cb0e8

