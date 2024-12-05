from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Stay With Me In 2025 . I Love You "

if __name__ == "__main__":
  app.run(host ="0.0.0.0", debug = True)