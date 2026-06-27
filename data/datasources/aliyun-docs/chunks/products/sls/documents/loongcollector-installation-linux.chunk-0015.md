### LoongCollector版本升级/Logtail升级到LoongCollector
在服务器上执行下载命令获取最新安装包，示例代码中${region_id}可使用cn-hangzhou替换，若想加快安装包下载速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行升级命令：升级请使用upgrade命令。若使用install命令，将执行覆盖安装，丢失原配置。
chmod +x loongcollector.sh; sudo ./loongcollector.sh upgrade;
若显示以下信息，则表示升级成功。
Upgrade loongcollector files successfully. Starting loongcollector ... Upgrade loongcollector successfully.
