## Linux
重要
升级Logtail时，请使用upgrade命令。若使用install命令，将会执行覆盖安装，丢失原配置。
升级过程中，Logtail会短暂停止运行，升级完成后，Logtail 将自动启动，并注册为开机启动项。升级仅覆盖必要的文件，配置文件和Checkpoint文件将被保留，确保升级期间日志不会丢失。
说明
示例代码中${region_id}为日志服务Project所在地域，请参见[开服地域](sls-supported-regions1.md)后替换，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
请根据表格选择Logtail升级方式：

| 操作系统 | 下载方式 | 升级方式 |
| --- | --- | --- |
| ARM 与 x86-64 | 主机可联网： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh; | 下载完成后执行升级命令： chmod +x logtail.sh; sudo ./logtail.sh upgrade; |
| ARM | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/aarch64/logtail-linux64.tar.gz; | 请 将安装脚本和安装包拷贝至需要升级 Logtail 的服务器上后，执行如下升级命令： chmod +x logtail.sh; ./logtail.sh upgrade-local; |
| x86-64 | 主机离线，需先在可以访问公网的服务器上下载安装脚本与安装包： wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh; wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail-linux64.tar.gz; |  |
