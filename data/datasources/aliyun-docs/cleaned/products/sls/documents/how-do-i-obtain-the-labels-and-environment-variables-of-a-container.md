# 获取Docker容器Label和环境变量以配置Logtail采集过滤-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/how-do-i-obtain-the-labels-and-environment-variables-of-a-container

# 如何获取Docker容器的Label和环境变量
当您使用Logtail采集容器日志时，可以通过Label和环境变量对待采集的容器进行过滤。Label指运行docker inspect命令时显示的容器元数据中的标签信息，环境变量是在容器启动时设置的运行时环境参数。本文介绍如何获取容器的Label和环境变量。
重要
本文仅适合获取Docker容器的Label和环境变量，采集K8s日志容器过滤推荐使用[K8s Pod](collect-container-text-logs-through-the-daemonset-console.md)[标签白名单](collect-container-text-logs-through-the-daemonset-console.md)和[K8s Pod](collect-container-text-logs-through-the-daemonset-console.md)[标签黑名单](collect-container-text-logs-through-the-daemonset-console.md)。
## 获取容器Label
登录容器所在的宿主机。ECS实例的登录步骤，请参见[使用](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[工具以](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[SSH](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[协议登录](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行如下命令，列出所有正在运行的容器。
docker ps
返回结果，其中f******a是容器ID。
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg. CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES f******a docker.io/library/nginx:latest nginx -g daemon o... 6 seconds ago Up 7 seconds 0.0.0.0:8080->80/tcp my-nginx
执行如下命令，获取容器Label。
docker inspect ${容器ID}
返回结果中的Labels字段表示容器标签。
## 获取容器环境变量
登录容器所在的宿主机。ECS实例的登录步骤，请参见[使用](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[工具以](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[SSH](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[协议登录](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行如下命令，列出所有正在运行的容器。
docker ps
返回结果，其中f******a是容器ID。
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg. CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES f******a docker.io/library/nginx:latest nginx -g daemon o... 6 seconds ago Up 7 seconds 0.0.0.0:8080->80/tcp my-nginx
执行如下命令，获取容器的环境变量。
docker exec ${容器ID} env
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
