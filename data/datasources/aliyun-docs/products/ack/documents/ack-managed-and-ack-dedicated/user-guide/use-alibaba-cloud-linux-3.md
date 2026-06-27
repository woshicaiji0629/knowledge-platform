# AlibabaCloudLinux3操作系统优势特性全解-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-linux-3

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 操作系统Alibaba Cloud Linux 3

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器服务 Kubernetes 版已全面支持阿里云新一代操作系统Alibaba Cloud Linux 3的节点创建，并结合Alibaba Cloud Linux 3高版本内核的特性提供了多场景优化。本文介绍Alibaba Cloud Linux 3操作系统的优势和场景，以及如何使用Alibaba Cloud Linux 3作为ACK节点系统镜像。

## Alibaba Cloud Linux 3概述

Alibaba Cloud Linux是阿里云打造的Linux服务器操作系统发行版。Alibaba Cloud Linux积极吸收了开源社区成果，为云上应用程序提供Linux社区的增强功能，还通过引入更完善的发行版质量体系，保障产品品质。同时，Alibaba Cloud Linux结合阿里云基础设施进行了深度优化，为您提供企业级的支持和维护，提升操作系统服务的使用体验。在继承Alibaba Cloud Linux 2且兼容容器服务 Kubernetes 版的同时，Alibaba Cloud Linux 3还进行了大量优化，包括但不仅限于：

- 

提供更新的基础软件和应用软件，带来更新的原生社区功能。

- 

与容器服务 Kubernetes 版协同优化的同时，基于云场景和用户场景持续改进。

- 

针对新的八代云服务器实例（例如Yitian、Sapphire Rapids、Genoa等）提供深度优化。

- 

提供操作系统自研功能，包括性能优化、新功能支持、易用性优化等。

- 

提供更加详细的版本说明，便于您了解版本演进和变化。

