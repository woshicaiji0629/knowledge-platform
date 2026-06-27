iyun.com)，在Project列表中单击目标Project。
在日志存储的日志库页签中，单击+图标。
填写Logstore名称，其余配置保持默认无需修改。
服务器网络要求
安装LoongCollector的机器需在出口方向开放80（HTTP）端口和443（HTTPS）端口，供LoongCollector上传数据。
安装LoongCollector的机器至少需要保证能够连通下列地址：
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在访问域名中可查看当前Project的域名信息，替换后执行命令。
当安装方式选择：[同账号同地域](loongcollector-installation-linux.md)、[不同账号同地域](loongcollector-installation-linux.md)时，数据传输方式为内网传输，替换${project名称}为Project名称，${域名信息}为私网域名。
当安装方式选择：[同账号不同地域](loongcollector-installation-linux.md)、[其他云/自建服务器](loongcollector-installation-linux.md)时，数据传输方式为公网传输，替换${project名称}为Project名称，${域名信息}为公网域名。
curl https://${project名称}.${域名信息}
返回类似信息{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}，说明网络畅通。否则检查目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
返回Error信息是因为访问链接缺少必要参数。当前测试仅验证网络连通性，未使用完整链接，因此在网络正常的情况下会显示Error的提示信息。
