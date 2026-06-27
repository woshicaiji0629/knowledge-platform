# 本文介绍了如何使用Argo Workflow在云上通过动态DAG方式编排Fan-out/Fan-in任务，实现大规模子任务的并行处理与资源弹性调度，适用于数据处理、机器学习等场景。-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/use-cases/use-argo-workflows-to-orchestrate-dynamic-dag-fan-out-fan-in-tasks

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 使用Argo Workflow编排动态DAG Fan-out/Fan-in任务

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在工作流编排过程中，为了加快大任务处理的速度，可以使用Fan-out Fan-in任务编排，将大任务分解成小任务，然后并行运行小任务，最后聚合结果。分布式工作流Argo集群（简称工作流集群）支持动态DAG方式编排Fan-out Fan-in任务，可按需调度云上算力、利用云上弹性可调用数万核CPU资源，减少运行时间，运行结束后能够及时回收资源节省成本。本文为您介绍如何使用工作流集群的Argo Workflow编排动态DAG Fan-out Fan-in任务。

## 背景信息

### Fan-out Fan-in

Fan-out和Fan-in常用于构建高效的并发处理流程，通过拆分（Fan-out）和聚合（Fan-in）操作，能够充分利用多核、多机资源，实现大规模数据的高效处理。

如上图所示，工作流编排过程中，可以使用DAG（有向无环图）编排Fan-out Fan-in任务。子任务的拆分方式分为有静态（静态DAG）和动态（动态DAG）。

- 

静态DAG：拆分的子任务分类是固定的。例如：在数据收集场景中，同时收集数据库1和数据库2中的数据，最后聚合结果。

- 

动态DAG：拆分的子任务分类是动态的，取决于前一个任务的输出结果。

如上图所示，在数据处理场景中，任务A可以扫描待处理的数据集，为每个子数据集（例如：一个子目录）启动子任务Bn处理，当所有子任务Bn运行结束后，在子任务C中聚合结果。具体启动多少个子任务B取决于任务A的输出结果，根据实际的业务场景，可以在任务A中自定义子任务的拆分规则。

### 容器Argo工作流集群

在实际业务场景中，为了提升大任务的执行效率，往往需要将一个大任务拆分成数千个子任务，为了保证这数千个子任务的同时运行，需要调度数万核的CPU资源。叠加多任务需要竞争资源，一般IDC离线任务难以满足需求。

例如：自动驾驶仿真任务，修改算法后进行回归测试，需要对所有驾驶场景进行仿真，每个驾驶场景为一个子任务运行，研发团队为了提高迭代速度，会要求所有子场景测试并行执行。

基于以上业务场景，您可以使用Argo工作流集群编排工作流，工作流集群支持全托管Argo Workflow，提供完善的售后技术支持，可通过动态DAG方式编排Fan-out Fan-in任务，支持弹调度云上算力，调度数万核CPU资源支撑大规模子任务的并行运行。任务运行结束时能够及时回收资源节省成本，一般可用于数据处理、机器学习、仿真计算、CI/CD等业务。

