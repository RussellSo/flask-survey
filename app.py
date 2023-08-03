from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey
app = Flask(__name__)
from flask_debugtoolbar import DebugToolbarExtension
app.config["SECRET_KEY"] = "secretdog"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
import pdb



#1 play with class in ipython
#2 create app start page - create a data list
#3 link to question page - id or maybe index will be dynamic in url as we iterate over
#3a every question page should have yes/no radio buttons and text that dynamically puts choices
#3b ?? submitting form should: fire a post request to /answer, then redirect to next iterated question??
#3c submitting form should also pend to global data list.
#4 IF: we reach end of list/ no more data/ reach question ?4? ?undefined? we link to a thank you page
#DEBUGGING AND TESTING: ipython to test class, flask debugger to check variables?


@app.route("/")
def start_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("start.html", title=title, instructions=instructions)

# dynamic quesetions
# id will be passed in to question through the url
# id will be passed into arguments
# will use argument into rendering question in html

@app.route("/question/<int:id>")
def show_question(id):
    question = satisfaction_survey.questions[id].question
    choices = satisfaction_survey.questions[id].choices

    if (RESPONSES is None):
        return redirect("/")
    
    if (id != len(RESPONSES)):
        return redirect(f"/questions/{len(RESPONSES)}")
    
    return render_template("question.html", question=question, choices=choices)
# will redirect to the length of responses now

RESPONSES = []
@app.route("/answers", methods=["POST"])
def answers():
    choices = request.form["choices"]
    RESPONSES.append(choices)
    if (len(RESPONSES) == len(satisfaction_survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/question/{len(RESPONSES)}")

@app.route("/complete")
def show_complete():
    return render_template("complete.html")

## SOLUTIONS - I couldnt figure out how to push through questions while dynamically matching url
## now i understand how to use len of responses to push through
## will only work if our original question func is dynamic to take in a integer url
