### 6. 创建用户自定义标识机器组
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project。
在左侧导航栏中，选择资源>机器组，单击机器组右侧的>创建机器组。
在创建机器组对话框中，配置如下参数，单击确定。
名称：机器组名称，创建后不可修改。命名规则如下：
只能包括小写字母、数字、短划线（-）和下划线（_）。
必须以小写字母或者数字开头和结尾。
长度必须在 2~128 字符之间。
机器组标识：选择用户自定义标识。
用户自定义标识：填入您在[1. 修改业务](loongcollector-installation-kubernetes-1.md)[Pod YAML](loongcollector-installation-kubernetes-1.md)[配置](loongcollector-installation-kubernetes-1.md)YAML文件中为 LoongCollector 容器设置的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID的值。必须完全一致，否则无法关联成功。
检查机器组心跳状态：创建完成后，单击目标机器组名称，在机器组状态区域，查看心跳状态。
OK：表示LoongCollector 已成功连接到日志服务，机器组注册成功。
FAIL：
可能是配置未生效，配置生效时间大约需要2分钟，请稍后刷新页面重试。
如果2分钟后仍为FAIL，请参考[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组问题排查思路](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行诊断。
每个 Pod 对应一个独立的 LoongCollector 实例，建议为不同业务或环境使用不同的自定义标识，便于精细化管理。
