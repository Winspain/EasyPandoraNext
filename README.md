# EasyPandoraNext

> 一个小白也能使用docker快速部署PandoraNext的项目.

![PandoraNext](https://img.shields.io/badge/Nginx-PandoraNext-blue)
![docker](https://img.shields.io/badge/docker--compose-8A2BE2)

🚀 紧跟[PandoraNext](https://github.com/pandora-next/deploy)项目迭代，当前0.3.1

😀 小白放心食用

👉 如需获取token或session，可点击 [fakeopen](https://ai.fakeopen.com/auth)

- 使用docker-compose
- 快速部署Nginx+PandoraNext
- 挂载宿主机data目录

## Installation

Linux:

```sh
cd /root
git clone https://github.com/Winspain/Next-Web-Pandora.git
```

## Usage example

- (必做) 获取[license_id](https://dash.pandoranext.com/)填写在data/config.json中
- (可选) 建议在/data/config.json文件中设置site_password
- (可选) tokens.json中设置内置账号

```sh
mv docker-compose-example.yml docker-compose.yaml
docker-compose up -d
```

## 更新镜像

```sh
docker-compose pull
docker-compose up -d
```

## 相关文档

更多环境变量设置请参考[PandoraNext](https://github.com/pandora-next/deploy)

使用指南 [fakeopen-wiki](https://fakeopen.org/PandoraNext/)

欢迎issue提问

### TODO

- [ ] 暂无