# 心跳异常问题汇总排查-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/troubleshooting-of-abnormal-heartbeat-problems

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 心跳异常问题汇总排查

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

机器组心跳用于检测服务器与日志服务间的通信状态，若心跳异常将导致数据无法传输至日志服务。本文将分析心跳异常的产生原因及常见场景的解决方案。

## 心跳异常原因分析

服务器上的LoongCollector通过以下配置项，来确定目标Project并上报心跳，因此解决心跳异常并不复杂，仅需确认配置项取值，并检查网络情况即可。

- 

日志服务Project所属阿里云主账号：指定该账号有权限访问、采集这台服务器的日志。

- 

Project所属地域与传输方式：日志服务访问域名由地域和传输方式动态拼接生成，需确保服务器与访问域名之间网络通畅。相关概念请参考[网络传输方式与域名](products/sls/documents/loongcollector-installation-linux.md)。

- 

用户自定义标识/IP：通过IP或用户自定义标识与机器组关联，建立心跳。

### 建立心跳的过程

- 

LoongCollector获取配置的一个或多个阿里云账号ID信息，地域与传输方式拼接组成的访问域名，用户自定义标识或IP信息。

- 

LoongCollector上报心跳与上述信息至指定地域中的Project。

- 

符合条件的一个或多个Project比较机器组中IP或用户自定义标识与上送信息是否一致。

- 

信息一致的一个或多个Project将成功建立心跳，机器组显示心跳为OK。

## 常见心跳异常场景

### 新增加的服务器心跳为FAIL

心跳为FAIL时，可能是初次建立心跳需要花费一些时间，请等待两分钟左右后刷新心跳状态，若仍为FAIL，请按如下步骤检查：

- 

检查LoongCollector安装场景选择是否有误，若安装场景正确进行下一步。否则请卸载后重新安装。

- 

- 

