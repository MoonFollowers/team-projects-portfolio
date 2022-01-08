from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.sparta_3team

doc = {'name':'sea_elephant'}
db.users.insert_one(doc)


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

# GEt, Post 요청 확인 ajax 코드입니다.
#      }$.ajax({
# #     type: "GET",
# #     url: "/test?title_give=봄날은간다",
# #     data: {},
# #     success: function(response){
# #        console.log(response)
# #
#   })
# $.ajax({
#     type: "POST",
#     url: "/test",
#     data: { title_give:'봄날은간다' },
#     success: function(response){
#        console.log(response)
#     }
#   })
# 깃허브 테스트