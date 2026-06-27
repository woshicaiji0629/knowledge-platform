### 公网
根据日志服务Project所在地域，获取对应的${region_id}。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
执行以下命令下载Logtail安装脚本并完成安装，注意替换${region_id}为实际地域值。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-internet
