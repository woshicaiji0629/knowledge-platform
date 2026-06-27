# 为告警监控规则添加标签和标注-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/labels-and-annotations

# 添加标签和标注
在创建告警监控规则时，您可以设置标签（labels）和标注（annotations）信息。标签主要应用于告警降噪、通知路由和管理分派等场景，标注主要应用于内容模板、管理分派等场景。
## 标签
标签主要应用于告警降噪、通知路由和管理分派等场景。
### 添加标签
在创建告警监控规则时添加。例如添加标签env和team。
说明
建议标签的名称为英文字符。
标签为静态文本，支持自定义。触发的告警会自动添加该标签作为告警属性。
在分组评估中指定的字段可自动成为标签。
### 使用场景
告警去重
标签属于触发告警的标识性属性，是告警指纹中的一部分，可用于告警去重。比如系统产生两条告警Alert1和Alert2，因为标签信息（labels）相同，只保留其中一条告警数据。告警指纹原理，请参见[基于告警指纹去重](deduplicate-alerts-based-on-fingerprints.md)。
// Alert1 { "aliuid": "12345", "project": "Project1", "alert_id": "alert-123", "labels": { "host": "host-1" }, "annotations": { "title": "CPU使用率过高", "desc": "CPU当前使用率为90%" } } // Alert2 { "aliuid": "12345", "project": "Project1", "alert_id": "alert-123", "labels": { "host": "host-1" }, "annotations": { "title": "CPU使用率过高", "desc": "CPU当前使用率为95%" } }
内容模板中引用标签
标签属于map类型，当您在告警规则中添加了标签，您可在告警内容模板中通过${labels}引用标签信息。
降噪控制
在告警策略中，标签信息可作为降噪控制的合并基准。比如您在合并基准时使用按告警规则+所有标签进行合并配置，如下图。更多信息，请参见[合并基准](deduplicate-alerts.md)。
通知分派
告警管理系统和通知管理系统根据标签属性进行告警管理和通知分派。比如您在配置行动策略时，根据标签配置不同的行动组，如下图。
## 标注
标注主要应用于内容模板、管理分派等场景。
### 添加标注
在创建告警监控规则时添加。例如添加如下标注。
说明
建议标注的名称为英文字符。
固定有title和desc两个属性。
title是告警固定的非标识性属性，可以在通知内容模板中以${annotations.title}被引用。
desc是告警固定的非标识性属性，可以在通知内容模板中以${annotations.desc}被引用。
触发告警的非标识性属性，键值对格式，值可以是动态的。例如标注信息为"annotations": {"title": "${service} CPU使用率过高","desc": "${service} CPU当前使用率为90%"}。
您在配置标注内容时可以使用内置变量，也可引用分组评估中的字段变量。引用分组评估中的字段变量时，实际值为触发告警时对应的属性值。使用的内置变量如下表。
| 变量 | 说明 |
| --- | --- |
| __count__ | 分组后每组的行数（不分组时，默认所有结果在一个组） |
| __pass_count__ | 分组后每组满足条件的行数（不分组默认所有数据在一个组） |
| __0_count__ | 第一个查询结果的行数 |
| __1_count__ | 第二个查询结果的行数 |
| __2_count__ | 第三个查询结果的行数 |
| aliuid | 阿里云账号 ID |
| alert_instance_id | 告警触发的实例的 ID |
| alert_id | 告警规则 ID |
| alert_name | 告警规则名称 |
| project | 告警规则所在 Project |
### 使用场景
告警管理系统和通知管理系统根据标注属性进行告警管理和通知分派。例如您可在告警策略中根据标注属性作为条件配置不同的分组合并。在行动策略中根据标注属性作为条件配置不同的行动组。
## 自动标注
自动标注是对告警标注的补充。您在配置告警监控规则时，打开自动添加标注开关后，系统自动添加字段到标注中。
说明
当字段中存在多个值时，默认选择第一个值添加到标注中。
内置字段__count__表示集合操作结果的行数。
分组
您在配置告警监控规则时，配置分组评估为标签自定义或标签自动，且打开自动添加标注开关，则系统自动将集合操作结果中的非分组字段和内置字段（__count__）添加到标注中。
例如集合操作结果中包括host和pv，并且根据host字段进行分组，则开启标签自动添加功能后，pv字段和__count__字段将被添加到标注中。
未分组
您在配置告警监控规则时，配置分组评估为不分组，且打开自动添加标注开关，则系统自动将集合操作结果中的所有字段和内置字段（__count__）添加到标注中。
例如集合操作结果中包括host和pv，则开启标签自动添加功能后，host字段、pv字段和__count__字段将被添加到标注中。
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
