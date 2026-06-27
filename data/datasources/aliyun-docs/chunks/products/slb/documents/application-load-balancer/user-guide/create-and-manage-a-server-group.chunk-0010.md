### 函数计算类型
支持FC 2.0和FC 3.0。ALB与函数计算之间通过阿里云内部网络安全通信。
使用前需先开通函数计算服务。2024年8月27日之后注册并完成实名认证的阿里云账号无需开通，可直接使用。
使用限制
[ALB](../product-overview/supported-regions-and-zones.md)[挂载函数计算支持的地域](../product-overview/supported-regions-and-zones.md)。
ALB实例和函数须属于同一地域。
一个函数计算类型服务器组仅支持添加一个函数。
函数计算2.0请求处理程序类型为处理事件请求时，需配置HTTP触发器才能关联ALB。
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑后端服务器。
在后端服务器页签，单击设置函数计算。在添加后端服务器面板，选择以下任意方式完成配置，然后单击确定。
通过选择资源
函数名称：选择已创建的函数。如果没有可用的函数，可创建新的函数，参考[新建函数](../../../../fc/documents/user-guide/function-instance-1.md)。
版本或别名：选择指定版本或指定别名。新创建的函数默认只有一个LATEST版本。
通过ARN配置
ARN：输入目标函数的ARN。可在函数计算控制台的函数详情页面[获取函数](../../../../fc/documents/user-guide/creating-an-event-function.md)[ARN](../../../../fc/documents/user-guide/creating-an-event-function.md)。
