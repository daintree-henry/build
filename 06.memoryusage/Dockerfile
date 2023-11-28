# 파이썬 공식 이미지를 베이스 이미지로 사용합니다.
FROM python:3.8

# 작업 디렉토리를 설정합니다.
WORKDIR /usr/src/app

# 파이썬 스크립트를 컨테이너에 복사합니다.
COPY memory_usage.py ./

# 컨테이너가 시작될 때 스크립트를 실행하도록 설정합니다.
CMD ["python", "./memory_usage.py"]

