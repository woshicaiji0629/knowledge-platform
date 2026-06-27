### LoongCollector回滚到Logtail
说明
必须要重新下载logtail.sh脚本，不能使用原来的logtail.sh脚本。
在服务器上执行下载命令获取安装包，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh;
执行回滚命令。如需指定版本，如指定 1.8.7 版本，参考注释，根据实际情况替换版本号。
chmod +x logtail.sh; sudo ./logtail.sh upgrade; #chmod +x logtail.sh; sudo ./logtail.sh upgrade -v 1.8.7;
