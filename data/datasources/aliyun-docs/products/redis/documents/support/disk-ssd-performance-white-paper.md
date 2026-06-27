# Tair磁盘（SSD）型性能基准测试-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/support/disk-ssd-performance-white-paper

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 磁盘（SSD）型性能白皮书

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍Tair（企业版）磁盘（SSD）型性能测试的测试环境、测试工具、测试方法与测试结果。

## 测试环境

- 

- 

- 

| 测试环境信息 | 说明 |
| --- | --- |
| 地域和可用区域 | 所有测试均在华东 1（杭州）地域的可用区 I 中完成。 |
| Redis 实例架构 | 标准版（双副本）架构，详情请参见 [标准架构](products/redis/documents/product-overview/standard-master-replica-instances.md) 。 |
| 部署压测工具的机器 | [云服务器](products/ecs/documents/user-guide/what-is-ecs.md) [ECS](products/ecs/documents/user-guide/what-is-ecs.md) 实例，规格为 ecs.g6e.13xlarge，规格详情请参见 [实例规格族](products/ecs/documents/user-guide/overview-of-instance-families.md) 。 |
| 磁盘（SSD）型实例规格 | tair.localssd.c1m4.2xlarge tair.localssd.c1m4.4xlarge tair.localssd.c1m4.8xlarge |


测试主要针对下述两种场景进行：

- 

内存大于数据场景：绝大部分数据可以在内存中访问到，此场景下内存与数据的比例约为7:1。

- 

数据大于内存场景：只有部分数据缓存在内存，部分访问请求需要读取硬盘中的数据，根据负载不同，需要访问磁盘的比例也不一样，此场景下内存与数据的比例约为1:4。

## 测试工具

