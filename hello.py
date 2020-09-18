from flask import Flask

app = Flask(__name__)

# 코드 수정할 때마다 바로 웹 애플리케이션에 반영하기 위해 디버그 모드 활성화.
app.debug = True 

# 파이썬 데코레이터
# 어떤 함수를 파라미터로 전달받아서 실행하는 함수를 사용하겠다는 표시다.
@app.route("/")

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

