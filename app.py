import re
from unidecode import unidecode
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

dico = set([unidecode(line.upper().strip()) for line in open("./data/words.txt").readlines()])
dico = sorted(list(dico))

def all_yellow_in_word(yellow_letters, word):
    for letter in yellow_letters:
        if unidecode(letter.upper()).isalpha() and unidecode(letter.upper()) not in word:
            return False
     
    return True

def grey_in_word(grey_letters, word):
    for letter in grey_letters:
        if unidecode(letter.upper()) in word:
            return True
    return False

def lookup(attempt, yellow_letters, grey_letters):
    attempt = re.sub("[^A-Z\.]", "", unidecode(attempt.upper().strip()))
    regex = re.compile(f"^{attempt}$")
    for word in dico:
        if regex.search(word) and all_yellow_in_word(yellow_letters, word) and not grey_in_word(grey_letters, word):
            yield word

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST' and "attempt" in request.form:
        attempt = request.form["attempt"]
        yellow_letters = request.form["yellow"]
        grey_letters = request.form["grey"]
        candidates = list(lookup(attempt, yellow_letters, grey_letters))
        print(candidates)
        if len(candidates) == 0:
            return render_template("index.html", error_message="Error")
        else:
            return render_template('index.html', candidates=candidates)
    return render_template('index.html')


    
    

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 5002))
    # while True:
    #     attempt = input("attempt:\n> ")
    #     yellow = input("yellow:\n> ")
    #     for c in lookup(attempt, yellow):
    #         print(c)