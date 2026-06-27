### 服务器无法连接外部网络时如何安装
在需要安装LoongCollector的服务器上执行uname -m查看系统架构后，在可以访问公网的服务器上选择对应下载命令执行：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
ARM架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/aarch64/main/loongcollector-linux64.tar.gz;
x86-64架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/x86_64/main/loongcollector-linux64.tar.gz;
将下载的安装脚本和安装包拷贝至需要安装LoongCollector的服务器上，执行如下命令：${region_id}需替换为Project所属地域的[RegionID](loongcollector-installation-linux.md)。
chmod +x loongcollector.sh; ./loongcollector.sh install-local ${region_id}-internet
执行查看命令，返回loongcollector is running表示启动成功。
sudo /etc/init.d/loongcollectord status
由于服务器无法访问公网，你还需要通过[配置代理](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)的方式与公网建立连接。
