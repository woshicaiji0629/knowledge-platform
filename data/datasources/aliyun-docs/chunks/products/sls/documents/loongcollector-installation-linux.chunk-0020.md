### 服务器无法连接外部网络时如何升级
在需要升级LoongCollector的服务器上执行uname -m查看系统架构后，在可以访问公网的服务器上选择对应命令执行：${region_id}需替换为Project所属地域的[地域](loongcollector-installation-linux.md)。
ARM架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/aarch64/main/loongcollector-linux64.tar.gz;
x86-64架构：
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh;wget http://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/x86_64/main/loongcollector-linux64.tar.gz;
将安装脚本和安装包拷贝至需要升级LoongCollector的服务器上后，执行命令：
chmod +x loongcollector.sh;./loongcollector.sh upgrade-local;
