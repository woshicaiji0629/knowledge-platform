# 通过Logtail跨阿里云账号采集Kubernetes容器日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-logtail-to-collect-container-logs-across-accounts

# 通过Logtail跨阿里云账号采集容器日志
本文介绍跨阿里云账号采集阿里云Kubernetes中的容器日志的操作步骤。
## 背景信息
例如某电商公司拥有两个电商应用，部署在阿里云杭州地域的Kubernetes集群中，并使用杭州地域的日志服务进行日志管理。
应用A部署在阿里云账号A（12****456）下的Kubernetes集群中，并使用该账号下的日志服务进行日志管理。
应用B部署在阿里云账号B（17****397）下的Kubernetes集群中，并使用该账号下的日志服务进行日志管理。
现公司业务调整，计划将两个应用的日志集中采集到阿里云账号A（12****456）下的日志服务中，即将两个应用的日志分别采集到同一个日志服务Project下的不同LogStore中。因此您需要新增一个Logtail采集配置、机器组和LogStore，用于采集和存储应用B相关的日志。应用A相关的日志采集保持不变（使用原有的Logtail采集配置、机器组和LogStore）。
## 步骤一：设置阿里云账号为用户标识
## loongcollector 组件配置
设置阿里云账号A为用户标识。
使用阿里云账号B登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
在集群列表页面，单击目标集群名称。
在左侧导航栏，选择应用>Helm。
在Helm页面，选择kube-system命名空间，单击loongcollector应用操作列的更新。
在更新发布的弹框的目标 Helm Chart 的参数配置（Values）区域：
配置aliUid：配置阿里云账号A的ID，多个账号之间使用半角逗号（,）相隔，例如17****397,12****456。
记录baseMachineGroupName的值：该值为机器组用户标识参数，在创建日志服务机器组时需设置用户自定义标识为该值，例如：k8s-group-cc47****54428。在 Helm Chart更新发布对话框的目标版本参数配置区域，accessKeyID和accessKeySecret字段以及clusterAgent字段为需要重点填写的配置项。确认参数后，勾选免责声明并单击确定完成更新。
勾选我已知晓更新时当前参数会被上述内容全量覆盖，并了解相关风险《免责声明》，单击确定更新发布loongcollector应用。
在左侧导航栏，单击工作负载>守护进程集，在kube-system命名空间下，单击loongcollector-ds进入详情页面，确认各个容器组的状态为Running且创建时间为您更新配置后的时间，以确保更新生效。
## logtail-ds 组件配置
设置阿里云账号A为用户标识。
使用阿里云账号B登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择配置管理>配置项。
选择命名空间为kube-system，然后在配置项列表中单击alibaba-log-configuration对应的编辑。
在编辑面板中，完成如下操作，然后单击确定。
在log-ali-uid配置项中增加阿里云账号A的ID，然后记录log-machine-group配置项的值（例如k8s-group-cc47****54428），在创建机器组时需设置用户自定义标识为该值。
多个账号之间使用半角逗号（,）相隔，例如17****397,12****456。
重启logtail-ds，使配置生效。
在logtail-ds详情页面，确认各个容器组的状态为Running且创建时间为您更新配置后的时间。
## 步骤二：创建机器组
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
选择机器组右侧的>创建机器组。
在创建机器组对话框中，配置如下参数，然后单击确定。
其中用户自定义标识需设置为您在[步骤一：设置阿里云账号为用户标识](use-logtail-to-collect-container-logs-across-accounts.md)中获取的机器组标识（例如k8s-group-cc47****54428）。其他参数说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。名称设置为k8s-group，机器组标识选择用户自定义标识，在用户自定义标识输入框中填写自定义标识值（如k8s-group-cc{实例标识}）。
检查机器组中的服务器心跳都为OK。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看容器节点（ECS）的心跳状态。
心跳为OK表示容器节点与日志服务的连接正常。如果显示FAIL请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。确认所有节点的心跳状态均显示为OK，表示机器组创建成功。
## 步骤三：创建Logtail采集配置
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在数据接入区域，单击Kubernetes-文件。
选择目标Project和LogStore，单击下一步。
单击使用现有机器组。
选中您在[步骤二：创建机器组](use-logtail-to-collect-container-logs-across-accounts.md)中所创建的机器组，将该机器组从源机器组移动到应用机器组，单击下一步。
设置Logtail采集配置，单击下一步。
具体参数说明，请参见[通过](use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)[DaemonSet-控制台方式采集容器文本日志](use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode.md)。
重要
默认一个文件只能匹配一个Logtail采集配置。此时账号B下的采集未停止，账号A下的Logtail采集配置无法生效，因此您需要使用如下方式使账号A下的Logtail采集配置生效。
停止账号B下的采集，即使用账号B登录日志服务控制台，从目标机器组中移除Logtail采集配置。具体操作，请参见[应用](manage-machine-groups.md)[Logtail](manage-machine-groups.md)[采集配置到指定机器组](manage-machine-groups.md)。
在账号A下添加强制采集配置。更多信息，请参见[如何实现文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
此处创建Logtail采集配置成功后，请删除阿里云账号B下的原有Logtail采集配置，避免重复采集日志。如何删除，请参见[删除](manage-logtail-configurations-for-log-collection.md)[Logtail](manage-logtail-configurations-for-log-collection.md)[采集配置](manage-logtail-configurations-for-log-collection.md)。
预览数据及设置索引，单击下一步。
日志服务默认开启全文索引。您也可以根据采集到的日志，手动或者自动设置字段索引。更多信息，请参见[创建索引](create-indexes.md)。
## 相关操作
如果您需要将阿里云账号B下的历史数据迁移到当前的LogStore中，可以在原LogStore中创建数据加工任务，将数据复制到当前LogStore中。具体操作，请参见[复制](replicate-data-from-a-logstore.md)[LogStore](replicate-data-from-a-logstore.md)[数据](replicate-data-from-a-logstore.md)。
重要
跨账号加工数据时，需使用自定义角色方式进行授权，此处以自定义角色为例。
第一个角色ARN用于授予数据加工任务使用该角色来读取源LogStore中的数据。角色权限配置说明请参见[授权](access-data-by-using-a-custom-role.md)[RAM](access-data-by-using-a-custom-role.md)[角色只读访问源](access-data-by-using-a-custom-role.md)[LogStore](access-data-by-using-a-custom-role.md)。
第二个角色ARN用于授予数据加工任务使用该角色将数据加工结果写入目标LogStore。角色权限配置说明请参见[授权](access-data-by-using-a-custom-role.md)[RAM](access-data-by-using-a-custom-role.md)[角色写数据到目标](access-data-by-using-a-custom-role.md)[LogStore（跨账号）](access-data-by-using-a-custom-role.md)。
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
