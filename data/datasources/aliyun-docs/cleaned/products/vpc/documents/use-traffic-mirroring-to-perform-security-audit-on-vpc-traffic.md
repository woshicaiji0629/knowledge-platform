# 使用流量镜像对VPC流量进行安全审查-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/use-traffic-mirroring-to-perform-security-audit-on-vpc-traffic

# 使用流量镜像对VPC流量进行安全审查
云上网络安全，往往是用户将核心业务部署上云时优先考虑的因素。您可使用VPC的流量镜像功能对云上网络流量的安全性进行实时检测与分析。
## 场景示例
某公司将核心业务部署上云，需要保证云上业务的正常运行的同时，高效且无侵入地监控阿里云ECS实例的网络流量，以识别并记录潜在的安全威胁，进行安全审查。
在本场景下，使用[流量镜像](traffic-mirroring-overview.md)，将ECS的网络流量复制到另一台部署着网络威胁检测系统的ECS上，通过配置安全规则，实时检测镜像网络流量。
流量镜像：从目标ECS实例的弹性网卡ENI复制网络流量，并将流量转发给指定的ENI，适用于内容检查、威胁监控和问题排查等场景。
流量审查：使用[Suricata](https://docs.suricata.io/en/latest/)作为报文接收和异常检测的核心组件，因其支持VXLAN解封装、提供入侵检测（IDS）、入侵防御（IPS）和网络安全监控功能，能有效识别恶意流量模式，易与现有的Elasticsearch等可视化分析系统集成。用户也可以自行选择云市场中其他安全厂商的分析工具。
日志处理与存储：通过Filebeat采集Suricata日志，通过Elasticsearch进行索引存储，在Kibana进行可视化查询、分析和展示。
索引文件存储：配置Elasticsearch将经过索引标记的流量记录备份至阿里云OSS，确保数据的安全存储与长期可访问性。
## 前提条件
已创建两个VPC，每个VPC内创建1台ECS实例。
您可以结合业务需求，为ECS1绑定EIP，通过EIP提供公网服务。
ECS2作为镜像目的，绑定EIP访问公网，以部署Suricata。
本文示例中服务器操作系统统一为Alibaba Cloud Linux 3.2104 LTS 64位。
确保ECS2的安全组入方向放开4789端口，允许ECS1封装的UDP协议报文访问ECS2的4789端口，以接收镜像流量。
初次使用流量镜像功能时，根据提示开通流量镜像功能。
镜像源和镜像目的不属于同一个VPC时，需要确保VPC间互通。本文示例通过[VPC](create-and-manage-vpc-peering-connection.md)[对等连接](create-and-manage-vpc-peering-connection.md)连通两个VPC。
已创建阿里云Elasticsearch实例并开启Kibana公网访问，[将本机公网](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)[IP](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)[地址添加到白名单](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#t614906.html)。
## 操作步骤
### 步骤一：配置Suricata
您需要在ECS2服务器中部署Suricata，接收网络流量并进行安全审查。
登录ECS2服务器，执行如下命令，安装Suricata。
#安装依赖 sudo dnf install -y gcc libpcap-devel pcre-devel libyaml-devel file-devel \ zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel #安装suricata sudo dnf install suricata -y #确保suricata自动启动 sudo systemctl enable suricata sudo systemctl start suricata
配置Suricata。
Suricata的配置存放在/etc/suricata/suricata.yaml，使用默认配置即可。
更新安全规则。
执行suricata-update更新规则文件，默认保存在/var/lib/suricata/rules/suricata.rules。
执行sudo service suricata restart重启Suricata。
### 步骤二：配置流量镜像
创建筛选条件。
登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。在左侧导航栏，选择运维与监控>流量镜像>筛选条件。
在筛选条件页面，单击创建筛选条件。在规则配置区域的出方向规则页签下，单击添加规则，按照默认配置添加规则，采集全部流量。
创建并启动镜像会话。
在左侧导航栏，选择运维与监控>流量镜像>镜像会话。
在镜像会话页面，单击创建镜像会话。基础配置保持默认，关联筛选条件选择上一步创建的规则，镜像源选择ECS1的弹性网卡，镜像目的选择ECS2的弹性网卡。
在镜像会话页面，找到目标镜像会话，在操作列单击启动。
流量镜像配置完成且Suricata正常运行时，会在/var/log/suricata/目录下产生一系列日志文件。
/var/log/suricata/ ├── certs ├── core ├── eve.json ##以JSON格式产生的所有捕获的flow，alert，stats等日志，以及例如HTTP等协议的应用日志 ├── fast.log ##检测分析产生的alert日志 ├── files ├── stats.log ##捕获，处理数据包数量的详细统计 ├── suricata.log ##服务运行时的详细日志 └── suricata-start.log ##服务启动时的详细日志
### 步骤三：采集并存储Suricata日志
您可以使用Filebeat将Suricata日志数据传输至阿里云Elasticsearch进行索引存储，并通过Kibana进行可视化展示与分析。
登录ECS2服务器，执行如下命令，安装Filebeat。
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.10.0-x86_64.rpm sudo rpm -vi filebeat-7.10.0-x86_64.rpm
修改Suricata模块配置，指定待采集的Suricata流量日志文件。
执行sudo filebeat modules enable suricata命令，启用Suricata模块。
执行sudo vim /etc/filebeat/modules.d/suricata.yml命令，按照以下内容修改Suricata模块配置。
- module: suricata # 配置采集的流量日志文件 eve: enabled: true var.paths: ["/var/log/suricata/eve.json"]
按下Esc键，输入:wq并回车，以保存并关闭文件。
执行sudo vim /etc/filebeat/filebeat.yml配置filebeat.yml文件，设置连接信息。
修改Filebeat modules配置。
filebeat.config.modules: # 全局加载 path: /etc/filebeat/modules.d/suricata.yml # 允许动态地重新加载和应用新的配置文件或设置 reload.enabled: true # 在设定的时间周期内系统自动检查指定路径下的文件是否有任何更改 reload.period: 1s
修改Kibana配置。
setup.kibana: host: "https://es-cn-8l**********2r7ln-kibana.cn-hangzhou.elasticsearch.aliyuncs.com:5601"
host：Kibana的访问地址，可[在](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)[Kibana](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)[配置页面获取](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)，格式为<Kibana公网地址>:5601。
修改Elasticsearch output配置。
output.elasticsearch: # 配置存储日志的Elasticsearch实例 hosts: ["http://es-cn-8ly**********r7ln.elasticsearch.aliyuncs.com:9200"] username: "elastic" password: "<your_password>"
host：Elasticsearch的访问地址，[可在实例的基本信息页面获取](https://help.aliyun.com/zh/es/user-guide/view-the-basic-information-of-a-cluster-1#task-2449896)，格式为<实例的私网或公网地址>:9200。
username：Elasticsearch实例的访问用户名，默认为elastic。
password：创建实例时设定的密码，若遗忘，可选择[重置实例访问密码](https://help.aliyun.com/zh/es/user-guide/reset-the-access-password-for-an-elasticsearch-cluster#task-2458093)。
按下Esc键，输入:wq并回车，以保存并关闭文件。
执行以下命令，将Dashboard等信息上传到Elasticsearch和Kibana中，并启用Filebeat服务。
sudo filebeat setup sudo service filebeat start
### 步骤四：可视化分析VPC流量
[登录目标](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[Elasticsearch](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[实例的](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[Kibana](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[控制台](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)。在左侧导航栏，单击Kibana>Discover，更改索引模式为filebeat。
您可以添加alert筛选条件，在页面右上角选择查询时间，查看对应时间段内的有潜在威胁的VPC流量。
例如，在查询栏输入alert and 192.168.0.201进行搜索，索引模式为filebeat-*，可查看源 IP 为 192.168.0.201 的告警日志。搜索结果命中 409 条 Suricata 告警记录，告警签名为SURICATA TCPv4 invalid checksum，类别为Generic Protocol Command Decode，严重级别为 3。
### 步骤五：告警验证
登录ECS1，执行curl http://testmynids.org/uid/index.html命令，模仿ID命令的输出，以触发警报。
curl http://testmynids.org/uid/index.html uid=0(root) gid=0(root) groups=0(root)
Suricata规则集中包含如下规则，当数据包的内容具有字符串值uid=0|28|root|29|并且流量被分类为未知流量时，将丢弃数据包并生成警报。
alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root"; content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:2100498; rev:7; metadata:created_at 2010_09_23, updated_at 2010_09_23;)
在Kibana页面，添加GPL筛选条件，即可查看匹配到Suricata IDS特征规则“GPL ATTACK_RESPONSE id check returned root”的告警事件。在 Kibana 日志检索界面搜索关键词GPL，可查看到一条 Suricata IDS 告警命中记录。展开日志详情，event_type为alert，源 IP 为18.155.192.120，目的 IP 为192.168.0.201，协议为 TCP（源端口 80，目的端口 57978），signature为GPL ATTACK_RESPONSE id check returned root，category为Potentially Bad Traffic，severity 为 2，表明告警已成功触发。
### 后续步骤：数据备份
您可以将阿里云Elasticsearch索引存储的数据备份，确保数据安全存储与长期可访问性。Elasticsearch默认开启数据自动备份，您可以[将自动备份快照保存至阿里云](https://help.aliyun.com/zh/es/user-guide/enable-automatic-creation-of-snapshots-and-store-the-snapshots-to-an-oss-repository)[OSS](https://help.aliyun.com/zh/es/user-guide/enable-automatic-creation-of-snapshots-and-store-the-snapshots-to-an-oss-repository)[仓库](https://help.aliyun.com/zh/es/user-guide/enable-automatic-creation-of-snapshots-and-store-the-snapshots-to-an-oss-repository)。
## 常见问题
### 修改Filebeat配置后如何生效？
修改配置文件后，需要重启服务以应用新的设置。您需要执行以下命令重启Filebeat。
sudo systemctl restart filebeat
### 配置流量镜像后，如何验证流量已被正确转发至镜像目的？
登录镜像目的ECS2，执行如下命令，查看是否可以获取到报文的数据包。
tcpdump -i eth0 udp port 4789 -nne
vni 1为镜像会话的标识，表示镜像目的通过镜像会话，成功获取到数据包。
[root@ixxxZ ~]# tcpdump -i eth0 udp port 4789 -nne dropped privs to tcpdump tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes 16:21:48.673510 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 110: 192.168.0.201.27551 > 172.16.0.105.4789: VXLAN, flags [I] (0x08), vni 1 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 60: 45.200.149.95.57388 > 192.168.0.201.7432: Flags [R], seq 950507569, win 1200, options [mss 1460], length 0 16:21:48.673706 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 188: 192.168.0.201.41566 > 172.16.0.105.4789: VXLAN, flags [I] (0x08), vni 1 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 138: 172.16.0.105 > 192.168.0.201: ICMP 172.16.0.105 udp port 4789 unreachable, length 104
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
