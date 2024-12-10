from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'san francisco',
    'salary' : '100 $'
  },
  {
    'id' : 2,
    'title' : 'Data scientist',
    'location' : 'Qairo',
    'salary' : '150 $'
  },
  {
    'id' : 3,
    'title' : 'Backend Engineer',
    'location' : 'Tanta',
    'salary' : '170 $'
  },
  {
    'id' : 4,
    'title' : 'Frontend Engineer',
    'location' : 'Basion',
    'salary' : '180 $'
  }
]

@app.route("/")
def hello():
  return render_template("home.html",
                        jobs = JOBS)

if __name__ == "__main__":
  app.run(host ="0.0.0.0", debug = True)