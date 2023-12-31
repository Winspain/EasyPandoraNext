# EasyPandoraNext

> 仅需两步！🚀小白也能使用docker快速部署PandoraNext🚀

![PandoraNext](https://img.shields.io/badge/Nginx-PandoraNext-blue)
![docker](https://img.shields.io/badge/docker--compose-8A2BE2)

🚀 紧跟[PandoraNext](https://github.com/pandora-next/deploy)项目迭代，当前v0.6.1

- v0.6.1更新内容
- Added a new endpoint in proxy mode for direct retrieval of refresh_token.
/api/auth/login2 POST (1:1000)

😀 小白放心食用

- 使用docker-compose
- 快速部署Nginx+PandoraNext
- 挂载宿主机data目录
- 映射sessions目录，保留登录的session，避免重启容器登录状态丢失

## Installation

Linux:

```sh
cd /root
git clone https://github.com/Winspain/Next-Web-Pandora.git
```

## Usage example

1️⃣ 配置data目录下文件

- (必做) 获取[license_id](https://dash.pandoranext.com/)填写在data/config.json的license_id中
- (可选) 建议在/data/config.json文件中设置site_password（需包含字母和数字）以初步保护网站

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

[文档站](https://docs.pandoranext.com/)

欢迎issue提问

## ToDo
- [ ] 引入pandora-next-helper项目管理token

## Thanks

Thanks JetBrains for the free open source license

<a href="https://www.jetbrains.com/?from=gev" target="_blank">
	<img src="https://i.loli.net/2021/02/08/2aejB8rwNmQR7FG.png" width = "260" align=center />
</a>