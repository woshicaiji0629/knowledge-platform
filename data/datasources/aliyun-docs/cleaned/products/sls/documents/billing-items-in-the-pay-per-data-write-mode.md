# 按写入数据量付费模式计费项-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/billing-items-in-the-pay-per-data-write-mode

# 按写入数据量计费模式计费项
日志服务按写入数据量计费模式的计费项是单独计费的，例如您上传数据会产生数据写入费用，存储日志会产生日志存储费用等。本文介绍日志服务按写入数据量计费模式计费项及付费方式。
## 注意事项
您可以在[日志服务控制台](https://sls.console.aliyun.com)查看前一天的写入流量、读取流量、存储量等信息。
沙特（利雅得）、河源专属云汽车合规地域，不支持使用资源包抵扣按写入数据量计费。
## 什么是OCU？
可观测资源额度OCU（Observability Capacity Unit）是阿里云云原生可观测推出的新版计费单位，可根据每小时资源使用情况自动统计OCU用量，中国站公共云OCU的定价为0.15元/个。
日志服务计算型功能收费计划逐步通过OCU进行计量，以用户实际消耗的计算资源作为计量的度量维度。在 CPU 场景下一个OCU的性能约等于0.5 Core CPU、2 GB内存、3000 IOPS，在计算OCU的总数时，会按照消耗的CPU核心数、内存大小和IOPS三个维度分别计算三个OCU数量，然后取三个OCU数量的最大值作为OCU的最终值，用于计费。
在 GPU 场景下一个OCU的性能约等于 1/60 A10卡的算力，将按照消耗的 GPU 算力计算 OCU 的最终值。
假设您的计算作业消耗了1 Core CPU，2GB内存，3000 IOPS，则这个作业消耗2个OCU。在一个计量周期（1小时）内，计算平均消耗的OCU可参考：数据写入处理器处理1GB数据，大约消耗1/3个OCU。数据加工（新版）处理1GB数据，大约消耗1/3个OCU。规则消费处理1GB数据，约消耗0.3个OCU。
假设您使用 SLS 的向量索引功能向量化一批数据，消耗了1/60 A10卡的算力，则在一个计量周期（1小时）内计量产生了 1 OCU 的用量。
## 计费项说明
日志服务按写入数据量计费模式的计费项如下所示，详细价格说明请参见[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.11.66cd2aab6wAn6p#/sls/detail/sls)。
| 计费项 | 计费说明 | 付费方式 | 免费额度 |
| --- | --- | --- | --- |
| 原始写入数据量 | 数据被上传到日志服务时，按照传输的数据量（未压缩）计算原始写入数据量。 | 按量付费：原始写入数据量费用=日累计原始写入数据量（GB）×每 GB 单价 新版 资源包-预付计划 2.0（推荐） ：换算成资源额度（CU）进行抵扣。 | 无 |
| 存储空间-日志热存储 | 存储超过 30 天后，日志（压缩后）的存储量和日志（未压缩）被建立索引所产生的存储量。 例如：原始日志量为 1 GB，上传到日志服务并配置其中两个字段的索引。上传时的压缩率为 20%，两个目标字段的索引数据量为 0.5 GB，则日志存储空间为 0.2 GB+0.5 GB=0.7 GB。 | 按量付费：存储空间-日志热存储费用=日累计存储量（GB）×每 GB 单价 新版 资源包-预付计划 2.0（推荐） ：换算成资源额度（CU）进行抵扣。 | 无 |
| 存储空间-日志低频存储 | 开启智能存储分层功能时，当日志的存储时间超过您所配置的 热存储层数据保存时间 后，日志将转为低频存储（原冷存储），按照低频存储的存储空间计费。低频存储的存储空间包括日志（压缩后）的存储量和日志（未压缩）被建立索引所产生的存储量。 例如：原始日志量为 1 GB，上传到日志服务并配置其中两个字段的索引。上传时的压缩率为 20%，两个目标字段的索引数据量为 0.5 GB，则低频存储的存储空间为 0.2 GB+0.5 GB=0.7 GB。 | 按量付费：存储空间-日志低频存储费用=日累计存储量（GB）×每 GB 单价 新版 资源包-预付计划 2.0（推荐） ：换算成资源额度（CU）进行抵扣。 | 无 |
| 存储空间-日志归档存储 | 开启智能分层存储功能后，当日志的存储时间超过您所配置的 热存储层数据保存时间 或 低频存储层数据保存时间 后，日志将转为归档存储，按照归档存储的存储空间计费。归档存储的存储空间包括日志（压缩后）的存储量和日志（未压缩）被建立索引所产生的存储量。 例如：原始日志量为 1 GB，上传到日志服务并配置其中两个字段的索引。上传时的压缩率为 20%，两个目标字段的索引数据量为 0.5 GB，则归档存储的存储空间为 0.2 GB+0.5 GB=0.7 GB。 | 按量付费：存储空间-日志归档存储费用=日累计存储量（GB）×每 GB 单价 资源包： 新版 资源包-预付计划，换算成资源额度（CU）进行抵扣 | 无 |
| 外网读取流量 | 从日志服务公网域名所在接口拉取数据时，会产生外网读取流量（按照压缩后的数据量计算）。 | 按量付费：外网读取流量费用=日累计外网读取流量×每 GB 单价 新版 资源包-预付计划 2.0（推荐） ：换算成资源额度（CU）进行抵扣。 | 无 |
| 传输加速 | 按照用户使用传输加速，通过传输加速域名产生的上下行流量进行计费。 传输加速按照实际传输的数据量进行统计，如数据上传场景经过数据压缩，流量统计为压缩后的流量。 更多信息，请参见 [管理传输加速](transmission-acceleration.md) 。 | 按量付费：传输加速费用 = 传输加速产生的上下行流量 × 每 GB 单价 | 无 |
| 写入处理器 | 在日志数据写入 LogStore 前对数据进行处理，例如数据过滤、字段提取、字段扩展、数据脱敏，可以使用写入处理器。写入处理器按照数据处理消耗的资源量进行计费，计费单位为 OCU。 在一个计量周期（1 小时）内，计算平均消耗的 OCU 可参考：数据写入处理器处理 1GB 数据，大约消耗 1/3 个 OCU。 | 按量付费：写入处理器费用=写入处理器消耗资源对应 OCU 数×OCU 单价。 | 无 |
| AI 计算 | 按照用户使用向量索引调用 embedding 模型向量化数据以及调用语义富化 LLM 函数进行数据语义富化消耗的资源量进行计费，计费单位为 OCU。 在一个计量周期（1 小时）内， 调用 `sls-multilang-v3` 模型进行向量化百万 token 大约消耗 3.3 个 OCU。 调用 `qwen-turbo` 模型进行语义富化输入百万 token 大约消耗 3 个 OCU，输出百万 token 大约消耗 6 个 OCU。 | 按量付费：AI 计算=各 AI 计算功能模块消耗的计算资源对应 OCU 数×OCU 单价。 | 无 |
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
