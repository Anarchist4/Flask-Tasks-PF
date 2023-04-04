from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "hello world!"

@app.route('/<int:num>')
def square(num:int):
    return f'square of the number is : {num*num}!'

if __name__=='__main__':
    app.run(debug=True)