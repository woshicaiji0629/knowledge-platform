## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在连接信息区域框，单击公网访问对应的申请连接地址。
说明
若连接信息区域未显示专有网络或公网连接地址，请先根据提示[设置](../getting-started/step-2-configure-whitelists.md)[IP](../getting-started/step-2-configure-whitelists.md)[白名单](../getting-started/step-2-configure-whitelists.md)。
若没有申请连接地址按钮或该按钮为灰色，表示该实例为云原生版集群架构直连模式实例，不支持申请公网地址。
在右侧弹出的面板中，设置连接地址和端口。

| 配置 | 说明 |
| --- | --- |
| 连接地址 | 目前仅支持修改连接地址的前缀（前缀默认为实例 ID）。 自定义前缀需由小写英文字母和数字组成，以小写字母开头，长度为 8~40 个字符。 |
| 端口 | 可在修改连接地址的同时，修改端口，范围为 1024~65535。 |

单击确定。
申请操作完成后，连接信息区域框中将展示公网连接地址。
