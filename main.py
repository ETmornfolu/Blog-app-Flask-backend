from flask import Flask
import random

random_numbers=random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTExNjBzazMxMjQzdGFvNjlqOTNhOTZndmNpbjI4OGU4OGJoejU5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fUQ4rhUZJYiQsas6WD/giphy.gif'>")

@app.route("/<int:numbers_random>")
def random_pages(numbers_random):
    if numbers_random == random_numbers:
        return ("<h1>Correct guess<h1/>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif numbers_random > random_numbers:
        return ("<h1>Too high. Try again<h1/>"
                "<img src='High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        return ("<h1>Too Low.Try again<h1/>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")

#
# @app.route("/username/<name>")
# def greet(name):
#     return f"<h1>Good morning, {name}</h1>"


if __name__ == '__main__':
    app.run(debug=True)