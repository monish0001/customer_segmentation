from flask import Flask

app=Flask(__name__)


@app.route('/')
def Home():
  return "<h1>False App</h1>"


if __name__ == '__main__':
  app.run(debug=True)