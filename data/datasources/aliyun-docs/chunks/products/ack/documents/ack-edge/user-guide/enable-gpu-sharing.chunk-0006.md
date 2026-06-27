### 已部署云原生AI套件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>云原生AI套件。
在调度组件ack-ai-installer所在行，单击操作列的部署。
（可选）在弹出的参数配置窗口，修改cGPU的policy字段。
如果对cGPU算力共享无特殊要求，建议使用默认policy: 5，即原生调度。cGPU支持的policy，请参见[安装并使用](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[cGPU](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)[服务](https://help.aliyun.com/zh/egs/developer-reference/use-docker-to-install-and-use-the-cgpu-component-of-kubergpu-products#table-vde-zd3-930)。
修改完成后，单击确定。
组件安装完成后，ack-ai-installer的状态为已部署。
