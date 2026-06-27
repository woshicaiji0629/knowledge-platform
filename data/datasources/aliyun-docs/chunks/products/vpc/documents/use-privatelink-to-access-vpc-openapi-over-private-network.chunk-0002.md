### 控制台
前往[终端节点 - 创建终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/endpoints/new)页面。
配置接口终端节点：
基础配置：
所属地域：选择访问阿里云服务入口所在地域。
名称与描述：统一标识云资源。
类型：选择阿里云服务。
可用的服务：依据终端节点服务名称选择访问的阿里云服务。
可用：阿里云服务已在所属地域部署，且服务使用方具备连接到对应阿里云服务的权限。
VPC OpenAPI：com.aliyuncs.privatelink.{RegionId}.vpc
VPC对等连接 OpenAPI：com.aliyuncs.privatelink.{RegionId}.vpcpeer
网络配置：
为确保服务高可用，建议至少选择2个可用区下的交换机。可以为终端节点可用区的弹性网卡指定交换机内的 IP 地址，如不指定，将由系统默认分配。
不允许为弹性网卡指定交换机的[系统保留地址](vpc-and-vswitch.md)。
IP版本：VPC OpenAPI 和 VPC对等连接 OpenAPI 的终端节点服务暂不支持双栈，客户端仅可以使用IPv4地址访问服务。
安全组：与接口终端节点关联，管控全部终端节点可用区的弹性网卡的入方向流量。
高级配置：
是否开启自定义服务域名：服务使用方开启后，可使用自定义域名访问阿里云服务。
VPC OpenAPI：vpc-vpc.cn-beijing.aliyuncs.com（以北京地域为例）
VPC对等连接 OpenAPI：vpcpeer.vpc-proxy.aliyuncs.com
终端节点策略：保持默认终端节点策略，即允许完全访问。
创建完成后，可使用同 VPC 的 ECS 执行以下命令测试是否连通。
ping <终端节点可用区的弹性网卡的IP> # 可在实例详情页的可用区与网卡页签下，查看弹性网卡的 IP 地址 # 如为 HTTP/HTTPS 服务，建议直接访问服务端口 curl -sI http://<终端节点域名> # 可在实例列表页查看终端节点域名 # 安全组入方向需开放HTTP（80）和HTTPS（443）端口，用于终端节点所在的VPC通过HTTP协议或者HTTPS协议访问服务。 # 是否可使用HTTPS协议访问，由对应的服务决定。
