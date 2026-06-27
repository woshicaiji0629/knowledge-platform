# 云助手状态异常时如何处理-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions

# 查看云助手状态及异常状态处理
本文介绍如何查看云助手状态，以及云助手状态异常时如何处理。
## 查看云助手状态
## 控制台
访问[ECS](https://ecs.console.aliyun.com/cloud-assistant/region)[控制台-云助手](https://ecs.console.aliyun.com/cloud-assistant/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在ECS实例页签下，查看云助手状态。
正常：云助手运行良好，可以正常使用。
在ECS 云助手页面的实例列表中，查看云助手状态列，确认目标实例的状态显示为正常。
未安装：实例上没有安装云助手Agent，您可以参考以下方式安装云助手Agent。
单击一键安装自动化安装云助手Agent。
一键安装云助手Agent时，需要重启实例才能生效。
手动安装云助手Agent，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
在 ECS 云助手控制台的实例列表中，若目标实例的云助手状态列显示为未安装，可单击对应的一键安装按钮完成安装。
异常：出现异常的原因较多，需要根据具体原因来分析。更多信息，请参见[云助手异常状态处理](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
在ECS 云助手控制台的ECS实例页签中，实例列表的云助手状态列会展示各实例的云助手运行状态，状态为异常时以黄色图标标识。
## API
调用[DescribeCloudAssistantStatus](../developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)，返回参数中"CloudAssistantStatus": "true"代表云助手状态正常，如果状态异常，请参见[云助手异常状态处理](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
## 云助手异常状态处理
## Linux实例
远程连接Linux实例。
具体操作，请参见[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行如下命令，查看云助手安装目录是否存在。
CoreOS操作系统
cd /opt/local/share/ ls
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）
cd /usr/local/share/ ls
如果aliyun-assist文件夹存在，请继续执行步骤[3](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
如果aliyun-assist文件夹不存在，说明云助手被卸载，需要重新[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
查看云助手服务状态。
先确定ECS实例的初始化系统，不同内核版本的Linux系统，查看云助手服务状态命令不同。
ls -l /sbin/init
如果输出指向systemd例如/lib/systemd/systemd，说明系统使用systemd。
如果输出指向upstart例如/sbin/upstart，说明系统使用Upstart。
如果输出指向init例如/sbin/init，说明系统使用sysvinit。
## systemd
执行如下命令，查看云助手状态。
systemctl status aliyun.service
当云助手状态为inactive (dead)，说明云助手服务已停止，需要执行systemctl start aliyun.service启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
[ @iZuf68j5ei93s share]# systemctl status aliyun.service ● aliyun.service - Aliyun Assist Loaded: loaded (/etc/systemd/system/aliyun.service; enabled; vendor preset: enabled) Active: inactive (dead) since Mon 2023-09-11 17:18:33 CST; 47s ago Process: 1951 ExecStart=/usr/local/share/aliyun-assist/2.2.3.515/aliyun-service (code=exited, status=0/SUCCESS) Main PID: 1951 (code=exited, status=0/SUCCESS) Tasks: 2 (limit: 22694) Memory: 1.3G CGroup: /system.slice/aliyun.service ├─5608 gpg-agent --homedir /var/cache/dnf/remi-modular-6408ecca79e22107/pubring --use-standard-socket --daemon └─5648 gpg-agent --homedir /var/cache/dnf/remi-safe-ff04689114f71b24/pubring --use-standard-socket --daemon
当云助手状态为active (running)，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
[root@iZuf68j5ei93s8 ~ share]# systemctl status aliyun.service ● aliyun.service - Aliyun Assist Loaded: loaded (/etc/systemd/system/aliyun.service; enabled; vendor preset: enabled) Active: active (running) since Mon 2023-09-11 17:25:07 CST; 2s ago Main PID: 72998 (aliyun-service) Tasks: 10 (limit: 22694) Memory: 1.3G CGroup: /system.slice/aliyun.service ├─ 5608 gpg-agent --homedir /var/cache/dnf/remi-modular-6408ecca79e22107/pubring --use-standard-socket --daemon ├─ 5648 gpg-agent --homedir /var/cache/dnf/remi-safe-ff04689114f71b24/pubring --use-standard-socket --daemon └─72998 /usr/local/share/aliyun-assist/2.2.3.515/aliyun-service
## Upstart
执行如下命令，查看云助手状态。
/sbin/initctl status aliyun-service
当云助手状态为stop/waiting，说明云助手服务已停止，需要执行/sbin/initctl start aliyun-service启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
/sbin/initctl status aliyun-service aliyun-service stop/waiting
当云助手状态为start/running，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
/sbin/initctl status aliyun-service aliyun-service start/running, process 1129
## sysvinit
执行如下命令，查看云助手状态。
/etc/init.d/aliyun-service status
当云助手状态为Stopped，说明云助手服务已停止，需要执行/etc/init.d/aliyun-service start启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
[root@i7bp1hfzscxxx ~]# /etc/init.d/aliyun-service status Stopped
当云助手状态为Running，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
[root@i7bplhtzscxxxxxx ~]# /etc/init.d/aliyun-service status Running
在控制台查看云助手Agent状态。
如果云助手Agent状态为正常，说明异常已解决。
如果云助手Agent状态依旧异常，需要查看云助手日志来具体分析。
CoreOS操作系统：
cd /opt/local/share/aliyun-assist/<version>/log tail -100f aliyun_assist_main.log
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）：
cd /usr/local/share/aliyun-assist/<version>/log tail -100f aliyun_assist_main.log
## Windows实例
远程连接Windows实例。
具体操作，请参见[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录](connect-to-a-windows-instance-through-workbench.md)[Windows](connect-to-a-windows-instance-through-workbench.md)[实例](connect-to-a-windows-instance-through-workbench.md)。
查看云助手安装目录C:\ProgramData\aliyun\assist是否存在。
如果assist文件夹存在，请继续执行[步骤](check-the-status-of-cloud-assistant-and-handle-exceptions.md)[3](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
如果assist文件夹不存在，说明云助手被卸载，需要重新安装云助手，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
查看云助手服务状态。
单击开始菜单，选择Windows 管理工具>计算机管理。
选择计算机管理（本地）>服务和应用程序>服务。
找到Aliyun Assist Service，查看Aliyun Assist Service状态。
若状态列为正常运行，表示Aliyun Assist Service状态正常。
若状态列无显示，表示Aliyun Assist Service已停止，请单击启动，启动Aliyun Assist Service。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
在控制台查看云助手Agent状态。
如果云助手Agent状态为正常，说明异常已解决。
如果云助手Agent状态还是异常，需要查看云助手日志来具体分析。
云助手默认日志路径：C:\ProgramData\aliyun\assist\<version>\log，<version>为云助手Agent的具体版本号。
该目录下重点关注aliyun_assist_main.log及其日期轮转备份文件（如aliyun_assist_main.log.20230912），通过查看这些日志文件定位云助手 Agent 异常原因。
## 常见问题
### 为什么云助手日志中出现context deadline exceeded (Client.Timeout exceeded while awaiting headers)错误信息？
time="2023-05-23T00:01:17+08:00" level=info msg=GET_HOST_ERROR time="2023-05-23T00:04:17+08:00" level=info msg="http://100.100.100.200/latest/meta-data/region-id cn-shanghai <nil>" time="2023-05-23T00:04:22+08:00" level=info msg="https://cn-shanghai.axt.aliyun.com/luban/api/connection_detect Get \"https://cn-shanghai.axt.aliyun.com/luban/api/connection_detect\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:22+08:00" level=info msg="Poll region id for instance in classic network" time="2023-05-23T00:04:27+08:00" level=info msg="https://cn-hangzhou.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-hangzhou.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:32+08:00" level=info msg="https://cn-qingdao.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-qingdao.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:37+08:00" level=info msg="https://cn-beijing.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-beijing.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:42+08:00" level=info msg="https://cn-zhangjiakou.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-zhangjiakou.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:47+08:00" level=info msg="https://cn-huhehaote.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-huhehaote.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:52+08:00" level=info msg="https://cn-shanghai.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-shanghai.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:04:57+08:00" level=info msg="https://cn-shenzhen.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-shenzhen.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:05:02+08:00" level=info msg="https://cn-hongkong.axt.aliyun.com/luban/api/classic/region-id Get \"https://cn-hongkong.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:05:07+08:00" level=info msg="https://eu-west-1.axt.aliyun.com/luban/api/classic/region-id Get \"https://eu-west-1.axt.aliyun.com/luban/api/classic/region-id\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)" time="2023-05-23T00:05:07+08:00" level=info msg=GET_HOST_ERROR
出现该错误一般是ECS实例与云助手服务器间的网络连通异常，您可以运行以下命令，查看网络连通性。
说明
请将<region-id>替换为地域的ID。更多信息，请参见[地域和可用区](regions-and-zones.md)。
ping <region-id>.axt.aliyun.com curl https://<region-id>.axt.aliyun.com/luban/api/instance/instance-id
正常情况下域名能够正常解析并且连通，且接口能够返回正常的instance_id。
若不能解析或者不能正常返回实例ID，则说明实例网络存在问题，需要进行排查。具体操作，请参见[配置云助手](configure-network-permissions-for-the-cloud-assistant-agent.md)[Agent](configure-network-permissions-for-the-cloud-assistant-agent.md)[网络权限](configure-network-permissions-for-the-cloud-assistant-agent.md)。
[ xxx@iZuf62n-xxx : ~]# ping -c 5 cn-shanghai.axt.aliyun.com PING cn-shanghai.axt.aliyun.com (100.100.xxx) 56(84) bytes of data. 64 bytes from 100.100.36.108 (100.100.xxx): icmp_seq=1 ttl=102 time=1.32 ms 64 bytes from 100.100.36.108 (100.100.xxx): icmp_seq=2 ttl=102 time=1.30 ms 64 bytes from 100.100.36.108 (100.100.xxx): icmp_seq=3 ttl=102 time=1.32 ms 64 bytes from 100.100.36.108 (100.100.xxx): icmp_seq=4 ttl=102 time=1.30 ms 64 bytes from 100.100.36.108 (100.100.xxx): icmp_seq=5 ttl=102 time=1.30 ms --- cn-shanghai.axt.aliyun.com ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 4005ms rtt min/avg/max/mdev = 1.295/1.305/1.318/0.010 ms [ @iZuf62njf1dkb ~]# curl https://cn-shanghai.axt.aliyun.com/luban/api/instance/instance-id i-uf62njf1dkbc2c xxx root@iZuf62njf1dkb xxx ~]#
### 为什么托管实例注册成功但显示状态异常？
若托管的实例显示注册成功，但云助手控制台显示云助手状态异常，可以查看云助手日志是否出现invalid timestamp错误。
说明
云助手默认日志路径如下，<version>为云助手Agent的具体版本号。
Linux实例
CoreOS操作系统：/opt/local/share/aliyun-assist/<version>/log
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）：/usr/local/share/aliyun-assist/<version>/log
Windows实例：C:\ProgramData\aliyun\assist\<version>\log
云助手日志中出现invalid timestamp错误的示例如下。其中code:400、errCode:BAD_REQUEST、errMsg:invalid timestamp为关键错误信息。
M/s1Kpi+KHyHOSytaIf6q7qPc8cGRXbaKR4ZtzJMOKTRoW1V1Y2t6cMaW7v9pZY9phJKeqQo4TMtAZasr/68EqS3xfaYmBRpvlnqvR6b3CR0336R1OQ== time="2023-09-04T16:54:37+08:00" level=info msg="https://cn-shanghai.axt.aliyuncs.com/luban/api/metrics {\"code\":400,\"errCode\":\"_BAD_REQUEST_\",\"errMsg\":\"invalid timestamp: 1693817677756,\"instanceId\":\"mi-sh03vea8ivh50qo\",\"requestId\":\"efb3ccca-7834-43e2-b0ce-1f5aacb37aad\" {\"eventId\":\"agent.startup\",\"category\":\"STARTUP\",\"subCategory\":\"\",\"eventLevel\":\"INFO\",\"eventTime\":\"1693817677755\",\"common\":\"\",\"arch\":\"amd64\",\"instanceId\":\"\",\"unknown\",\"osVersion\" \"Linux_#1 SMP Tue Mar 31 23:36:51 UTC 2020_x86_64\",\"virtualType\":\"unknown\",\"distribution\":\"\",\"centos 7.8.2003\",\"kernelVersion\":\"3.10.0-1127.el7.x86_64\",\"keywords\":\"\",\"osName\":\"Linux_#1 SMP Tue Mar 31 23:36:51 UTC 2020 x86_64\",\"type\":\"\"not cold start\"} time="2023-09-04T16:54:37+08:00" level=info msg="https://cn-shanghai.axt.aliyuncs.com/luban/api/l/task?reason=startup&cold=false&currentTime=1693817677756&offset=28800&timeZone=Asia%2FShanghai {\"code\":400,\"errCode\":\"_BAD_REQUEST_\",\"errMsg\":\"invalid timestamp: 1693817677756\",\"instanceId\":\"mi-sh03vea8ivh50qo\",\"requestId\":\"bcbb8f3e-781a-43f1-afa8-e2Seef3cf116\"} <nil>" time="2023-09-04T16:54:37+08:00" level=info msg="mi-sh03vea8ivh50qo1d678715bd3442d9bf66b7b5712a5 251693817677961439582&d-a299-486c-94d7-ba71f537f248 LEv1C0x/ZhbRS57+A7/60/SOJe51CxxXKKq4f97phnz1o FBwCKREpDDBbEhZth1CzOQqXqauSt1xmAQW==" gxSud7 9MnI1TUJav3jyMdmK+s2BGZGHzZstWSinn7cjaTj fA+dgkhNAqvOMoq63Z6BWR4N0rZt1oLCrrFIG4JAIFLAyfmOmrkygk5/abOezyk4DH/1V7vN2wQ 7FYEi7VVY45BzrKEvGtIzNefc0dltkNKSP0MHRsWMR6xibFWDe/u/0z3KJ9oQYZ JaTn6g5uzlnIZ91Lx09ssJz/JU6cOnd8fOrXCaBPFpg20SmcUBZu1HQ== time="2023-09-04T16:54:38+08:00" level=info msg="https://cn-shanghai.axt.aliyuncs.com/luban/api/metrics {\"code\":400,\"errCode\":\"_BAD_REQUEST_\",\"errMsg\":\"invalid timestamp: 1693817677961\",\"instanceId\":\"mi-sh03vea8ivh50qo\",\"requestId\":\"4395828d-a299-486c-94d7-ba71f537f248\" {\"eventId\":\"agent.kdump\",\"category\":\"KDUMP\",\"eventLevel\":\"INFO\",\"eventTime\":\"1693817677961\",\"common\":\"\",\"arch\":\"amd64\",\"unknown\",\"osVersion\":\"Lin ux_#1 SMP Tue Mar 31 23:36:51 UTC 2020_x86_64\",\"virtualType\":\"unknown\",\"distribution\":\"centos 7.8.2003\",\"kernelVersion\":\"3.10.0-1127.el7.x86_64\",\"keywords\":\"\",\"status\":\"\"ON\"\"} <nil>" time="2023-09-04T16:54:54+08:00" level=info msg="Stopping ......"
出现该错误是由于托管实例上的时间戳和实际时间有误差导致，可以尝试校准ECS实例时间解决。更多信息，请参见[手动同步时间](alibaba-cloud-ntp-server.md)。
## 相关文档
您可以通过[ListPluginStatus](../developer-reference/api-ecs-2014-05-26-listpluginstatus.md)来查询实例中云助手插件的状态。同时，您也可以在接口的返回信息中，查看云助手第一次上报插件状态的时间（FirstHeartbeatTime参数）和云助手最近一次上报插件状态的时间（LastHeartbeatTime参数）。
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
