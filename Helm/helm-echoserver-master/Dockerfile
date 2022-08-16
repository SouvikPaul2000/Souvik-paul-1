FROM golang:1.10.0-alpine
WORKDIR /bin

RUN go mod download
COPY go.mod ./
COPY go.sum ./
COPY *.go ./
ENV PORT 8080
COPY server.go src/server.go

RUN echo "A default content line." > /tmp/content \
    && apk update \
    && apk add git \
    && go get github.com/labstack/echo \
    && go get github.com/dgrijalva/jwt-go \
    && cd src && go build server.go && chmod +x server && mv server /bin/server


ENTRYPOINT exec server -p ${PORT}