# 如何通过Logtail导入历史日志文件-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/import-historical-logs

# 导入历史日志文件
Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。如果您需要采集历史日志，可使用Logtail自带的导入历史日志文件功能。
重要
本文介绍的基于 local_event.json 的历史文件采集方式已不再推荐使用。
日志服务已推出全新的[一次性采集主机文本日志](one-time-collection-of-host-text-logs.md)功能。新版功能支持通过控制台批量下发配置、支持断点续传、具备完善的进度监控和资源控制能力。请优先选择新版功能进行历史数据导入。
## 前提条件
已在服务器上安装0.16.15（Linux系统）或1.0.0.1（Windows系统）及以上版本的Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)或[安装](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
已创建Logtail配置并应用到机器组。具体操作，请参见[文本日志概述](overview-10.md)。
说明
如果该Logtail配置只用来导入历史日志文件，可以设置一个不存在的采集路径。
## 背景信息
Logtail基于监听文件的修改事件进行日志采集，还支持从本地文件中加载事件，以驱动日志采集。采集历史日志文件就是基于本地事件加载实现的功能。
说明
导入本地事件最长延迟为1分钟。
由于加载本地事件属于特殊行为，Logtail会向服务器发送LOAD_LOCAL_EVENT_ALARM消息。
如果您导入的文件量较大，建议修改Logtail启动参数，建议将CPU调整至2.0及以上，内存调整至512MB及以上。更多信息，请参见[设置](configure-the-startup-parameters-of-logtail.md)[Logtail](configure-the-startup-parameters-of-logtail.md)[启动参数](configure-the-startup-parameters-of-logtail.md)。
如果您的日志文件中存在中文，需要设置文件字符集。
您需要在Logtail的安装目录下执行导入历史日志文件的操作，该安装目录在不同操作系统中位于不同位置，具体说明如下表所示。
| 操作系统 | Logtail | Logtail 安装目录 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail |
## 操作步骤
获取Logtail配置的唯一标识。
您可以在Logtail安装目录下的user_log_config.json文件中获取Logtail配置的唯一标识。此处以Linux系统为例，查看Logtail配置的唯一标识。
grep "##" /usr/local/ilogtail/user_log_config.json | awk '{print $1}'
添加本地事件。
在Logtail安装目录下，创建local_event.json文件。
在local_event.json文件中添加本地事件，类型为标准JSON，格式如下所示。
重要
为了防止Logtail加载无效的JSON，建议您先将本地事件配置保存在临时文件中，编辑完成后拷贝到local_event.json文件中。
[ { "config" : "${your_config_unique_id}", "dir" : "${your_log_dir}", "name" : "${your_log_file_name}" }, { ... } ... ]
| 参数 | 说明 |
| --- | --- |
| config | 填写步骤 [1](import-historical-logs.md) 中获取的 Logtail 配置唯一标识，例如 ##1.0##log-config-test$ecs-test 。 |
| dir | 历史日志文件所在目录，例如： /data/logs 。 重要 文件夹不能以 / 结尾。 文件夹目录不能是 Logtail 安装目录（ /usr/local/ilogtail ）。 |
| name | 历史日志文件名，支持通配符，例如 access.log.2018-08-08、access.log*。 |
本文以Linux系统为例，介绍配置示例。
$ cat /usr/local/ilogtail/local_event.json [ { "config": "##1.0##log-config-test$ecs-test", "dir": "/data/log", "name": "access.log*" }, { "config": "##1.0##log-config-test$tmp-test", "dir": "/tmp", "name": "access.log.2017-08-09" } ]
## 常见问题
检查Logtail是否加载Logtail配置。
通常情况下，保存local_event.json文件后，Logtail会在1分钟内将文件内容加载到内存中，并将local_event.json文件中的内容清空。
您可以通过以下方式检查Logtail是否已加载Logtail采集配置。
local_event.json文件中的内容被清空，则说明Logtail已读取到事件信息。
检查Logtail安装目录中的ilogtail.LOG文件中是否包含process local event参数。如果local_event.json文件被清空但未查询到process local event参数，可能是因为local_event.json文件内容不合法而被过滤。
已加载Logtail采集配置但未采集到数据，是什么原因？
Logtail采集配置不合法。
local_event.json文件配置不合法。
日志文件不在Logtail采集配置已设定的路径下。
该日志文件已被Logtail采集过。
## 后续操作
导入历史文件采集成功后，查询和分析请参见[通过索引模式查询和分析日志](query-and-analyze-logs-in-index-mode.md)。
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
