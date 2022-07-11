from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/ai")
def ai():
    # my_ai 파일을 임포트해서 그 안에 run()이라는 함수를 수행한다. 
    # run() 함수는 결과를 문자열로 보내준다.   
    import myai
    results = myai.run()
    results = "<h1>Hello World - ai</h1>"
    return results
