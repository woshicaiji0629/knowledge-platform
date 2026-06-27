# 创建CDN报警规则-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/set-an-alert-rule

# 设置报警
当您需要监控CDN域名的使用情况时，可以创建报警规则。如果资源的监控指标达到报警条件，云监控自动发送报警通知，帮助您及时得知异常监控数据，并快速处理。
## 前提条件
已成功添加域名，具体请参见[添加加速域名](../add-a-domain-name.md)。
已开通云监控服务。尚未开通的用户可登录[云监控产品首页](https://www.aliyun.com/product/jiankong)开通服务。
## 操作步骤
进入云监控控制台。
方式一：登录[云监控控制台](https://cloudmonitornext.console.aliyun.com/)。
方式二：
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，单击页面右上角的监控告警设置，跳转到云监控控制台。
在左侧导航栏，选择云资源监控>云产品监控。
筛选并进入CDN监控页面。
单击创建报警规则。
在创建报警规则面板中，设置下表中的报警规则相关参数，其他参数保持默认即可。如果您需要了解其他参数配置情况，请参见[创建报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-rule)。
| 参数 | 说明 |
| --- | --- |
| 产品 | 选择 CDN 。 |
| 资源范围 | 报警规则作用的资源范围。取值： 全部资源 ：报警规则作用于 CDN 所有域名上，对于新添加的域名生效。 应用分组 ：报警规则作用于 CDN 的指定应用分组内的全部域名上，对于新添加的域名生效。 实例 ：报警规则作用于 CDN 的指定域名。 |
| 规则描述 | 报警规则的主体。当监控数据满足报警条件时，触发报警规则。规则描述的设置方法如下： 单击 添加规则 ，在下滑菜单中选择合适的指标类型。 在 添加规则描述 面板，先输入 规则名称 ，再设置规则条件。 简单指标 ：先选择监控指标，再为其设置阈值和报警级别。 组合指标 ：先选择报警级别，再配置多指标报警描述为两个或两个以上的监控指标设置报警条件。 说明 如果设置了多个指标报警规则，则目标资源必须在每个指标上均有数据，只有在满足条件后才能够正常触发报警。例如：在多指标报警规则中，如果包含公网的监控指标，而 ECS 主机资源并未配置公网 IP，则将无法正常触发报警。 表达式 ：先选择报警级别，再配置报警表达式。 智能阈值 ：关于智能阈值的更多信息，请参见 [概览](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/overview-alert) 和 [创建智能阈值报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-a-dynamic-threshold-alarm-rule) 。 说明 关于如何设置复杂的报警条件，请参见 [报警规则表达式说明](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/alert-rule-expressions#concept-2276873) 。 |
| 通道沉默周期 | 报警发生后未恢复正常，间隔多久重复发送一次报警通知。取值：5 分钟、15 分钟、30 分钟、60 分钟、3 小时、6 小时、12 小时和 24 小时。 某监控指标达到报警阈值时发送报警，如果监控指标在通道沉默周期内持续超过报警阈值，在通道沉默周期内不会重复发送报警通知；如果监控指标在通道沉默周期后仍未恢复正常，则云监控再次发送报警通知。 例如：当 通道沉默周期 选择 12 小时 时，如果报警未恢复正常，则间隔 12 小时后，云监控会再次发送报警通知。 |
| 生效时间 | 报警规则的生效时间。报警规则仅在生效期内才会发送报警通知。 说明 当报警规则不在生效期时，不会发送报警通知，但是报警历史记录仍然会显示在报 警历史列表 中。 |
| 报警联系人组 | 发送报警的联系人组。 应用分组的报警通知会发送给该报警联系人组中的报警联系人。报警联系人组是一组报警联系人，可以包含一个或多个报警联系人。 关于如何创建报警联系人和报警联系人组，请参见 [创建报警联系人或报警联系人组](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-contact-or-alert-contact-group#task-2514452) 。 |
| 标签 | 报警规则的标签。包括标签名称和标签值。 说明 您最多可设置 6 组标签。 |
单击确认。
## 报警规则配置示例
您可以参照以下示例为CDN域名配置报警规则，及时得知异常监控数据并快速处理。
### 配置单个指标监控
例如：当指定域名下行流量的最小值大于等于500 Mbytes，连续3个周期触发紧急报警；当下行流量的最大值大于等于300 Mbytes，连续3个周期触发警告报警。资源范围和规则描述的配置项建议如下。
资源范围：实例。
关联资源：选择目标域名example.aliyundoc.com。
在资源范围区域，单击实例页签。
规则描述
各报警级别的通知方式不同：紧急为电话+短信+邮件+WebHook，警告为短信+邮件+WebHook，普通为邮件+WebHook。
| 参数 | 示例值 |
| --- | --- |
| 指标类型 | 简单指标 |
| 监控指标 | 实例维度 > 下行流量 |
| 阈值及报警级别 | 周期均选择 连续 3 个周期（1 周期=1 分钟） 。 报警级别： 紧急 ，最小值大于等于 500 Mbytes。 报警级别： 警告 ，最大值大于等于 300 Mbytes。 报警级别： 普通 ，平均值大于等于 100 Mbytes。 |
### 配置多个指标监控
例如：当指定域名下行流量的最大阈值大于等于300 Mbps，或回源状态码502占比最大阈值大于等于1%，任意一个指标连续3个周期触发警告报警。资源范围和规则描述的配置项建议如下。
资源范围：实例。
关联资源：选择目标域名example.aliyundoc.com。
规则描述
| 参数 | 示例值 |
| --- | --- |
| 指标类型 | 组合指标 |
| 报警级别 | 警告（Warn） |
| 指标类型 | 标准创建 |
| 多指标报警描述 | 单击 添加指标 ，在 监控指标 下拉框中选择 实例维度 > 下行流量 。 设置最大值大于等于 300 Mbytes。 然后参照以上步骤依次设置 实例维度 > 回源状态码 502 占比 指标，最大值大于等于 1%。 说明 关于如何设置复杂的报警条件，请参见 [报警规则表达式说明](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/alert-rule-expressions#concept-2276873) 。 |
| 多指标关系 | 有一个满足条件就报警（||） |
| 发出报警需要满足达到阈值的次数 | 连续 3 个周期（1 周期=1 分钟） |
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