采用开源社区的YCSB压测工具进行压测。YCSB是一款Java编写的支持多种数据库的性能测试工具，具体安装和使用方法请参见[YCSB](https://github.com/brianfrankcooper/YCSB/tree/master/redis)。

本测试中，对YCSB的相关内容做了一定的修改，使其支持导入long类型的recordcount参数、支持测试Redis的String相关命令，修改后的完整源代码请参见[YCSB](https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/120287/cn_zh/1601176553772/YCSB.tar.gz)[源码](https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/120287/cn_zh/1601176553772/YCSB.tar.gz)。

## 测试命令

下述脚本以数据大于内存场景为例。

#! /bin/bash ip=192.168.0.23 port=3100 timeout=30000 command_group=string recordcount=640000000 run_operationcount=20000000 fieldcount=1 fieldlength=100 threads=32 load_sleep_time=600 run_sleep_time=60 echo "##################################### $command_group ############################################" #Load ./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=${ip}" -p "redis.port=${port}" -p "recordcount=${recordcount}" -p "operationcount=${recordcount}" -p "redis.timeout=${timeout}" -p "redis.command_group=${command_group}" -p "fieldcount=${fieldcount}" -p "fieldlength=${fieldlength}" -threads ${threads} sleep ${load_sleep_time} #Uniform-Read ./bin/ycsb run redis -s -P workloads/workloadc -p "redis.host=${ip}" -p "redis.port=${port}" -p "recordcount=${recordcount}" -p "operationcount=${run_operationcount}" -p "redis.timeout=${timeout}" -p "redis.command_group=${command_group}" -p "fieldcount=${fieldcount}" -p "fieldlength=${fieldlength}" -p "requestdistribution=uniform" -threads ${threads} sleep ${run_sleep_time} #Zipfian-Read ./bin/ycsb run redis -s -P workloads/workloadc -p "redis.host=${ip}" -p "redis.port=${port}" -p "recordcount=${recordcount}" -p "operationcount=${run_operationcount}" -p "redis.timeout=${timeout}" -p "redis.command_group=${command_group}" -p "fieldcount=${fieldcount}" -p "fieldlength=${fieldlength}" -p "requestdistribution=zipfian" -threads ${threads} sleep ${run_sleep_time} #Uniform-50%Read-50%Update ./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=${ip}" -p "redis.port=${port}" -p "recordcount=${recordcount}" -p "operationcount=${run_operationcount}" -p "redis.timeout=${timeout}" -p "redis.command_group=${command_group}" -p "fieldcount=${fieldcount}" -p "fieldlength=${fieldlength}" -p "requestdistribution=uniform" -threads ${threads}

表 1.参数说明

- 

- 

| 参数 | 说明 |
| --- | --- |
| ip | Tair 实例的 IP 地址。 |
| port | Tair 实例的服务端口。 |
| timeout | 测试命令的超时时间，单位为 ms。 |
| command_group | 测试类型，配置为 String。 |
| recordcount | 数据加载阶段准备的数据量。 |
| run_operationcount | Run 阶段操作的数据量。本测试中： 内存大于数据场景下，配置和 recordcount 参数相同的值。 数据大于内存场景下，配置的值为 recordcount 参数值除以 32。 |
| fieldcount | 字段个数，配置为 1。 |
| fieldlength | 值长度，配置为 100。 |
| threads | YCSB 线程数，根据实例规格配置。 |


## 测试结果

| 测试指标 | 说明 |
| --- | --- |
| QPS | 每秒处理的读写操作数，单位为次/秒。 |
| Average Latency | 读或写操作的平均延迟，单位为微秒（us）。 |
| 99th Percentile Latency | 处理速度最快的 99%的操作中，最长的延迟时间，单位为微秒。例如该指标的值为 500 微秒，表示 99%的请求可以在 500 微秒内被处理。 |


### 内存大于数据场景

| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.localssd.c1m4.2xlarge | recordcount=40000000 run_operationcount=40000000 threads=64 | Load | 59830 | 1066 | 2761 |
| Uniform-Read | 158221 | 389 | 891 |  |  |
| Zipfian-Read | 164233 | 379 | 873 |  |  |
| Uniform-50%Read-50%Update | 78099 | READ：651 | READ：2012 |  |  |
| UPDATE：974 | UPDATE：2731 |  |  |  |  |
| tair.localssd.c1m4.4xlarge | recordcount=80000000 run_operationcount=80000000 threads=128 | Load | 91991 | 1388 | 3077 |
| Uniform-Read | 302940 | 414 | 921 |  |  |
| Zipfian-Read | 305639 | 410 | 899 |  |  |
| Uniform-50%Read-50%Update | 124929 | READ：798 | READ：2231 |  |  |
| UPDATE：1234 | UPDATE：3013 |  |  |  |  |
| tair.localssd.c1m4.8xlarge | recordcount=160000000 run_operationcount=160000000 threads=256 | Load | 132865 | 1924 | 3323 |
| Uniform-Read | 489287 | 513 | 1313 |  |  |
| Zipfian-Read | 501847 | 499 | 1272 |  |  |
| Uniform-50%Read-50%Update | 187390 | READ：1069 | READ：2749 |  |  |
| UPDATE：1644 | UPDATE：3613 |  |  |  |  |


### 数据大于内存场景

| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.localssd.c1m4.2xlarge | recordcount=1280000000 run_operationcount=1280000000 threads=64 | Load | 50396 | 1258 | 4463 |
| Uniform-Read | 74611 | 842 | 1745 |  |  |
| Zipfian-Read | 106366 | 588 | 1406 |  |  |
| Uniform-50%Read-50%Update | 47833 | READ：1232 | READ：4049 |  |  |
| WRITE：1402 | WRITE：4583 |  |  |  |  |
| tair.localssd.c1m4.4xlarge | recordcount=2560000000 run_operationcount=2560000000 threads=128 | Load | 81097 | 1573 | 4119 |
| Uniform-Read | 118141 | 1071 | 3085 |  |  |
| Zipfian-Read | 194704 | 634 | 1595 |  |  |
| Uniform-50%Read-50%Update | 75625 | READ：1562 | READ：4999 |  |  |
| UPDATE：1795 | UPDATE：5419 |  |  |  |  |
| tair.localssd.c1m4.8xlarge | recordcount=5120000000 run_operationcount=5120000000 threads=256 | Load | 115660 | 2210 | 5235 |
| Uniform-Read | 202365 | 1252 | 3985 |  |  |
| Zipfian-Read | 309019 | 804 | 2551 |  |  |
| Uniform-50%Read-50%Update | 122318 | READ：1861 | READ：5603 |  |  |
| UPDATE：2307 | UPDATE：6415 |  |  |  |  |


## 相关文档

[磁盘型](products/redis/documents/product-overview/essd-based-instances-1.md)

[上一篇：磁盘（ESSD）型性能白皮书](products/redis/documents/support/performance-white-paper-of-essd-based-instances.md)[下一篇：Tair扩展数据结构](products/redis/documents/support/performance-whitepapers-of-tair-extended-data-modules.md)

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
