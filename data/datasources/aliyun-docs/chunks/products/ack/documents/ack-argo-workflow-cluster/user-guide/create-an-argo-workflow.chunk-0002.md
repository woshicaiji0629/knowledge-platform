### 步骤一：安装Argo CLI
阿里云Argo CLI完全兼容开源Argo CLI，并增强了Metrics能力和日志能力。阿里云Argo CLI支持查看工作流的CPU、内存资源消耗及运行成本，并获取已删除Pod的日志。
下载阿里云Argo CLI。
以下步骤以Linux系统为例，Darwin（macOS）版Argo CLI的下载链接是[https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin](https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-darwin)。wget https://ack-one.oss-cn-hangzhou.aliyuncs.com/cli/v3.4.12/argo-cli-aliyun-linux
为argo-cli-aliyun-linux授予可执行权限。
chmod +x argo-cli-aliyun-linux
将执行文件移动到环境变量包含的目录下，例如：/usr/local/bin/。
mv argo-cli-aliyun-linux /usr/local/bin/argo
