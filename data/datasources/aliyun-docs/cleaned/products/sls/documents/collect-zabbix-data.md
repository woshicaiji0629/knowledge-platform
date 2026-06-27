# 采集Zabbix数据-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-zabbix-data

# 采集Zabbix数据
Zabbix作为常用的开源监控系统，提供了丰富的告警规则用于系统监控。日志服务支持采集Zabbix中的监控数据。本文介绍将Zabbix数据采集到日志服务的操作步骤。
## 前提条件
已下载及安装Zabbix。具体操作，请参见[下载与安装](https://www.zabbix.com/cn/download?zabbix=5.4&os_distribution=centos&os_version=8&db=mysql&ws=nginx)[Zabbix](https://www.zabbix.com/cn/download?zabbix=5.4&os_distribution=centos&os_version=8&db=mysql&ws=nginx)。
本教程中，将Zabbix安装在阿里云ECS上为例。
已创建Project和LogStore。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[创建基础](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## 步骤一：配置数据存储路径
Zabbix会将监控数据保存在其所在的机器上，您可以根据如下步骤设置监控数据的存储路径。
登录Zabbix所在服务器。
打开zabbix_server.conf文件。
vim /etc/zabbix/zabbix_server.conf
在zabbix_server.conf文件中，设置数据存储路径。
使用Zabbix的实时导出（Real-time Export）功能，将Zabbix 的监控数据（事件、历史值、趋势）以JSON格式导出。该功能要求Zabbix版本号不能低于4.0。具体操作，请参见[Real-time export](https://www.zabbix.com/documentation/5.4/en/manual/appendix/install/real_time_export)。
不建议使用ExportDir=/tmp/，/tmp通常为 tmpfs（内存文件系统），写入速度极快但占用内存资源。若导出数据量大（如高频率监控项），可能导致内存耗尽或系统 OOM（Out Of Memory）。
ExportDir=/data/zabbix_export
重启Zabbix服务，使配置生效。
systemctl restart zabbix-server
配置生效后，Zabbix会在/data/zabbix_export目录下生产文件（文件名后缀为.ndjson），用于保存监控数据。
## 步骤二：创建LoongCollector采集配置
登录[日志服务控制台](https://sls.console.aliyun.com)。
- 在接入数据区域，选择JSON-文本日志。
选择目标Project和LogStore，单击下一步。
创建机器组。
单击主机场景>ECS>创建机器组，在创建机器组面板中，选择与Project同地域的ECS实例，单击创建机器组。
如果ECS与日志服务不同地域，如果Zabbix是安装在自建集群或其他云厂商服务器上，需要手动安装。具体操作，请参见[安装采集器](loongcollector-installation-linux.md)。
等待安装完成，填写名称后单击确定。
点击下一步，如果心跳为FAIL，点击自动重试后等待两分钟左右直到心跳变为OK，点击下一步。此处自动安装LoongCollector同时也为您配置了IP类型机器组，如果您希望修改为用户自定义标识机器组，您可以参考[机器组与采集配置关联指南](machine-group-and-collection-configuration-association-guide.md)。
创建采集配置，单击下一步。
Zabbix监控数据为JSON类型，所以推荐使用JSON模式进行数据采集。其中日志路径需设置为您在[步骤一：配置数据存储路径](collect-zabbix-data.md)中设置的数据存储路径，其他参数详情请参见[使用](collect-logs-in-json-mode.md)[JSON](collect-logs-in-json-mode.md)[模式采集日志](collect-logs-in-json-mode.md)。
日志服务默认开启全文索引。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将自动生成字段索引。更多信息，请参见[创建索引](create-indexes.md)。
查询分析日志。
单击查询日志，系统将跳转至LogStore查询分析页面。
您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。查询和分析日志的详细步骤，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
说明
如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。
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
