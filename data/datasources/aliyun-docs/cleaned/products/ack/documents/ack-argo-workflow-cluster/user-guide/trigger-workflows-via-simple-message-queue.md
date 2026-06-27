# 通过轻量消息队列（原 MNS）触发工作流-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/trigger-workflows-via-simple-message-queue

# 通过轻量消息队列（原 MNS）触发工作流
容器Argo工作流集群支持使用轻量消息队列（原 MNS）作为事件源，利用事件驱动触发工作流运行。
## 适用范围
已[开通轻量消息队列（原 MNS）并授权](https://help.aliyun.com/zh/mns/getting-started/activate-message-service-and-grant-permissions)
已[获取集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[KubeConfig](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[并通过](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[kubectl](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[工具连接集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。
已[安装](create-an-argo-workflow.md)[Argo CLI](create-an-argo-workflow.md)。
## 步骤一：创建Event Bus
Event Bus可以被命名空间中的事件驱动工作流共享，您可以通过NATS和轻量消息队列（原 MNS）两种方式创建，如果已经创建，请直接执行[步骤二：创建](trigger-workflows-via-simple-message-queue.md)[Event Source](trigger-workflows-via-simple-message-queue.md)。
## 通过NATS创建
创建event-bus.yaml文件。Event Bus示例代码如下所示：
apiVersion: argoproj.io/v1alpha1 kind: EventBus metadata: name: default spec: nats: native: replicas: 3 auth: token
执行以下命令，创建EventBus。
kubectl apply -f event-bus.yaml
说明
命令执行成功后，会在default命名空间下创建Event Bus Pod。后续操作需在同一命名空间下。
执行以下命令，查看Event Bus Pod是否正常启动。
kubectl get pod
## 通过轻量消息队列（原 MNS）创建
登录[轻量消息队列（原 MNS）控制台](https://mns.console.aliyun.com/)。
在主题列表页面创建主题argoeventbus，并在主题详情页面的接入点区域获取Endpoint。
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建RAM用户，为RAM用户授予AliyunMNSFullAccess权限，并获取RAM用户的AK和SK。
具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)、[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)、[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)和[查看](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[用户的](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[AccessKey](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[信息](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)。
创建Secret用于存储AK和SK。
kubectl create secret generic mns-secret\ --from-literal=accesskey=*** \ --from-literal=secretkey=***
创建event-bus-mns.yaml文件，将示例中的参数修改为实际使用的参数值。
topic：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中创建的轻量消息队列（原 MNS）中的主题名称。
endpoint：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中获取的Endpoint。
apiVersion: argoproj.io/v1alpha1 kind: EventBus metadata: name: default spec: alimns: accessKey: key: accesskey name: mns-secret secretKey: key: secretkey name: mns-secret topic: argoeventbus # 对应轻量消息队列（原 MNS）中的主题名称。 endpoint: http://165***368.mns.<region>.aliyuncs.com # 对应轻量消息队列（原 MNS）的Endpoint。
应用event-bus-mns.yaml文件创建Event Bus资源。
kubectl apply -f event-bus-mns.yaml
## 步骤二：创建Event Source
登录[轻量消息队列（原 MNS）控制台](https://mns.console.aliyun.com/)。
在队列列表页面创建队列test-event-queue，并在队列详情页面的接入点区域获取Endpoint。
若是通过轻量消息队列（原 MNS）创建了Event Bus，则步骤3~步骤5可直接跳过，直接执行[步骤](trigger-workflows-via-simple-message-queue.md)[6](trigger-workflows-via-simple-message-queue.md)。
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建RAM用户，为RAM用户授予AliyunMNSFullAccess权限，并获取RAM用户的AK和SK。
具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../../ram/documents/user-guide/create-a-ram-user.md)、[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)、[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)和[查看](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[RAM](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[用户的](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[AccessKey](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[信息](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)。
创建Secret用于存储AK和SK。
kubectl create secret generic mns-secret\ --from-literal=accesskey=*** \ --from-literal=secretkey=***
创建event-source.yaml文件，将示例中的参数修改为实际使用的参数值。
topic：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中创建的轻量消息队列（原 MNS）中的主题名称。
endpoint：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中获取的Endpoint。
apiVersion: argoproj.io/v1alpha1 kind: EventSource metadata: name: ali-mns spec: mns: example: jsonBody: true accessKey: key: accesskey name: mns-secret secretKey: key: secretkey name: mns-secret queue: test-event-queue # 对应轻量消息队列（原 MNS）中的队列名称。 waitTimeSeconds: 20 endpoint: http://165***368.mns.<region>.aliyuncs.com # 对应轻量消息队列（原 MNS）的Endpoint。
应用event-source.yaml文件创建Event Source。
kubectl apply -f event-source.yaml
查看Event Source Pod是否正常启动。
kubectl get pod
## 步骤三：创建Event Sensor
通过轻量消息队列（原 MNS）创建Eventbus时，在Event Sensor创建完成后，会自动创建一个轻量消息队列（原 MNS）与之对应，队列命名格式为：ackone-argowf-<namespace>-<sensor-name>-<sensor-uid>。
创建event-sensor.yaml文件，在Event Sensor中嵌入待执行的工作流定义。Event Sensor示例代码如下所示：
展开查看示例代码
apiVersion: argoproj.io/v1alpha1 kind: Sensor metadata: name: ali-mns spec: template: serviceAccountName: default dependencies: - name: test-dep eventSourceName: ali-mns # 匹配eventsource名称。 eventName: example # 匹配eventsource中的事件名称定义。 triggers: - template: name: mns-workflow k8s: operation: create source: resource: apiVersion: argoproj.io/v1alpha1 # 嵌入工作流定义。 kind: Workflow metadata: generateName: ali-mns-workflow- spec: entrypoint: whalesay arguments: parameters: # 参数传递事件内容。 - name: message # this is the value that should be overridden value: hello world templates: - name: whalesay inputs: parameters: - name: message container: image: docker/whalesay:latest command: [cowsay] args: ["{{inputs.parameters.message}}"] parameters: - src: # 解析事件内容，传递给工作流。 dependencyName: test-dep dataKey: body dest: spec.arguments.parameters.0.value
应用event-sensor.yaml文件创建Event Sensor。
kubectl apply -f event-sensor.yaml
查看Event Sensor Pod是否正常启动。
kubectl get pod
## 步骤四：验证通过向轻量消息队列（原 MNS）发送消息触发工作流
登录[轻量消息队列（原 MNS）控制台](https://mns.console.aliyun.com/)。
在队列列表页面中，找到队列test-event-queue，在其操作列单击收发消息。
在收发消息快速体验页面中，输入消息内容test trigger argo workflow，然后单击发送消息。
在工作流集群中查看工作流的运行情况。
argo list
预期输出如下：
NAME STATUS AGE DURATION PRIORITY ali-mns-workflow-5prz7 Running 6s 6s 0
获取工作流日志，查看消息内容。
argo logs ali-mns-workflow-5prz7
重要
该命令中的工作流名称必须和上一步骤中返回的工作流名称一致，ali-mns-workflow-5prz7仅为示例值，请修改为实际环境中的返回值。
消息内容使用Base64编码。
预期输出如下：
ali-mns-workflow-5prz7-whalesay-2429203954: time="2023-12-14T08:33:37.964Z" level=info msg="capturing logs" argo=true ali-mns-workflow-5prz7-whalesay-2429203954: ali-mns-workflow-5prz7-whalesay-2429203954: < dGVzdCBOcmlnZ2VyIGFyZ28gd29ya2Zsb3c= > ali-mns-workflow-5prz7-whalesay-2429203954: ----------------------------------------- ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: ## . ali-mns-workflow-5prz7-whalesay-2429203954: ## ## ## == ali-mns-workflow-5prz7-whalesay-2429203954: ## ## ## ## === ali-mns-workflow-5prz7-whalesay-2429203954: /""""""""""""""""___/ === ali-mns-workflow-5prz7-whalesay-2429203954: ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~ ali-mns-workflow-5prz7-whalesay-2429203954: \______ o __/ ali-mns-workflow-5prz7-whalesay-2429203954: \ \ __/ ali-mns-workflow-5prz7-whalesay-2429203954: \____\______/ ali-mns-workflow-5prz7-whalesay-2429203954: time="2023-12-14T08:33:38.979Z" level=info msg="sub-process exited" argo=true error="<nil>"
## 步骤五：清除Event相关资源
清除相关资源。
清除Event Sensor
kubectl delete sensor ali-mns
清除Event Source
kubectl delete eventsource ali-mns
清除Event Bus
kubectl delete eventbus default
查看Pod状态，确认所有资源已清除。
kubectl get pod
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
