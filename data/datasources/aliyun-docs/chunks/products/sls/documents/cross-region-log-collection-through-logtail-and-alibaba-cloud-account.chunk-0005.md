### 传输加速
根据日志服务Project所在地域，获取对应的${region_id}。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
使用传输加速安装Logtial后，需要进入Project，开启传输加速域名后方可生效。具体操作，请参见[开启](transmission-acceleration.md)[Project](transmission-acceleration.md)[的传输加速域名](transmission-acceleration.md)。
执行以下命令下载Logtail安装脚本并完成安装，注意替换${region_id}为实际地域值。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-acceleration
