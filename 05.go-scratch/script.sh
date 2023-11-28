1. easydocker 폴더에서 소스코드 다운로드
git clone https://github.com/daintree-henry/go-world

2. 이미지 빌드
docker build -t helloworld .

3. 컨테이너 실행
docker run -d -p 8080:8080 --name go-helloworld helloworld


