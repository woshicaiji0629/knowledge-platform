ttps://${project名称}.${域名信息}
返回类似信息{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}，说明网络畅通。否则检查目标地址是否被拦截以及其他网络方面的检查（例如出口方向是否开放80（HTTP）端口和443（HTTPS）端口、DNS配置、安全组等）。
返回Error信息是因为访问链接缺少必要参数。当前测试仅验证网络连通性，未使用完整链接，因此在网络正常的情况下会显示Error的提示信息。
修改/usr/local/ilogtail/ilogtail_config.json中参数：
config_servers：此参数为获取采集配置路径，修改为"http://logtail.${域名信息}"，其中${域名信息}替换为公网域名。
data_servers：
region：此参数为数据传输使用的地域信息，修改为"${RegionID}"，其中${RegionID}替换为日志服务Project地域的[RegionID](loongcollector-installation-linux.md)。
endpoint_list：此参数为数据传输使用的路径，修改为"${域名信息}"，其中${域名信息}替换为公网域名。
保存修改后重启LoongCollector。
若使用的是Logtail采集器，重启命令为：sudo /etc/init.d/ilogtaild restartsudo /etc/init.d/loongcollectord restart
检查用户自定义标识或IP的值：
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组，在机器组中单击目标机器组。
查看机器组配置页面，并确认机器组标识内容后选择对应操作：
