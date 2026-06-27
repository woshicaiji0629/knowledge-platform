# 如何使用Fluid加速边缘节点访问OSS文件-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# 使用Fluid加速边缘节点访问OSS文件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Fluid是一个开源的Kubernetes原生的分布式数据集编排和加速引擎，主要服务于云原生场景下的数据密集型应用，如大数据应用、AI应用等。在边缘场景中，借助Fluid的数据集加速引擎，可以显著提升边缘节点访问OSS文件的速度。本文介绍如何在ACK Edge集群中使用Fluid数据加速功能。

## 前提条件

- 

已创建ACK Edge集群，且集群版本为1.18及以上。具体操作，请参见[创建集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)。

- 

已创建一个边缘节点池，并为其添加边缘节点，具体操作，请参见[创建边缘节点池](products/ack/documents/create-an-edge-node-pool-1.md)、[添加边缘节点](products/ack/documents/ack-edge/user-guide/add-an-edge-node.md)。

- 

已安装云原生AI套件并部署ack-fluid组件。

重要

若您已安装开源Fluid，请卸载后再部署ack-fluid组件。

- 

未安装云原生AI套件：安装时开启Fluid数据加速。具体操作，请参见[部署](products/ack/documents/ack-edge/user-guide/deploy-ai-suite-console.md)[AI](products/ack/documents/ack-edge/user-guide/deploy-ai-suite-console.md)[套件控制台](products/ack/documents/ack-edge/user-guide/deploy-ai-suite-console.md)。

- 

