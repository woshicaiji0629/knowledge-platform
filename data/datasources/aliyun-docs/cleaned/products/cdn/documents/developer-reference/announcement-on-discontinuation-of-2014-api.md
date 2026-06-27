# 关于2014旧版API下线的公告-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/developer-reference/announcement-on-discontinuation-of-2014-api

# 关于2014旧版API下线的公告
阿里云CDN 2014旧版API接口已经于2021年2月25日零点起逐步下线。如果您的系统仍在调用2014旧版API，请尽快更新至2018版API，避免因旧版API下线而导致系统服务不可用。如果您有任何疑问，可以提交工单。
## 资源监控
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeDomainBpsData | 查询带宽数据。 | [DescribeDomainBpsData](../api-describedomainsrcbpsdata-1.md) |
| DescribeDomainHitRateData | 查询字节命中率（命中字节百分比）。 | [DescribeDomainHitRateData](../api-describedomainhitratedata.md) |
| DescribeDomainHttpCodeData | 查询 HTTP 返回码的总数和占比数据。 | [DescribeDomainHttpCodeData](../api-describedomainhttpcodedata.md) |
| DescribeDomainQpsData | 获取 5 分钟计算粒度加速域名的每秒访问次数 QPS。 | [DescribeDomainQpsData](../api-describedomainqpsdata.md) |
| DescribeDomainReqHitRateData | 查询请求命中率（命中请求百分比）。 | [DescribeDomainReqHitRateData](../api-describedomainreqhitratedata.md) |
| DescribeDomainSrcBpsData | 查询回源带宽数据。 | [DescribeDomainSrcBpsData](../api-describedomainsrcbpsdata-2.md) |
| DescribeDomainSrcFlowData | 获取回源流量监控数据。 | [DescribeDomainSrcTrafficData](../api-describedomainsrctrafficdata.md) |
| DescribeDomainFlowData | 获取网络流量监控数据。 | [DescribeDomainTrafficData](../api-describedomaintrafficdata.md) |
| DescribeDomainPathData | 获取加速域名路径级别的 5 分钟维度的监控数据，包括流量和访问次数。 | 该功能在 2018 版 API 中不再默认开放，需要提交工单申请使用。 |
| DescribeCdnMonitorData | 查询 CDN 监控数据。 |  |
## 实时监控
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeDomainRealTimeBpsData | 查询加速域名的 1 分钟粒度实时带宽数据。 | [DescribeDomainRealTimeBpsData](../api-describedomainrealtimebpsdata.md) |
## 统计分析
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeDomainRegionData | 获取用户区域分布数据统计。 | [DescribeCdnReport](../api-describecdnreport.md) |
| DescribeDomainISPData | 获取运营商分布数据统计。 | [DescribeCdnReport](../api-describecdnreport.md) |
| DescribeTopDomainsByFlow | 获取按流量排名的加速域名。 | [DescribeCdnReport](../api-describecdnreport.md) |
## 用量查询
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeDomainMax95BpsData | 查询加速域名 95 带宽峰值监控数据。 | [DescribeDomainMax95BpsData](https://help.aliyun.com/zh/document_detail/193704.html#doc-api-Cdn-DescribeDomainMax95BpsData) |
| DescribeDomainsUsageByDay | 查询加速域名天粒度的监控统计数据。 | [DescribeDomainsUsageByDay](../api-describedomainsusagebyday.md) |
## 域名管理
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| BatchSetCdnDomainConfig | 进行域名批量配置。 | [BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md) |
| SetPathCacheExpiredConfig | 设置目录缓存过期功能。 |  |
| SetReqAuthConfig | 设置访问鉴权功能。 |  |
| SetIpBlackListConfig | 设置加速域名的 IP 黑名单。 |  |
| AddCdnDomain | 添加加速域名。 | [AddCdnDomain](../api-addcdndomain.md) |
| DescribeCdnDomainDetail | 查询指定加速域名的基本配置。 | [DescribeCdnDomainDetail](../api-describecdndomaindetail.md) |
| DescribeDomainsBySource | 按源站查询加速域名。 | [DescribeDomainsBySource](../api-describedomainsbysource.md) |
| DescribeUserDomains | 查询用户名下所有的域名与状态。 | [DescribeUserDomains](../api-describeuserdomains.md) |
| DescribeDomainConfigs | 获取指定加速域名的配置。 | [DescribeCdnDomainConfigs](../api-describecdndomainconfigs.md) |
## 日志管理
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeCdnDomainLogs | 查询域名的离线日志下载地址。 | [DescribeCdnDomainLogs](../api-describecdndomainlogs.md) |
## 刷新预热
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeCdnUserQuota | 查询用户配额上限和余量信息。 | [DescribeCdnUserQuota](../api-describecdnuserquota.md) |
| PushObjectCache | 刷新节点上的缓存内容。 |  |
| RefreshObjectCaches | 刷新源站最新文件内容到缓存节点。 |  |
| DescribeRefreshQuota | 获取刷新预热的配额信息。 | [DescribeRefreshQuota](../api-describerefreshquota.md) |
| DescribeRefreshTasks | 获取刷新预热任务信息。 | [DescribeRefreshTasks](../api-describerefreshtasks.md) |
## 服务相关
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeCdnService | 查询 CDN 服务状态。 | [DescribeCdnService](../api-describecdnservice.md) |
| OpenCdnService | 开通 CDN 服务。 | [OpenCdnService](../api-opencdnservice.md) |
## 证书相关
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeDomainCertificateInfo | 查询指定加速域名证书信息。 | [DescribeDomainCertificateInfo](../api-describedomaincertificateinfo.md) |
## 辅助工具
| 2014 旧版 API 名称 | API 功能 | 对应的 2018 版 API 名称 |
| --- | --- | --- |
| DescribeUserVipsByDomain | 按域名查询 VIP 列表。 | [DescribeUserVipsByDomain](../api-describeuservipsbydomain.md) |
| DescribeIpInfo | 验证指定的 IP 是否为阿里云 CDN 节点的 IP 地址。 | [DescribeIpInfo](../api-describeipinfo.md) |
| DescribeL2VipsByDomain | 查询指定域名的 L2 节点的 IP 地址。 | [DescribeL2VipsByDomain](../api-describel2vipsbydomain.md) |
| BlockObjectCaches | 封禁 CDN 节点上指定 URL。 | 该功能在 2018 版 API 中不再默认开放，需要提交工单申请使用。 |
## 视频直播相关接口
阿里云CDN 2014旧版提供的视频直播相关API接口，在CDN 2018版API接口中不再提供。该部分接口功能由阿里云视频直播服务继续提供。
| 2014 旧版 API 名称 | API 功能 | 对应的视频直播 API 名称 |
| --- | --- | --- |
| DescribeLiveStreamTranscodeStreamNum | 实时查询转码流路数。 | DescribeLiveStreamTranscodeStreamNum 说明 该接口仅对白名单用户开放。 |
| DescribeLiveStreamsFrameRateAndBitRateData | 实时查询直播流帧率和码率数据。 | [DescribeLiveDomainFrameRateAndBitRateData](https://help.aliyun.com/zh/live/developer-reference/api-describelivedomainframerateandbitratedata#doc-api-live-DescribeLiveDomainFrameRateAndBitRateData) |
| DeleteLivePullStreamInfo | 删除拉流信息。 | [DeleteLivePullStreamInfoConfig](https://help.aliyun.com/zh/live/developer-reference/api-deletelivepullstreaminfoconfig#doc-api-live-DeleteLivePullStreamInfoConfig) |
| DescribeLiveStreamRecordIndexFile | 查询单个录制索引文件。 | [DescribeLiveStreamRecordIndexFile](https://help.aliyun.com/zh/live/developer-reference/api-describelivestreamrecordindexfile#doc-api-live-DescribeLiveStreamRecordIndexFile) |
| DescribeLiveStreamSnapshotInfo | 查询一段时间内截图内容。 | [DescribeLiveStreamSnapshotInfo](https://help.aliyun.com/zh/live/developer-reference/api-describelivestreamsnapshotinfo#doc-api-live-DescribeLiveStreamSnapshotInfo) |
| AddLivePullStreamInfo | 添加拉流信息。 | [AddLivePullStreamInfoConfig](https://help.aliyun.com/zh/live/developer-reference/api-addlivepullstreaminfoconfig#doc-api-live-AddLivePullStreamInfoConfig) |
| DescribeLiveStreamPushData | 查询推流质量监控数据。 | 该功能在视频直播 API 中不再提供。 |
| CreateLiveStreamRecordIndexFiles | 创建录制索引文件。 |  |
| ResumeLiveStream | 恢复某条直播流的推送。 | [ResumeLiveStream](https://help.aliyun.com/zh/live/developer-reference/api-resumelivestream#doc-api-live-ResumeLiveStream) |
| ForbidLiveStream | 禁止某条流的推送。 | [ForbidLiveStream](https://help.aliyun.com/zh/live/developer-reference/api-forbidlivestream#doc-api-live-ForbidLiveStream) |
| DescribeLiveStreamsOnlineList | 查询指定域名或指定域名下某个应用的所有在线流信息。 | [DescribeLiveStreamsOnlineList](https://help.aliyun.com/zh/live/developer-reference/api-describelivestreamsonlinelist#doc-api-live-DescribeLiveStreamsOnlineList) |
| DescribeLiveStreamRecordIndexFiles | 查询某个时间段内的所有录制索引文件。 | [DescribeLiveStreamRecordIndexFiles](https://help.aliyun.com/zh/live/developer-reference/api-describelivestreamrecordindexfiles#doc-api-live-DescribeLiveStreamRecordIndexFiles) |
| DescribeLiveStreamOnlineUserNum | 查询域名下所有流的在线人数信息。 | [DescribeLiveDomainOnlineUserNum](https://help.aliyun.com/zh/live/developer-reference/api-describelivedomainonlineusernum#doc-api-live-DescribeLiveDomainOnlineUserNum) |
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
