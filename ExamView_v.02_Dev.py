# ______________________________________________________
# v.01
import sys
import time
import re
from colorama import Fore
from canvasapi import Canvas
import urllib.request
import csv
import datetime


class Error (Exception):
    """Base class for other exceptions"""
    pass


class NoMatchHTML(Error):
    pass


class MissingHTMLBody(Error):
    pass


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

with open('apikeyinfo.txt', encoding='utf8') as apikeyinfo:
    for each in apikeyinfo:
        API_KEY = each

API_URL = "https://canvas.instructure.com"
# initialize a new canvas object
canvas = Canvas(API_URL, API_KEY)

# except NameError:
#     print('There is no key. Place your key in a file called: "apikey.txt" in the same folder as the program')
#     sys.exit()

print(Fore.LIGHTBLUE_EX + '******************************************************************')
print('* CanvasQuizCSVImport v.02 Creates MC Quizzes')
print('******************************************************************'+Fore.RESET)

with open('quizcontent.csv', newline='', encoding='utf8') as csvFile:
    data = csv.reader(csvFile, dialect='excel', delimiter=',')
    # creates a zip object of each 1st object in each row, etc.
    columns = zip(*data)
    # creates a dictionary of those tuples
    dataMap = {d[0]: d[1:] for d in columns}

# Counts the quiz questions based on whether there is data in the question
count = 0
for listItem in dataMap.keys():
    questionLookup = re.match(r'q\d{1,3}N', listItem)
    if questionLookup:
        listItem = dataMap.get(listItem)
        # print(listItem[0])
        if len(listItem[0]) > 0:
            count = count + 1
print(str('Creating ' + str(count) + ' MC Questions'))

course_id = ''.join(dataMap["course_id"])
title = ''.join(dataMap["title"])
description = ''.join(dataMap["description"])
time = ''.join(dataMap["time"])
points = ''.join(dataMap["q_Pts"])
course = canvas.get_course(course_id)
course_name = course.name

qt = datetime.datetime.now()
qt = qt.strftime("%m%d%Y_%H%M%S")
uniqueQuizTitle = title + ' ' + qt

print('For: ' + course_name + ' (' + str(course_id)+')')
print('Quiz: ' + uniqueQuizTitle)
print('Description: ' + description)
print('Time to complete: ' + time)
print('Points: ' + str(points))

course.create_quiz(quiz={'title': uniqueQuizTitle, 'description': description,
                         'time_limit': time, 'shuffle_answers': True,
                         'published': True, 'quiz_type': 'assignment'})

quizList = course.get_quizzes()
for quiz in quizList:
    qTitle = quiz.title
    if qTitle == uniqueQuizTitle:
        quiz_id = quiz.id
        # print(quiz_id)

course = canvas.get_course(course_id)
quiz = course.get_quiz(quiz_id)
title = quiz.title

###############################
# question #
###############################
while count > 0:
    count = str(count)
    q1N = ''.join(dataMap["q"+count+"N"])
    q_Pts = ''.join(dataMap["q_Pts"])
    q1c1 = ''.join(dataMap["q"+count+"c1"])
    q1c1_w = ''.join(dataMap["q"+count+"c1_w"])
    q1c2 = ''.join(dataMap["q"+count+"c2"])
    q1c2_w = ''.join(dataMap["q"+count+"c2_w"])
    q1c3 = ''.join(dataMap["q"+count+"c3"])
    q1c3_w = ''.join(dataMap["q"+count+"c3_w"])
    q1c4 = ''.join(dataMap["q"+count+"c4"])
    q1c4_w = ''.join(dataMap["q"+count+"c4_w"])

    quiz.create_question(question={'question_text': q1N,
                                   'question_type': 'multiple_choice_question',
                                   'points_possible': q_Pts,
                                   'correct_comments': 'Great Work!',
                                   'incorrect_comments': 'Im sorry thats not correct',
                                   'neutral_comments': 'Good Effort! You are on the right track.',
                                   'text_after_answers': 'Thank you for answering this question!',
                                   'answers[0][weight]': q1c1_w,
                                   'answers[0][answer_text]': q1c1,
                                   'answers[1][answer_text]': q1c2,
                                   'answers[1][weight]': q1c2_w,
                                   'answers[2][answer_text]': q1c3,
                                   'answers[2][weight]': q1c3_w,
                                   'answers[3][answer_text]': q1c4,
                                   'answers[3][weight]': q1c4_w})
    count = int(count)
    count = count - 1
