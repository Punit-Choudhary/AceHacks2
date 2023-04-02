from flask import Blueprint, request


import models.ask as ask_db


ask = Blueprint('sdnt', __name__)

@ask.route('/')
def ask_home():
    # return all questions
    questions = ask_db.get_questions()


@ask.route('/ask', methods=['POST'])
def ask_question():
    if request.method == 'POST':
          question_data = {
               "question": request.json['question'],
               "user": request.json['user'],
               "respondent": "",
               "answer": ""
          }

          

