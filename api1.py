from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "hello world!"

@app.route('/<string:name>')
def name(name:str):
    return f'Hello {name}!'

if __name__=='__main__':
    app.run(debug=True)