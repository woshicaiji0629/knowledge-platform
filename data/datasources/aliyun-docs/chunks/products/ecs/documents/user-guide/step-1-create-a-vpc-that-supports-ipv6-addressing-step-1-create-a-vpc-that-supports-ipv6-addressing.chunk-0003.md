### 步骤二：分配IPv6地址
为ECS实例分配IPv6地址，以使其能够通过IPv6协议与其他实例或外部网络进行通信。
为已有实例分配IPv6地址
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到目标ECS实例，点击进入实例详情页。在全部操作中选择网络和安全组>管理IPv6。
在管理辅助私网IP对话框中，在IPv6区域下方，单击增加。
若无指定 IPv6 地址，设置IPv6地址的输入框留空即可，系统将自动生成。
单击确定。
新建实例时分配IPv6地址
创建实例时，需要注意以下信息（其他配置说明，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)）：
网络及可用区：选择已开通IPv6的专有网络和交换机。
实例：点击查看更多规格参数，筛选出支持IPv6的实例规格，并选择一个实例规格。
带宽和安全组：单击弹性网卡｜IPv6（选填），然后选中免费分配 IPv6 地址。
分配完成后，您可以通过ECS管理控制台查看IP地址详情。具体操作，请参见[IP](ip-address.md)[地址](ip-address.md)。
