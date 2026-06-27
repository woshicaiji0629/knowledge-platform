## Ubuntu 22.04 UEFI镜像
执行以下命令，更新包列表。
sudo apt update
执行以下命令，安装build-essential编译工具。
sudo apt install -y build-essential
编译示例代码SampleEnclave。
执行以下命令，进入SampleEnclave目录。
cd /opt/intel/sgxsdk/SampleCode/SampleEnclave/
执行以下命令，编译SampleEnclave。
sudo make SGX_DEBUG=1
运行编译出的可执行文件。
sudo ./app
出现类似如下信息时，表示SGX功能运行正常。