Argo Workflows是开源CNCF毕业项目，聚焦云原生领域下的工作流编排，使用Kubernetes CRD编排离线任务和DAG工作流，并使用Kubernetes Pod在集群中调度运行。更多信息，请参见[Argo Workflow](https://argo-workflows.readthedocs.io/en/latest/)。

## 使用Argo Workflow编排Fan-out Fan-in任务

- 

[创建](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[Argo](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)[工作流集群](products/ack/documents/ack-argo-workflow-cluster/user-guide/create-an-argo-workflow-cluster.md)，并[为集群开启公网访问能力](https://help.aliyun.com/zh/cs/user-guide/enable-public-network-access-for-an-existing-cluster)。

- 

创建阿里云OSS存储卷（参考：[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[静态存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)），将测试所需文件（[log-count-data.txt](https://github.com/AliyunContainerService/argo-workflow-examples/blob/main/log-count/python/log-count-data.txt)）拷贝到OSS存储卷的根目录下。

- 

挂载阿里云OSS存储卷，以便工作流可以像操作本地文件一样操作OSS上的文件。

具体操作，请参见[使用存储卷](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/use-volumes.md)。

- 

使用以下YAML创建一个工作流。

具体操作，请参见[创建工作流](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/create-a-workflow.md)。

展开查看YAML示例

apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: dynamic-dag-map-reduce- spec: entrypoint: main # claim a OSS PVC, workflow can read/write file in OSS through PVC. volumes: - name: workdir persistentVolumeClaim: claimName: pvc-oss # how many tasks to split, default is 5. arguments: parameters: - name: numParts value: "5" templates: - name: main # DAG definition. dag: tasks: # split log files to several small files, based on numParts. - name: split template: split arguments: parameters: - name: numParts value: "{{workflow.parameters.numParts}}" # multiple map task to count words in each small file. - name: map template: map arguments: parameters: - name: partId value: '{{item}}' depends: "split" # run as a loop, partId from split task json outputs. withParam: '{{tasks.split.outputs.result}}' - name: reduce template: reduce arguments: parameters: - name: numParts value: "{{workflow.parameters.numParts}}" depends: "map" # The `split` task split the big log file to several small files. Each file has a unique ID (partId). # Finally, it dumps a list of partId to stdout as output parameters - name: split inputs: parameters: - name: numParts container: image: acr-multiple-clusters-registry.cn-hangzhou.cr.aliyuncs.com/ack-multiple-clusters/python-log-count command: [python] args: ["split.py"] env: - name: NUM_PARTS value: "{{inputs.parameters.numParts}}" volumeMounts: - name: workdir mountPath: /mnt/vol # One `map` per partID is started. Finds its own "part file" and processes it. - name: map inputs: parameters: - name: partId container: image: acr-multiple-clusters-registry.cn-hangzhou.cr.aliyuncs.com/ack-multiple-clusters/python-log-count command: [python] args: ["count.py"] env: - name: PART_ID value: "{{inputs.parameters.partId}}" volumeMounts: - name: workdir mountPath: /mnt/vol # The `reduce` task takes the "results directory" and returns a single result. - name: reduce inputs: parameters: - name: numParts container: image: acr-multiple-clusters-registry.cn-hangzhou.cr.aliyuncs.com/ack-multiple-clusters/python-log-count command: [python] args: ["merge.py"] env: - name: NUM_PARTS value: "{{inputs.parameters.numParts}}" volumeMounts: - name: workdir mountPath: /mnt/vol outputs: artifacts: - name: result path: /mnt/vol/result.json

- 

使用动态DAG方式实现Fan-out Fan-in编排任务。

- 

大文件拆分为多个split子任务后，会在标准输出中输出一个JSON字符串，包含子任务要处理的partId，例如：

["0", "1", "2", "3", "4"]

- 

map任务使用withParam引用split任务的输出，并解析JSON字符串获得所有{{item}}，并使用每个{{item}}作为输入参数启动多个map任务。

- name: map template: map arguments: parameters: - name: partId value: '{{item}}' depends: "split" withParam: '{{tasks.split.outputs.result}}'

更多定义方式，请参见[开源](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)[Argo Workflow](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)。

- 

工作流运行后，您可以在[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)查看任务DAG流程与运行结果。

- 

阿里云OSS文件列表中，log-count-data.txt为输入日志文件，split-output，cout-output为中间结果目录，result.json为最终结果文件。

## 相关参考

- 

了解Argo Workflow的具体内容，请参见[开源](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)[Argo Workflow](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)。

- 

完整的Argo工作流示例代码，请参见[argo-workflow-examples](https://github.com/AliyunContainerService/argo-workflow-examples/tree/main/log-count)。

- 

如果您对于ACK One有任何反馈或疑问，请加入钉群（钉群号：35688562）联系我们。

[上一篇：迁移Batch批量计算到容器Argo工作流集群](products/ack/documents/ack-argo-workflow-cluster/use-cases/migrate-batch-computing-to-argo-workflow-clusters.md)[下一篇：使用Argo Workflows安全高效管理文件](products/ack/documents/ack-argo-workflow-cluster/use-cases/manage-files-securely-and-efficiently-with-argo-workflows.md)

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
