## 卸载LoongCollector
示例代码中${region_id}可使用cn-hangzhou替换，若想加快执行速度，请参考[地域](loongcollector-installation-linux.md)替换${region_id}为ECS所属地域。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行卸载命令。
chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;
