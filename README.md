# EasyPandoraNext

> 一个小白也能使用docker快速部署PandoraNext的项目.

![Dockerfile](https://img.shields.io/badge/Dockerfile-Nginx-blue
)
![PandoraNext](https://img.shields.io/badge/PandoraNext-8A2BE2
)

当前fakeopen的api已关闭，建议直接部署PandoraNext使用  
如需获取token或session，可点击 [fakeopen](https://ai.fakeopen.com/auth)
- 快速部署Nginx+PandoraNext
- 挂载宿主机data目录
- 挂载宿主机data目录

## Installation

Linux:

```sh
cd /root
git clone https://github.com/Winspain/Next-Web-Pandora.git
```

## Usage example

- 按PandoraNext文档拉取license.jwt(可放置data目录)
- 获取license.jwt内容并填入docker-compose.yaml的PANDORA_NEXT_LICENSE
- 按需在/data/config.json文件中设置site_password
- 按需在tokens.json中设置内置账号

```sh
mv docker-compose-example.yml docker-compose.yaml
docker-compose up -d
```

## docker-compose

### PandoraNext

- PANDORA_NEXT_LICENSE:填入license.jwt的值

更多环境变量设置请参考[PandoraNext](https://github.com/pandora-next/deploy)

使用指南 [fakeopen-wiki](https://fakeopen.org/PandoraNext/)

欢迎issue提问

### TODO

- [ ] 暂无