# 빌드 스테이지
FROM golang:alpine AS builder
WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o helloworld main.go

# 운영 스테이지
FROM scratch
COPY --from=builder /app/helloworld .
EXPOSE 8080
ENTRYPOINT ["./helloworld"]

