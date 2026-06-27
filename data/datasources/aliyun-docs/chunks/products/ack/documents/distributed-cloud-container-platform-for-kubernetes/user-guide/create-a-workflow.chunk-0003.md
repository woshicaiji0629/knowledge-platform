### 阿里云Argo CLI
阿里云Argo CLI完全兼容开源Argo CLI，并增强了Metrics能力和日志能力。您可以使用阿里云Argo CLI查看工作流的CPU、内存资源消耗及运行成本，并获取已删除Pod的日志。
安装步骤如下：
说明
以下安装步骤以Linux系统为例，Darwin和Linux系统的下载链接分别如下：
Darwin：[argo-cli-aliyun-darwin](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin)
Linux：[argo-cli-aliyun-linux](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux)
执行如下命令，下载阿里云Argo CLI。
wget https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux
执行如下命令为argo-cli-aliyun-linux授予可执行权限。
chmod +x argo-cli-aliyun-linux
将执行文件移动到环境变量包含的目录下，例如：/usr/local/bin/。
mv argo-cli-aliyun-linux /usr/local/bin/argo
