# 重启实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/restart-instances

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 重启实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当ECS实例完成资源规格、主机名等配置的变更，或需要响应系统运维事件的重启任务时，为使变更正确生效，需通过控制台或API发起重启实例操作，重启会中断业务并存在数据丢失风险。

## 影响与风险

业务中断：重启实例需实例停止再启动，会导致业务中断。

内存数据丢失（强制重启实例）：强制重启实例时，在内存中未及时保存到存储设备的缓存数据会丢失。

## 操作步骤

### 步骤一：重启前检查与准备

- 

评估重启时间：建议在业务低峰期执行该操作。

- 

停止应用程序：在操作系统内部手动停止应用服务，确保所有正在处理的请求和数据写入都已完成。

若希望重启后快速恢复业务，可以检查关键业务程序是否配置开机自启动。

- 

数据备份：为避免服务器重启出现意外后无法恢复数据，建议先[手动创建单个快照](products/ecs/documents/user-guide/create-a-snapshot.md)备份数据，再执行重启操作。

快照属于收费功能，计费详情请参考[快照计费](products/ecs/documents/snapshots-1.md)。

### 步骤二：执行重启操作

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标实例ID进入实例详情页，在页面右上角单击重启。

- 

在弹窗中，选择重启模式。

- 

不勾选强制重启实例（默认）：操作系统会尝试正常关闭所有进程后，执行重启操作。

- 

勾选强制重启实例：相当于执行断电操作，存在丢失内存数据和文件系统损坏的风险，建议仅在实例无法响应非强制重启时使用。

- 

执行重启操作：

- 

立即重启：单击确定即可。

- 

定时执行重启：可以通过勾选设置定时执行，指定未来某一时刻开始执行实例重启操作，根据页面提示完成时间配置及角色选择后，单击确定生成定时重启实例任务。任务创建后可前往[系统运维管理](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)[OOS](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)[控制台-定时运维](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)修改任务配置。

重启实例时，实例内部操作系统需释放进程、CPU、内存等资源，同时虚拟化层也需释放相关资源，整个操作所需的时间可能较长，请耐心等待，预计耗时为3~5分钟，最长不超过20分钟。

## API

可以通过调用以下API重启一台或多台ECS实例。

- 

重启一台处于运行中（Running）状态的ECS实例：[重启实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-rebootinstance.md)。

- 

重启一台或多台处于运行中（Running）状态的ECS实例：[批量重启实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-rebootinstances.md)。

- 

重新启动已过期或欠费回收的ECS实例：[重新激活已过期或欠费回收的实例](products/ecs/documents/developer-reference/api-ecs-2014-05-26-reactivateinstances.md)。

若需定时重启实例，可参考[系统运维管理](https://oos.console.aliyun.com/cn-hangzhou/template/public/detail/ACS-ECS-ScheduleToRebootInstances)[OOS-公共任务模板-定时重启任务](https://oos.console.aliyun.com/cn-hangzhou/template/public/detail/ACS-ECS-ScheduleToRebootInstances)进行配置。

## 常见问题

为什么使用reboot重启实例后变更未生效？

建议通过控制台或API重启ECS实例。这种方式会加载实例的完整配置，从而应用操作系统无法感知的底层变更。因此，在修改实例资源、主机名、离线扩容云盘后，或响应系统运维事件需要重启实例时，必须通过控制台或API重启实例才能使变更生效，此时操作系统内部的reboot命令无效。

实例重启后长时间处于停止或启动中状态怎么办？

可参见[实例启动/停止异常常见问题](products/ecs/documents/support/examples-of-start-or-stop-abnormal-common-problems.md)排查当前实例问题。

如果使用RAM账号重启ECS实例需要什么权限？

若当前用户为RAM用户，需授予ecs:DescribeInstances及ecs:RebootInstance权限。

如何查找和修改已创建的定时重启任务？

通过ECS控制台创建的定时重启任务由云助手执行。查找和修改已有的定时重启任务，路径为：ECS控制台左侧导航栏，选择运维与监控>发送命令/文件（云助手），单击任务页签，在任务列表中找到对应的定时重启任务，单击操作列的修改即可编辑任务的执行计划、命令内容等配置。具体操作，请参见[修改任务执行信息](products/ecs/documents/user-guide/modify-task-execution-information.md)。

## 相关文档

- 

[通过云助手命令停止或重启实例](products/ecs/documents/user-guide/use-a-specified-exit-code-to-stop-or-restart-instances.md)

- 

[修改预约重启时间](products/ecs/documents/user-guide/modify-the-scheduled-restart-time.md)

[上一篇：启动实例](products/ecs/documents/user-guide/start-an-instance.md)[下一篇：停止实例](products/ecs/documents/user-guide/stop-an-instance.md)

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
