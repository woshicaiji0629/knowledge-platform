# 状态码缓存过期时间配置与规则-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/user-guide/create-a-cache-rule-for-http-status-codes

# 配置状态码过期时间
CDN节点从源站获取资源时，源站会返回响应状态码，您可以在阿里云CDN上配置状态码缓存时间，当客户端再次请求相同资源时，由CDN直接响应状态码，不会触发回源，减轻源站压力。当状态码超过设置的缓存时间，会重新触发回源。
## 适用场景
配置状态码过期时间主要适用于源站响应了异常状态码的情况下，用于指定CDN节点上执行的缓存处理动作。
正常情况下CDN节点成功从源站获取到所请求的资源，即源站响应了2xx状态码时，会按照[阿里云](configure-the-cdn-cache-expiration-time.md)[CDN](configure-the-cdn-cache-expiration-time.md)[默认缓存规则及优先级](configure-the-cdn-cache-expiration-time.md)进行缓存。如果源站无法迅速响应所有状态码（例如非2xx状态码），且不希望所有请求全部由源站响应，那么可以配置状态码过期时间，由CDN节点直接响应状态码，减轻源站压力。
典型场景
文件A在源站已被删除，但客户端仍持续访问，CDN节点没有缓存文件A，所有针对文件A的请求都将被转发回源，由源站响应4xx状态码，这将会大幅增加源站的压力。如果CDN节点上配置了缓存4xx状态码，那么CDN节点针对文件A的请求首次回源后，会缓存4xx状态码，在预设缓存时间内，当客户端再次请求文件A时，将会由CDN节点直接响应4xx状态码，无需回源。
## 异常状态码缓存规则
对于204、305、404、405、414、424、429、500、501、502、503和504状态码，缓存规则如下：
如果源站返回set-cookie响应头，CDN不缓存。
如果源站没有返回Set-Cookie响应头，则遵循CDN控制台配置的状态码过期时间来缓存，配置多条规则时生效方式请参考多条规则生效优先级说明。
如果源站没有返回Set-Cookie响应头，CDN控制台也没有配置状态码过期时间，则按照源站设置的Pragma、Cache-Control或者Expires响应头来缓存。
如果源站没有返回Set-Cookie、Pragma、Cache-Control或者Expires响应头，CDN控制台也没有配置状态码过期时间，则默认缓存1秒。
对于302、307和403状态码，缓存规则如下：
如果源站返回set-cookie响应头，CDN不缓存。
如果源站没有返回Set-Cookie响应头，则遵循CDN控制台配置的状态码过期时间来缓存，配置多条规则时生效方式请参考多条规则生效优先级说明。
如果源站没有返回Set-Cookie响应头，CDN控制台也没有配置状态码过期时间，则按照源站设置的Pragma、Cache-Control或者Expires响应头来缓存。
如果源站没有返回Set-Cookie、Pragma、Cache-Control或者Expires响应头，CDN控制台也没有配置状态码过期时间，不缓存。
针对304状态码，CDN将不进行缓存，且无法通过任何方式设置缓存时间。
对于其他异常状态码，如400状态码，缓存规则如下：
如果源站返回set-cookie响应头，CDN不缓存。
如果源站没有返回Set-Cookie响应头，则遵循CDN控制台配置的状态码过期时间来缓存，配置多条规则时生效方式请参考多条规则生效优先级说明。
其他场景不缓存。
对于采用range方式回源的请求，CDN节点如果收到源站响应的非206状态码，则CDN节点会删除已缓存的分片文件（回源超时不会删除缓存文件）。
Range回源情况下，源站会把一个大文件分割成多个小的文件分片来返回给CDN节点。比如有个文件被分割成了10个分片，CDN节点已经缓存了5个分片，在请求第6个分片时，源站响应了5xx状态码，这时会把前面已经缓存的5个分片全部删除。
## 多条规则生效优先级说明
支持设置多条状态码缓存规则，当某个请求同时匹配了多条规则时，只会有一条规则生效，生效规则如下：
判断顺序：
先判断规则类型（文件后缀名＞目录），再判断规则创建时间（先创建的＞后创建的）。
不同类型规则的生效优先级：文件后缀名＞目录。
例如，如果用户的请求同时匹配了2条规则（均配置了404状态码），规则类型分别为文件后缀名和目录类型，404状态码的过期时间以类型为文件后缀名的规则为准。具体示例，请参见[配置示例](create-a-cache-rule-for-http-status-codes.md)。
相同类型规则的生效优先级：先创建的＞后创建的（规则列表由上而下）。
例如，如果用户的请求同时匹配2条规则（均配置了404状态码），规则类型相同（均为文件后缀名或均为目录类型），404状态码的过期时间以“最早创建”的规则为准。具体示例，请参见[配置示例](create-a-cache-rule-for-http-status-codes.md)。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击缓存配置。
单击状态码过期时间页签。
单击添加，配置状态码过期时间。
| 类型 | 注意事项 |
| --- | --- |
| 类型 | 支持 目录 和 文件后缀名 这两种类型，请根据您的实际需求选择。 说明 不同类型规则的生效优先级：文件后缀名＞目录，具体请参见 [异常状态码缓存规则](create-a-cache-rule-for-http-status-codes.md) 。 |
| 地址 | 类型选择为 目录 ，填写说明如下： 每次只能添加一条目录。 支持输入目录的完整路径，须以正斜线（/）开头，例如 /directory/aaa 。 类型选择为 文件后缀名 ，填写说明如下： 支持输入一个或多个文件后缀名，多个文件后缀名用半角逗号（,）分隔，例如 jpg,txt 。 说明 不同记录中配置的文件后缀名类型完全相同，仅有大小写区分时，后面创建的会覆盖掉前面创建的，例如创建 jpg,txt 规则后，再创建 jpg,txt 规则时，会覆盖掉之前创建的 jpg,txt 记录。此时，如果需要配置小写规则，可以单独创建 txt 和 jpg 的规则。配置规则实际生效的时候是严格区分大小写。 不支持用星号（*）匹配所有的文件类型。 |
| 状态码过期时间设置 | 需要缓存的状态码及其缓存时间，最长可设置 3 年，单位：秒，配置规则如下： 多个状态码用半角逗号（,）分隔。 对于 2xx、3xx 状态码，仅支持单个精准配置，不支持模糊批量配置。例如，201=10（支持），2xx=12（不支持）。 对于 4xx、5xx 状态码，既支持单个精准配置，也支持模糊批量配置。例如，401=10（支持），4xx=12（也支持）。 |
| 优先遵循源站缓存策略 | 开启后，如果源站响应了缓存策略标头（包括 Cache-Control 和 Pragma ），那么源站响应的缓存策略将会优先生效。 |
| 忽略源站不缓存标头 | 开启后， CDN 节点将会忽略源站响应的以下几个缓存策略标头（这几个标头均表示不缓存）。 Cache-Control: no-store Cache-Control: no-cache Cache-Control: max-age=0 Pragma: no-cache |
| 客户端跟随 CDN 缓存策略 | 开启后， CDN 节点会将最终生效的缓存策略响应给客户端。 |
| 强制内容重新验证 | 该参数只在缓存过期时间为 0 时生效，使用效果如下： 关闭（默认）： CDN 的缓存过期时间配置为 0 时， CDN 节点上不缓存文件，每次请求都需要回源获取内容。 开启： CDN 的缓存过期时间配置为 0 时，支持在 CDN 节点上缓存文件，每次请求都需要回源验证缓存内容。 |
单击确定，完成配置。
成功配置状态码过期时间后，您可以在状态码过期时间列表中，对当前的配置进行修改或删除操作。
## 配置示例
示例一：目录类型规则
创建目录类型规则如下图所示：
在/directory/aaa目录下，所有4xx状态码缓存时间为10秒，201状态码缓存时间为15秒，在该时间区间内，由CDN节点直接响应对应的访问请求；超过该时间后，会触发回源。
示例二：文件后缀名类型规则
创建文件后缀名类型规则如下图所示：
文件后缀为.jpg或.txt类型，403状态码缓存时间为10秒，404状态码缓存时间为15秒，在该时间区间内，由CDN节点直接响应对应的访问请求；超过该时间后，会触发回源。
示例三：不同类型规则的生效优先级
分别创建了一条“目录类型规则”和一条“文件后缀名类型规则”，设置了不同的状态码过期时间，如下图所示：
用户请求http://example.com/directory/aaa/test.jpg，CDN节点上没有缓存资源，CDN节点向源站请求资源，源站响应了404状态码，这里同时匹配上了“目录类型规则”和“文件后缀名类型规则”，因为在规则类型不同的情况下，规则生效优先级是文件后缀名＞目录，所以“文件后缀名类型规则”生效，404状态码的实际缓存时间是20秒。
示例四：相同类型多条规则的生效优先级
先创建了一条“目录类型规则一”，匹配的地址是“/directory”，然后再创建另一条“目录类型规则二”，匹配的地址是“/directory/aaa”，设置了不同的状态码过期时间，如下图所示：
用户请求http://example.com/directory/aaa/test.jpg，CDN节点上没有缓存资源，CDN节点向源站请求资源，源站响应了404状态码，这里同时匹配上了两条“目录类型规则”，因为在规则类型相同的情况下，规则生效优先级是早创建的＞晚创建的，所以最早创建的“目录类型规则一”生效，404状态码的实际缓存时间是15秒。
## 相关API
[BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md)
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
