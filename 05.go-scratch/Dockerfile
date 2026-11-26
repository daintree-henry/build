# Build stage
FROM golang:alpine AS builder
WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o helloworld main.go

# Production stage
FROM scratch
COPY --from=builder /app/helloworld .
EXPOSE 8080
ENTRYPOINT ["./helloworld"]

