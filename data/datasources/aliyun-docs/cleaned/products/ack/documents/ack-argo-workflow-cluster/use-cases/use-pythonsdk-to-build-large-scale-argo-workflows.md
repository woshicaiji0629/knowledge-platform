# 使用PythonSDK构建大规模Argo Workflows-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/use-cases/use-pythonsdk-to-build-large-scale-argo-workflows

# 使用PythonSDK构建大规模Argo Workflows
Argo Workflows是一个强大的工作流管理工具，广泛应用于定时任务、机器学习和ETL数据处理等场景，但是使用YAML定义工作流程可能会增加学习难度。Hera Python SDK提供了一种简洁易用的替代方案，Hera允许用户以Python代码构建工作流，支持复杂任务，易于测试，并与Python生态无缝集成，显著降低了工作流设计的门槛。本文将介绍如何使用Python SDK构建大规模Argo Workflows。
## 背景信息
Argo Workflows是一个专为Kubernetes环境设计的开源工作流管理工具，它专注于实现复杂工作流程的自动化编排。允许用户定义一系列任务，并灵活安排这些任务的执行顺序及依赖关系，Argo Workflows助力用户高效构建和管理高度定制化的自动化工作流程。
Argo Workflows的应用场景非常广泛，包括定时任务、机器学习、仿真计算、科学计算、ETL数据处理、模型训练、CI/CD等。Argo Workflows主要依赖YAML来定义工作流程，这种设计目的在于实现配置的清晰与简洁。然而，对于初次接触或不熟悉YAML的用户来说，面对复杂的工作流设计时，YAML的严格缩进要求及层次化的结构可能会增加一定的学习曲线和配置难度。
Hera是一个专为构建和提交Argo工作流程设计的Python SDK框架，其主要目标是简化工作流程的构建和提交，对于数据科学家而言，通过使用Python能更好地兼容平时的使用习惯，克服YAML的阻碍。
### 编辑方式对比
|  | YAML | Hera Framework |
| --- | --- | --- |
| 简洁性 | 较高 | 高，代码量少 |
| 复杂工作流编写难易程度 | 难 | 易，有效避免 YAML 可能产生的语法错误 |
| Python 生态集成难易程度 | 难 | 易，丰富的 Python Lib |
| 可测试性 | 难，容易出现语法错误 | 易，可使用测试框架，提高代码的质量和可维护性 |
Hera Framework以优雅的方式将Python生态体系与Argo Workflows框架结合，使繁琐的工作流设计变得直观简明。它不仅为大规模任务编排提供了一条免受YAML复杂性困扰的通路，同时也有效连接了数据工程师与他们熟悉的Python语言，使得构建和优化机器学习工作流变得无缝和高效，迅速实现创意到部署的迭代循环，从而推动智能应用的快速落地与持续发展。下方示例中使用了Hera Framework进行编辑。
## 步骤一：创建集群并获取Token
[创建](../user-guide/create-an-argo-workflow-cluster.md)[Argo](../user-guide/create-an-argo-workflow-cluster.md)[工作流集群](../user-guide/create-an-argo-workflow-cluster.md)，然后[开启](../user-guide/enable-argo-server-for-a-workflow-cluster.md)[Argo Server](../user-guide/enable-argo-server-for-a-workflow-cluster.md)[并访问工作流控制台](../user-guide/enable-argo-server-for-a-workflow-cluster.md)。
创建集群Token。
kubectl create token default -n default
## 步骤二：使用Hera Python SDK提交Workflows
安装Hera。
pip install hera
编写并提交Workflows。
## 场景一：Simple DAG Diamond
在Argo Workflows中，DAG（有向无环图）常用于定义复杂的任务依赖关系，其中Diamond结构是一种常见的工作流模式，可以实现多个任务并行执行后，将它们的结果汇聚到一个共同的后续任务。这种结构在合并不同数据流或处理结果的场景中非常有效。下面是一个具体示例，展示如何使用Hera定义一个具有Diamond结构的工作流，其中两个任务taskA和taskB并行运行，它们的输出共同作为输入传递给taskC。
使用以下内容，创建simpleDAG.py。
# 导入相关包。 from hera.workflows import DAG, Workflow, script from hera.shared import global_config import urllib3 urllib3.disable_warnings() # 配置访问地址和Token。 global_config.host = "https://{{argo_server_IP}}:2746" global_config.token = "abcdefgxxxxxx" # 填入之前获取的Token。 global_config.verify_ssl = "" # 装饰器函数script是Hera实现近乎原生的Python函数编排的关键功能。 # 它允许您在Hera上下文管理器（例如Workflow或Steps上下文）下调用该函数。 # 该函数在任何Hera上下文之外仍将正常运行，这意味着您可以在给定函数上编写单元测试。 # 该示例是打印输入的信息。 @script(image="mirrors-ssl.aliyuncs.com/python:3.10") def echo(message: str): print(message) # 构建workflow，Workflow是Argo中的主要资源，也是Hera的关键类，负责保存模板、设置入口点和运行模板。 with Workflow( generate_name="dag-diamond-", entrypoint="diamond", namespace="default", ) as w: with DAG(name="diamond"): A = echo(name="A", arguments={"message": "A"}) # 构建Template。 B = echo(name="B", arguments={"message": "B"}) C = echo(name="C", arguments={"message": "C"}) D = echo(name="D", arguments={"message": "D"}) A >> [B, C] >> D # 构建依赖关系，B、C任务依赖A，D依赖B和C。 # 创建Workflow。 w.create()
提交工作流。
python simpleDAG.py
工作流运行后，您可以在工作流控制台（Argo）查看任务DAG流程与运行结果。
示例工作流dag-diamond-g9v45呈钻石形 DAG 拓扑：顶层节点A完成后并行执行B和C，最终汇聚至节点D，所有节点均显示为执行成功状态。
## 场景二：Map-Reduce
在Argo Workflows中实现MapReduce风格的数据处理的关键在于有效利用其DAG（有向无环图）模板，以组织和协调多个任务，从而模拟Map和Reduce阶段。以下是一个更加详细的示例，展示了如何使用Hera构建一个简单的MapReduce工作流，用于处理文本文件的单词计数任务。每一步都是一个Python函数，便于和Python生态进行集成。
[配置](../user-guide/configure-artifacts.md)[Artifacts](../user-guide/configure-artifacts.md)。
使用以下内容，创建map-reduce.py。
展开查看代码内容
from hera.workflows import DAG, Artifact, NoneArchiveStrategy, Parameter, OSSArtifact, Workflow, script from hera.shared import global_config import urllib3 urllib3.disable_warnings() # 设置访问地址。 global_config.host = "https://{{argo_server_IP}}:2746" global_config.token = "abcdefgxxxxxx" # 填入之前获取的Token。 global_config.verify_ssl = "" # 使用script装饰函数时，将script参数传递给script装饰器。这包括image、inputs、outputs、resources等。 @script( image="mirrors-ssl.aliyuncs.com/python:alpine3.6", inputs=Parameter(name="num_parts"), outputs=OSSArtifact(name="parts", path="/mnt/out", archive=NoneArchiveStrategy(), key="{{workflow.name}}/parts"), ) def split(num_parts: int) -> None: # 根据输入参数num_parts创建多个文件，文件中写入foo字符和parts编号 import json import os import sys os.mkdir("/mnt/out") part_ids = list(map(lambda x: str(x), range(num_parts))) for i, part_id in enumerate(part_ids, start=1): with open("/mnt/out/" + part_id + ".json", "w") as f: json.dump({"foo": i}, f) json.dump(part_ids, sys.stdout) # script中定义image、inputs、outputs @script( image="mirrors-ssl.aliyuncs.com/python:alpine3.6", inputs=[Parameter(name="part_id", value="0"), Artifact(name="part", path="/mnt/in/part.json"),], outputs=OSSArtifact( name="part", path="/mnt/out/part.json", archive=NoneArchiveStrategy(), key="{{workflow.name}}/results/{{inputs.parameters.part_id}}.json", ), ) def map_() -> None: # 根据文件中foo字符的个数，生成新文件，将foo内容parts编号乘以2，写入bar内容 import json import os os.mkdir("/mnt/out") with open("/mnt/in/part.json") as f: part = json.load(f) with open("/mnt/out/part.json", "w") as f: json.dump({"bar": part["foo"] * 2}, f) # script中定义image、inputs、outputs、resources @script( image="mirrors-ssl.aliyuncs.com/python:alpine3.6", inputs=OSSArtifact(name="results", path="/mnt/in", key="{{workflow.name}}/results"), outputs=OSSArtifact( name="total", path="/mnt/out/total.json", archive=NoneArchiveStrategy(), key="{{workflow.name}}/total.json" ), ) def reduce() -> None: # 计算每个parts对应bar值的总和。 import json import os os.mkdir("/mnt/out") total = 0 for f in list(map(lambda x: open("/mnt/in/" + x), os.listdir("/mnt/in"))): result = json.load(f) total = total + result["bar"] with open("/mnt/out/total.json", "w") as f: json.dump({"total": total}, f) # 构建workflow，输入name、设置入口点、namespace、全局参数等。 with Workflow(generate_name="map-reduce-", entrypoint="main", namespace="default", arguments=Parameter(name="num_parts", value="4")) as w: with DAG(name="main"): s = split(arguments=Parameter(name="num_parts", value="{{workflow.parameters.num_parts}}")) # 构建Templates。 m = map_( with_param=s.result, arguments=[Parameter(name="part_id", value="{{item}}"), OSSArtifact(name="part", key="{{workflow.name}}/parts/{{item}}.json"),], ) # 输入参数并构建templates。 s >> m >> reduce() # 构建任务依赖关系。 # 创建工作流。 w.create()
提交工作流。
python map-reduce.py
工作流运行后，您可以在工作流控制台（Argo）查看任务DAG流程与运行结果。提交后，在WORKFLOW DETAILS页面，工作流 DAG 视图显示split、4 个并行map节点及reduce节点均执行成功（绿色对勾）。
## 相关文档
Hera相关文档。
如果需要详细了解Hera相关信息，请参见[Hera](https://hera.readthedocs.io/en/stable/)[概述](https://hera.readthedocs.io/en/stable/)。
通过Hera进行LLM训练的过程，请参见[Train LLM with Hera](https://www.youtube.com/watch?v=nRYf3GkKpss)。
YAML部署示例。
以YAML的方式部署simple-diamond示例，请参见[dag-diamond.yaml](https://github.com/argoproj/argo-workflows/blob/main/examples/dag-diamond.yaml)。
以YAML的方式部署map-reduce示例，请参见[map-reduce.yaml](https://github.com/argoproj/argo-workflows/blob/main/examples/map-reduce.yaml)。
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
