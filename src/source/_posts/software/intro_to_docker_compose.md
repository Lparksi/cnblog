---
title: "如何使用 Docker Compose 让你的项目快速部署"
date: 2025-08-02 09:17:20
tags:
  - Docker
categories:
  - Docker
sticky: 
thumbnail: https://img0.parksi.top/ShareX/2025/08/chrome_UQuDNJITYV.webp
excerpt: Docker 是一种容器化技术，通过 Dockerfile 打包程序为镜像，使用 Docker Compose 编排程序与数据库（如 Postgres 和 Redis），实现快速部署和一致运行环境，简化开发与上线流程。
cover: https://img0.parksi.top/ShareX/2025/08/chrome_UQuDNJITYV.webp
expires: 
mathjax: false
---
## Why
Docker 是一种容器化技术，可以将程序打包进容器，使其在不同主机上运行的效果相同（类似于虚拟机），将程序及其环境使用 Docker Compose 编排起来，可以实现快速敏捷上线。

## How
那么如何实现呢？首先要将程序本身打包为 Docker 镜像，具体的方法是使用 DockerFile

这是一个典型的 Go语言两阶段部署方案，首先将go二进制文件编译出来，然后将其拷贝至极简的  apline 内核运行，同时暴露9000端口为业务端口

tips： 如果你的业务涉及时区，就需要`RUN apk add --no-cache tzdata` ，`golang:1.24-alpine`是没有这个时区包的。
```dockerfile
FROM golang:1.24-alpine AS builder  
WORKDIR /app  
COPY go.mod go.sum ./  
RUN go mod download  
COPY . .  
  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server ./cmd/server  
FROM alpine:latest  
RUN apk add --no-cache tzdata  
ENV TZ=Asia/Shanghai  
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime  
  
LABEL maintainer="i@parksi.top"  
LABEL description="bacend of project-ay"  
LABEL version="dev"  
LABEL name="project-ay"  
  
ENV GIN_MODE=release  
ENV APP_SERVER_HOST=0.0.0.0  
COPY --from=builder /app/server .  
COPY --from=builder /app/config ./config  
  
EXPOSE 9000  
  
CMD ["./server"]
```

程序本身的容器搞定了，那数据库呢？这个项目使用了 **postgres + gis扩展** 和 **redis** 为数据库，gis扩展的安装就已经很麻烦了，redis 更是在 Windows 下没有支持，那么使用 Docker 镜像来运行是一种方法。

下面来看 compose
```yaml
name: ay-backend  
services:  
  postgres:  
    image: postgis/postgis:17-3.5-alpine  
    restart: always  
    environment:  
      POSTGRES_USER: postgres  
      POSTGRES_PASSWORD: postgres  
      POSTGRES_DB: postgres  
    healthcheck:  
      test: ["CMD-SHELL", "pg_isready -U postgres"]  
      interval: 5s  
      timeout: 5s  
      retries: 5  
    volumes:  
      - pgdata:/var/lib/postgresql/data  
#    ports:  
#      - "5433:5432"  
  redis:  
    image: redis:bookworm  
    restart: always  
    healthcheck:  
      test: ["CMD-SHELL", "redis-cli ping"]  
      interval: 5s  
      timeout: 5s  
      retries: 5  
    volumes:  
      - redisdata:/data  
    ports:  
      - "6379:6379"  
  
  app:  
    image: ay-backend:latest  
    build:  
      context: ..  
      dockerfile: scripts/Dockerfile  
    ports:  
      - "9001:9000"  
    logging:  
      driver: json-file  
      options:  
        max-size: 10m  
    environment:  
      - APP_POSTGRES_HOST=postgres  
      - APP_POSTGRES_PORT=5432  
      - APP_POSTGRES_USER=postgres  
      - APP_POSTGRES_PASSWORD=postgres  
      - APP_POSTGRES_DATABASE=postgres  
      - APP_REDIS_HOST=redis  
      - GIN_MODE=debug  
    depends_on:  
      postgres:  
        condition: service_healthy  
      redis:  
        condition: service_healthy  
    healthcheck:  
      test: [ "CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:9000/api/v1/health" ]  
      interval: 30s  
      timeout: 10s  
      retries: 3  
      start_period: 40s  
volumes:  
    pgdata:  
    redisdata:
```

可以看出，不需要像往常一样下载postgres，gis扩展，redis...安装，Docker管理了这一切，你只需要指定一个靠谱的Docker镜像，配置参数，让后启动即可！这就是Docker的魅力。
需要注意的是：
- Docker默认并不会映射数据库的数据文件，也就是说，你不手动映射的话，每次启动你都会获得一个全新的数据库，推荐做法是使用 *volume* 进行存储。
- 在生产环境中，数据库端口没有必要开放，除了对外服务的`9001:9000`是必要的外，数据库的`6379、5432` 都不是必要的，是同一个编排内，Docker compose会自动创建一个网络，他们使用容器名为host进行通信，举个例子，容器内要访问redis只要使用`redis:6379`即可，不需要暴露至主机。
- 这三个容器是有依赖关系的，主程序必须等到两个数据库初始化完成才能启动，此处使用 `depends_on` 和 `healthcheck` 完成这一点

