# 通过Logtail跨地域采集日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/cross-region-log-collection-through-logtail-and-alibaba-cloud-account

# 通过Logtail跨地域采集日志
本文以Linux系统为例介绍同阿里云账号跨地域采集日志的操作步骤。
## 方案概览
假如某公司的网站应用部署在地域A，日志服务Project部署在地域B，现计划通过Logtail采集配置将部署在地域A的ECS实例中的日志数据发送到地域B的日志服务Project中。您可通过以下步骤配置：
[步骤一：在地域](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[A](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[的](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[ECS](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[实例中安装](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[Logtail](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)
[步骤二：在地域](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[A](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[的](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[ECS](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[实例中配置用户自定义标识](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)
[步骤三：在地域](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[B](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[的日志服务](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[Project](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[中创建用户自定义标识机器组](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)
[步骤四：在地域](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[B](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[的日志服务](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[Project](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[中创建](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[Logtail](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)[采集配置](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)
配置流程图如下所示：
## 前提条件
已创建Project和LogStore。更多信息，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[创建基础](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## 步骤一：在地域A的ECS实例中安装Logtail
### 网络传输说明
| 传输方式 | 适用场景 |
| --- | --- |
| 公网 | 阿里云云服务器实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 |
| 传输加速 | 服务器分布在海外各地的自建机房或者来自海外云厂商，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，推荐选择 传输加速 。更多信息，参见 [管理传输加速](transmission-acceleration.md) 。 |
登录地域A的ECS实例，请参考[网络传输说明](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)根据您的网络环境选择安装Logtail脚本。安装Logtail支持的Liunx系统，请参见[使用限制](install-logtail-on-a-linux-server.md)。
### 公网
根据日志服务Project所在地域，获取对应的${region_id}。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
执行以下命令下载Logtail安装脚本并完成安装，注意替换${region_id}为实际地域值。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-internet
### 传输加速
根据日志服务Project所在地域，获取对应的${region_id}。
重要
各地域对应的${region_id}请参见[开服地域](sls-supported-regions1.md)，例如华东 1（杭州）对应的${region_id}为cn-hangzhou。
使用传输加速安装Logtial后，需要进入Project，开启传输加速域名后方可生效。具体操作，请参见[开启](transmission-acceleration.md)[Project](transmission-acceleration.md)[的传输加速域名](transmission-acceleration.md)。
执行以下命令下载Logtail安装脚本并完成安装，注意替换${region_id}为实际地域值。
wget http://logtail-release-${region_id}.oss-${region_id}.aliyuncs.com/linux64/logtail.sh -O logtail.sh chmod +x logtail.sh ./logtail.sh install ${region_id}-acceleration
## 步骤二：在地域A的ECS实例中配置用户自定义标识
在指定目录下建立用户自定义标识文件user_defined_id并配置用户自定义标识。
重要
同一机器组中不允许同时存在Linux和Windows服务器，请勿在Linux和Windows服务器上配置相同的用户自定义标识。
一个服务器可配置多个用户自定义标识，标识之间以换行符分割。
Linux环境
登录已安装Logtail的Linux服务器，使用以下命令配置用户自定义标识。
说明
如果目录/etc/ilogtail/不存在，请先手动创建该目录。
echo "user-defined-1" > /etc/ilogtail/user_defined_id
（可选）使用以下命令检查用户自定义标识是否写入成功。如果返回user-defined-1，则表示写入成功。
cat /etc/ilogtail/user_defined_id
新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如果需要立即生效，请执行以下命令重启Logtail。
/etc/init.d/ilogtaild stop /etc/init.d/ilogtaild start
Windows环境
登录已安装Logtail的Windows服务器，在C:\LogtailData目录下新建user_defined_id文件并写入user-defined-1，完成后保存。
说明
如果目录C:\LogtailData不存在，请先手动创建该目录。
新增、删除、修改user_defined_id文件后，默认情况下，1分钟内生效。如需立即生效，请根据以下步骤重启Logtail。
选择开始>控制面板>管理工具>服务。
在服务对话框中，选择对应的服务。
如果是0.x.x.x版本，选择LogtailWorker服务。
如果是1.0.0.0及以上版本，选择LogtailDaemon服务。
右键单击重新启动使配置生效。
容器环境
用户自定义标识配置在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID中，可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID命令查看。
## 步骤三：在地域B的日志服务Project中创建用户自定义标识机器组
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表，单击打开目标Project。
左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。
在弹出的创建机器组页面，填写以下信息，并单击确定。
| 参数 | 说明 |
| --- | --- |
| 名称 | 机器组 名称，命名规则如下所示： 只能包括小写字母、数字、短划线（-）和下划线（_）。 必须以小写字母或者数字开头和结尾。 长度必须在 2~128 字符之间。 重要 创建后，不支持修改机器组名称，请谨慎填写。 |
| 机器组标识 | 选择 IP 地址 。 |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。更多信息，请参见 [日志主题](log-topics.md) 。 |
| IP 地址 | 填入 Logtail 自动获取的服务器 IP。 重要 存在多台服务器时，请手动输入对应的 IP 地址，IP 地址之间需使用换行符分隔。 同一机器组中不允许同时存在 Linux 和 Windows 服务器。请勿将 Windows 和 Linux 服务器 IP 添加到同一 机器组 中。 |
在机器组列表中，单击目标机器组。在机器组配置页面，检查机器组配置信息以及服务器状态。
## 步骤四：在地域B的日志服务Project中创建Logtail采集配置
重要
安装Logtail的主机需要在出口方向开放80（HTTP）端口和443（HTTPS）端口。ECS实例的端口由安全组规则控制，添加安全组规则的步骤请参见[添加安全组规则](../../ecs/documents/user-guide/add-a-security-group-rule.md)。
服务器日志的内容持续新增。Logtail只采集增量日志，如果下发Logtail配置后日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
如需采集历史数据，请参见[导入历史日志文件](import-historical-logs.md)。
## 相关文档
使用Logtail采集日志后，如果预览页面为空或查询页面无数据，请按照[Logtail](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)进行排查。在使用Logtail采集日志时，可能遇到正则解析失败、文件路径不正确、流量超过Shard服务能力等错误。查看Logtail采集错误的步骤，请参见[如何查看](user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](user-guide/how-do-i-view-logtail-collection-errors.md)。采集数据常见的错误类型请参见[日志服务采集数据常见的错误类型](log-collection-error-type.md)。
默认情况下，一个日志文件只能匹配一个Logtail配置。如果同一份日志需要被采集多份，请参见[如何实现文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
将企业内网服务器日志采集到日志服务，请参见[采集企业内网服务器日志](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
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
