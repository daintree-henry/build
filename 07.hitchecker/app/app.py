from flask import Flask
from redis import Redis
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hit Checked! 이 페이지는 %s 번 방문되었습니다.' % redis.get('hits').decode('utf-8')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
