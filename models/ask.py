from models import mongo_client

ask_db = mongo_client['ask']


def get_questions(roll):
    return ask_db.find_all({})


def ask_question(roll, question_data):
    try:
        ask_db.insert_one(question_data)
    except Exception as e:
        print(f"Error/ask_question: {e}")


def answer_question(answer_data):
    try:
        ask_db.update_one(
            {"_id": answer_data['question_id']},
            {"$set": {
                "answer": answer_data['answer'],
                "respondent": answer_data['respondent']
                }
            }
        )
    except Exception as e:
        print(f"Error/answer_question: {e}")
