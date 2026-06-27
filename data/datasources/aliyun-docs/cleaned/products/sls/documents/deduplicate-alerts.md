# 告警降噪控制的合并集合去重机制-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/deduplicate-alerts

# 告警分组合并
告警管理根据路由合并策略对符合条件的告警发送通知。
## 路由合并规则
告警路由合并基于合并基准、行动策略、首次等待时间、变化等待时间和重复等待时间完成。只有上述配置完全相同时，才会被归到同一个合并集合中。
例如某服务中的2个主机分别从20:00和20:01开始每分钟触发一次高CPU告警。此时您可以按照服务名称创建告警合并策略，在首次及新增的告警被发送后，后续重复的告警将被延迟发送。
## 合并基准
合并基准表示根据告警属性和告警标签进行合并。告警提供内置合并基准和自定义合并基准，详细说明如下表所示。
| 合并基本类型 | 说明 |
| --- | --- |
| 内置合并基准 | 日志服务提供内置的合并基准。 按告警源规则+所有标签：由相同告警规则触发的告警，且其标签相同时，合并为一组进行告警通知。 按告警源规则：由相同告警规则触发的告警合并为一组，进行告警通知。 按告警源项目：属于同一 Project 下的告警合并为一组，进行告警通知。 按告警源项目+严重度：属于同一 Project 下的告警，且其严重度相同时，合并为一组进行告警通知。 按告警源项目+所有标签：属于同一 Project 下的告警，且其标签相同时，合并为一组进行告警通知。 |
| 自定义合并基准 | 您使用告警属性和告警标签自定义合并基准。 可作为合并基准的告警属性包括用户 aliuid、告警规则 ID、告警显示名称、告警严重度、规则所在区域和规则所在项目。 可作为合并基准的告警标签包括不使用标签、使用所有标签和自定义标签。 |
## 行动策略
行动策略定义了告警通知的发送方式。您可以在设置告警路由合并策略时或创建告警规则时关联相应的行动策略。如果在合并策略配置中选择了动态行动策略，则优先采用告警规则创建时指定的行动策略。若选择了其他行动策略，则按照合并策略中指定的行动策略。
## 首次等待、变化等待和重复等待
场景1：在首次等待时间内只产生告警A。
假设首次等待时间为5秒、变化等待时间为1分钟、重复等待时间为4小时，橙色表示告警A、蓝色代表告警B。
在00:00:00时，告警A产生，同时告警合并集合被创建，但是由于设置了首次等待时间，所以日志服务不会立即发送通知。
在00:00:05（达到首次等待时间）时，日志服务第一次发送告警通知。
第一次发送告警通知后，以变化等待时间为周期，对合并集合内的告警进行检查。第一个变化等待时间（1分钟）内，告警B产生并进入合并集合。所以在00:01:05时，日志服务第二次发送告警通知。
继续以变化等待时间为周期进行检查，该合并集合内一直只有告警A和告警B。直到距离上次发送告警的间隔达到重复等待时间（4小时），即在04:01:05时，日志服务第三次发送告警通知。
场景2：在首次等待时间内产生了告警A和告警B。
假设首次等待时间为5秒、变化等待时间为1分钟、重复等待时间为4小时，橙色表示告警A、蓝色代表告警B。
在00:00:00~00:00:05期间，告警A和告警B产生，同时告警合并集合被创建，但是由于设置了首次等待时间，所以日志服务不会立即发送通知。
在00:00:05（达到首次等待时间）时，第一次发送告警通知。
第一次发送告警通知后，以变化等待时间为周期，对合并集合内的告警进行检查。在00:00:05~04:01:05期间，该合并集合内一直只有告警A和告警B。直到距离上次发送告警的间隔达到重复等待时间（4小时），即在04:01:05时，第二次发送告警通知。
| 参数 | 说明 |
| --- | --- |
| 首次等待 | 首次创建合并集合后，等待多久发送第一次告警通知。通常设置为秒级别的时间。 |
| 变化等待 | 合并集合内的告警数据（新增告警或告警状态改变）发生变化后，等待多久发送告警通知。通常设置为分钟级别的时间。如果您需要尽快收到告警通知，也可设置为秒级时间。 |
| 重复等待时间 | 合并集合内的告警数据重复（无新增告警和状态变化，仅其他属性例如标题、内容等改变）后，等待多久发送告警通知。通常设置为小时级别的时间。 说明 当您在创建时配置了动态行动策略，则无需在告警策略中配置重复等待时间。系统默认用告警监控规则的重复等待时间覆盖告警分组的重复等待时间。 |
## 示例
创建告警监控规则时，您可以配置不同的告警策略，将触发的告警进行分组合并或者不合并操作。以下是具体示例。
### 场景1：分组合并
按照规则所在项目、env标签和service标签，对告警进行合并。
告警事件
// 告警A { "alert_name": "Alert1", "project": "Project1", "labels": { "env": "test", "service": "service1" } } // 告警B { "alert_name": "Alert2", "project": "Project1", "labels": { "env": "prod", "service": "service2" } } // 告警C { "alert_name": "Alert3", "project": "Project1", "labels": { "env": "test", "service": "service1" } } // 告警D { "alert_name": "Alert4", "project": "Project1", "labels": { "env": "prod", "service": "service2" } }
配置
在分组合并配置面板中，将合并基准设置为自定义，告警属性选择规则所在项目，告警标签设置为自定义，在自定义标签中输入env,service，行动策略选择SLS内置行动策略，首次等待设置为30秒。
合并结果
告警A和告警C归到同一个合并集合中，告警B和告警D被归到同一个合并集合中。
### 场景2：不合并机制
在告警策略的路由合并配置中，如果设置合并基准为告警规则+所有标签，则告警会按照合并基准分到不同合并集合。例如，有如下两个告警监控规则：
告警监控规则1开启分组评估，告警策略配置为不打开高级模式开关，合并基准为告警规则+所有标签。那么告警管理将分别发送主机1告警、主机2告警和主机3告警通知。
告警监控规则2不开启分组评估，告警策略配置为不打开高级模式开关，合并基准为告警规则+所有标签。那么告警管理将发送一条包含所有主机的告警通知。
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
