## 准备工作
在安装前，请在集群节点上验证与日志服务服务端点的网络连通性，确保LoongCollector可以正常上报数据。
获取服务接入点：
登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.70905a3dccueNa)，在Project列表中，单击目标Project。
单击Project名称右侧的进入项目概览页面。
在基础信息中找到当前Project所在地域的公网和内网Endpoint。
执行连通性测试：登录到将要安装LoongCollector组件的集群节点上，执行以下curl命令。请将${Project名称}和${SLS_ENDPOINT}替换为您的实际信息。
curl https://${Project名称}.${SLS_ENDPOINT}
查看测试结果：
如果命令返回{"Error":{"Code":"OLSInvalidMethod",...}}，表明您的节点与日志服务之间的网络是通畅的。
说明
此测试仅验证网络层连通性。由于请求缺少必要的 API 参数，日志服务返回错误响应是预期结果。
如果命令超时或返回其他网络层错误（如Connection refused），则表示网络不通，请检查节点的网络配置、安全组规则或 DNS 解析。
