from flask import Flask
from flask import render_template, request

import tw

app = Flask(__name__)

@app.route('/')
def home():
    tweet = tw.get_tweet()
    return render_template("home.html", tweet=tweet)
    
if __name__ == "__main__":
    app.run()
        
