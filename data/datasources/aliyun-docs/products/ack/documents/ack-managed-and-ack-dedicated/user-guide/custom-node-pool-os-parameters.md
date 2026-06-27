# 配置节点池OS参数实现性能调优-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters

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

# 自定义节点池OS参数

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当Linux系统的OS参数默认配置无法满足业务需求，您希望对集群节点进行个性化调整时，您可以在节点池维度自定义节点的OS参数配置，以调优系统性能。自定义OS参数后，系统将按批次变更节点配置。节点池中已有节点将即时生效，新增节点也会使用新配置。

## 使用说明

本功能仅支持1.28及以上版本的[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)、[ACK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)[专有集群（已停止新建）](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster.md)、[ACK Edge](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)[集群](products/ack/documents/ack-edge/user-guide/create-an-ack-edge-cluster-1.md)。如需升级集群，请参见[手动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。

## 注意事项

- 

动态修改OS节点配置有可能会造成节点上已存在的Pod发生配置变更，从而触发Pod重建。请在使用前确保应用的高可用。

- 

不恰当的OS参数调整会改变Linux内核的运作方式，可能导致节点性能恶化或不可用，从而对业务产生影响。请在修改前深入了解待修改参数的作用，并在生产环境操作前进行充分测试。

## 配置节点池OS参数

您可以在节点池维度配置sysctl参数和Transparent Hugepage（THP）参数。这些参数均可通过修改配置文件的方式配置；[THP](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)[参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)和[部分](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)[sysctl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)[参数](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)还支持通过控制台或OpenAPI配置。

### 通过控制台或OpenAPI配置

## 控制台

自定义OS参数后，系统将按批次变更节点配置。配置变更后，节点池中已有节点将即时生效，新增节点也会使用新配置。自定义OS参数生效时会改变已有节点的OS参数配置，可能会对业务产生一定影响。请在业务低峰期操作。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。

- 

在节点池列表的操作列，单击目标节点池对应的>OS 配置。

- 

仔细阅读当前页面上的注意事项，单击+ 自定义参数选择需要配置的参数，指定待升级的节点，设置每批次的最大并行数（最大为10），然后单击提交，按照页面指引完成操作。

配置每批次的最大并行数后，OS配置将按批次对节点生效。执行过程中，您可以在事件记录区域查看进度，并控制执行过程（暂停、继续、取消等）。您可以使用暂停功能对已升级的节点进行验证。暂停时，正在配置的节点会继续完成执行，未执行的节点在任务继续前不会被执行自定义配置。

重要

请尽快完成自定义配置任务。处于暂停状态的任务将在7天后自动取消，相关的事件和日志信息也会被清理。

## OpenAPI

除控制台外，您也可以通过[ModifyNodePoolNodeConfig](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-modifynodepoolnodeconfig.md)接口自定义OS参数。

### 通过配置文件配置

ACK允许将自定义参数写入至/etc/sysctl.d/99-user-customized.conf，该文件是节点初始化和重启时预留的可供自定义配置的文件。写入到该配置文件的 sysctl 参数会在节点重启时优先生效，覆盖操作系统默认值和通过节点池自定义 sysctl 配置功能写入的参数值。

重要

调整 sysctl 参数会改变 Linux 内核的运作方式，可能导致节点性能恶化或不可用，影响业务正常运行。请在操作前请充分评估变更风险。

- 

对于节点池中的存量节点，可[登录节点](products/ecs/documents/user-guide/connect-to-instance.md)修改该自定义参数配置文件，同时手动执行sysctl -p /etc/sysctl.d/99-user-customized.conf命令使配置生效。

- 

对于节点池未来扩容的节点，可将对自定义参数配置文件的写入脚本配置到节点池实例预自定义数据中，以确保新增节点可默认使用这些自定义参数值。方式如下。

在节点池配置中的实例预自定义数据中配置echo '${sysctl_key}=${sysctl_value}' > /etc/sysctl.d/99-user-customized.conf（${sysctl_key}和${sysctl_value}需替换实际值），将自定义配置写入/etc/sysctl.d/目录下的配置文件。

操作入口，请参见[创建和管理节点池](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)。

## sysctl参数列表

说明

- 

下表中的默认值指通过ACK初始化节点池时ACK默认设置的值。

- 

下列参数的取值范围请参见[Linux Kernel sysctl](https://www.kernel.org/doc/Documentation/sysctl/fs.txt)[参数](https://www.kernel.org/doc/Documentation/sysctl/fs.txt)文档。

- 

对于暂未支持通过控制台或 OpenAPI 配置的参数，以及未在表中列出的参数，您可以参见[通过配置文件配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/custom-node-pool-os-parameters.md)进行修改。

| 字段名称 | 说明 | 默认值 | 是否支持控制台或 OpenAPI 配置 |
| --- | --- | --- | --- |
| fs.aio-max-nr | 异步 I/O 操作的最大数量。 | 65536 |  |
| fs.file-max | 系统级别能够打开的最大文件句柄数。 | 2097152 |  |
| fs.inotify.max_user_watches | 单用户能够创建的 inotify 监视的最大数量。 | 524288 |  |
| fs.nr_open | 每个进程能够打开的文件描述符数的最大数量。 此值应小于 fs.file-max 的取值 | 1048576 |  |
| kernel.pid_max | 系统可分配的最大 PID 数量。 | 4194303 |  |
| kernel.threads-max | 系统可创建的最大线程数量。 | 504581 |  |
| net.core.netdev_max_backlog | 接口接收数据包的速度快于内核的处理速度时，可以在 INPUT 端排队的数据包的最大数量。 | 16384 |  |
| net.core.optmem_max | 每个网络套接字允许的最大辅助缓冲区（Ancillary Buffer）大小，以字节为单位。 | 20480 |  |
| net.core.rmem_max | 每个网络套接字接收缓冲区的最大大小，以字节为单位。 | 16777216 |  |
| net.core.wmem_max | 每个网络套接字发送缓冲区的最大大小，以字节为单位。 | 16777216 |  |
| net.core.wmem_default | 每个网络套接字发送缓冲区的默认大小，以字节为单位。 | 212992 |  |
| net.ipv4.tcp_mem | TCP 栈可以使用的内存量，以内存页（大小通常为 4KB）为单位。该参数由三个整数值组成，分别表示低水位、压力水位和最高水位，必须严格按照顺序设置。 | 根据系统总内存动态计算 |  |
| net.ipv4.neigh.default.gc_thresh1 | ARP 缓存中保留的最少条目数。缓存中的条目数量低于此值时，系统不会执行垃圾收集。 | 系统预设置 |  |
| net.ipv4.neigh.default.gc_thresh2 | ARP 缓存中的最大条目数，为软限制，即缓存中的条目数量达到此值时，系统会开始考虑执行垃圾收集，但不会立即强制执行，而会等待 5 秒延迟。 | 1024 |  |
| net.ipv4.neigh.default.gc_thresh3 | ARP 缓存中要保留的最大条目数，为硬限制，即缓存中的条目数量达到此值时，系统会立即执行垃圾收集。如果缓存中的条目数量一直超过此值，系统会不断进行清理。 | 8192 |  |
| user.max_user_namespaces | 单个用户支持创建的 User Namespace 数量上限。 | 0 |  |
| kernel.softlockup_panic | 发生软锁定时，内核会触发 Panic 并重启系统，以快速恢复系统状态。 | 1 |  |
| kernel.softlockup_all_cpu_backtrace | 检测到软锁定时，捕获所有 CPU 的调试信息，便于问题诊断。 | 1 |  |
| vm.max_map_count | 限制单个进程可拥有的最大内存映射区域数量，防止内存过度使用。 | 262144 |  |
| net.core.somaxconn | 设置 Socket 监听队列的最大连接数，控制并发连接处理能力。 | 32768 |  |
| net.ipv4.tcp_wmem | 配置 TCP 连接发送缓冲区的最小值（minimum）、默认值（default）和最大值（maximum）。单位：字节。 此设置直接影响 TCP 连接的网络吞吐量和内存占用。 | 4096 12582912 16777216 |  |
| net.ipv4.tcp_rmem | 配置 TCP 接收缓冲区的最小值（minimum）、默认值（default）和最大值（maximum）。单位：字节。 此设置直接影响 TCP 连接的网络吞吐量和内存占用。 | 4096 12582912 16777216 |  |
| net.ipv4.tcp_max_syn_backlog | 限制 SYN 队列中未完成三次握手的连接请求数量。 | 8096 |  |
| net.ipv4.tcp_slow_start_after_idle | 控制 TCP 连接在长时间空闲后是否重新使用慢启动算法。 | 0 |  |
| net.ipv4.ip_forward | 启用 IPv4 数据包转发功能，允许系统作为路由器转发数据包。 | 1 |  |
| net.bridge.bridge-nf-call-iptables | 使桥接设备在二层转发时应用 iptables 三层规则，以确保网络安全策略生效。 | 1 |  |
| fs.inotify.max_user_instances | 限制单个用户可创建的 inotify 监视器数量，防止资源耗尽。 | 16384 |  |
| fs.inotify.max_queued_events | 设置内核队列中可缓存的文件系统事件数量。 | 16384 |  |
| fs.may_detach_mounts | 允许内核在挂载点仍被进程访问时将其从命名空间中安全分离，避免整个命名空间被锁定。 | 1 |  |


## THP参数列表

透明大页THP（Transparent Huge Pages）是Linux内核中的一个通用特性，可以自动将小页面（通常为4 KB）合并成大页面（通常为2 MB或更大），以减少内存访问页表项PTE（Page Table Entries）大小和访问次数，同时减轻了TLB（Translation Lookaside Buffer）缓存的压力，提高内存访问的效率。

说明

- 

以下参数均支持通过控制台或OpenAPI配置。

- 

根据操作系统及其内核版本的不同，下列参数的默认值不同。更多信息，请参见[Linux Kernel THP](https://docs.kernel.org/admin-guide/mm/transhuge.html)[参数](https://docs.kernel.org/admin-guide/mm/transhuge.html)文档。

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

| 字段名称 | 说明 | 可取值 |
| --- | --- | --- |
| transparent_enabled | 是否在系统全局开启 THP 功能。 | always：系统全局开启 THP 功能。 never：系统全局关闭 THP 功能。 madvise：仅在通过 madvise() 进行系统调用，并且设置了 MADV_HUGEPAGE 标记的内存区域中开启 THP 功能。 |
| transparent_defrag | 是否开启透明大页 THP 相关的碎片整理配置。启用后，如果内存中的小页能够被合并成一个大页，可以减少页表的大小并提高系统的性能。 | always：当系统分配不出透明大页时，暂停内存分配行为，总是等待系统进行内存的直接回收和内存的直接整理。内存回收和整理结束后，如果存在足够的连续空闲内存，则继续分配透明大页。 defer：当系统分配不出透明大页时，转为分配普通的 4 KB 页。同时，系统会唤醒 kswapd 守护进程进行内存的后台回收，唤醒 kcompactd 守护进程进行内存的后台整理。一段时间后，如果存在足够的连续空闲内存， khugepaged 守护进程可将此前分配的 4 KB 页合并为 2 MB 的透明大页。 madvise：仅在通过 madvise() 进行系统调用，并且设置了 MADV_HUGEPAGE 标记的内存区域中，内存分配行为等同于 always。 其余部分的内存分配行为仍然为：发生缺页异常时，转为分配普通的 4 KB 页。 defer+madvise：仅在通过 madvise() 进行系统调用，并且设置了 MADV_HUGEPAGE 标记的内存区域中，内存分配行为等同于 always。其余部分的内存分配行为仍然为 defer。 never：禁止碎片整理。 |
| khugepaged_defrag | khugepaged 是一个内核线程，主要负责管理和整理大页，以减少内存碎片化并提高性能。它会监视系统中的大页面，当发现分散的大页时，尝试将它们合并成更大的页，以提高内存利用率和性能。 由于该操作会在内存路径中执行锁定操作，且 khugepaged 守护进程可能会在错误的时间启动扫描和转换大页的操作，因此存在影响应用性能的可能性。 | 0：关闭 khugepaged 碎片整理功能。 1： khugepaged 守护进程会在系统空闲时周期性唤醒，尝试将连续的 4 KB 页合并成 2 MB 的透明大页。 |
| khugepaged_alloc_sleep_millisecs | 当透明大页 THP 分配失败时， khugepaged 守护进程进行下一次大页分配前需要等待的时间，以避免短时间内连续发生大页分配失败。单位为毫秒。 | 请参见 [khugepaged](https://help.aliyun.com/zh/alinux/support/performance-tuning-method-related-to-transparent-large-page-thp-in#95896c5cd73ld) [碎片整理](https://help.aliyun.com/zh/alinux/support/performance-tuning-method-related-to-transparent-large-page-thp-in#95896c5cd73ld) 。 |
| khugepaged_scan_sleep_millisecs | khugepaged 守护进程每次唤醒的时间间隔。单位为毫秒。 |  |
| khugepaged_pages_to_scan | khugepaged 守护进程每次唤醒后扫描的内存页数量。单位为页。 |  |


[上一篇：自定义节点池containerd配置](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/customize-the-containerd-configurations-of-a-node-pool.md)[下一篇：节点初始化流程介绍](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-to-node-initialization.md)

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
