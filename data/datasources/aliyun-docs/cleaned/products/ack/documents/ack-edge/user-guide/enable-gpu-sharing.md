# 在ACK Edge集群中使用共享GPU调度能力-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/enable-gpu-sharing

# 在ACK Edge集群中使用共享GPU调度能力
通过共享GPU调度能力，您可以将多个Pod调度到同一张GPU卡上，以共享GPU的计算资源，从而提高GPU的利用率并节省成本。在实现GPU共享调度的同时，确保运行在同一张GPU上的多个容器之间能够互相隔离，并根据各自申请的资源使用量运行，避免某个容器的资源使用量超标，进而影响其他容器的正常工作。本文介绍如何在ACK Edge集群中使用共享GPU调度能力。
## 前提条件
已创建ACK Edge集群，且集群版本为1.18及以上。具体操作，请参见[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)。
已开通云原生AI套件。关于云原生AI套件的介绍及计费说明，请参见[AI](cloud-native-ai-suite-overview.md)[套件概述](cloud-native-ai-suite-overview.md)、[云原生](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md)[AI](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md)[套件计费说明](../../cloud-native-ai-suite/product-overview/cloud-native-ai-suite-free-open-instructions.md)。
[已获取集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
## 使用限制
ACK Edge集群的云端节点支持完整的共享GPU调度和显存隔离以及算力隔离能力。
ACK Edge集群的边缘节点池仅支持共享GPU调度，不支持显存隔离、算力隔离的能力。
## 注意事项
针对纳入K8s集群管理的GPU节点，为业务应用申请和使用GPU资源时，请关注以下注意事项。
请勿直接在节点上运行GPU应用程序。
请勿通过docker、podman、nerdctl等工具命令创建容器并为容器申请GPU资源。例如，执行docker run --gpus all或docker run -e NVIDIA_VISIBLE_DEVICES=all并运行GPU程序。
请勿在Pod YAML的env中直接添加环境变量NVIDIA_VISIBLE_DEVICES=all或NVIDIA_VISIBLE_DEVICES=<GPU ID>等，通过容器的环境变量NVIDIA_VISIBLE_DEVICES直接为Pod申请GPU资源，并运行GPU程序。
在Pod YAML中未设置环境变量NVIDIA_VISIBLE_DEVICES，制作Pod所使用的镜像时，请勿将环境变量默认配置为NVIDIA_VISIBLE_DEVICES=all，并运行GPU程序。
请勿在Pod的securityContext中配置privileged: true，并运行GPU程序。
通过以上非标方式为业务应用申请的GPU资源，将存在如下安全隐患。
通过以上方式为业务应用申请的GPU资源，并未在调度器的设备资源账本中统计，有可能造成节点GPU资源的分配情况与调度器设备资源账本中记录的值不一致。调度器仍然会调度某些申请GPU资源的Pod到这个节点上，导致用户业务因为在同一张GPU卡上出现资源争抢（比如GPU显存申请）而运行失败的情况。
非标操作可能引发其他未知问题，例如[NVIDIA](https://github.com/NVIDIA/nvidia-docker/issues/1671)[社区的已知报错](https://github.com/NVIDIA/nvidia-docker/issues/1671)。
## 步骤一：安装共享GPU组件
### 未部署云原生AI套件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>云原生AI套件。
在云原生AI套件页面，单击一键部署。
在一键部署云原生AI套件页面，选中调度策略扩展（批量任务调度、GPU共享、GPU拓扑感知）。
（可选）单击调度策略扩展（批量任务调度、GPU共享、GPU拓扑感知）右侧的高级配置。在弹出的参数配置窗口，修改cGPU的policy字段。修改完成后，单击确定。
如果对cGPU算力共享无特殊要求，建议使用默认policy: 5，即原生调度。cGPU支持的policy，请参见[安装并使用](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[cGPU](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[服务](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)。
在云原生AI套件页面最下方，单击部署云原生AI套件。
组件安装成功后，在云原生AI套件页面的组件列表中能看到已安装的共享GPU组件ack-ai-installer。
### 已部署云原生AI套件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>云原生AI套件。
在调度组件ack-ai-installer所在行，单击操作列的部署。
（可选）在弹出的参数配置窗口，修改cGPU的policy字段。
如果对cGPU算力共享无特殊要求，建议使用默认policy: 5，即原生调度。cGPU支持的policy，请参见[安装并使用](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[cGPU](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[服务](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)。
修改完成后，单击确定。
组件安装完成后，ack-ai-installer的状态为已部署。
## 步骤二：创建GPU节点池
创建云端GPU节点池，以开启GPU共享调度能力、显存隔离和算力共享能力。
创建边缘GPU节点池，以开启GPU共享调度能力。
## 云端节点池
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，单击创建节点池。参见[创建和管理节点池](../../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)完成相关配置。
在创建节点池页面，设置创建节点池的配置项，然后单击确认配置。重要配置项及其说明如下：
| 配置项 | 说明 |
| --- | --- |
| 期望节点数 | 设置节点池初始节点数量。如无需创建节点，可以填写为 0。 |
| 节点标签 | 标签的值需根据您的业务需求添加。关于节点标签的详细说明，请参见 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。 下文以标签值 cgpu 为例，该值表示节点开启共享 GPU 调度能力，每个 Pod 仅需申请 GPU 显存资源，多个 Pod 在一张卡上实行显存隔离和算力共享。 单击 节点标签 的 ，设置 键 为 ack.node.gpu.schedule ， 值 为 cgpu 。 重要 关于 cGPU 隔离功能注意事项，请参见 [cGPU FAQ](../../ack-managed-and-ack-dedicated/user-guide/usage-notes-for-memory-isolation-capability-of-cgpu.md) 。 添加共享 GPU 调度标签后，请勿通过 kubectl label nodes 命令切换节点 GPU 调度属性标签值或使用控制台 节点 页面的标签管理功能更改节点标签，以避免引发潜在的问题，请参见 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。推荐您 [开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md) 。 |
## 边缘节点池
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，单击创建边缘节点池。
在创建节点池页面，设置创建节点池的配置项，然后单击确认配置。此处仅介绍主要配置项，其余配置项请参见[边缘节点池属性](edge-node-pool-management.md)。
节点标签（Labels）：单击节点标签（Labels）的，设置键为ack.node.gpu.schedule，值为share。仅开启GPU共享调度能力。关于节点标签的更多信息，请参见[开启调度功能](../../ack-managed-and-ack-dedicated/user-guide/enable-scheduling.md)。
## 步骤三：添加GPU节点
分别在云端节点池和边缘节点池中添加GPU节点。
### 云端节点
说明
如果您添加节点池时已经创建GPU节点，可以跳过此步骤。
完成创建节点池后，您还可以在节点池中添加GPU节点。添加GPU节点时，您需要指定实例规格的架构为GPU云服务器。具体操作，请参见[添加已有节点](../../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md)或[创建和管理节点池](../../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)。
### 边缘节点
在边缘节点池中添加GPU节点的具体操作，请参见[添加](add-a-gpu-node.md)[GPU](add-a-gpu-node.md)[节点](add-a-gpu-node.md)。
## 步骤四：在云端节点安装和使用GPU资源查询工具
下载kubectl-inspect-cgpu。需将执行文件下载至PATH环境变量包含目录下，本文以/usr/local/bin/为例。
如果您使用的是Linux系统，您可以通过以下命令下载kubectl-inspect-cgpu。
wget http://aliacs-k8s-cn-beijing.oss-cn-beijing.aliyuncs.com/gpushare/kubectl-inspect-cgpu-linux -O /usr/local/bin/kubectl-inspect-cgpu
如果您使用的是macOS系统，您可以通过以下命令下载kubectl-inspect-cgpu。
wget http://aliacs-k8s-cn-beijing.oss-cn-beijing.aliyuncs.com/gpushare/kubectl-inspect-cgpu-darwin -O /usr/local/bin/kubectl-inspect-cgpu
执行以下命令，为kubectl-inspect-cgpu添加执行权限。
chmod +x /usr/local/bin/kubectl-inspect-cgpu
执行以下命令，查看集群GPU使用情况。
kubectl inspect cgpu
预期输出：
NAME IPADDRESS GPU0(Allocated/Total) GPU Memory(GiB) cn-shanghai.192.168.6.104 192.168.6.104 0/15 0/15 ---------------------------------------------------------------------- Allocated/Total GPU Memory In Cluster: 0/15 (0%)
## 步骤五：部署共享GPU调度示例
## 云端节点池
执行以下命令查询集群的GPU共享能力。
kubectl inspect cgpuNAME IPADDRESS GPU0(Allocated/Total) GPU1(Allocated/Total) GPU Memory(GiB) cn-shanghai.192.168.0.4 192.168.0.4 0/7 0/7 0/14 --------------------------------------------------------------------- Allocated/Total GPU Memory In Cluster: 0/14 (0%)
说明
您可以执行命令kubectl inspect cgpu -d，查询GPU共享能力详细信息。
部署共享GPU示例应用，该示例应用申请3 GiB显存。
apiVersion: batch/v1 kind: Job metadata: name: gpu-share-sample spec: parallelism: 1 template: metadata: labels: app: gpu-share-sample spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxxx # 此处需替换为您创建的云端节点池ID。 containers: - name: gpu-share-sample image: registry.cn-hangzhou.aliyuncs.com/ai-samples/gpushare-sample:tensorflow-1.5 command: - python - tensorflow-sample-code/tfjob/docker/mnist/main.py - --max_steps=100000 - --data_dir=tensorflow-sample-code/data resources: limits: # 单位为GiB，该Pod总共申请了3 GiB显存。 aliyun.com/gpu-mem: 3 # 设置GPU显存大小。 workingDir: /root restartPolicy: Never
## 边缘节点池
部署共享GPU示例应用，该示例应用申请4 GiB显存。
apiVersion: batch/v1 kind: Job metadata: name: tensorflow-mnist-share spec: parallelism: 1 template: metadata: labels: app: tensorflow-mnist-share spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxxx # 此处需替换为您创建的边缘节点池ID。 containers: - name: tensorflow-mnist-share image: registry.cn-beijing.aliyuncs.com/ai-samples/gpushare-sample:tensorflow-1.5 command: - python - tensorflow-sample-code/tfjob/docker/mnist/main.py - --max_steps=100000 - --data_dir=tensorflow-sample-code/data resources: limits: aliyun.com/gpu-mem: 4 # 总共申请4 GiB显存。 workingDir: /root restartPolicy: Never
## 步骤六：结果验证
## 云端节点池
登录目标Master节点。
执行以下命令，查看已部署应用的日志，验证cGPU显存隔离是否部署成功。
kubectl logs gpu-share-sample --tail=1
预期输出：
2023-08-07 09:08:13.931003: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1326] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 2832 MB memory) -> physical GPU (device: 0, name: Tesla T4, pci bus id: 0000:00:07.0, compute capability: 7.5)
预期输出表明，容器申请的显存为2832 MB。
执行以下命令，登录容器查看容器被分配显存总量。
kubectl exec -it gpu-share-sample nvidia-smi
预期输出：
Mon Aug 7 08:52:18 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 418.87.01 Driver Version: 418.87.01 CUDA Version: 10.1 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | |===============================+======================+======================| | 0 Tesla T4 On | 00000000:00:07.0 Off | 0 | | N/A 41C P0 26W / 70W | 3043MiB / 3231MiB | 0% Default | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+ | Processes: GPU Memory | | GPU PID Type Process name Usage | |=============================================================================| +-----------------------------------------------------------------------------+
预期输出表明，该容器被分配显存总量为3231 MiB 。
登录带有GPU设备的节点，查看示例应用所在节点的GPU显存总量。
nvidia-smi
预期输出：
Mon Aug 7 09:18:26 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 418.87.01 Driver Version: 418.87.01 CUDA Version: 10.1 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | |===============================+======================+======================| | 0 Tesla T4 On | 00000000:00:07.0 Off | 0 | | N/A 40C P0 26W / 70W | 3053MiB / 15079MiB | 0% Default | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+ | Processes: GPU Memory | | GPU PID Type Process name Usage | |=============================================================================| | 0 8796 C python3 3043MiB | +-----------------------------------------------------------------------------+
预期输出表明，主机上的显存总量为15079 MiB，其中3053 MiB分配给容器。
## 边缘节点池
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>容器组。
在创建的容器所在行（例如tensorflow-mnist-multigpu-***），单击操作列的终端。然后从下拉列表中选择需要登录的容器，执行如下命令。
nvidia-smi
预期输出：
Wed Jun 14 06:45:56 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 515.105.01 Driver Version: 515.105.01 CUDA Version: 11.7 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 Tesla V100-SXM2... On | 00000000:00:09.0 Off | 0 | | N/A 35C P0 59W / 300W | 334MiB / 16384MiB | 0% Default | | | | N/A | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| +-----------------------------------------------------------------------------+
Pod内部能够发现整张GPU卡的总显存16384 MiB（本文示例使用GPU卡为V100），而在有隔离模块参与的场景下，该值与Pod申请值一致（本文示例为4 GiB），说明配置生效。
业务应用需要从两个环境变量中读取该业务能够使用的显存值。
ALIYUN_COM_GPU_MEM_CONTAINER=4 # 该Pod能够使用的显存值。 ALIYUN_COM_GPU_MEM_DEV=16 # 每张GPU卡总共的显存值。
如果应用需要的是显存的百分比，可以使用上述两个环境变量计算：
percetange = ALIYUN_COM_GPU_MEM_CONTAINER / ALIYUN_COM_GPU_MEM_DEV = 4 / 16 = 0.25
## 相关文档
关于共享GPU调度更多信息，请参见[共享](../../ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)[GPU](../../ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)[调度](../../ack-managed-and-ack-dedicated/user-guide/cgpu-overview.md)。
如需升级共享GPU调度组件，请参见[升级共享](../../ack-managed-and-ack-dedicated/user-guide/install-and-use-ack-ai-installer-and-the-gpu-inspection-tool.md)[GPU](../../ack-managed-and-ack-dedicated/user-guide/install-and-use-ack-ai-installer-and-the-gpu-inspection-tool.md)[调度组件](../../ack-managed-and-ack-dedicated/user-guide/install-and-use-ack-ai-installer-and-the-gpu-inspection-tool.md)。
如需关闭对应用的GPU隔离能力，请参见[关闭对应用的](../../ack-managed-and-ack-dedicated/user-guide/disable-the-memory-isolation-capability-of-cgpu.md)[GPU](../../ack-managed-and-ack-dedicated/user-guide/disable-the-memory-isolation-capability-of-cgpu.md)[隔离能力](../../ack-managed-and-ack-dedicated/user-guide/disable-the-memory-isolation-capability-of-cgpu.md)。
如需了解更多共享GPU调度的高级能力，请参见[高级能力](../../ack-managed-and-ack-dedicated/user-guide/cgpu-professional-edition-1.md)。
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
