# Next-Web-Pandora
> 一个结合了ChatGPT-Next-Web和Pandora的项目.

![Python version](https://img.shields.io/badge/Python-3.11-blue)
![ChatGPT-Next-Web](https://img.shields.io/badge/ChatGPT--Next--Web-8A2BE2)
![Pandora](https://img.shields.io/badge/Pandora-8A2BE2)


快速部署nginx+ChatGPT-Next-Web+Pandora

使用Pandora的pool，来满足多账户并发

脚本自动续期

## Installation

OS X & Linux:

```sh
cd /root
git clone https://github.com/Winspain/Next-Web-Pandora.git
```


## Usage example
```sh
htpasswd -c /root/Next-Web-Pandora/passwd '输入任意账号名'
mv docker-compose-example.yaml docker-compose.yaml
docker build -t refresh-pool-token .
```

## docker-compose
### chatgpt-next-web
- CODE:填入任意值，如pandora
- OPENAI_API_KEY:填入Pandora项目生成的pool token

更多环境变量设置请参考chatgpt-next-web项目

### refresh-pool-token
- UNIQUE_NAME:建议填入和CODE相同的值
- USER_INFO:openAI账号密码，格式为xxxx@gmail.com:yourpassword,yyyy@gmail.com:yourpassword
- POOL_TOKEN
