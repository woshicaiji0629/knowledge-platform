# 通过Logtail采集Open-Falcon数据-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/collect-metric-data-from-open-falcon

# 采集Open-Falcon数据
Open-Falcon是一款企业级、高可用、可扩展的开源监控解决方案，用于监控服务器的状态，例如磁盘空间、端口存活、网络流量等。本文介绍如何通过Logtail和Transfer将Open-Falcon数据上传至日志服务。
## 前提条件
已创建Project和MetricStore。具体操作，请参见[创建项目](manage-a-project.md)[Project](manage-a-project.md)和[创建](manage-a-metricstore.md)[MetricStore](manage-a-metricstore.md)。
## 使用限制
您所使用的Open-Falcon版本需包含[Influxdb support](https://github.com/open-falcon/falcon-plus/commit/df7a2f80e27902a7e081c595bd1a24080cc624e7)功能。
只有Linux Logtail 0.16.44及以上版本的Logtail支持采集Open-Falcon数据。如果您已在服务器上安装旧版本的Logtail，需先升级。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
出于性能和可靠性考虑，推荐将Logtail和Open-Falcon的transfer模块安装在相同服务器上。
## 步骤一：创建Logtail采集配置
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在时序存储>时序库页签中，在目标MetricStore下面选择数据接入>logtail配置，然后在右侧页面单击添加Logtail配置。
在快速数据接入对话框中，单击Ping监控。
在创建机器组页签中。
如果已有可用的机器组，请单击使用现有机器组。
如果您还没有可用的机器组，请执行以下操作（以ECS为例）。
在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。
具体操作，请参见[安装](install-logtail-on-ecs-instances.md)[Logtail（ECS](install-logtail-on-ecs-instances.md)[实例）](install-logtail-on-ecs-instances.md)。
重要
如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](configure-a-user-identifier.md)。
安装完成后，单击确认安装完毕。
在创建机器组页面，输入名称，单击下一步。
日志服务支持创建IP地址机器组和用户自定义标识机器组，具体操作，请参见[创建机器组](manage-machine-groups.md)。
确认目标机器组已在应用机器组区域，单击下一步。
重要
创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{ "inputs": [ { "detail": { "Format": "influx", "Address": ":127.0.0.1:8476" }, "type": "service_http_server" } ], "global": { "AlwaysOnline": true, "DelayStopSec": 500 } }
| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 service_http_server。 |
| Format | string | 是 | 数据类型，固定为 influx。 |
| Address | string | 是 | 监听地址与端口，格式为 ip:port 。 |
## 步骤二：修改Open-Falcon配置
登录Open-Falcon所在服务器。
添加transfer配置。
打开配置文件。
配置文件默认为cfg.json。
将如下脚本添加到配置文件中。
address中配置的IP地址和端口号要与您在步骤[7](collect-metric-data-from-open-falcon.md)中配置的Address中的IP地址和端口号一致，详情参数说明请参见[Transfer](https://book.open-falcon.org/zh/install_from_src/transfer.html)。
"influxdb": { "enabled": true, "batch": 200, "retry": 3, "maxConns": 32, "precision": "s", "address": "http://127.0.0.1:8478", "timeout": 5000 }
## 后续步骤
采集到Open-Falcon数据后，您可以在MetricStore中进行查询和分析操作。具体操作，请参见[查询和分析时序数据](query-and-analyze-metric-data.md)。
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
