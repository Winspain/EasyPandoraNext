FROM python:3.11-alpine

# 设置工作目录
WORKDIR /app

# 复制你的Python脚本到容器中
COPY entry.py /app

# 安装所需的依赖库（requests和schedule）
RUN pip install requests schedule

# 指定脚本的入口命令
CMD ["python", "entry.py"]
