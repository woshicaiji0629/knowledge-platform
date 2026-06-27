# 配置Range回源-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/object-chunking

# 配置Range回源
Range回源，指CDN节点在回源的HTTP请求里面携带了Range信息，源站在收到CDN节点的回源请求时，根据HTTP请求头中的Range信息返回指定范围的内容数据给CDN节点。Range回源可有效提高文件分发效率，减少回源流量消耗和源站压力，并且提升资源响应速度。
## 背景信息
Range是HTTP请求头之一，可用来指定需获取的内容的范围。例如，Range: bytes=0-100表示回源请求该文件的前101个字节的数据内容。
开启Range回源功能后，CDN收到用户的请求时，如果CDN节点上未缓存该资源或资源已过期，CDN节点回源会采用Range请求，从源站分段获取用户需要的部分资源并缓存到CDN节点上。
开启Range回源的工作原理如下图所示：
## 注意事项
开启Range回源有以下注意事项：
开启Range回源前需确认源站是否支持Range请求，即HTTP请求头中包含Range字段，并且源站能够响应正确的206文件分片。如果源站不支持Range请求，开启Range回源可能导致缓存异常或客户端请求失败。
Range回源是可选配置项，控制台默认未开启。
Multipart Ranges特性状态默认关闭，开启Range回源功能也不会同步开启Multipart Ranges特性，请[提交工单](https://smartservice.console.aliyun.com/service/create-ticket?spm=a2c4g.11186623.0.0.629c1faeE1XJOx)申请开启Multipart Ranges特性。
开启Range回源功能以后，会导致回源的QPS升高，如果源站有设置频次控制功能，需要注意避免触发源站的限流；规避办法是通过[DescribeL2VipsByDomain](../developer-reference/api-cdn-2018-05-10-describel2vipsbydomain.md)查询回源节点的IP地址 ，并且将回源节点的IP加入源站的访问IP白名单。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击视频相关。
在Range回源区域，单击修改配置。
根据下方的参数介绍，选择不使用Range回源，跟随客户端Range请求或开启Range回源（大文件场景推荐配置）。
当选择跟随客户端Range请求或者开启Range回源（大文件场景推荐配置）时，可以设置分片大小。分片大小默认为512 KB。
| 参数 | 选项 | 描述 | 示例 |
| --- | --- | --- | --- |
| Range 回源 | 不使用 Range 回源 | 默认为 不使用 Range 回源 ，无论客户端是否使用 Range 请求 CDN 节点， CDN 节点回源时都会请求整个文件，在大文件场景下的文件分发效率较低。 | 例如，客户端向 CDN 节点发起的请求中含有 Range: bytes=0-100 ，则 CDN 节点向源站发起的请求中不会携带 Range 参数。源站会响应 CDN 节点完整文件（假设完整文件大小为 10 MB，源站就会响应 10 MB 的文件给 CDN 节点）， CDN 节点收到源站响应的文件后，会将文件缓存下来，同时响应客户端 Range: bytes=0-100 的内容。 |
| 跟随客户端 Range 请求 | 开启 跟随客户端 Range 请求 后，当客户端使用 Range 请求 CDN 节点时， CDN 节点才会采用 Range 请求回源。 CDN 节点第一次回源请求会按照用户请求中的 Range 大小向上取整来请求用户源站（此处的向上取整为分片大小的整数倍），后面全部按照用户指定的分片大小来请求用户源站。 | 例如，当分片大小为 512 KB 时，如果客户端向 CDN 节点发起的请求中含有 Range:bytes=0-614399 （即 600 KB）， CDN 节点上如果没有缓存文件，则第一次回源请求会按照 1024KB 的分片大小回源（600 KB 向上取整为 1024KB），后续客户端访问此文件的其他未缓存的分片， CDN 节点将按照 512KB 的分片大小访问源站。 |  |
| 开启 Range 回源（大文件场景推荐配置） | 开启 Range 回源（大文件场景推荐配置） 后，无论客户端是否使用 Range 请求 CDN 节点， CDN 节点都会采用 Range 请求回源。 CDN 节点的所有回源 Range 请求都按照用户指定的分片大小来请求用户源站。 | 无 |  |
| 分片大小 | 512 KB 1 MB 2 MB 4 MB | 回源模式为 跟随客户端 Range 请求 或 开启 Range 回源（大文件场景推荐配置） 的情况下可以设置 Range 分片大小，默认按 512 KB 生效。 | 1 MB |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 | 不使用 |
单击确定，完成配置。
## HTTP Range超出有效区间的兼容性配置
CDN回源OSS源站获取大文件的场景下，如果OSS响应了cache-control:no-cache不缓存策略，或者客户端请求访问CDN触发Range请求回源OSS时，可能会出现异常，具体表现为：下载异常缓慢甚至超时（30秒左右）、下载至超Range片时触发连接中断（如文件末尾的最后一片）。
未设置兼容策略情况下的行为
如果HTTP Range请求合法，响应返回值为206并在响应头中包含Content-Range。如果HTTP Range请求不合法，或者指定范围不在有效区间，会导致Range不生效，响应返回值为200，并传送整个Object内容。如下为HTTP Range请求不合法的示例及错误说明。
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。为避免指定的Range超出范围，可在Range读取前进行[HeadObject](../../../oss/documents/developer-reference/headobject.md)请求，获取对象大小。
Range: byte=0-499：格式错误，byte应为bytes。
Range: bytes=0-1000：末字节1000超出有效区间。
Range: bytes=1000-2000：指定范围超出有效区间。
Range: bytes=1000-：首字节超出有效区间。
Range: bytes=-2000：指定范围超出有效区间。
可以通过如下命令测试Range参数的有效性：
curl -r 0-100 http://xxxx.oss-cn-hangzhou.aliyuncs.com/xx.zip -o /tmp/xx1.zip -v
设置兼容策略以后的行为
使用HTTP Range时，增加请求头x-oss-range-behavior:standard，可以改变指定范围不在有效区间时OSS的行为。行为改变的示例如下：
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。如通过HTTP Range请求获取大文件的部分内容时，因选取了无效的范围，导致OSS返回InvalidRange错误码，请参见[OSS](../../../oss/documents/user-guide/http-status-code-416.md)[返回](../../../oss/documents/user-guide/http-status-code-416.md)[416](../../../oss/documents/user-guide/http-status-code-416.md)[错误](../../../oss/documents/user-guide/http-status-code-416.md)进行解决，详细错误信息如下：
The requested range cannot be satisfied
Range: bytes=500-2000：末字节超出有效区间，返回500~999字节范围内容。
Range: bytes=1000-2000：首字节超出有效区间，返回错误416 (InvalidRange)。
Range: bytes=1000-：首字节超出有效区间，返回错误416 (InvalidRange)。
Range: bytes=-2000：指定范围超出有效区间，返回0~999字节，即完整的文件内容。
针对上述内容，本文提供如下HTTP Range请求示例。
说明
此处假设Object资源大小为1000字节，Range有效区间为0~999。
请求Object资源0~499字节范围内的内容。
GET /ObjectName Range: bytes=0-499 Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 02:51:30 GMT Authorization: Sigature 206 (Partial Content) content-length: 500 content-range: bytes 0-499/1000 connection: keep-alive etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA928B227D52731327DE078 date: Fri, 18 Oct 2019 02:51:30 GMT [500 bytes of object data]
请求Object资源第500字节到文件结尾的内容。
GET /ObjectName Range: bytes=500- Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 03:24:39 GMT Authorization: Signature 206 (Partial Content) content-length: 500 content-range: bytes 500-999/1000 etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA9307750EBE33332E3720A date: Fri, 18 Oct 2019 03:24:39 GMT [500 bytes of object data]
请求Object资源最后500字节的内容。
GET /ObjectName Range: bytes=-500 Host: bucket.oss-cn-hangzhou.aliyuncs.com Date: Fri, 18 Oct 2019 03:23:22 GMT Authorization: Signature 206 (Partial Content) content-length: 500 content-range: bytes 500-999/1000 etag: "CACF99600561A31D494569C979E6FB81" x-oss-request-id: 5DA9302A6646AC37397F7039 date: Fri, 18 Oct 2019 03:23:22 GMT [500 bytes of object data]
说明
建议在大文件（平均单个文件大小在20 MB以上）内容分发场景下，CDN回源OSS的配置中都进行该项配置。
如果在阿里云OSS源站上开启了访问鉴权功能，并且由客户端来实现回源请求的签算，那么客户端在签算的时候需要把回源请求头x-oss-range-behavior:standard加入签算。阿里云OSS计算签名时会包含所有x-oss-前缀的请求头。若客户端签算未包含x-oss-range-behavior请求头将导致签名不一致而被拒绝。
## 相关API
[批量配置域名](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)
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
