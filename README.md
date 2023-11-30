# EasyPandoraNext

> 仅需两步！🚀小白也能使用docker快速部署PandoraNext🚀

![PandoraNext](https://img.shields.io/badge/Nginx-PandoraNext-blue)
![docker](https://img.shields.io/badge/docker--compose-8A2BE2)

🚀 紧跟[PandoraNext](https://github.com/pandora-next/deploy)项目迭代，当前0.4.1

😀 小白放心食用

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

1️⃣ 配置data目录下文件

- (必做) 获取[license_id](https://dash.pandoranext.com/)填写在data/config.json的license_id中
- (可选) 建议在/data/config.json文件中设置site_password以初步保护网站

🍉 其余选项均为可选，按需配置，不配置也可直接启动使用！

🍊 如需获取token或session，可点击 [fakeopen](https://ai.fakeopen.com/auth)

🍓 更多环境变量设置请参考[PandoraNext](https://github.com/pandora-next/deploy)

2️⃣ 执行命令

```sh
mv docker-compose-example.yml docker-compose.yaml
docker-compose up -d
```

## 如何更新镜像

```sh
docker-compose pull
docker-compose up -d
```

## 相关文档

[更多使用指南](https://fakeopen.org/PandoraNext/)

欢迎issue提问

### TODO

- [ ] 使用watchtower监控pandora版本变化
- [ ] 版本变化时，使用钉钉通知