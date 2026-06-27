## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在连接信息的右侧，单击设置免密访问。
在右侧弹出的面板中，阅读相关提示并单击确定。
请刷新页面，当设置免密访问按钮转变为关闭免密访问时，表示已开启该功能。
若实例为云原生版，您必须将同一专有网络客户端的IP地址添加到实例的白名单中，才能使用VPC免密连接。
若实例为经典版，则无需添加白名单即可连接。经典版实例可以通过#no_loose_check-whitelist-always参数进行控制：
默认情况下，#no_loose_check-whitelist-always参数被设置为no，即开启免密访问后，同一专有网络的客户端连接可直接访问Tair实例时，无需将其IP地址添加至实例的白名单中，更多信息请参见[Redis](supported-parameters.md)[开源版配置参数列表](supported-parameters.md)。
在对已启用VPC免密访问的实例进行部分配置变更的场景下，需要预先完成两项前置操作以确保服务的连续性。将实例所属的专有网络IP地址段加入访问白名单 ，并设置no_loose_check-whitelist-always参数的值为yes。若未执行这些步骤，实例在配置变更后将有访问失败的风险。
说明
云原生版不支持设置#no_loose_check-whitelist-always参数。
