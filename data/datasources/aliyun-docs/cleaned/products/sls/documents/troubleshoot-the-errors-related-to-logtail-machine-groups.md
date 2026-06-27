# 如何排查Logtail机器组问题-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/troubleshoot-the-errors-related-to-logtail-machine-groups

# Logtail机器组问题排查思路（主机场景）
本文主要介绍如何系统排查主机场景下的机器组无心跳问题。
## 机器组安装示例
| 安装方式 | 适用场景 |
| --- | --- |
| [同账号同地域](loongcollector-installation-linux.md) | 仅当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，所属 [地域](loongcollector-installation-linux.md) 也相同时适用。 |
| [同账号不同地域](loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个阿里云账号，但不属于同一个 [地域](loongcollector-installation-linux.md) 时适用。 |
| [不同账号同地域](loongcollector-installation-linux.md) | 当服务器为阿里云 ECS，且 ECS 与 Project 属于同一个 [地域](loongcollector-installation-linux.md) ，但不属于同一个阿里云账号时适用。 |
| [其他云/自建服务器](loongcollector-installation-linux.md) | 当服务器不是阿里云 ECS，例如自建服务器或其他云服务器时适用。 当服务器为阿里云 ECS，但 ECS 与 Project 不属于同一个阿里云账号，也不在同一个 [地域](loongcollector-installation-linux.md) 时，可视为自建服务器。 |
## 问题排查必读指南
[步骤一：检查](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[是否正常运行](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：检查Logtail在服务器是否正常运行。
[步骤二：确认机器组中的](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[IP](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[地址是否为](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[获取的](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[IP](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[地址](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：确认机器组中的IP地址是否和Logtail的app_info.json文件中的IP地址一致，不一致会导致心跳失败。
[步骤三：检查](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[启动参数是否正确](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：检查ilogtail_config.json文件中配置的Project地域是否正确。
[步骤四：检查网络是否通畅](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：检查服务器与Project之间网络是否通畅。
[步骤五：检查](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[所在服务器的系统时间是否正确](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：如果系统时间明显快于或慢于当前真实时间，需要修改。
[步骤六：跨账号采集需检查用户标识](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：如果服务器类型不是ECS，或使用的ECS与Project属于不同阿里云账号，则必须检查是否配置正确的用户标识。
[步骤七：如果是用户自定义标识机器组，检查是否已配置自定义标识](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：如果机器组是用户自定义标识机器组，检查是否已配置自定义标识。
[步骤八：重启](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)：完成上述修改后，必须重启Logtail。
### 后续步骤
[如何查看](user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](user-guide/how-do-i-view-logtail-collection-errors.md)：心跳OK后，还是采集不到日志，通过查看Logtail错误信息排查。
## 步骤一：检查Logtail是否正常运行
### Linux系统
登录已安装Logtail的机器。
执行如下命令。
ps -ef | grep ilogtail
返回结果中出现两条如下类似信息（分别代表Logtail守护进程和Logtail工作进程）时，说明Logtail正常运行。
UID PID PPID C STIME TTY TIME CMD ... root 12 1 0 Nov10 ? 00:00:00 /usr/local/ilogtail/ilogtail root 14 12 0 Nov10 ? 03:07:43 /usr/local/ilogtail/ilogtail ...
重要
如果返回结果中出现3条及以上Logtail运行信息，则说明当前服务器中有多个Logtail实例在运行，存在重复采集的风险，请检查是否为预期行为。
如果返回结果显示Logtail相关进程未运行。
已经安装Logtail，但是未启动。请参见[启动和停止](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
未安装Logtail，请安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
重要
安装时，请务必选择支持安装Logtail的操作系统、按照日志服务Project所属地域选择安装参数以及根据网络类型选择安装方式。关于网络类型的更多信息，请参见[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
### Windows系统
登录Logtail所在的机器。
打开运行窗口，输入services.msc。
查看LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本）的运行状态。
如果上述服务未运行。
已经安装Logtail，但是未启动。请参见[手动启动和停止](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
未安装Logtail，请安装Logtail。具体操作，请参见[安装](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
重要
安装时，请务必选择支持安装Logtail的操作系统、按照日志服务Project所属地域选择安装参数以及根据网络类型选择安装方式。关于网络类型的更多信息，请参见[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
## 步骤二：确认机器组中的IP地址是否为Logtail获取的IP地址
说明
Logtail获取Linux服务器IP地址的方式如下：
如果您没有设置主机名绑定，则Logtail会获取服务器中第一块网卡的IP地址。
如果想自定义IP地址，可以在[步骤三](troubleshoot-the-errors-related-to-logtail-machine-groups.md)的ilogtail_config.json文件中设置working_ip。设置此参数后，app_info.json文件中的ip字段将自动与working_ip字段值同步更新。关于working_ip，请参见[设置启动参数](configure-the-startup-parameters-of-logtail.md)。
如果您在/etc/hosts文件中设置了主机名绑定，则Logtail会获取绑定的主机名对应的IP地址。
获取app_info.json文件中的ip字段值。
该文件在不同系统下的默认路径说明如下表所示：
| 操作系统 | Logtail | app_info.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/app_info.json |
| Windows（64 位操作系统） | Logtail （64 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\app_info.json |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
Logtail将获取的IP地址记录在app_info.json文件的ip字段中。
{ "UUID" : "", "hostname" : "iZ8vbdlzf******azuhZ", "instance_id" : "E9633380-***********-00163E1AA597_172.16.2.200_166****11", "ip" : "172.**.**.200", "logtail_version" : "1.3.1", "os" : "Linux; 4.19.91-26.1.al7.x86_64; #1 SMP Tue Jul 26 17:52:28 CST 2022; x86_64", "update_time" : "2022-12-27 05:38:33" }
确认机器组中使用的是Logtail获取的IP地址。
日志服务机器组包括IP地址机器组和用户自定义标识机器组。更多信息，请参见[机器组](machine-group-overview.md)。
IP地址机器组：请查看IP地址是否包含[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址。
若不包含，请确认主机IP的正确值，当IP地址文本框内填写了目标Logtail的其它IP地址（例如公网地址）时，修改IP地址机器组内IP地址，若[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址有误，则在[设置](select-a-network-type.md)[Logtail](select-a-network-type.md)[启动参数](select-a-network-type.md)中修改参数working_ip的值并重启Logtail。然后观察机器心跳是否正常。如果正常，则可以结束本次排查。
用户自定义标识机器组：请查看机器组状态是否包含[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址。如果心跳显示OK，则可以结束本次排查流程。
## 步骤三：检查Logtail启动参数是否正确
ilogtail_config.json文件记录了Logtail的相关启动参数。
登录Logtail所在的机器。
查找ilogtail_config.json文件。
该文件在不同系统下的默认路径说明如下表所示：
| 操作系统 | Logtail | ilogtail_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
打开ilogtail_config.json文件，确认配置文件参数是否正确。
{ "config_server_address" : "http://logtail.<config_region>.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "<project地域>", "endpoint" : "<endpoint>" } ], ... }
如果ilogtail_config.json文件中的启动参数符合下述表格中的说明，则表示Logtail启动参数正确。
如果Logtail启动参数错误，请根据下述表格修改ilogtail_config.json文件，然后重启Logtail。具体操作，请参见[重启](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。
Project地域信息请参见[开服地域](sls-supported-regions1.md)。
| 场景 | 网络类型 | <config_region> | <endpoint> |
| --- | --- | --- | --- |
| 服务器为 ECS，且与 Project 属于同一地域 | 阿里云内网 | <project 地域>-intranet | <project 地域>-intranet.log.aliyuncs.com |
| 其它情况 | 公网 | <project 地域> | <project 地域>.log.aliyuncs.com |
| 传输加速 | log-global.aliyuncs.com |  |  |
## 步骤四：检查网络是否通畅
使用Logtail上传数据成功，至少需要保证Logtail所在服务器能够连通下列地址。
重要
如果使用内网，需要在<endpoint>后添加-intranet。
ilogtail_config.json文件中的config_server_address字段指定的地址及其HTTPS版本。
http://<project名>.<endpoint>。
Project的名称和地域，可以通过如下方式查看。
<endpoint>为ilogtail_config.json文件中data_server_list.endpoint字段指定的地址。
http://ali-<project地域>-sls-admin.<endpoint>。其中<endpoint>为ilogtail_config.json文件中data_server_list.endpoint字段指定的地址。
具体的网络检查及解决方法如下：
### Linux系统
登录Logtail所在的机器。
执行curl命令依次连接上述地址。
curl http://<project名>.cn-hangzhou-intranet.log.aliyuncs.com
所有返回结果都为如下类似信息，说明网络畅通。
{"Error":{"Code":"OLSInvalidMethod","Message":"The script name is invalid : /","RequestId":"5D****09"}}
如果网络不畅通，请检查网络环境中80和443端口是否已经开放、目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
### Windows系统
登录Logtail所在的机器。
调用telnet命令依次尝试连接上述地址。
telnet <project名>.cn-hangzhou-intranet.log.aliyuncs.com 80 # 如果是HTTPS协议，则端口号为443。
所有返回结果都为如下类似信息，说明网络畅通。
Trying 100*0*7*5... Connected to xxx. Escape character is '^]'.
如果网络不畅通，请检查网络环境中80和443端口是否已经开放、目标地址是否被拦截以及其他网络方面的检查（例如DNS配置、安全组等）。
## 步骤五：检查Logtail所在服务器的系统时间是否正确
### Linux系统
登录Logtail所在的机器。
执行date命令查看系统时间。
Wed Dec 28 06:59:26 UTC 2022
如果系统时间明显快于或慢于当前真实时间，请尝试如下修改。
调整系统时间至真实时间。
如果不能修改系统时间，请修改Logtail启动参数，即在ilogtail_config.json文件中增加配置项"enable_log_time_auto_adjust": true。修改后，需要重启Logtail。具体操作，请参见[重启](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。ilogtail_config.json文件路径说明请参见[步骤三：检查](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[启动参数是否正确](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。
### Windows系统
登录Logtail所在的机器。
查看桌面右下角任务栏中时间信息。
调整系统时间至真实时间。
如果不能修改系统时间，请修改Logtail启动参数，即在ilogtail_config.json文件中增加配置项"enable_log_time_auto_adjust": true。修改后，需要重启Logtail。具体操作，请参见[重启](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。ilogtail_config.json文件路径说明，请参见[步骤三：检查](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[启动参数是否正确](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。
## 步骤六：跨账号采集需检查用户标识
重要
服务器类型不是ECS，或使用的ECS和Project属于不同阿里云账号，必须检查是否存在正确的用户标识。
用户标识必须是阿里云账号ID（主账号ID）。具体操作请参见[配置用户标识](configure-a-user-identifier.md)。
您可以通过指定目录下的用户标识文件判断是否存在用户标识。如果返回结果为空，则您需要查看指定路径中是否已有用户标识文件。用户标识的作用在于标识这台服务器有权限被该账号访问。
说明
用户标识文件路径如下：
Linux系统：/etc/ilogtail/users/
Windows系统：C:\LogtailData\users\
如果指定路径下无用户标识文件或用户标识文件配置错误，请按照如下方法解决。
Linux系统：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。其中<uid>为Project所属的阿里云账号ID。
Windows系统：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。其中<uid>为Project所属的阿里云账号ID。
如果指定路径下存在以当前Project所属的阿里云账号ID命名的文件，则说明用户标识配置正确。
## 步骤七：如果是用户自定义标识机器组，检查是否已配置自定义标识
若您使用了用户自定义标识机器组，您可以通过指定目录下的user_defined_id文件判断是否已在服务器上配置用户自定义标识。
如果返回结果为空，您需要查看是否存在user_defined_id文件或该文件中是否已配置用户自定义标识。
说明
user_defined_id文件路径如下：
Linux系统：/etc/ilogtail/user_defined_id
Windows系统：C:\LogtailData\user_defined_id
如果user_defined_id文件不存在，则新增一个user_defined_id的文件，然后在文件中输入机器组的用户自定义标识。具体操作，请参见[配置用户自定义标识](create-a-user-defined-identity-machine-group.md)。
如果user_defined_id文件中无用户自定义标识或自定义标识配置错误，则在文件中新增一行，然后输入机器组的用户自定义标识。具体操作，请参见[配置用户自定义标识](create-a-user-defined-identity-machine-group.md)。
如果user_defined_id文件已包含您在机器组中设置的用户自定义标识，则说明用户自定义标识配置正确。
## 步骤八：重启Logtail
完成上述修改后，必须重启Logtail。
### Linux系统
登录Logtail所在的机器。
运行如下命令。
sudo /etc/init.d/ilogtaild restart
### Windows系统
登录Logtail所在的机器。
打开运行窗口，输入services.msc。
重启LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本）。
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
