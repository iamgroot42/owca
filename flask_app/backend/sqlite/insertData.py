import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_instructor(conn, instructor):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO instructors(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, instructor)
    conn.commit()
    return cur.lastrowid

def create_course(conn, course):
    sql = ''' INSERT INTO courses(instructor_id, name, description)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, course)
    conn.commit()
    return cur.lastrowid

def create_announcement(conn, announcement):
    sql = ''' INSERT INTO announcements(course_id, title, text, timestamp)
              VALUES(?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, announcement)
    conn.commit()
    return cur.lastrowid

def create_assignment(conn, assignment):
    sql = ''' INSERT INTO assignments(course_id, name, description, assignment_link)
              VALUES(?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, assignment)
    conn.commit()
    return cur.lastrowid


def insert_instructors(conn):
    instructor = ('Seongkook Heo',);
    instructor_id = create_instructor(conn, instructor)

def insert_courses(conn):
    course = (1, 'CS 6501: Human-Computer Interaction', 'This HCI course is designed for graduate students to learn how to conduct HCI research. You will learn how to formulate problems into research questions, how to do a literature review, and design and conduct user studies. You will read, present, and discuss state-of-art and classic papers. And ultimately, you will conduct an HCI research project to solve a usability problem as a team.')
    create_course(conn, course)

def insert_announcements(conn):
    announcements = [
        (1, 'Meeting password is hci', 'Zoom meeting password is hci', '2020-08-26 17:03:09.123'),
        (1, 'HCI Problems are now online', """Hi all, 

Thanks for submitting very interesting HCI problems!

Now it's time for you to take a look at them and find the one that you'd like to work on this semester. 

The list is here: https://docs.google.com/spreadsheets/d/15Jmj02rzAuzn3Y03aCK3F3JRtIgssSO56FLl1qRaBX8/edit?usp=sharing

Please

Read all of them before tomorrow's class
Put your name next to the problem that you're interested in (At least one, up to 3 problems)
You'll be able to change your choice during tomorrow's class. 

 

Seongkook""", '2020-09-08 14:38:09.123'),
        (1, 'HCI Proposal Presentation Order', """Hi all,

I hope you are all having a nice weekend. Here’s the presentation order for Monday.

Order	Team Number	Team Name	Members
1	3	Remote ATM Interaction Using Cellular Devices	Bingxu Li (bl2qu), William Wong (ww5zf), Mengyu Gong (mg7dy), Liwei Guo (lg8sp)
2	7	Small Business Helper	Jianqiang Chen (jc3ze), Ze Liu (zl8vx), Peng Wang (pw7nc), Jie Fan (jf6wt)
3	1	OWCA	Anshuman Suri (as9rw), James Ku (jk2mf), Kamya Desai (kd4wa), Nidhi Manu (nm4hf), Rakshita Kaulgud (rrk7pb)
4	2	DoItLater	Dexuan Zhang (dz5se), Hongyi Li (hl9fh), Leizhen Shi (ls2gc), Minjie Tang (mt7nk), Shilin Yan (sy8cd)
5	4	Titans	Sanchit Sinha (ss7mu), Gaurav Jindal (gj3bg), Arijit Pande (ap6bd), Rishab Bamrara (rb6xj), Akhila Ranga (ar8aq), Akhil Peddireddy (ap3ub)
6	6	Pryocted	Hannah Chen (yc4dx), Sanxing Chen (sc3hn), Jiajia Liang (jl9pg), Aidan San (aws9xm), Stephanie Schoch (sns2gr)
7	5	University Virtual Affairs	Ryan Kann (rak3me), Andrew Jackman (aj6eb), Archana Narayanan (an2adv), Hemanthkumar Goalla (hg6va), Adil Rahman (ar9fb)
Each team has 10 minutes, and you may send me the video to play if you cannot join in person.

 

During tomorrow’s session, we will use the following document for giving feedback:
https://docs.google.com/document/d/1H-ZmLiuvjnUvFZ1hBJyy5MwGy8gLx4RK74ria5SH8b8/edit?usp=sharing

 

Look forward to your presentation! :)

Seongkook""", '2020-09-27 13:45:09.123'),
        (1, 'Breadth area of this course', """Hi,

I recently heard about a concern regarding the breadth area of this course, so I wanted to clarify that. 

This course falls under "Cyber Physical Systems, Internet of Things, Embedded Systems".

If you started before Fall 2020, you may have different breadth area requirements. While this course falls under "Application Systems" in the previous version of breadth requirements, you may choose to fulfill the new breadth requirement instead of the previous requirements. 

If you have issues regarding the breadth area, please let me know so that we can discuss possible ways to deal with it. 

 

Best,
Seongkook""", '2020-10-05 18:45:09.123'),
        (1, 'Some announcements from today\'s class', """First, I want to apologize for the bad internet connection. I'll make sure to have a good connection. Slides are online now. 

Topic Presentation

* Each team will have two or three members

* Topic sign-up is due tonight. If you don't sign up by tonight, you'll be assigned to a topic with fewer members

* It's a first-come, first-serve. If you're interested in a topic but it's full, then write your computing id in the waitlist and move back when there's a space.

* First two teams presenting on Oct 26 will get bonus points of 0.5

Formative study

* This is the assignment 2, and it's for your project.

* You should find participants who are part of your target group and conduct individual interviews or a group interview.

Assignment 1

* Your grade for assignment 1 should now be online. Check it and let TA or me know if there's an issue. 

* We will review this on Wednesday

 

Thanks all, have a nice evening. """, '2020-10-12 18:32:09.123'),
        (1, 'Progress presentation order', """Hi all, 

Here's the randomly generated progress presentation order:

10/19 (Mon)

4, 3, 6, 2

10/21 (Wed)

5, 1, 7

 

If you have any issues presenting on the assigned day, please let me know. 

Seongkook""", '2020-10-13 22:12:09.123'),
        (1, 'Class video location', """Good morning!

Yesterday's class recording is moved from "Online Meetings" to "Lecture Capture", because it needed some edits and Zoom+Collab integration does not allow uploading of edited video. 

Automatic Zoom recordings may have your video or screen in an unwanted way. If you are concerned about any parts of the recordings and want it to be removed, please feel free to reach out to me. 

 

Seongkook""", '2020-10-20 22:15:09.123'),
        (1, 'Topic Presentation Update', """Hi all,

Thanks for the presentation yesterday. I want to make some changes to our topic presentation to facilitate more discussions.

First, let’s keep the presentation to be a bit shorter, to be 30 minutes max.
Second, let’s use Slack channel #topic-discussion for questions and discussions, instead of Zoom Chat.
By doing so, we can keep having discussions after the class, and those watching the recorded video can also join the conversation.

I know you have a lot to do at this time of the semester, and some of you have other difficulties attending live lectures, but if you could, I would recommend you to join classes live and participate in discussions. I’m sure that it’ll be more fun to see and participate in the discussion (even offline on Slack) than just watching the recorded presentation.

 

Thanks, 
Seongkook""", '2020-10-27 11:00:09.123'),
    ]
    for announcement in announcements:
        create_announcement(conn, announcement)

def insert_assignments(conn):
    # course_id, name, description, assignment_link
    assignments = [
        (1, 'Reading Response 1', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/2ba655aa-f3e7-445a-90db-67be9187791d/e7def6b6-4c70-46b4-a48c-44688d94c494&sakai_action=doView_grade'),
        (1, 'Find an HCI problem', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/41ea1f05-9f5e-406e-8e33-f440e02cb74e/d4f0e8d6-a087-4733-b0a8-b640eae190bc&sakai_action=doView_grade'),
        (1, 'Reading Response 2', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/7c8d089e-f843-4452-bc92-8e8b841170bb/1ba0d8c2-61a1-47ad-b22f-88e8b0974a60&sakai_action=doView_grade'),
        (1, 'Team Formation Report', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?assignmentReference=/assignment/a/b69a0900-b4b4-41de-b8c2-21a864b70229/cef7bf2f-5976-42a7-8b0b-51f1a8ea4d4e&sakai_action=doView_submission'),
        (1, 'Reading Response 3', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/599c9ffe-9548-453a-a03e-f58cc4295419/d17f8f86-db37-4b1f-b401-26e284496d89&sakai_action=doView_grade'),
        (1, 'Project Proposal', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/4a1ff022-c950-4dbb-bac9-b97150d5ba57/e1b80db5-ca9f-45a4-9c1b-2b6ea2047aa2&sakai_action=doView_grade'),
        (1, 'Assignment 1: Quantitative Evaluation', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/57072bf9-576e-4d4c-9ba0-c236d6005854/43a407ff-8579-43a1-ae17-a840ff290675&sakai_action=doView_grade'),
        (1, 'Topic Presentation Sign Up', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?assignmentReference=/assignment/a/b69a0900-b4b4-41de-b8c2-21a864b70229/ec426073-b1d8-40a9-bcc8-8751477129ae&sakai_action=doView_submission'),
        (1, 'Reading Response 4', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/2c0eec27-ddbd-451c-bcc5-bc491c2343a9/43ab7c0f-f2ea-4e15-b129-23fb55f703a8&sakai_action=doView_grade'),
        (1, 'Assignment 2: Formative Study', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/d08bc45f-912a-434d-84e1-b0001737ebac/923b6490-d0ad-4882-80b3-939db8256e91&sakai_action=doView_grade'),
        (1, 'Project Progress Report', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/8ff8c80e-f69d-44b8-ab8c-0f2ba7a35ffa/736cadcd-9e23-4cb2-9733-97d33b001a9e&sakai_action=doView_grade'),
        (1, 'Reading Response 5: Based on Topic Presentation List T1/T2', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/c03e1666-ef08-487f-b11e-0bb76b75e943/aa424436-c330-4810-a94d-54aeb950e23e&sakai_action=doView_grade'),
        (1, 'Reading Response 6: Based on Topic Presentation List T3/T4', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/0f6231f5-f453-4a30-9e09-3ba6dc2a839b/c77ec38e-de4e-47b2-900f-7bd28951ba9d&sakai_action=doView_grade'),
        (1, 'Reading Response 7: Based on Topic Presentation List T5/T6', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?submissionId=/assignment/s/b69a0900-b4b4-41de-b8c2-21a864b70229/f38cfcbb-1d3f-4c82-9b04-25f61af58ca9/d6376eca-2eed-491d-966b-cf9a981714dd&sakai_action=doView_grade'),
        (1, 'Reading Response 8: Based on Topic Presentation List T7/T8', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?assignmentReference=/assignment/a/b69a0900-b4b4-41de-b8c2-21a864b70229/0be88aa6-168a-44fe-91f7-5b0db3b68a18&sakai_action=doView_submission'),
        (1, 'Reading Response 9: Based on Topic Presentation List T9/T10', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?assignmentReference=/assignment/a/b69a0900-b4b4-41de-b8c2-21a864b70229/59952799-88df-44dd-a461-7a6cf6c0cf5e&sakai_action=doView_submission'),
        (1, 'Reading Response 10: Based on Topic Presentation List T11/T12', '', 'https://collab.its.virginia.edu/portal/site/b69a0900-b4b4-41de-b8c2-21a864b70229/tool/c2e78b95-f0ab-4b6a-a6f3-c0d67ff7924d?assignmentReference=/assignment/a/b69a0900-b4b4-41de-b8c2-21a864b70229/3acae051-552c-4fbe-ab2a-35c88383e360&sakai_action=doView_submission'),

    ]
    for assignment in assignments:
        create_assignment(conn, assignment)




def main():
    database = r"sqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        insert_instructors(conn)
        insert_courses(conn)
        insert_announcements(conn)
        insert_assignments(conn)

        # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)


if __name__ == '__main__':
    main()