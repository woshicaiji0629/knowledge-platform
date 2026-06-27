# 排查容器日志采集异常-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers

# 如何排查容器日志采集异常
当您使用Logtail采集容器（标准容器、Kubernetes）日志时，如果采集状态异常，可以根据本文进行问题排查、运行状态检查等运维操作。
## 排查机器组心跳是否异常
您可以通过检查机器组心跳的状态来判断容器中的Logtail是否已正确安装。
查看机器组心跳状态。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看机器组状态并记录心跳状态为OK的节点数。
检查容器集群中Worker节点数。
[连接集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
执行如下命令，查看集群中Worker节点数。
kubectl get node | grep -v master
系统会返回如下类似结果。
NAME STATUS ROLES AGE VERSION cn-hangzhou.i-bp17enxc2us3624wexh2 Ready <none> 238d v1.10.4 cn-hangzhou.i-bp1ad2b02jtqd1shi2ut Ready <none> 220d v1.10.4
对比心跳状态为OK的节点数是否和容器集群中Worker节点数一致。根据对比结果选择排查方式。
机器组中所有节点的心跳状态均为Failed。
如果您要采集标准Docker容器日志，请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)，检查${your_region_name}、${your_aliyun_user_id}、${your_machine_group_user_defined_id}是否填写正确。
如果您使用的是自建Kubernetes集群，请参见[通过](collect-container-text-logs-through-sidecar-console.md)[Sidecar](collect-container-text-logs-through-sidecar-console.md)[方式采集](collect-container-text-logs-through-sidecar-console.md)[Kubernetes](collect-container-text-logs-through-sidecar-console.md)[容器文本日志](collect-container-text-logs-through-sidecar-console.md)，检查{regionId}、{aliuid}、{access-key-id}和{access-key-secret}是否已正确填写。
如果填写错误，请执行helm del --purge alibaba-log-controller命令，删除安装包，然后重新安装。
机器组心跳状态为OK的节点数量少于集群中的Worker节点数量。
判断是否已使用YAML文件手动部署DaemonSet。
执行如下命令。如果存在返回结果，则表示您之前已使用YAML文件手动部署DaemonSet。
kubectl get po -n kube-system -l k8s-app=logtail
[下载最新版本](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[DaemonSet](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[模板。](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)
根据实际值，配置${your_region_name}、${your_aliyun_user_id}、${your_machine_group_name}等参数。
执行如下命令，更新文件。
kubectl apply -f ./logtail-daemonset.yaml
## 排查容器日志采集是否异常
如果您在日志服务控制台的预览或LogStore查询页面未查到日志，则说明日志服务未采集到您的容器日志。请确认容器状态，然后执行如下检查。
重要
采集容器文件中的日志时，需注意如下事项。
Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
只支持采集容器默认存储或挂载到本地的文件中的日志，暂不支持其他存储方式。
采集到日志后，您需要先创建索引，才能在LogStore中查询和分析日志。具体操作，请参见[创建索引](create-indexes.md)。
查看机器组心跳是否存在异常。具体操作，请参见[排查机器组心跳是否异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
检查Logtail配置是否正确。
检查Logtail配置中的IncludeLabel、ExcludeLabel、IncludeEnv、ExcludeEnv等配置是否符合您的采集需求。
说明
其中此处的Label为容器Label，即Docker inspect中的Label，不是Kubernetes中的Label。
您可以将IncludeLabel、ExcludeLabel、IncludeEnv和ExcludeEnv配置临时去除，查看是否可以正常采集到日志。如果可以，则说明是上述参数的配置存在问题。
## 其他运维操作
### 登录Logtail容器
普通Docker
在宿主机上执行如下命令，查询Logtail容器。
docker ps | grep logtail
系统将返回如下类似结果。
223****6e registry.cn-hangzhou.aliyuncs.com/log-service/logtail "/usr/local/ilogta..." 8 days ago Up 8 days logtail-iba
执行如下命令，在Logtail容器内启动bash shell。
docker exec -it 223****6e bash
其中，223****6e为容器ID，请根据实际值替换。
Kubernetes
执行如下命令，查询Logtail的Pod。
kubectl get po -n kube-system | grep logtail
系统将返回如下类似结果。
logtail-ds-****d 1/1 Running 0 8d logtail-ds-****8 1/1 Running 0 8d
执行如下命令，登录Pod。
kubectl exec -it -n kube-system logtail-ds-****d -- bash
其中，logtail-ds-****d为Pod ID，请根据实际值替换。
### 查看Logtail的运行日志
Logtail日志存储在Logtail容器中的/usr/local/ilogtail/目录中，文件名为ilogtail.LOG和logtail_plugin.LOG。
登录Logtail容器。具体操作，[登录](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)[Logtail](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)[容器](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
打开/usr/local/ilogtail/目录。
cd /usr/local/ilogtail
查看ilogtail.LOG和logtail_plugin.LOG文件。
cat ilogtail.LOG cat logtail_plugin.LOG
### Logtail容器的标准输出（stdout）说明
Logtail容器中的标准输出并不具备参考意义，请忽略以下标准输出内容。
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57fe840c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44beab6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640b1e16c22dbe/merged: must be superuser to unmount ...... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
### 查看Kubernetes集群中日志服务相关组件的状态
执行如下命令，查看日志服务的Deployment的状态和信息。
kubectl get deploy -n kube-system | grep -E 'alibaba-log-controller|loongcollector-operator'
返回结果：
NAME READY UP-TO-DATE AVAILABLE AGE alibaba-log-controller 1/1 1 1 11d
执行以下命令，查看关于DaemonSet资源的状态信息。
kubectl get ds -n kube-system | grep -E 'logtail-ds|loongcollector-ds'
返回结果：
NAME DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR AGE logtail-ds 2 2 2 2 2 **ux 11d
### 查看Logtail的版本号、IP地址、启动时间
在宿主机执行如下命令，查看Logtail的版本号、IP地址、启动时间。
相关信息存储在Logtail容器的/usr/local/ilogtail/app_info.json文件中。
kubectl exec logtail-ds-****k -n kube-system cat /usr/local/ilogtail/app_info.json
系统将返回如下类似结果。
{ "UUID" : "", "hostname" : "logtail-****k", "instance_id" : "0EB****_172.20.4.2_1517810940", "ip" : "172.20.4.2", "logtail_version" : "0.16.2", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2018-02-05 06:09:01" }
### 误删由CRD创建的LogStore后，如何处理
如果您删除了由CRD自动创建出的LogStore，则已采集的数据无法恢复，并且针对此LogStore的CRD配置会失效，您可以选择以下方案避免日志采集异常。
在CRD配置中使用其他LogStore，避免使用手动误删的LogStore。
重启alibaba-log-controllerPod。
您可通过如下命令查找该Pod。
kubectl get po -n kube-system | grep alibaba-log-controller
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
