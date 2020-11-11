import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import asyncio

from backend.db import init_db
from datetime import datetime, timedelta


def prepare_messages(users, course, assignment, picked):
   titles     = []
   bodies     = []
   receipents = []

   for user in users:
      body = ["Hi %s," % user.name]
      body += [""]
      body += ["This is a reminder for your deadline %s" % assignment.title]
      
      # If due in an hour and this reminder not sent so far
      if (assignment.due_date - datetime.now()) <= timedelta(seconds=60*60):
         if picked == 1:
            body += ["Due <b>in less than one hour</b>"]
            picked -= 1 # Don't re-send reminders
      elif (assignment.due_date - datetime.now()) <= timedelta(seconds=5 * 60*60):
         if picked == 2:
            body += ["Due <b>in less than five hours</b>"]
            picked -= 1 # Shift to above level
      # If due today and this reminder not sent so far
      elif (assignment.due_date - datetime.now()) <= timedelta(days=1):
         if picked == 3:
            body += ["Due <b>in less than 24 hours</b>"]
            picked -= 1 # Shift to above level
      
      # Add assignment description if available
      if len(assignment.description) > 0:
         body += ["Here's the assignment description:"]
         body += [assignment.description]
   
      # Don't add extra space
      if len(assignment.attachments) > 0 or len(assignment.upload_link) > 0:
         body += [""]

      # Add attachment link if exists
      if len(assignment.attachments) > 0:
         body += ['Click <a href="%s">here</a> to see more information for this deadline' % (assignment.attachments)]

      # Add upload link if exists
      if len(assignment.upload_link) > 0:
         body += ['Click <a href="%s">here</a> to submit this deadline' % assignment.upload_link]
      
      # Sign off
      body += [""]
      body += ['Cheers!']
      body += ['OWCA']

      assgt_title = assignment.title
      if len(assignment.title) > 15: assgt_title = assgt_title[:15] + "..."

      titles.append("[%s] [Deadline Reminder : %s]" % (course.course_name, assgt_title))
      bodies.append("<br>".join(body))
      receipents.append("%s@virginia.edu" % user.alias)
   
   return titles, bodies, receipents, picked


def make_mapping(course_objs):
   mapping = {c:([], []) for c in course_objs.keys()}
   for c, co in course_objs.items():
      # Check deadlines
      assignments = co.get_assignments()
      # Filter out the ones that have passed
      picked = [x for x in assignments if x.due_date >= datetime.now()]

      levels = []
      for p in picked:
         if (p.due_date - datetime.now()) <= timedelta(seconds=60*60):
            levels.append(1)
         elif (p.due_date - datetime.now()) <= timedelta(seconds=5 * 60*60):
            levels.append(2)
         else:
            levels.append(3)

      # Add information to mapping
      mapping[c] = (picked, levels)
   return mapping


def done_with_courses(course_objs, user_objs, IDENTITY, PASSWORD, mapping):
   for c, asgts in mapping.items():
      
      # Get students enrolled in this course
      concerned = []
      for u in user_objs.values():
         if c in u.courses:
            concerned.append(u)
      
      # Get assignments and levels
      assignments, levels = asgts
      # Filter and pick the ones due today
      picked = []
      lvls   = []
      for i, x in enumerate(assignments):
         if (x.due_date - datetime.now()) <= timedelta(days=1):
            picked.append(x)
            lvls.append(i)

      to_send = []
      # Send out an email for each assignment
      for i, pick in enumerate(picked):
         current_level = levels[lvls[i]]
         titles, bodies, receipents, after_level = prepare_messages(concerned,
                              course_objs[c], pick, current_level)
         # To be sent only if level change
         if after_level == current_level:
            to_send.append(False)
         else:
            to_send.append(True)
         # Update new level
         mapping[c][1][lvls[i]] = after_level

         # Send out these emails
         for ts, t, b, r in zip(to_send, titles, bodies, receipents):
            # Send email onyl if level changes
            if ts: send_email(IDENTITY, PASSWORD, r, t, b)


def send_email(IDENTITY, PASSWORD, receiver_address, subject, body):
   #Setup the MIME
   message = MIMEMultipart()
   message['From'] = IDENTITY
   message['To'] = receiver_address
   message['Subject'] = subject
   #The body and the attachments for the mail
   message.attach(MIMEText(body, 'html'))
   #Create SMTP session for sending the mail
   session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
   session.starttls() #enable security
   session.login(IDENTITY, PASSWORD) #login with mail_id and password
   text = message.as_string()
   session.sendmail(IDENTITY, receiver_address, text)
   session.quit()
   print("Mail sent!")


if __name__ == '__main__':
   # Read data from Excel Sheet
   EXCEL_FILE_PATH = os.path.join("backend", "data", "hci_data.xlsx")
   #The mail addresses and password
   IDENTITY = 'hcifall2020@gmail.com'
   PASSWORD = 'SuperSecure!!!'

   # Load data from excel sheet
   (course_objs, user_objs, _) = init_db(EXCEL_FILE_PATH)

   # Get mapping of courses and their assignments, along with how many reminders have been sent out
   mapping = make_mapping(course_objs)

   def course_sender():
      return done_with_courses(course_objs, user_objs,
                  IDENTITY, PASSWORD, mapping)

   async def periodic():
      while True:
         course_sender()
         # Sleep 30 minutes
         await asyncio.sleep(60 * 30)

   loop = asyncio.get_event_loop()
   task = loop.create_task(periodic())

   try:
       loop.run_until_complete(task)
   except asyncio.CancelledError:
       pass
