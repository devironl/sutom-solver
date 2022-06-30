import re
from unidecode import unidecode
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dico = set([unidecode(line.upper().strip()) for line in open("./data/words.txt").readlines()])
dico = sorted(list(dico))

def all_yellow_in_word(yellow_letters, word):
    for letter in yellow_letters:
        if unidecode(letter.upper()).isalpha() and unidecode(letter.upper()) not in word:
            return False
     
    return True

def lookup(attempt, yellow_letters):
    regex = re.compile(f"^{attempt.upper().strip()}$")
    for word in dico:
        if regex.search(word) and all_yellow_in_word(yellow_letters, word):
            yield word

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST' and "attempt" in request.form:
        attempt = request.form["attempt"]
        yellow_letters = request.form["yellow"]
        candidates = list(lookup(attempt, yellow_letters))
        return render_template('index.html', candidates=candidates)
    return render_template('index.html')


    
    

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
    # while True:
    #     attempt = input("attempt:\n> ")
    #     yellow = input("yellow:\n> ")
    #     for c in lookup(attempt, yellow):
    #         print(c)