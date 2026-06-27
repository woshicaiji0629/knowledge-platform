### 自动化运维能力
启用节点池的自动化运维能力能够降低Worker节点的运维负担，让ACK自动化完成某些运维操作，例如操作系统（OS）CVE漏洞自动修复、kubelet自动升级、节点故障自愈等。但如果业务对底层节点的变更比较敏感，无法容忍节点的重启以及业务Pod的迁移，不推荐启用。
准备工作
确保操作系统为[Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images)[容器优化版](https://help.aliyun.com/zh/alinux/alibaba-cloud-linux-3-container-optimized-images)、[ContainerOS](containeros-overview.md)、Alibaba Cloud Linux、Red Hat、Ubuntu。
关于ACK集群支持的操作系统镜像介绍及镜像的使用限制，请参见[操作系统](overview-of-os-images.md)。
使用节点池的自动化运维能力前，需在[容器服务管理控制台](https://cs.console.aliyun.com)的节点池页面完成以下操作（配置完成后均支持修改）。
关于如何创建和编辑节点池，请参见[创建和管理节点池](create-a-node-pool.md)。
展开查看操作流程
为节点池开启托管能力
新建节点池：创建节点池的过程中选择托管节点池。
存量节点池：在节点池列表的操作列，单击节点池对应的更多>开启托管。
按需启用节点池的自动化运维能力
包括开启节点自愈、自动升级kubelet、运行时和OS版本、自动修复OS CVE漏洞等。
配置集群维护窗口
节点池的自动化运维能力需配置集群维护窗口使用，节点池会在集群维护窗口内执行自动化运维任务。
新建节点池：创建节点池的过程中配置托管节点池的集群维护窗口。
存量节点池：在节点池列表的操作列，单击存量托管节点池对应的更多>托管配置，配置维护窗口。
功能介绍
