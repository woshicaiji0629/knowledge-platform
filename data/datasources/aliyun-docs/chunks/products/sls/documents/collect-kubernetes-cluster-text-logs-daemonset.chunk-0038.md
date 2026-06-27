### 卸载 ACK 中的 loongcollector(logtail-ds) 组件时提示依赖错误
问题现象：在阿里云容器服务（ACK）中尝试删除loongcollector（logtail-ds） 日志采集组件时，系统报错：该组件的依赖不满足
Dependencies of addons are not met: terway-eniip depends on logtail-ds(>0.0) whose version is v3.x.x.x-aliyun or will be v3.x.x.x-aliyun。
问题原因：terway-eniip网络插件启用了日志采集功能，其依赖于loongcollector（logtail-ds）组件。因此，在未解除该依赖关系前，ACK 不允许直接卸载loongcollector（logtail-ds）。
解决方案：请按以下步骤操作，先解除依赖再卸载组件：
登录[容器服务管理控制台](https://cs.console.aliyun.com/)。；
在集群列表中，单击目标集群名称，进入集群详情页面。
在左侧导航栏，单击组件管理。
在组件列表中，搜索并找到terway-eniip组件，单击关闭日志。
在弹出的对话框中，单击确定。
待配置生效后，重新尝试卸载loongcollector（logtail-ds）组件。
