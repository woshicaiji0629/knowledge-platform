# 如何通过Logtail跨阿里云账号采集服务器日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-logtail-to-collect-logs-across-accounts

# 将其他阿里云账号ECS上的日志集中采集到日志服务
介绍如何将一个阿里云账号（源账号）下的ECS服务器日志，统一采集到另一个阿里云账号（目标账号）的日志服务Project中。该方案通过在源ECS上配置授权，允许目标账号的Logtail进行日志采集，实现日志的集中管理和分析。
## 背景信息
您要通过Logtail采集服务器日志时，在服务器上安装Logtail后，还需配置日志服务所在阿里云账号ID为用户标识，表示该账号有权限通过Logtail采集该服务器日志。否则在机器组中会显示服务器心跳失败，导致Logtail无法采集日志到日志服务。
例如某电商公司拥有两个电商应用，部署在阿里云杭州地域的ECS集群上，并使用杭州地域的日志服务进行日志管理。
应用A部署在阿里云账号A（12****456）下的ECS集群（Linux系统）上，并使用该账号下的日志服务进行日志管理。
应用B部署在阿里云账号B（17****397）下的ECS集群（Linux系统）上，并使用该账号下的日志服务进行日志管理。
现公司业务调整，计划将两个应用的日志集中采集到阿里云账号A（12****456）下的日志服务中，即将两个应用的日志分别采集到同一个日志服务Project下的不同LogStore中。因此您需要新增一个Logtail采集配置、机器组和LogStore，用于采集和存储应用B相关的日志。应用A相关的日志采集保持不变（使用原有的Logtail采集配置、机器组和LogStore）。
## 步骤一：创建用户标识文件
登录阿里云账号B下的ECS服务器。
重要
您需要在ECS集群B的每台ECS服务器中创建用户标识文件。
执行如下命令创建用户标识文件。
您需要配置阿里云账号A为用户标识，即创建阿里云账号A的同名文件。更多信息，请参见[配置用户标识](configure-a-user-identifier.md)。
touch /etc/ilogtail/users/12****456
## 步骤二：创建用户自定义标识机器组
在ECS服务器上创建机器组的自定义用户标识文件。
重要
您需要在ECS集群B的每台ECS服务器中创建机器组的用户自定义标识文件。
登录阿里云账号B下的ECS服务器。
在指定目录下创建/etc/ilogtail/user_defined_id文件并添加用户自定义标识。
例如配置用户自定义标识为application_b，则在文件中输入application_b，并保存。文件路径说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。
在日志服务控制台上创建机器组。
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
选择机器组右侧的>创建机器组。
在创建机器组对话框中，配置如下参数，然后单击确定。
其中用户自定义标识需设置为您在步骤[1](use-logtail-to-collect-logs-across-accounts.md)中设置的用户自定义标识。其他参数说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。设置名称为group-b，机器组标识选择用户自定义标识，用户自定义标识填写application_b。
检查机器组中的服务器心跳都为OK。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看使用了相同用户自定义标识的ECS服务器及其心跳状态。
心跳为OK表示ECS服务器与日志服务的连接正常。如果显示FAIL请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。确认机器组中共4台机器的心跳状态均显示为OK，表示所有机器已正常连接至日志服务。
## 步骤三：采集日志
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
单击快速接入。
快速接入数据区域位于日志服务控制台首页右下方，其中包含蓝色的接入数据按钮。
在快速接入数据对话框中，选择正则-文本日志。
在接入数据向导中，选择目标Project和LogStore，单击下一步。
配置机器组配置。
使用场景选择主机场景。
安装环境选择ECS。
选中您在[步骤二](use-logtail-to-collect-logs-across-accounts.md)中创建的机器组，将该机器组从源机器组移动到应用机器组，单击下一步。
创建Logtail采集配置，单击下一步。
具体参数说明，请参见[使用完整正则模式采集日志](collect-logs-in-full-regex-mode.md)。
重要
默认一个文件只能匹配一个Logtail采集配置。此时账号B下的采集未停止，账号A下的Logtail采集配置无法生效，因此您需要使用如下方式使账号A下的Logtail采集配置生效。
停止账号B下的采集，即使用账号B登录日志服务控制台，从目标机器组中移除Logtail采集配置。具体操作，请参见[应用](manage-machine-groups.md)[Logtail](manage-machine-groups.md)[采集配置到指定机器组](manage-machine-groups.md)。
在账号A下添加强制采集配置。更多信息，请参见[如何实现文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
此处创建Logtail采集配置成功后，请删除阿里云账号B下的原有Logtail采集配置，避免重复采集日志。如何删除，请参见[删除](manage-logtail-configurations-for-log-collection.md)[Logtail](manage-logtail-configurations-for-log-collection.md)[采集配置](manage-logtail-configurations-for-log-collection.md)。
在Logtail采集配置表单中，设置配置名称为application_b，日志路径为/tmp/**/*.log，模式选择完整正则模式，开启单行模式。
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
