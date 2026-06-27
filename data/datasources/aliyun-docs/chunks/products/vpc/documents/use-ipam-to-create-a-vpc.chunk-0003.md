### 步骤二：创建顶级池
在左侧导航栏，单击IPAM地址池。
在IPAM地址池页面，单击创建地址池，按下图进行配置，其他参数可保持默认值或根据实际情况修改。此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](create-and-manage-address-pools.md)[IPAM](create-and-manage-address-pools.md)[地址池](create-and-manage-address-pools.md)。
归属IPAM作用范围：只支持选择私网类型的IPAM作用范围。
CIDR范围：选择IPAM，创建的当前地址池为顶级池。
生效地域：IPAM地址池设置的生效地域需在所属IPAM生效地域的范围内，且一旦设置不允许修改。
自动导入发现的资源：开启后，IPAM将通过资源发现能力持续查找VPC，将CIDR在当前地址池范围内且CIDR在IPAM中未分配的资源自动导入到IPAM中。
预置CIDR：您可以单击添加CIDR，添加多个CIDR，只支持创建IPv4类型的CIDR。
分配规则：设置地址池内分配给资源的最小网络掩码长度、默认网络掩码长度以及最大网络掩码长度。
