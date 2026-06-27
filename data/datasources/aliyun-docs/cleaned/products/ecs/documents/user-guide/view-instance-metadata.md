# 通过元数据服务从ECS实例内部获取实例属性等信息-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata

# 实例元数据
运行于ECS实例的应用，可通过元数据服务动态查询实例ID、IP等实例元数据信息，避免硬编码。为防范[SSRF](view-instance-metadata.md)[攻击](view-instance-metadata.md)导致元数据泄露，建议通过加固模式访问元数据（需先获取访问令牌），并配置实例仅允许加固模式访问，以有效规避普通模式下的安全风险。
## 获取实例元数据
实例元数据是实例自身属性的集合，包含实例ID、网络环境、凭证等关键属性。
## 方式一：加固模式（推荐）
通过加固模式访问元数据时，需先获取临时访问令牌（Token），然后携带令牌获取元数据。
## Linux
[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)实例。
获取临时令牌（Token）。
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:21600"`参数X-aliyun-ecs-metadata-token-ttl-seconds: 令牌有效期，取值范围：1~21600（秒）
携带令牌（Token）获取元数据。
curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/meta-data/instance-id命令末尾的instance-id代表获取实例ID，可替换为其他需要获取的[元数据项](view-instance-metadata.md)。例如mac（获取MAC地址）或hostname（获取主机名）。
成功执行后，终端将仅输出实例ID字符串，例如：i-bp1******
## Windows
[登录](connect-to-a-windows-instance-through-workbench.md)实例。
获取临时令牌（Token）。
$token = Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://100.100.100.200/latest/api/token参数X-aliyun-ecs-metadata-token-ttl-seconds: 令牌有效期，取值范围1~21600（秒）。
携带令牌（Token）获取元数据。
Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token" = $token} -Method GET -Uri http://100.100.100.200/latest/meta-data/instance-id命令末尾的instance-id代表获取实例ID，可替换为其他需要获取的[元数据项](view-instance-metadata.md)。例如mac（获取MAC地址）或hostname（获取主机名）。
成功执行后，终端将仅输出实例ID字符串，例如：i-bp1******
## 方式二：普通模式
警告
普通模式是一种不安全的访问方式，不推荐使用。
Linux：
# 直接发送GET请求获取实例ID curl http://100.100.100.200/latest/meta-data/instance-id
Windows：
# 直接发送GET请求获取实例ID。 Invoke-RestMethod -Uri http://100.100.100.200/latest/meta-data/instance-id -Method Get
## 开启仅允许加固模式访问元数据
为防范严重安全风险，建议为ECS实例启用仅加固模式，启用后，仅能通过加固模式访问元数据，任何普通模式访问都会报错（403 - Forbidden）。默认情况下，ECS实例支持无令牌访问元数据（普通模式），存在被服务器端请求伪造 (SSRF) 攻击的严重风险。
典型攻击场景：利用应用程序从外部URL下载图片的功能，构造恶意请求，诱使服务器代替其访问内部元数据服务，窃取实例绑定的RAM角色的临时访问凭证，若该角色权限过高，攻击者便可能获得云资源控制权限，甚至接管整个云账号。
## 创建新实例时启用仅加固模式
## 控制台
在[自定义购买实例](create-an-instance-by-using-the-wizard.md)时，将高级选项>元数据访问模式调整为仅加固模式。
使用自定义镜像创建实例时，若无仅加固模式选项，需对镜像进行[升级](view-instance-metadata.md)。
## CLI
在通过[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance](../developer-reference/api-ecs-2014-05-26-createinstance.md)创建实例时，可通过配置HttpEndpoint=enabled和HttpTokens=required设置实例的元数据访问模式为仅加固模式。命令示例如下：
执行该命令后，会创建一台仅加固模式的Linux实例。aliyun ecs RunInstances \ --region cn-hangzhou \ --RegionId 'cn-hangzhou' \ --ImageId 'aliyun_3_x64_20G_alibase_20250629.vhd' \ --InstanceType 'ecs.g7.large' \ --VSwitchId 'vsw-bp1******trg' \ --SecurityGroupId 'sg-bp1******dgl' \ --SystemDisk.Size 40 \ --SystemDisk.Category cloud_essd \ --HttpEndpoint enabled \ --HttpTokens required
## API
在通过[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance](../developer-reference/api-ecs-2014-05-26-createinstance.md)创建实例时，通过配置HttpEndpoint=enabled和HttpTokens=required设置实例的元数据访问策略为仅加固模式。
## 将已有实例升级到仅加固模式
### 适用范围
Windows实例：不支持开启仅加固模式。强行开启将导致实例初始化异常，并影响主机名修改、KMS激活等多项关键功能。
Linux实例：支持升级，但在操作前必须完成下文所述的依赖项排查与改造。
### 步骤一：排查并升级代码及依赖项
在切换到仅加固模式之前，实例及其中部署的应用，必须确保满足以下要求：
确保Cloud-init版本不低于23.2.2：可登录实例并执行cloud-init --version命令查看当前版本。若版本过低，切换仅加固模式后将导致实例启动异常，请先[升级](install-cloud-init.md)Cloud-init版本到23.2.2或更高版本。
所有应用代码/脚本已通过[方式一：加固模式](view-instance-metadata.md)访问实例元数据。
重要
若应用代码依赖Credentials库获取STS Token配置SDK，需将Credentials依赖升级至[支持加固模式的版本](view-instance-metadata.md)。
升级完成后，可[如何检测](view-instance-metadata.md)[ECS](view-instance-metadata.md)[实例是否存在普通模式的元数据访问？](view-instance-metadata.md)，在确定不存在普通模式访问后，开启实例的仅加固模式。
### 步骤二：切换到仅加固模式
## 控制台
进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，选择地域与资源组。
在操作列单击>修改实例元数据访问信息。
开启是否启用实例元数据访问通道开关，并设置实例元数据访问模式为仅加固模式，然后单击确定。
## CLI
调用[ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md)，设置HttpEndpoint=enabled、HttpTokens=required切换实例元数据访问模式为仅加固模式。命令示例：
aliyun ecs ModifyInstanceMetadataOptions \ --region cn-hangzhou \ --RegionId 'cn-hangzhou' \ --InstanceId 'i-bp1******ke' \ --HttpEndpoint enabled \ --HttpTokens required
## API
调用[ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md)，设置HttpEndpoint=enabled、HttpTokens=required切换实例元数据访问模式为仅加固模式。
切换完成后，建议持续监控实例的元数据访问情况和应用运行状态，确保业务平稳运行，避免因遗漏改造的应用而导致服务中断。若出现异常，建议先切换回普通模式和加固模式，优先恢复业务，然后重新进一步[步骤一：排查并升级代码及依赖项](view-instance-metadata.md)。
## 实例元数据明细
实例元数据采用类似目录结构的层级方式进行组织，支持逐级访问。当访问一个元数据目录时，将返回其包含的下一级元数据条目或子目录。例如访问meta-data/instance/，会显示instance-name和instance-type等信息。
| 分类 | 元数据 | 说明 | 示例 |
| --- | --- | --- | --- |
| 实例基本信息 | instance-id | 实例 ID。 | i-bp13znx0m0me8cquu**** |
| instance/instance-name | 实例名称。 | iZbp1bfqfsvqzxhmnd5**** |  |
| hostname | 实例的主机名。 | iZbp13znx0m0me8cquu**** |  |
| instance/instance-type | 实例规格。 | ecs.g6e.large |  |
| serial-number | 实例所对应的序列号。 | 4acd2b47-b328-4762-852f-998**** |  |
| region-id | 实例所属地域 ID。 | cn-hangzhou |  |
| zone-id | 实例所属可用区。 | cn-hangzhou-i |  |
| owner-account-id | 实例拥有者的阿里云账号 ID。 | 1609**** |  |
| tags/instance/[tagKey] | 用于获取实例的指定标签值，其中 [tagKey] 为要查询的标签键。 使用此功能，需先调用 [ModifyInstanceMetadataOptions](../developer-reference/api-ecs-2014-05-26-modifyinstancemetadataoptions.md) 接口，将实例的 InstanceMetadataTags 参数设置为 enabled ，以启用此功能。 | dev |  |
| 镜像信息 | image-id | 创建实例时所使用的镜像 ID。 | aliyun_3_x64_20G_alibase_20210425.vhd |
| image/market-place/product-code | 云市场镜像的商品码。 | cmjj01**** |  |
| image/market-place/charge-type | 云市场镜像的计费方式。 | PrePaid |  |
| source-address | 镜像库地址，主要为 yum 源或者 apt 源，供 Linux 实例的包管理软件获取更新。 | http://mirrors.cloud.aliyuncs.com |  |
| 基础网络配置 | network-type | 网络类型，只支持 VPC 类型实例。 | vpc |
| vpc-id | 实例所属 VPC ID。 | vpc-bp1e0g399hkd7c8q**** |  |
| vpc-cidr-block | 实例所属 VPC CIDR 段。 | 192.168.XX.XX/16 |  |
| vswitch-id | 实例所属虚拟交换机 ID。 | vsw-bp1ygryo03m39xhsy**** |  |
| vswitch-cidr-block | 实例所属虚拟交换机 CIDR 段。 | 192.168.XX.XX/24 |  |
| instance/max-netbw-egress | 实例规格的出方向内网最大带宽。单位：Kbit/s。 | 1228800 |  |
| dns-conf/nameservers | 实例的 DNS 配置。 | 100.100.XX.XX |  |
| ntp-conf/ntp-servers | NTP 服务器地址。 | ntp1.aliyun.com |  |
| 主网卡 IP 地址 | mac | 实例的 MAC 地址，如果实例存在多个网卡，则只显示 eth0 上的 MAC 地址。 | 00:16:3e:0f:XX:XX |
| private-ipv4 | 实例主网卡的私网 IPv4 地址。 | 192.168.XX.XX |  |
| public-ipv4 | 实例主网卡的公网 IPv4 地址。 | 120.55.XX.XX |  |
| eipv4 | 获取实例的固定公网 IPv4 地址或主网卡挂载的弹性公网 IPv4 地址。 | 120.55.XX.XX |  |
| 弹性网卡详细信息 | network/interfaces/macs/[mac]/network-interface-id | 网卡的标识 ID。 [mac]参数需要替换为实例的 MAC 地址（可通过元数据 mac 获取），下同。 | eni-bp1b2c0jvnj0g17b**** |
| network/interfaces/macs/[mac]/vpc-id | 网卡所属的 VPC ID。 | vpc-bp1e0g399hkd7c8q3**** |  |
| network/interfaces/macs/[mac]/vswitch-id | 网卡所属的虚拟交换机 ID。 | vsw-bp1ygryo03m39xhsy**** |  |
| network/interfaces/macs/[mac]/primary-ip-address | 网卡主私有 IP 地址。 | 192.168.XX.XX |  |
| network/interfaces/macs/[mac]/private-ipv4s | 网卡分配的私网 IPv4 地址列表。 | ["192.168.XX.XX"] |  |
| network/interfaces/macs/[mac]/ipv4-prefixes | 网卡分配的私网 IPv4 前缀列表。 | 192.168.XX.XX/28 |  |
| network/interfaces/macs/[mac]/netmask | 网卡对应的子网掩码。 | 255.255.XX.XX |  |
| network/interfaces/macs/[mac]/gateway | 网卡对应的 IPv4 网关地址。 | 192.168.XX.XX |  |
| network/interfaces/macs/[mac]/vswitch-cidr-block | 网卡所属的虚拟交换机 IPv4 CIDR 段。 | 192.168.XX.XX/24 |  |
| network/interfaces/macs/[mac]/vpc-cidr-block | 网卡所属的 VPC IPv4 CIDR 段。 | 192.168.XX.XX/16 |  |
| network/interfaces/macs/[mac]/ipv6s | 网卡分配的 IPv6 地址列表，仅支持已配置了 IPv6 的 VPC 类型实例。 | [2408:XXXX:325:a204:1875:217f:184a:e4e] |  |
| network/interfaces/macs/[mac]/ipv6-prefixes | 网卡分配的 IPv6 前缀列表。 | 2001:db8:1234:1a00:XXXX::/80 |  |
| network/interfaces/macs/[mac]/ipv6-gateway | 网卡所属的 VPC 的 IPv6 网关地址。 | 2408:XXXX:325:a204:ffff:ffff:ffff:fff7 |  |
| network/interfaces/macs/[mac]/vswitch-ipv6-cidr-block | 网卡所属的虚拟交换机 IPv6 CIDR 段，仅支持已配置了 IPv6 的 VPC 类型实例。 | 2408:XXXX:325:a204::/64 |  |
| network/interfaces/macs/[mac]/vpc-ipv6-cidr-blocks | 网卡所属的 VPC IPv6 CIDR 段，仅支持已配置了 IPv6 的 VPC 类型实例。 | [2408:XXXX:325:a200::/56] |  |
| 云盘信息 | disks/ | 云盘序列号。 | bp131n0q38u3a4zi**** |
| disks/[disk-serial]/id | 云盘 ID。 | d-bp131n0q38u3a4zi**** |  |
| disks/[disk-serial]/name | 云盘名称。 | testDiskName |  |
| 安全与凭证 | public-keys/[keypair-id]/openssh-key | 公有密钥。仅在实例启动时提供了公有密钥的情况下可用。 | ssh-rsa ****3NzaC1yc2EAAAADAQABAAABAQDLNbE7pS****@****.com |
| ram/security-credentials/[role-name] | 与实例关联的 RAM 角色的临时安全凭证。[role-name]需替换为角色名称。凭证在 Expiration 字段指定时间后失效，需重新调用接口获取。 | { "AccessKeyId": "****", "AccessKeySecret": "****", "Expiration": "2024-11-08T09:44:50Z", "SecurityToken": "****", "LastUpdated": "2024-11-08T03:44:50Z", "Code": "Success" } |  |
| 实例高级属性 | instance/virtualization-solution | ECS 虚拟化方案，支持 Virt 1.0 和 Virt 2.0。 | ECS Virt |
| instance/virtualization-solution-version | 内部 Build 号。 | 2 |  |
| instance/spot/termination-time | 抢占式实例的操作系统设置的停机释放时间，时区标准为 UTC+0，格式为 yyyy-MM-ddThh:mm:ssZ。 | 2020-04-07T17:03:00Z |  |
| Windows 特定配置 | kms-server | Windows 实例的 KMS 激活服务器。 | kms.cloud.aliyuncs.com |
| wsus-server/wu-server | Windows 实例的更新服务器。 | http://update.cloud.aliyuncs.com |  |
| wsus-server/wu-status-server | Windows 实例的更新状态监控服务器。 | http://update.cloud.aliyuncs.com |  |
## 常见问题
- 什么是SSRF攻击？仅加固模式防御SSRF攻击原理是什么？
SSRF（Server-Side Request Forgery，服务端请求伪造）是一种安全漏洞，攻击者通过诱导服务器发起任意网络请求，从而访问受保护的内部系统（如元数据服务、数据库等）。例如，攻击者提交包含http://100.100.100.200/latest/meta-data/的URL，诱使应用抓取并返回元数据中的敏感信息，造成元数据泄露。
默认情况下，ECS实例支持无令牌访问元数据（普通模式）。开启仅加固模式后，会强制启用令牌验证机制：客户端必须先发送PUT请求获取临时令牌，并在后续GET请求中携带该令牌。由于SSRF攻击难以发起PUT请求，无法获取令牌，从而有效阻断访问，提升元数据安全。
- 加固模式下，使用命令无法访问实例元数据，如何处理？
常见错误命令如下：
实例元数据访问凭证的有效期超出范围（400 - Missing or Invalid Parameters）
实例元数据访问凭证有效期范围为1秒~21600秒，超过这个限制，会报错400 - Missing or Invalid Parameters。
curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds: 21700"
请求中存在X-Forwarded-For标头（403 - Forbidden）
curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-Forwarded-For: www.ba****.com"
指定的实例元数据访问凭证无效（401 - Unauthorized）
curl -H "X-aliyun-ecs-metadata-token: aaa" -v http://100.100.100.200/latest/meta-data/
- 高频访问元数据服务被限流怎么办？
元数据服务存在访问频率限制。最佳实践是在应用启动时获取一次基本不变的元数据项（如instance-id），然后将其缓存在本地内存或文件中，并设置合理的缓存过期时间。
- 将实例元数据访问模式修改为仅加固模式后，应用无法正常工作如何排查？
可能是实例中应用或脚本中仍在使用旧的普通模式。请按照[升级到仅加固模式](view-instance-metadata.md)彻底排查并升级依赖普通模式的应用。
- 能否从本地主机访问这个元数据地址？
不能。100.100.100.200是一个本地地址，仅在ECS实例内部的虚拟网络接口上有效。任何从实例外部发往该地址的请求都无法路由，这是保障元数据安全的基础设计之一。
- 使自定义镜像创建实例时，不支持选择仅加固模式，如何解决？
当使用自定义Linux镜像创建ECS实例时，若发现无法选择或启用仅加固模式，这通常意味着该镜像尚未满足支持此安全特性的必要条件。需参考以下流程对镜像进行升级：
创建临时实例：使用需升级的自定义镜像，创建一个用于诊断改造的临时ECS实例。
改造临时实例：在第一步创建的临时实例上，参考[将已有实例升级到仅加固模式](view-instance-metadata.md)完成以下改造：
升级 Cloud-init：将其升级到 23.2.2 或更高版本。
改造应用/脚本：修改所有依赖“普通模式”的应用或脚本，使其适配“加固模式”。
创建新镜像并修改属性：改造完成后，基于这台实例创建新版自定义镜像。然后调用[ModifyImageAttribute](../developer-reference/api-ecs-2014-05-26-modifyimageattribute.md)调整镜像属性Features.ImdsSupport=v2。
释放资源：新镜像制作完成后，及时释放用于诊断和改造的临时实例，以节省成本。
- Credentials工具支持加固模式的版本
低版本的Credentials不支持通过加固模式访问元数据，在切换到仅加固模式时，会导致其无法通过普通模式获取元数据中的STS Token初始化SDK，造成业务异常。
在切换前，请升级Credentials依赖至支持加固模式的版本，具体版本要求如下：
Java：credentials-java版本 >=0.3.10。
Node.js：credentials版本 >=2.3.1。
PHP：credentials版本 >=1.2.0。
Python：alibabacloud_credentials版本 >=0.3.6。
Go：credentials-go版本 >=1.3.10。
- 如何检测ECS实例是否存在普通模式的元数据访问？
在排查实例中依赖普通模式的应用代码时，可通过以下两种方式，检测并定位到具体进程，以便后续进行改造升级。
方式一：通过云监控确认是否存在普通模式访问
在云监控控制台，通过查看ECS元数据监控，可以快速确认近期实例是否存在普通模式的访问。
进入[云监控控制台](https://cloudmonitornext.console.aliyun.com/)。
在左侧导航栏选择云资源监控>云产品监控页面，搜索并进入ECS元数据监控页面。
查看目标实例的普通模式访问成功次数指标。
若该指标值不为0，证明实例存在普通模式对元数据的访问，需要进一步找到依赖该模式的应用，并将其升级至加固模式。
方式二：通过云助手插件定位具体进程
使用云助手插件，可以辅助在实例内部，精准定位在使用普通模式访问元数据的进程。
适用操作系统
| Alibaba Cloud Linux 3 Alibaba Cloud Linux 3 Pro Anolis OS 8 CentOS Stream 8/9 CentOS 8 | Ubuntu: 20/24 Debian:10,11,12 Fedora 35+ AlmaLinux 8/9 Rocky Linux 8/9 | Red Hat Enterprise Linux 8/9 Red Hat 中需要自行下载 rpm 包 [安装云助手](install-the-cloud-assistant-agent.md) [Agent](install-the-cloud-assistant-agent.md) 。 SUSE 15.1/15.2/15.3/15.4/15.5/15.6 OpenSuse 15.2/15.3/15.4/15.5/15.6 |
| --- | --- | --- |
操作步骤
安装并启用云助手插件
[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)ECS实例，执行以下命令安装并启动监控服务，启用后会占用部分实例性能。
# 部署监控服务 sudo acs-plugin-manager --exec --plugin ACS-ECS-ImdsPacketAnalyzer # 查看监控服务状态 sudo systemctl status imds_tracer_tool
定位问题进程运行命令，查看哪些进程仍在以普通模式访问元数据。日志会显示相关进程的PID。
cat /var/log/imds/imds-trace.* | grep WARNING
分析并改造根据日志中的PID，找到对应的应用程序或脚本，并对其进行升级改造，通过加固模式访问元数据。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
