## Alibaba Cloud Linux 2/3 UEFI镜像
阿里云TEE SDK中提供了SGX示例代码用于验证SGX功能，默认位于/opt/alibaba/teesdk/intel/sgxsdk/SampleCode目录下。
安装编译工具。
ID=$(grep -w '^ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') VERSION_ID=$(grep -w '^VERSION_ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') if [ "$ID" = "alinux" ]; then case "$VERSION_ID" in "2.1903" ) sudo yum install -y devtoolset-9 ;; "3" ) sudo yum groupinstall -y "Development Tools" ;; esac fi
设置SGX SDK相关的环境变量。
if [ "$ID" = "alinux" -a "$VERSION_ID" = "2.1903" ]; then source /opt/rh/devtoolset-9/enable fi source /opt/alibaba/teesdk/intel/sgxsdk/environment
编译示例代码SampleEnclave。
执行以下命令，进入SampleEnclave目录。
cd /opt/alibaba/teesdk/intel/sgxsdk/SampleCode/SampleEnclave
执行以下命令，编译SampleEnclave。
sudo -E make
运行编译出的可执行文件。
sudo ./app
出现类似如下信息时，表示SGX功能运行正常。