## Alibaba Cloud Linux 3操作系统镜像优势

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 优势 | 说明 |
| --- | --- |
| 更新的基础软件和应用软件 | 内核：搭载阿里云研发的 Linux kernel 5.10 编译器：默认编译器 GCC 10、LLVM 15、RUST 1.66，同时支持 gcc-toolset-12 语言库：支持 glibc 2.32、OpenJDK 1.8、Python 3.8、Golang 1.19、Nodejs 14.21 主流应用软件： Web 类：支持 Nginx 1.20、HTTPd 2.4.37 数据库类：支持 Redis 6.2.7、MySQL 8.0.32、PostgreSQL 13.10、MariaDB 10.5.16 AI 类：通过 [龙蜥社区](https://openanolis.cn/sig/AI_SIG) [AI](https://openanolis.cn/sig/AI_SIG) [生态软件仓库（epao）](https://openanolis.cn/sig/AI_SIG) 兼容支持 Driver 驱动：支持 CUDA 11.4.4、NVIDIA Driver 470.199.02 Framework 框架：支持 TensorFlow 2.5.0、PyTorch 1.10.1 容器支持：支持 nvidia-container-toolkit 1.13.1、libnvidia-container 1.13.1 |
| ACK、ECS 实例协同优化 | 通过与 ECS 实例协同优化启动速度、内置环境依赖软件，同时结合 ACK 灵活高效的自动弹性伸缩能力，大大缩短 Alibaba Cloud Linux 3 的单节点创建时间。 |
| 通过与 ECS 实例深度结合优化，结合内核技术优化、编译器优化、配置优化等，极大提升 ACK 集群中各节点的运行时性能，针对大数据、Webserver、数据库、AI 等场景性能提升超 30%。 |  |
| 提供大量新的操作系统技术，提升云上体验 | 全面支持 cgroup v2 cgroup v2 是新一代 Linux cgroup 机制的 API，提供对进程或进程组统一的资源控制能力。相较于 cgroup v1，有如下改进： 独立统一的层次结构 更加安全的树形结构设计 新的内核 PSI 能力 资源分配和管理能力的增强 全面支持 eBPF 能力 更便捷的 eBPF 程序编写和调试体验，例如许多指令的限制放宽、性能提升、支持调试可见字节码对应的源代码等 更高性能的 XDP 和内核调测 更多用户态框架支持，例如 BPF skeleton、libbpf-bootstrap 等，优化 BPF 程序编写体验 更好地支持网络和安全项目 Cilium，例如网络带宽控制、流量加密、会话亲和性、BPF 层的路由及代理转发等 针对 BCC、Bpftrace 等工具提供更高性能和轻量的实现方式 提供 page cache 限制功能，同时满足 cgroup 级别的限制能力 Linux 系统通过 memcg（Memory Control Group）机制控制和管理进程组的内存使用，支持为每个进程组（或任务组）设置内存限制，避免不合理的资源浪费。memcg 达到设定的内存上限时，系统将触发 memcg 级别的直接内存回收，可能导致当前进程的性能抖动。尽管系统具有 [memcg](https://help.aliyun.com/zh/alinux/user-guide/memcg-backend-asynchronous-reclaim) [后台异步回收](https://help.aliyun.com/zh/alinux/user-guide/memcg-backend-asynchronous-reclaim) 功能，但对于突发性的内存申请来说，其效果有限。有些任务中，例如 Spark 计算框架，page cache 经常会占用大量内存，并且大部分为脏页（dirty page）。脏页的回收速度较慢，将导致预期外的 OOM。因此，为保持业务的稳定性和减少预期外的 OOM，限制 page cache 的使用量非常重要。 Alibaba Cloud Linux 3 新增了 Page Cache 限制功能，支持以 memcg 为粒度（包括根组即整机）限制 Page Cache 的使用。您可以设置 Page Cache 的上限，对超过限制的 Page Cache 进行异步或者同步回收。这可以帮助控制 Page Cache 的使用量，防止其占用过多的内存资源，从而提高系统的稳定性和可靠性。更多信息，请参见 [Page Cache](https://help.aliyun.com/zh/alinux/user-guide/page-cache-restriction-feature) [限制功能](https://help.aliyun.com/zh/alinux/user-guide/page-cache-restriction-feature) 。 |
| 为 AI 开发提供完善的平台支持 | 通过引入 [龙蜥社区](https://openanolis.cn/sig/AI_SIG) [AI](https://openanolis.cn/sig/AI_SIG) [生态软件仓库（epao）](https://openanolis.cn/sig/AI_SIG) ，支持一键安装主流 NVIDIA GPU 驱动以及 CUDA 加速库，节省匹配驱动版本以及手动安装的时间。 epao 仓库支持主流 AI 框架 TensorFlow、PyTorch，并在安装过程中自动解决 AI 框架的依赖问题。您无需进行额外编译，即可搭配系统 Python 环境进行 AI 任务快速开发。 所有提供 AI 能力的相关组件均经过兼容性测试。您可以一键安装对应的 AI 能力，无需修改环境配置中可能出现的系统依赖项，提高使用过程稳定性。 针对 Intel、AMD 等不同平台的 CPU 进行了 AI 专项优化，更好地释放硬件的全部性能。 |
| 其他 | Alibaba Cloud Linux 3 还对系统进行了多种优化，例如： 支持 TCP/IP 协议栈向 RDMA 透明转换 为使用透明大页 THP 而导致的内存膨胀问题提供优化方案 为 Intel 八代 SPR 实例提供多种加速器支持 更多信息，请参见 [Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/product-overview/release-notes-for-alibaba-cloud-linux) [镜像发布记录](https://help.aliyun.com/zh/alinux/product-overview/release-notes-for-alibaba-cloud-linux) 。 |


## 注意事项

- 

在Alibaba Cloud Linux 3中，iptables和nftables不兼容。使用iptables的组件，网络能力可能会受到影响。

- 

Alibaba Cloud Linux 3可能会将部分Hostname作为DNS搜索域，可能导致DNS解析的次数增加。

- 

使用Alibaba Cloud Linux 3时，请确保已安装组件及集群满足以下最低版本要求。

| 组件或集群 | 最低版本 |
| --- | --- |
| 集群 | 1.20.4 |
| ACK NodeLocal DNSCache | 1.5.0 |
| Flannel | v0.13.0.1-466064b-aliyun |
| Terway | v1.0.10.390-g5f3c461-aliyun |


## 使用Alibaba Cloud Linux 3作为集群节点系统镜像

您可以在创建集群的配置过程中，将操作系统选择为Alibaba Cloud Linux 3.2104来使用Alibaba Cloud Linux 3作为集群节点系统镜像。具体步骤，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

说明

如果您选用Alibaba Cloud Linux 3，在创建集群以及后续扩容节点、添加节点、自动伸缩节点时，ACK会自动检测Alibaba Cloud Linux 3的安全补丁更新并自动安装补丁。

## 相关文档

- 

[操作系统](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/overview-of-os-images.md)

- 

[Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/product-overview/release-notes-for-alibaba-cloud-linux)[镜像发布记录](https://help.aliyun.com/zh/alinux/product-overview/release-notes-for-alibaba-cloud-linux)

[上一篇：Alibaba Cloud Linux 3 容器优化版](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/alibaba-cloud-linux-3-container-optimized-image-overview.md)[下一篇：Alibaba Cloud Linux 2（停止维护）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-alibaba-cloud-linux-2.md)

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