| 安装方式 | 适用场景 |
| --- | --- |
| [同账号同地域](products/sls/documents/loongcollector-installation-linux.md) | 仅当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，所属 [地域](products/sls/documents/loongcollector-installation-linux.md) 也相同时适用。 |
| [同账号不同地域](products/sls/documents/loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，但不属于同一个 [地域](products/sls/documents/loongcollector-installation-linux.md) 时适用。 |
| [不同账号同地域](products/sls/documents/loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个 [地域](products/sls/documents/loongcollector-installation-linux.md) ，但不属于同一个阿里云账号时适用。 |
| [其他云/自建服务器](products/sls/documents/loongcollector-installation-linux.md) | 当服务器不是阿里云 ECS，例如自建服务器或其他云服务器时适用。 当服务器为阿里云 ECS，但 ECS 与 Project 不属于同一个阿里云账号，也不在同一个 [地域](products/sls/documents/loongcollector-installation-linux.md) 时，可视为自建服务器。 |


- 

在服务器上通过sudo /etc/init.d/loongcollectord status查看LoongCollector启动状态，返回loongcollector is running表示启动成功。否则执行如下命令启动LoongCollector：

若使用的是Logtail采集器，则查看Logtail启动状态命令为：sudo /etc/init.d/ilogtaild status，启动Logtail命令为：sudo /etc/init.d/ilogtaild start。sudo /etc/init.d/loongcollectord start

- 

若是跨账号场景（Project所属阿里云账号与服务器所属账号不同）：需手动配置用户ID文件，使该账号有权限访问、采集这台服务器的日志。

检查用户ID文件内容

- 

请检查是否存在/etc/ilogtail/users/{阿里云账号ID}文件，若不存在请创建。

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。注意需要复制主账号ID。

- 

在安装了LoongCollector的服务器上，以主账号ID作为文件名，创建用户ID文件。

touch /etc/ilogtail/users/{阿里云账号ID} #以主账号ID作为文件名，无需配置文件后缀。

- 

检查文件名是否满足下列要求，不满足请修改。

- 

{阿里云账号ID}必须为主账号ID。

- 

{阿里云账号ID}应为日志服务Project所属的主账号ID，而非服务器所属的账号。

- 

确认地域与传输方式正确，并能联通访问域名：查看服务器上/usr/local/ilogtail/ilogtail_config.json文件中region信息是否与日志服务Project地域的[RegionID](products/sls/documents/loongcollector-installation-linux.md)一致。一致则排查下一步，若不一致则修改：

测试访问域名联通性并修改服务器配置

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。

- 

单击Project名称右侧的进入项目概览页面。

- 

在访问域名中可查看当前Project的域名信息，替换${project名称}为Project名称，${域名信息}为公网域名后在服务器上执行命令。

curl https://${project名称}.${域名信息}

- 

返回类似信息{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}，说明网络畅通。否则检查目标地址是否被拦截以及其他网络方面的检查（例如出口方向是否开放80（HTTP）端口和443（HTTPS）端口、DNS配置、安全组等）。

返回Error信息是因为访问链接缺少必要参数。当前测试仅验证网络连通性，未使用完整链接，因此在网络正常的情况下会显示Error的提示信息。

- 

修改/usr/local/ilogtail/ilogtail_config.json中参数：

- 

config_servers：此参数为获取采集配置路径，修改为"http://logtail.${域名信息}"，其中${域名信息}替换为公网域名。

- 

data_servers：

- 

region：此参数为数据传输使用的地域信息，修改为"${RegionID}"，其中${RegionID}替换为日志服务Project地域的[RegionID](products/sls/documents/loongcollector-installation-linux.md)。

- 

endpoint_list：此参数为数据传输使用的路径，修改为"${域名信息}"，其中${域名信息}替换为公网域名。

- 

保存修改后重启LoongCollector。

若使用的是Logtail采集器，重启命令为：sudo /etc/init.d/ilogtaild restartsudo /etc/init.d/loongcollectord restart

- 

检查用户自定义标识或IP的值：

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。

- 

单击资源，单击机器组，在机器组中单击目标机器组。

- 

查看机器组配置页面，并确认机器组标识内容后选择对应操作：

## 用户自定义标识

- 

确认服务器上是否存在/etc/ilogtail/user_defined_id文件，若不存在请创建。

- 

向该文件中写入自定义的字符串作为用户自定义标识，此处以user-defined-test-1为例。

#向指定文件写入自定义字符串 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id

- 

修改用户自定义标识的取值为自定义的字符串，此例为user-defined-test-1。

## IP地址

将服务器上/usr/local/ilogtail/app_info.json中ip字段的信息添加到IP地址中。

ip取值规则：若已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。若没有设置主机名绑定，自动获取本机第一块网卡的IP地址。若设置了/usr/local/ilogtail/ilogtail_config.json中的working_ip参数，则以working_ip值作为服务器的IP地址。请至少保证一种情况下能获取到ip，否则ip字段值为空，无法建立心跳。

### 服务器曾经心跳成功但当前为FAIL

曾经心跳成功说明配置项正确，若机器组类型为用户自定义标识型，则配置项中阿里云主账号信息，地域与传输方式，用户自定义标识等是固定值，未修改不会改变心跳状态，可能需要检查网络能否联通访问域名。若机器组类型为IP型，则最有可能是IP地址冲突或IP改变导致心跳为FAIL，请参考如下步骤解决：

- 

在服务器上重启LoongCollector以获取最新IP信息。

若使用的是Logtail采集器，重启命令为：sudo /etc/init.d/ilogtaild restartsudo /etc/init.d/loongcollectord restart

- 

在服务器上查看/usr/local/ilogtail/app_info.json中ip字段的信息。

ip取值规则：若已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。若没有设置主机名绑定，自动获取本机第一块网卡的IP地址。若设置了/usr/local/ilogtail/ilogtail_config.json中的working_ip参数，则以working_ip值作为服务器的IP地址。

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。

- 

单击资源，单击机器组，在机器组中单击目标机器组。

- 

查看机器组配置页面，确认IP地址中信息是否包含/usr/local/ilogtail/app_info.json中ip字段。若不包含则添加ip字段的值到IP地址中。

- 

若一致但心跳仍为FAIL，则不适合使用IP型机器组，请切换机器组类型后尝试。

### 切换机器组标识类型后心跳FAIL

出现IP地址冲突或IP改变等情况时，不再适合使用IP型机器组，需切换为用户自定义标识型机器组。切换机器组类型并不影响网络联通情况，阿里云主账号信息，地域与传输方式等信息，因此仅需关注用户自定义标识取值是否正确。

- 

确认是否存在/etc/ilogtail/user_defined_id文件，若不存在请创建。

- 

向该文件中写入自定义的字符串作为用户自定义标识，此处以user-defined-test-1为例。

#向指定文件写入自定义字符串 echo "user-defined-test-1" > /etc/ilogtail/user_defined_id

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。

- 

单击资源，单击机器组，在机器组中单击目标机器组。

- 

查看机器组配置页面，并确认以下两项参数取值，若不正确请单击右上角修改，修改后保存。

- 

机器组标识：用户自定义标识。

- 

用户自定义标识：自定义的字符串，此例为user-defined-test-1。

## 常见问题

### 按文档排查后，各项配置均正确添加，为何心跳仍FAIL？

如果确认配置正确且网络正常，心跳为FAIL一般有两种可能：

- 

在该区域较长一段时间内无采集配置，心跳发送间隔被抑制

- 

向每个返回的区域发送请求获取配置时，为了降低对服务端的压力，如果从一个区域得不到采集配置，会降低对该区域的请求频率，最长间隔可达到 12 分钟，如果该值超过了该区域心跳 FAIL 的阈值，就会导致心跳 FAIL。

- 

解决办法：忽略心跳 FAIL，直接向该机器所在的机器组上应用采集配置，然后等待下一次向该区域发起请求，心跳即可恢复。如果希望立即恢复的话，重启即可。

- 

当前使用的配置并不是ilogtail_config.json中配置

- 

示例：使用了一个非默认配置启动后，运行期间ilogtail_config.json被修改而未重启。

- 

检查方法：

- 

最简单的办法：重启后自动加载最新配置。

- 

查看日志：如果担心对采集有影响，可以查看/usr/local/ilogtail/ilogtail.LOG文件，从开头处查找关键字load logtail config file，该行日志会包含当前运行中使用的配置，检查是否和本地文件一致。

[上一篇：通过修改配置解决常见采集问题](products/sls/documents/resolve-common-collection-issues-through-configuration-changes.md)[下一篇：Logtail机器组问题排查思路（主机场景）](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)

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
