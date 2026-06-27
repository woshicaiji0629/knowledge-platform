## Linux
根据日志服务Project所在地域，获取对应的${region_id}。替换${region_id}后，执行以下命令卸载Logtail。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh; chmod +x logtail.sh; ./logtail.sh uninstall
