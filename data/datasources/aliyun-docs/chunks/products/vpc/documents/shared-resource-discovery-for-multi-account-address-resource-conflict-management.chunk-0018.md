### 查看已发现资源的IP信息
资源发现支持查看已发现的VPC和交换机下所有已使用IPv4私网IP详细信息，包括IP地址、资源ID、资源归属地域、云服务类型等，帮助您全面掌握网络中的IP地址使用情况。
仅支持查询已被资源发现纳管的VPC和交换机下的IP信息。
支持按VPC ID、交换机ID、CIDR进行筛选，其中CIDR支持任意合法IPv4地址段，包括/32精确匹配单个IP地址，且需要与VPC ID或交换机ID组合使用。
支持的查询组合包括：仅VPC ID、仅交换机ID、VPC ID + CIDR、交换机ID + CIDR、VPC ID + 交换机ID + CIDR。
控制台
前往[IPAM](https://ipam.console.aliyun.com/cn-hangzhou/resource)[控制台 - 资源发现](https://ipam.console.aliyun.com/cn-hangzhou/resource)，单击目标资源发现实例ID进入详情页。
在已发现资源页签下，展开VPC或交换机资源树，单击目标资源IP资源信息列的查看，系统将自动跳转到IP资源信息页签并预设过滤条件。
您也可以直接单击IP资源信息页签，手动输入筛选条件查询。
API
调用[ListIpamDiscoveredIpAddresses](developer-reference/api-vpcipam-2023-02-28-listipamdiscoveredipaddresses.md)，指定VpcId、VSwitchId、Cidr参数查询已发现资源的IP地址详细信息。