已安装云原生AI套件：在[容器服务管理控制台](https://cs.console.aliyun.com)的云原生AI套件页面部署ack-fluid。

- 

已通过kubectl连接Kubernetes集群。具体操作，请参见[通过](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。

- 

已开通阿里云对象存储OSS服务。具体操作，请参见[开通](products/oss/documents/getting-started/activate-oss.md)[OSS](products/oss/documents/getting-started/activate-oss.md)[服务](products/oss/documents/getting-started/activate-oss.md)。

## 步骤一：准备OSS Bucket的数据

- 

执行以下命令，下载测试数据到ECS实例中。

wget https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz

- 

将下载的测试数据上传到[阿里云](https://cn.aliyun.com/product/oss)[OSS](https://cn.aliyun.com/product/oss)对应的Bucket中。

重要

上传到OSS的步骤以Alibaba Cloud Linux 3.2104 LTS 64位的ECS实例为例。其他操作系统的具体操作，请参见[命令行工具](products/oss/documents/developer-reference/ossutil.md)[ossutil](products/oss/documents/developer-reference/ossutil.md)[快速入门](products/oss/documents/developer-reference/ossutil.md)和[命令行工具](products/oss/documents/developer-reference/overview-59.md)[ossutil 1.0](products/oss/documents/developer-reference/overview-59.md)。

- 

[安装](products/oss/documents/developer-reference/install-ossutil.md)[ossutil](products/oss/documents/developer-reference/install-ossutil.md)。

- 

创建名称为examplebucket的存储空间。

- 

输入以下命令创建examplebucket。

ossutil mb oss://examplebucket

- 

以下输出结果表明已成功创建examplebucket。

0.668238(s) elapsed

- 

将下载的测试数据上传到新建的examplebucket中。

ossutil cp spark-3.0.1-bin-hadoop2.7.tgz oss://examplebucket

## 步骤二：创建Dataset和JindoRuntime

- 

在创建Dataset之前，创建一个mySecret.yaml文件。

apiVersion: v1 kind: Secret metadata: name: mysecret stringData: fs.oss.accessKeyId: xxx fs.oss.accessKeySecret: xxx

其中，fs.oss.accessKeyId和fs.oss.accessKeySecret是[步骤一](products/ack/documents/cloud-native-ai-suite/user-guide/use-jindofs-to-accelerate-access-to-oss.md)中用来访问OSS的AccessKey ID和AccessKey Secret。

- 

执行以下命令，生成Secret。K8s会对已创建的Secret使用加密编码，避免将其明文暴露。

kubectl create -f mySecret.yaml

- 

使用以下YAML文件样例创建一个名为resource.yaml的文件，里面包含两部分：

- 

创建一个Dataset，描述远端存储数据集和UFS的信息。

- 

创建一个JindoRuntime，启动一个JindoFS的集群来提供缓存服务。

apiVersion: data.fluid.io/v1alpha1 kind: Dataset metadata: name: hadoop spec: nodeAffinity: required: nodeSelectorTerms: - matchExpressions: - key: alibabacloud.com/nodepool-id operator: In values: - npxxxxxxxxxxxxxx mounts: - mountPoint: oss://<oss_bucket>/<bucket_dir> options: fs.oss.endpoint: <oss_endpoint> name: hadoop path: "/" encryptOptions: - name: fs.oss.accessKeyId valueFrom: secretKeyRef: name: mysecret key: fs.oss.accessKeyId - name: fs.oss.accessKeySecret valueFrom: secretKeyRef: name: mysecret key: fs.oss.accessKeySecret --- apiVersion: data.fluid.io/v1alpha1 kind: JindoRuntime metadata: name: hadoop spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxxx replicas: 2 tieredstore: levels: - mediumtype: MEM path: /dev/shm volumeType: emptyDir quota: 2Gi high: "0.99" low: "0.95"

说明

- 

在ACK Edge集群中，您需要通过nodeAffinity和nodeSelector将Dataset和JindoRuntime部署到同一个节点池中，确保节点池内的节点网络互通。

- 

由于边缘节点管控和OSS的访问都需要通过云边网络访问云上，建议您保证足够的网络带宽，以免影响到管控通道的稳定性。

相关参数解释如下表所示：

| 参数 | 说明 |
| --- | --- |
| mountPoint | oss://<oss_bucket>/<bucket_dir> 表示挂载 UFS 的路径。此路径必须指向一个目录，无法挂载单个文件，并且不需要包含 Endpoint 信息。 |
| fs.oss.endpoint | OSS Bucket 的 Endpoint 信息，公网或私网地址均支持。更多信息，请参见 [地域和](products/oss/documents/user-guide/regions-and-endpoints.md) [Endpoint](products/oss/documents/user-guide/regions-and-endpoints.md) 。 |
| replicas | 表示创建 JindoFS 集群的 Worker 数量。 |
| mediumtype | 表示缓存类型。在创建 JindoRuntime 模板样例时，JindoFS 暂时只支持 HDD/SSD/MEM 中的其中一种缓存类型。 |
| path | 表示存储路径，暂时只支持单个路径。当选择 MEM 做缓存时，需指定一个本地路径来存储 Log 等文件。 |
| quota | 表示缓存最大容量，单位 GB。 |
| high | 表示存储容量上限大小。 |
| low | 表示存储容量下限大小。 |


- 

执行以下命令，创建JindoRuntime和Dataset。

kubectl create -f resource.yaml

- 

执行以下命令，查看Dataset的部署情况。

kubectl get dataset hadoop

预期输出：

NAME UFS TOTAL SIZE CACHED CACHE CAPACITY CACHED PERCENTAGE PHASE AGE hadoop 210MiB 0.00B 4.00GiB 0.0% Bound 1h

- 

执行以下命令，查看JindoRuntime的部署情况。

kubectl get jindoruntime hadoop

预期输出：

NAME MASTER PHASE WORKER PHASE FUSE PHASE AGE hadoop Ready Ready Ready 4m45s

- 

执行以下命令，查看PV和PVC的创建情况。

kubectl get pv,pvc

预期输出：

NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGECLASS REASON AGE persistentvolume/hadoop 100Gi RWX Retain Bound default/hadoop 52m NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS AGE persistentvolumeclaim/hadoop Bound hadoop 100Gi RWX 52m

从上述输出的查询信息，可以知道Dataset和JindoRuntime已创建成功。

## 步骤三：创建应用容器体验加速效果

您可以通过创建应用容器使用JindoFS加速服务，或提交机器学习作业来体验其相关功能。本文将以创建一个应用容器多次访问同一数据为例，通过对比访问时间，展示JindoRuntime的加速效果。

- 

使用以下YAML文件样例，创建名为app.yaml 的文件。

apiVersion: v1 kind: Pod metadata: name: demo-app spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxx containers: - name: demo image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 volumeMounts: - mountPath: /data name: hadoop volumes: - name: hadoop persistentVolumeClaim: claimName: hadoop

说明

在ACK Edge集群中，您需要通过nodeSelector将测试Pod部署到[步骤二](products/ack/documents/ack-edge/user-guide/use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md)指定的节点池中。

- 

执行以下命令，创建应用容器。

kubectl create -f app.yaml

- 

执行以下命令，查看文件大小。

kubectl exec -it demo-app -- bash du -sh /data/spark-3.0.1-bin-hadoop2.7.tgz

预期输出：

210M /data/spark-3.0.1-bin-hadoop2.7.tgz

- 

执行如下命令，查看文件的拷贝时间。

time cp /data/spark-3.0.1-bin-hadoop2.7.tgz /dev/null

预期输出：

real 0m18.386s user 0m0.002s sys 0m0.105s

从上述输出信息，可以知道文件拷贝时间消耗了18s。

- 

执行以下命令，查看此时Dataset的缓存情况。

kubectl get dataset hadoop

预期输出：

NAME UFS TOTAL SIZE CACHED CACHE CAPACITY CACHED PERCENTAGE PHASE AGE hadoop 210.00MiB 210.00MiB 4.00GiB 100.0% Bound 1h

从上述输出信息，可以知道210 MiB的数据已经都缓存到了本地。

- 

执行以下命令，删除之前的应用容器，新建相同的应用容器。

说明

这样做的目的是为了避免其他因素（例如：Page Cache）对结果造成影响。

kubectl delete -f app.yaml && kubectl create -f app.yaml

- 

执行如下命令，查看文件拷贝时间。

kubectl exec -it demo-app -- bash time cp /data/spark-3.0.1-bin-hadoop2.7.tgz /dev/null

预期输出：

real 0m0.048s user 0m0.001s sys 0m0.046s

从上述输出信息，可以知道进行文件的cp拷贝观察时间消耗48 ms，整个拷贝的时间缩短了300多倍。

说明

由于文件已经被JindoFS缓存，第二次访问所需时间远小于第一次。

## （可选）环境清理

当您不再使用该数据加速功能时，您可以执行以下命令清理环境。

- 

执行以下命令，删除应用容器。

kubectl delete pod demo-app

- 

执行以下命令，删除Dataset和JindoRuntime。

kubectl delete dataset hadoop

[上一篇：使用ack-kserve组件](products/ack/documents/ack-edge/user-guide/user-guide-for-ack-kserve.md)[下一篇：容器镜像](products/ack/documents/ack-edge/user-guide/container-mirrors.md)

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
