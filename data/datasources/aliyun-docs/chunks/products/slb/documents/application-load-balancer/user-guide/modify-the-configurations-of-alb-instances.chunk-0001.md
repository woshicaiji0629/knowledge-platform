../../../eip/documents/billing-overview.md) [计费概述](../../../../eip/documents/billing-overview.md) 。 | 当前实例可用区或公网 ALB 实例绑定的 EIP 不满足您的业务需求或超出您的业务需求时，您可以更新实例可用区。 |

- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标实例，然后在操作列选择>编辑可用区/子网。
在编辑可用区/子网对话框中，选中目标可用区复选框并选择交换机，或取消选择目标可用区，然后单击确定。
选择交换机时，如果没有可选的交换机，您可以在下拉框中单击创建交换机。具体操作，请参见[创建和管理专有网络](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)。
公网ALB实例选中目标可用区复选框时，还需为该可用区分配EIP。
公网ALB实例分配EIP时选择新购创建的为按量付费（按使用流量计费）的BGP多线默认安全防护EIP。
公网ALB实例取消选择可用区时，支持保留ALB自动创建并绑定的EIP（Anycast EIP不支持保留），保留的EIP将按量计费；用户自行绑定的EIP自动保留。
