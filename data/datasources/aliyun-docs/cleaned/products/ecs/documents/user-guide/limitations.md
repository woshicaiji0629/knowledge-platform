# ECS资源使用限制与配额-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/limitations

# ECS使用限制与配额
云服务器ECS在产品功能、服务性能和相关配额上可能存在一些限制，部分限制可以通过提升限额来突破。建议您在实际使用之前了解相应的限制，提前规划并申请提升限额，或规避无法突破的限制，以确保云服务器ECS能够满足您的业务需求。本文介绍云服务器ECS存在的限制以及如何提升部分限制的限额。
## 表格维度说明
您可以查看本文各模块中的表格，了解该模块下的具体限制。对于本文表格各维度的解释如下：
限制项：存在限制的产品功能、服务性能或相关配额。
说明
配额指单个阿里云账号（主账号）可以使用的云资源的最大值或操作次数的最大值。
限制：针对当前限制项存在哪些具体的限制。
当限制项为ECS相关配额时，存在对应的配额ID，您可以根据配额ID查询该限制项的配额，即当前限制的最大额度。
提升限额方式：针对当前限制项是否有突破限制的方式。
若无法突破限制，则需要您提前规避限制，若可以突破限制，您可以根据提升限额方式进行相应的申请。
## 实例
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| vCPU 配额项 | 在特定地域和付费方式（包年包月、按量付费、抢占式）下，单个阿里云账号可持有的某实例规格族的 vCPU 数量上限。具体限制，请参见 [vCPU](limitations.md) [配额项](limitations.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| GPU 卡及 vGPU 配额项 | 在特定地域和付费方式（包年包月、按量付费、抢占式）下，单个阿里云账号可持有的某实例规格族的 GPU 卡数上限或 vGPU 实例数量上限。具体限制，请参见 [GPU](limitations.md) [卡及](limitations.md) [vGPU](limitations.md) [配额项](limitations.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| 单个阿里云账号在特定地域下单次可购买的包年包月实例的最大数量 | 请根据配额 ID q_prepaid-instance-count-per-once-purchase 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | 无 |
| 按量付费转包年包月 | 无数量或额度限制。 已停售的实例规格不支持转包年包月。更多信息请参见 [按量付费转包年包月](../change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md) 。 | 无 |
| 包年包月转按量付费 | 由于包年包月转按量付费时会产生退款，而退款将消耗 退款额度 ，故当月退款额度超限后不能再操作退款，即无法操作包年包月转按量付费。更多信息请参见 [包年包月转按量付费](../change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md) 。 说明 退款额度以转换页面显示为准，额度次月 1 号自动清零。 | 无 |
| 支持二次虚拟化的规格族 | 仅弹性裸金属服务器和超级计算集群支持二次虚拟化，其他规格族不支持安装虚拟化软件和二次虚拟化。 | 无 |
| 声卡应用 | 不支持声卡应用。 | 无 |
| 加载外接硬件设备 | 不支持直接加载外接硬件设备（如硬件加密狗、U 盘、外接硬盘、银行 UKey 等），您可以尝试软件加密狗或者动态口令二次验证等。 | 无 |
| 多播协议 | 不支持多播协议。如需实现类似多播的一对多通信功能，建议采用单播点对点方式进行替代。 | 无 |
| 网站备案 | 如果您需要对网站/APP 进行备案，则必须购买 3 个月及以上的包年包月 ECS 实例，且每台 ECS 实例最多可备案 5 个网站或 APP。详情请参见 [备案服务器检查](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-server-access-information-check#concept-m5j-vrl-zdb) 。 | 无 |
| License | 部分软件或应用的许可证（License）需要与云服务器的硬件信息绑定。云服务器迁移操作时可能会引起硬件信息的变更，进而导致 License 失效。 | 无 |
### vCPU配额项
说明
查看配额时，配额对应的数量为单个阿里云账号在当前地域下的vCPU数量上限，并非所有地域下的vCPU总量上限。
| 配额 ID | 配额项说明 | 对应规格族（具体规格请单击本列规格族链接查看） | 配额 | 提升限额方式 |
| --- | --- | --- | --- | --- |
| q_ecs_restrict_prepay_c | 包年包月的限购类实例 vCPU 数量上限 | [共享标准型实例规格族](shared-instance-families.md) [s6](shared-instance-families.md) [上一代共享型实例规格族](shared-instance-families.md) [xn4、n4、mn4、e4](shared-instance-families.md) [已停售的实例规格](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_local_storage_prepay_c | 包年包月的本地存储型实例（d、i）vCPU 数量上限 | [大数据型（d](big-data-instance-families.md) [系列）](big-data-instance-families.md) [本地](instance-families-with-local-ssds.md) [SSD](instance-families-with-local-ssds.md) [型（i](instance-families-with-local-ssds.md) [系列）](instance-families-with-local-ssds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_share_prepay_c | 包年包月的共享入门级实例（e、t）vCPU 数量上限 | [经济型实例规格族](shared-instance-families.md) [e](shared-instance-families.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t6](burst-performance-instance-overview.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t5](burst-performance-instance-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_ebm_prepay_c | 包年包月的弹性裸金属服务器实例（ebm）vCPU 数量上限 | [弹性裸金属服务器规格](elastic-bare-metal-server-overview.md) （不包含 GPU 计算型弹性裸金属服务器实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_hpc_prepay_c | 包年包月的高性能计算实例（ hpc、 scc）vCPU 数量上限 | [高性能计算优化型实例规格](overview-of-hpc-optimized-instance-families.md) [超级计算集群实例规格](overview-40.md) （不包含 GPU 计算型超级计算集群实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_high_mem_prepay_c | 包年包月的内存型实例（re、se）vCPU 数量上限 | [内存增强型实例规格族](enhanced-instance-families.md) [re7p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4e](enhanced-instance-families.md) [内存网络增强型实例规格族](memory-optimized-instance-families-1.md) [se1ne](memory-optimized-instance-families-1.md) [内存型实例规格族](memory-optimized-instance-families-1.md) [se1](memory-optimized-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_enterprise_prepay_c | 包年包月的企业级计算实例（g、c、r、u、hf、sn）vCPU 数量上限 | [通用型（g](general-purpose-instance-families.md) [系列）](general-purpose-instance-families.md) [计算型（c](compute-optimized-instance-families.md) [系列）](compute-optimized-instance-families.md) [增强型](enhanced-instance-families.md) （不包含 re7p、 re6p、re6、re4） [内存型（r](memory-optimized-instance-families-1.md) [系列）](memory-optimized-instance-families-1.md) （不包含 se1ne、se1） [通用算力型（U](general-work-force.md) [实例）](general-work-force.md) [高主频型（hf](instance-families-with-high-clock-speeds.md) [系列）](instance-families-with-high-clock-speeds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_restrict_postpay_c | 按量付费的限购类实例 vCPU 数量上限 | [共享标准型实例规格族](shared-instance-families.md) [s6](shared-instance-families.md) [上一代共享型实例规格族](shared-instance-families.md) [xn4、n4、mn4、e4](shared-instance-families.md) [已停售的实例规格](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_local_storage_postpay_c | 按量付费的本地存储型实例（d、i）vCPU 数量上限 | [大数据型（d](big-data-instance-families.md) [系列）](big-data-instance-families.md) [本地](instance-families-with-local-ssds.md) [SSD](instance-families-with-local-ssds.md) [型（i](instance-families-with-local-ssds.md) [系列）](instance-families-with-local-ssds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_share_postpay_c | 按量付费的共享入门级实例（e、t）vCPU 数量上限 | [经济型实例规格族](shared-instance-families.md) [e](shared-instance-families.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t6](burst-performance-instance-overview.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t5](burst-performance-instance-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_ebm_postpay_c | 按量付费的弹性裸金属服务器实例（ebm）vCPU 数量上限 | [弹性裸金属服务器规格](elastic-bare-metal-server-overview.md) （不包含 GPU 计算型弹性裸金属服务器实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_hpc_postpay_c | 按量付费的高性能计算实例（ hpc、 scc）vCPU 数量上限 | [高性能计算优化型实例规格](overview-of-hpc-optimized-instance-families.md) [超级计算集群实例规格](overview-40.md) （不包含 GPU 计算型超级计算集群实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_high_mem_postpay_c | 按量付费的内存型实例（re、se）vCPU 数量上限 | [内存增强型实例规格族](enhanced-instance-families.md) [re7p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4e](enhanced-instance-families.md) [内存网络增强型实例规格族](memory-optimized-instance-families-1.md) [se1ne](memory-optimized-instance-families-1.md) [内存型实例规格族](memory-optimized-instance-families-1.md) [se1](memory-optimized-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_enterprise_postpay_c | 按量付费的企业级计算实例（g、c、r、u、hf、sn）vCPU 数量上限 | [通用型（g](general-purpose-instance-families.md) [系列）](general-purpose-instance-families.md) [计算型（c](compute-optimized-instance-families.md) [系列）](compute-optimized-instance-families.md) [增强型](enhanced-instance-families.md) （不包含 re7p、 re6p、re6、re4） [内存型（r](memory-optimized-instance-families-1.md) [系列）](memory-optimized-instance-families-1.md) （不包含 se1ne、se1） [通用算力型（U](general-work-force.md) [实例）](general-work-force.md) [高主频型（hf](instance-families-with-high-clock-speeds.md) [系列）](instance-families-with-high-clock-speeds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_restrict_spot_c | 抢占式的限购类实例 vCPU 数量上限 | [共享标准型实例规格族](shared-instance-families.md) [s6](shared-instance-families.md) [上一代共享型实例规格族](shared-instance-families.md) [xn4、n4、mn4、e4](shared-instance-families.md) [已停售的实例规格](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_local_storage_spot_c | 抢占式的本地存储型实例（d、i）vCPU 数量上限 | [大数据型（d](big-data-instance-families.md) [系列）](big-data-instance-families.md) [本地](instance-families-with-local-ssds.md) [SSD](instance-families-with-local-ssds.md) [型（i](instance-families-with-local-ssds.md) [系列）](instance-families-with-local-ssds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_share_spot_c | 抢占式的共享入门级实例（e、t）vCPU 数量上限 | [经济型实例规格族](shared-instance-families.md) [e](shared-instance-families.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t6](burst-performance-instance-overview.md) [突发性能实例规格族](burst-performance-instance-overview.md) [t5](burst-performance-instance-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_ebm_spot_c | 抢占式的弹性裸金属服务器实例（ebm）vCPU 数量上限 | [弹性裸金属服务器规格](elastic-bare-metal-server-overview.md) （不包含 GPU 计算型弹性裸金属服务器实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_hpc_spot_c | 抢占式的高性能计算实例（ hpc、 scc）vCPU 数量上限 | [高性能计算优化型实例规格](overview-of-hpc-optimized-instance-families.md) [超级计算集群实例规格](overview-40.md) （不包含 GPU 计算型超级计算集群实例规格） | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_high_mem_spot_c | 抢占式的内存型实例（re、se）vCPU 数量上限 | [内存增强型实例规格族](enhanced-instance-families.md) [re7p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [持久内存型实例规格族](enhanced-instance-families.md) [re6p](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4](enhanced-instance-families.md) [内存增强型实例规格族](enhanced-instance-families.md) [re4e](enhanced-instance-families.md) [内存网络增强型实例规格族](memory-optimized-instance-families-1.md) [se1ne](memory-optimized-instance-families-1.md) [内存型实例规格族](memory-optimized-instance-families-1.md) [se1](memory-optimized-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_enterprise_spot_c | 抢占式的企业级计算实例（g、c、r、u、hf、sn）vCPU 数量上限 | [通用型（g](general-purpose-instance-families.md) [系列）](general-purpose-instance-families.md) [计算型（c](compute-optimized-instance-families.md) [系列）](compute-optimized-instance-families.md) [增强型](enhanced-instance-families.md) （不包含 re7p、 re6p、re6、re4） [内存型（r](memory-optimized-instance-families-1.md) [系列）](memory-optimized-instance-families-1.md) （不包含 se1ne、se1） [通用算力型（U](general-work-force.md) [实例）](general-work-force.md) [高主频型（hf](instance-families-with-high-clock-speeds.md) [系列）](instance-families-with-high-clock-speeds.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
### GPU卡及vGPU配额项
说明
查看配额时，配额对应的数量为单个阿里云账号在当前地域下的GPU卡数上限或vGPU实例数量上限，并非所有地域下的GPU卡数总量上限或vGPU实例总量上限。
| 配额 ID | 配额项说明 | 对应规格族（具体规格请单击本列规格族链接查看） | 配额 | 提升限额方式 |
| --- | --- | --- | --- | --- |
| q_ecs_ag_prepay_g | 包年包月的 ARM+GPU 类实例 GPU 卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7r](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [计算型弹性裸金属服务器实例规格族](retired-instance-types.md) [ebmgn6ia](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_vgpu_prepay_g | 包年包月的 GPU 虚拟化类（vGPU）实例数量上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn8ia](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn7i-vws（共享](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [CPU）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn7i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn6i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn6i](retired-instance-types.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn5i](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7i_prepay_g | 包年包月的(ebm)gn7i /ebmgn7ix /gn7s 的 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ix](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn5_prepay_g | 包年包月的 gn5/gn5i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6i_prepay_g | 包年包月的(ebm)gn6i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6v_prepay_g | 包年包月的(ebm)gn6v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6v](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6e_prepay_g | 包年包月的(ebm)gn6e 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6e](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8i_prepay_g | 包年包月的(ebm)gn8is 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8is](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7v_prepay_g | 包年包月的(ebm)gn7 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7e_prepay_g | 包年包月的(ebm)gn7e /gn7ex 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ex](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7e](elastic-bare-metal-server-overview.md) [GPU](overview-40.md) [计算型超级计算集群实例规格族](overview-40.md) [sccgn7ex](overview-40.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8v_prepay_g | 包年包月的(ebm)gn8v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn8v/gn8v-tee](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_ag_postpay_g | 按量付费的 ARM+GPU 类实例 GPU 卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7r](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [计算型弹性裸金属服务器实例规格族](retired-instance-types.md) [ebmgn6ia](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_vgpu_postpay_g | 按量付费的 GPU 虚拟化类（vGPU）实例数量上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn8ia](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn7i-vws（共享](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [CPU）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn7i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn6i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn6i](retired-instance-types.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn5i](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7i_postpay_g | 按量付费的(ebm)gn7i /ebmgn7ix /gn7s 的 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ix](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn5_postpay_g | 按量付费的 gn5/gn5i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6i_postpay_g | 按量付费的(ebm)gn6i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6v_postpay_g | 按量付费的(ebm)gn6v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6v](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6e_postpay_g | 按量付费的(ebm)gn6e 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6e](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8i_postpay_g | 按量付费的(ebm)gn8is 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8is](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7v_postpay_g | 按量付费的(ebm)gn7 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7e_postpay_g | 按量付费的(ebm)gn7e /gn7ex 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ex](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7e](elastic-bare-metal-server-overview.md) [GPU](overview-40.md) [计算型超级计算集群实例规格族](overview-40.md) [sccgn7ex](overview-40.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8v_postpay_g | 按量付费的(ebm)gn8v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn8v/gn8v-tee](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_ag_spot_g | 抢占式的 ARM+GPU 类实例 GPU 卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7r](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [计算型弹性裸金属服务器实例规格族](retired-instance-types.md) [ebmgn6ia](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_vgpu_spot_g | 抢占式的 GPU 虚拟化类（vGPU）实例数量上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn8ia](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [sgn7i-vws（共享](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [CPU）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn7i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [虚拟化型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [vgn6i-vws](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn6i](retired-instance-types.md) [GPU](retired-instance-types.md) [虚拟化型实例规格族](retired-instance-types.md) [vgn5i](retired-instance-types.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7i_spot_g | 抢占式的(ebm)gn7i /ebmgn7ix /gn7s 的 GPU 实例卡数上限 ebmgn7ix/gn7s 的 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ix](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn5_spot_g | 抢占式的 gn5/gn5i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn5i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6i_spot_g | 抢占式的(ebm)gn6i 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6i](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6v_spot_g | 抢占式的(ebm)gn6v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6v](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn6e_spot_g | 抢占式的(ebm)gn6e 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn6e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn6e](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8i_spot_g | 抢占式的(ebm)gn8is 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8is](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7v_spot_g | 抢占式的(ebm)gn7 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn7e_spot_g | 抢占式的(ebm)gn7e /gn7ex 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7ex](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7e](elastic-bare-metal-server-overview.md) [GPU](overview-40.md) [计算型超级计算集群实例规格族](overview-40.md) [sccgn7ex](overview-40.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
| q_ecs_gn8v_spot_g | 抢占式的(ebm)gn8v 系列 GPU 实例卡数上限 | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn8v/gn8v-tee](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8v](elastic-bare-metal-server-overview.md) | 请根据配额 ID 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS 规格配额](quota-management.md) 。 | [查看或提升云服务器 ECS 规格配额](quota-management.md) |
## 镜像
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下可以保有的自定义镜像最大数量 | 请根据配额 ID q_user-image-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 单个自定义镜像能够共享的用户数最大数量 | 请根据配额 ID q_user-per-image-shared-user-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 镜像与实例规格的限制 | 4 GiB 及以上内存的实例规格不能使用 32 位镜像。 | 无 |
关于镜像的更多内容，请参见[镜像概述](image-overview.md)。
## 块存储
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单实例系统盘数量 | 1 块 | 无 |
| 单实例数据盘数量 | 不同实例规格支持挂载的最多云盘数量不同，更多信息，请参见 [实例规格族](overview-of-instance-families.md) 。 说明 实例可挂载的云盘数量上限由其规格决定，可以通过 [DescribeInstanceTypes](../api-describeinstancetypes.md) 接口查询。创建实例时最多可指定 1 块系统盘和 64 块数据盘，具体以控制台显示为准。如需更多数据盘，可在创建实例后继续挂载。 | 无 |
| 单个阿里云账号在特定地域和可用区下的云盘容量配额 | 不同类型云盘的容量配额不同，您可以查看各类型云盘的对应配额，具体操作请参见 [查看或提升块存储配额](quota-management.md) 。 | [查看或提升块存储配额](quota-management.md) |
| 单块普通云盘容量 | 5 GiB~2,000 GiB | 无 |
| 单块 SSD 云盘容量 | 20 GiB~32,768 GiB | 无 |
| 单块高效云盘容量 | 20 GiB~32,768 GiB | 无 |
| 单块 ESSD 云盘容量 | PL0：1 GiB~65,536 GiB PL1：20 GiB~65,536 GiB PL2：461 GiB~65,536 GiB PL3：1,261 GiB~65,536 GiB | 无 |
| 单块 ESSD AutoPL 云盘容量 | 1 GiB~65,536 GiB | 无 |
| 单块 ESSD PL-X 云盘容量 | 40 GiB~32,768 GiB | 无 |
| 单块 ESSD Entry 云盘 | 10 GiB~32,768 GiB | 无 |
| 单块 ESSD 同城冗余云盘 | 1 GiB~65,536 GiB | 无 |
| 单块 SSD 本地盘容量 | 与实例规格有关，5 GiB~7,152 GiB | 无 |
| 单实例 SSD 本地盘总容量 | 与实例规格有关，最大支持 8*7,152 GiB | 无 |
| 单块弹性临时盘容量 | 64 GiB~8,192 GiB | 无 |
| 系统盘单盘容量限制 | Windows Server：40 GiB~2,048 GiB FreeBSD：30 GiB~2,048 GiB 其他 Linux：20 GiB~2,048 GiB 说明 普通云盘（上一代云盘产品，已逐步停止售卖）作为系统盘时容量上限为 500 GiB。 | 无 |
| 本地盘实例是否可以自行挂载新的本地盘 | 不允许。 | 无 |
| 本地盘实例是否支持变更配置 | 仅允许变更带宽。 | 无 |
| Linux 系统盘挂载点范围 | /dev/vda | 无 |
| Linux 数据盘挂载点范围 | 挂载的数据盘数量不同，挂载点的命名不同： 1~25 块数据盘： /dev/vd[b-z] 。 大于 25 块数据盘： /dev/vd[aa-zz] ，例如第 26 块数据盘会被命名为 /dev/vdaa ，第 27 块数据盘为 /dev/vdab ，以此类推。 | 无 |
说明
块存储按照二进制单位计算。二进制单位用于表示1024进制的数据大小。例如，1 GiB=1,024 MiB。
关于块存储的更多内容，请参见[块存储概述](elastic-block-storage-devices.md)。
## 快照
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单块云盘可以保留的手动快照个数 | 2,000 | 无 |
| 单块云盘可以保留的自动快照个数 | 2,000 | 无 |
| 单块云盘可以保留的归档快照个数 | 10,000 | 无 |
| 单个阿里云账号在单地域下可以保留的自动快照策略个数 | 100 | 无 |
| 单块云盘可以设置的自动快照策略个数 | 10 个 | 无 |
| 单块云盘并发创建快照个数 | ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余）：10 上一代云盘（SSD 云盘、高效云盘和普通云盘）：1 | 无 |
| 单块云盘并发归档快照个数 | 10 | 无 |
| 块存储类型 | ESSD PL-X 云盘、 本地盘和弹性临时盘均不支持创建快照。 目前仅 ESSD 系列云盘（ESSD、ESSD AutoPL 和 ESSD Entry） 支持快照一致性组功能，且云盘未开启 [多重挂载功能](enable-multi-attach.md) 。 仅 ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余） 支持快照极速可用能力。更多信息， 请参见 [快照极速可用能力](enable-or-disable-the-instant-access-feature.md) 。 | 无 |
| 下载或导出快照 | 不支持下载或导出已创建的快照。 您可以先 [使用快照创建自定义镜像](create-a-custom-image-from-a-snapshot.md) ，然后再 [导出自定义镜像](export-a-custom-image.md) 到本地。 | 无 |
| 手动快照和自动快照创建过程约束 | ESSD 系列云盘（ESSD、ESSD AutoPL、ESSD Entry 和 ESSD 同城冗余） 单块云盘支持手动和自动同时并发创建快照。但是并发创建快照有最大个数限制，详情请参见 [快照使用限制](limitations.md) 。如果云盘并发创建的快照个数达到了上限，则后续并发创建快照会失败。 上一代云盘（SSD 云盘、高效云盘和普通云盘） 不支持手动和自动同时并发创建快照。 在自动快照创建时间点，如果云盘正在执行创建快照任务（手动或自动创建快照），则系统不会创建该时间点的自动快照，而是在下一个时间点正常创建自动快照。 如果云盘正在执行创建自动快照任务，您需要等待自动快照完成后，才能手动创建快照。 | 无 |
关于快照的更多内容，请参见[快照概述](snapshot-overview.md)。
## SSH密钥对
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在单个地域的 SSH 密钥对配额 | 500 | 无 |
| 支持 SSH 密钥对的镜像类型 | 仅支持 Linux 系统。 | 无 |
关于SSH密钥对的更多内容，请参见[管理](ssh-key-pairs.md)[SSH](ssh-key-pairs.md)[密钥对](ssh-key-pairs.md)。
## 公网带宽
单个地域，单个阿里云账号下所有按量付费及抢占式实例的按固定带宽计费的公网带宽峰值售卖总和限制：
说明
如需更大售卖带宽，您可以根据配额IDq_internet-bandwidth-pay-by-bandwidth-of-postpaid-instance查看并申请提升该配额。具体操作，请参见[查看或提升云服务器 ECS](quota-management.md)[配额](quota-management.md)。
| 地域名称 | 限制 |
| --- | --- |
| 华北 2（北京）、华东 2（上海）、华东 1（杭州）、华南 1（深圳） | 50 Gbps |
| 中国香港、新加坡 | 20 Gbps |
| 其他 | 10 Gbps |
自2020年11月27日起，创建和变配ECS实例时带宽峰值受账户限速策略影响：
说明
如需更大带宽峰值，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)。
单个地域下，单个阿里云账号下所有按使用流量计费ECS实例的实际运行带宽峰值总和不大于5 Gbps。
单个地域下，单个阿里云账号下所有按固定带宽计费ECS实例的实际运行带宽峰值总和不大于50 Gbps。
单实例带宽峰值限制和更换公网IP限制：
重要
按使用流量计费模式下的出入网带宽峰值都是带宽上限，不作为业务承诺指标。当出现资源争抢时，带宽峰值可能会受到限制。如果您的业务需要带宽的保障，请使用按固定带宽计费模式。
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单实例入网带宽峰值 | 当所购出网带宽峰值小于等于 10 Mbit/s 时，阿里云会分配 10 Mbit/s 入网带宽。 当所购出网带宽峰值大于 10 Mbit/s 时，阿里云会分配与购买的出网带宽峰值相等的入网带宽。 | 无 |
| 单实例出网带宽峰值 | 按使用流量计费：100 Mbit/s 按固定带宽计费： 包年包月实例：200 Mbit/s 按量付费实例：100 Mbit/s 说明 单 ECS 实例的公网带宽上限也与实例规格有关，可以通过 [实例规格族](overview-of-instance-families.md) 列表的 网络带宽基础 指标查看，单实例的公网带宽之和不会高于此上限。 部分实例规格如 ecs.t6-c4m1.large、ecs.t6-c2m1.large、ecs.t6-c1m1.large、ecs.t6-c1m4.large 受网络基础带宽限制，峰值为 80 Mbit/s。 | 无 |
| 单实例更换分配的公网 IP 地址的限制 | 新建实例六小时内可以更换公网 IP 地址，一台实例最多可以更换三次。 | 无 |
关于公网带宽的更多内容，请参见[公网带宽](network-bandwidth.md)。
## 弹性网卡
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下能创建的弹性网卡（辅助网卡）的最大数量 | 请根据配额 ID q_elastic-network-interfaces 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 实例绑定弹性网卡的 VPC 及可用区限制 | 实例和绑定的弹性网卡，必须属于同一 VPC、同一可用区。 实例绑定的多张弹性网卡，可以属于同一 VPC、同一可用区下的不同子网（交换机）。 如果将来自同一子网的两个或多个网卡附加到一个实例，可能会遇到非对称路由等网络问题。您可以通过在一张弹性网卡（主网卡或辅助弹性网卡）上分配一个或多个辅助私网 IP 地址，实现专有网络 VPC 类型 ECS 实例的高利用率和负载故障时的流量转移。更多信息，请参见 [辅助私网](assign-secondary-private-ip-addresses.md) [IP](assign-secondary-private-ip-addresses.md) 。 | 无 |
| 单个实例可绑定的弹性网卡数量上限 | 实例可绑定的网卡数量由实例规格决定，更多信息，请参见 [实例规格族](overview-of-instance-families.md) 中的 弹性网卡 。 | 无 |
关于弹性网卡的更多内容，请参见[弹性网卡概述](eni-overview.md)。
## 前缀列表
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在单个地域的前缀列表数量上限 | 100 | 无 |
| 单个前缀列表中设置的条目数量上限 | 200 | 无 |
| 单个前缀列表的关联资源数量上限 | 1,000 | 无 |
关于前缀列表的更多内容，请参见[前缀列表概述](overview-32.md)。
## 端口列表
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号下在单个地域的端口列表数量上限 | 1000 | 无 |
| 单个端口列表中设置的条目数量上限 | 2000 | 无 |
| 单个端口列表的关联资源数量上限 | 1000 | 无 |
关于端口列表的更多内容，请参见[端口列表概述](overview-32.md)。
## 安全组
| 限制项 | 普通安全组限制 | 企业级安全组限制 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下的安全组总数量上限 | 请根据配额 ID q_security-groups 查看或申请提升对应配额。具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | 与普通安全组相同 |
| 单张弹性网卡可以关联的安全组数量 | 10 | 与普通安全组相同 |
| 单张弹性网卡关联的所有安全组的规则（包括入方向规则与出方向规则）数量之和的上限 | 1,000 | 与普通安全组相同 |
| 单个安全组中，授权对象为安全组的规则数量 | 20 | 0 条，在企业级安全组中，您不能添加授权对象为安全组的规则，也不能将企业级安全组作为其他安全组规则中的授权对象。 |
| 单个专有网络 VPC 类型的安全组能容纳的 VPC 类型 ECS 实例数量 | 不固定，受安全组能容纳的私网 IP 地址数量影响。 | 无限制 |
| 单个阿里云账号在特定地域下单个专有网络 VPC 类型的安全组能容纳的私网 IP 地址数量 | 6,000 说明 IP 占用数按照安全组关联的弹性网卡（包括实例主网卡、辅助网卡）的私网 IP 数量计数，包括主私网 IPv4、IPv6、辅助私网 IPv4、IPv4 前缀、IPv6 前缀等所有类型 IP 地址的数量总和。 如果您有超过 6,000 个私网 IP 需要内网互访，可以将这些私网 IP 的 ECS 实例分配到多个安全组内，并通过互相授权的方式允许互访。 您可以在 [配额中心](https://quotas.console.aliyun.com/products/ecs/quotas?spm=a2c4g.11186623.0.0.376656addmG73f) 根据配额 ID q_vpc-normal-security-group-ip-count 查看专有网络普通安全组内的私网 IP 地址数量上限。 | 65,536 说明 IP 占用数按照安全组关联的弹性网卡（包括实例主网卡、辅助网卡）的数量计数，即关联的所有弹性网卡的数量总和。 |
| 公网访问端口 | 基于安全考虑，ECS 实例 25 端口默认受限，建议您使用 SSL 加密端口（通常是 465 端口）来对外发送邮件。 具体操作，请参见 [使用](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [SSL](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [加密](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [465](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) [端口发送邮件](https://help.aliyun.com/zh/cloud-web-hosting/use-cases/encrypted-using-ssl-port-465-to-send-email#task-2669194) 。 | 与普通安全组相同 |
关于安全组的更多内容，请参见[安全组概述](overview-44.md)。
## 预留实例券
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在所有地域下的地域级预留实例券总数量 | 20 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 单个阿里云账号在单个可用区的可用区级预留实例券数量 | 20 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 预留实例券规格 | gn6i、t5 实例规格族不支持地域级预留实例券、也不支持拆分和合并。 说明 购买预留实例券时支持选择的实例规格以实际界面显示为准。 | 无 |
| 抵扣的资源类型 | 仅支持抵扣按量付费实例（不含抢占式实例）。 仅支持抵扣计算资源（vCPU 和内存）的费用，不支持抵扣网络、存储等资源的费用。关于 ECS 实例计费详情，请参见 [计费概述](../billing-overview.md) 。 Windows 类型的预留实例券还支持抵扣镜像的费用。 说明 Windows 类型的预留实例券在购买时已经包括了 Windows 镜像的费用，可以为运行 Windows 系统的按量付费实例抵扣镜像部分的账单。 | 无 |
关于预留实例券的更多内容，请参见[什么是预留实例券](../reserved-instances.md)。
## 节省计划
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号可购买的节省计划数量 | 200 | 无 |
| 抵扣的资源类型 | 仅支持抵扣 ECS 及 ECI 按量付费实例（不含抢占式实例），详细的抵扣项及抵扣规则信息请参见 [节省计划抵扣项及抵扣规则](../savings-plan-credit-rules.md) 。 ECS 实例仅支持抵扣：计算资源（vCPU 和内存）、镜像、系统盘、数据盘（包括容量费用、预配置性能费用、性能突发费用）、固定公网带宽。关于 ECS 实例计费详情，请参见 [计费概述](../billing-overview.md) 。 ECI 实例（非指定实例规格）仅支持抵扣：计算资源（vCPU 和内存），关于 ECI 实例计费详情，请参见 [ECI](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) [实例计费](https://help.aliyun.com/zh/eci/product-overview/elastic-container-instances) 。 | 无 |
关于节省计划的更多内容，请参见[什么是节省计划](../savings-plans.md)。
## 存储容量单位包
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单次可以购买的存储容量单位包最大容量 | 50 TiB | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) |
| 单个地域内最大支持购买 SCU 数量 | 100 | 无 |
| 存储容量单位包支持的产品类型 | ESSD 云盘、SSD 云盘、高效云盘和普通云盘。 容量型 NAS 和性能型 NAS。 标准快照。 标准型 OSS、低频型 OSS 和归档型 OSS。 云备份的备份库存储容量。 相册与网盘服务。 | 无 |
| 抵扣类型 | 仅支持抵扣按量付费账单，不支持抵扣抢占式实例中云盘的按量付费账单。 | 无 |
| 生效时间 | 支持设置生效时间，但生效时间不能超过创建时间六个月。 | 无 |
| 通过 API 创建和管理 SCU | 暂不支持。 | 无 |
关于存储容量单位包的更多内容，请参见[存储容量单位包](../storage-capacity-units-1.md)[SCU](../storage-capacity-units-1.md)。
## 实例启动模板
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下可拥有的启动模板的最大数量 | 请根据配额 ID q_launch-template-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 单个阿里云账号在特定地域下可拥有的单个启动模板的版本最大数量 | 请根据配额 ID q_launch-template-version-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 实例启动模板参数 | 创建实例启动模板时，所有参数都是可选的。但是，如果实例启动模板中未包含必要参数（例如实例规格、镜像等），则在使用该模板创建实例时还需要补充这些必要参数。 | 无 |
| 修改已创建的实例启动模板 | 实例启动模板创建成功后，无法进行修改。您可以通过创建启动模板的新版本来更改配置参数。具体操作，请参见 [管理实例启动模板版本](create-a-launch-template-version.md) 。 | 无 |
关于实例启动模板的更多内容，请参见[实例启动模板概述](overview-30.md)。
## 部署集
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下可拥有的部署集的最大数量 | 请根据配额 ID q_deployment-set-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 单个部署集内能容纳的实例数量 | 部署集内能容纳的实例数量和您选择的部署策略有关，请参见 [部署策略](overview-43.md) 。 | 无 |
| 部署集创建专有宿主机 | 部署集不支持创建专有宿主机。 | 无 |
| 地域与可用区限制 | 实例与部署集必须在同一地域；策略为网络低时延的部署集内的实例，必须都在同一可用区。 | 无 |
| 部署集内能创建的实例规格 | 不同部署策略仅支持创建特定的实例规格族，您可以调用 [DescribeDeploymentSetSupportedInstanceTypeFamily](../api-describedeploymentsetsupportedinstancetypefamily.md) 指定部署策略来获取各部署策略支持的实例规格族。 | 无 |
| 合并部署集 | 部署集之间不支持相互合并。 | 无 |
关于部署集的更多内容，请参见[部署集](overview-43.md)。
## 弹性供应组
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 跨地域供应实例 | 弹性供应组不支持跨地域供应实例。 | 无 |
| 单个弹性供应组可指定的配置来源最大数量 | 单个弹性供应组最多指定一个启动模板的特定版本作为实例的基本配置，但是您可以扩展模板中的实例规格，形成多个资源池。 | 无 |
| 单个弹性供应组可设置的资源池最大数量 | 单个弹性供应组下最多支持设置 20 个资源池（即可用区+实例规格的组合）。 | 无 |
| 单个弹性供应组下能创建的实例数量上限 | 1000 | 无 |
关于弹性供应组的更多内容，请参见[弹性供应概述](overview-46.md)。
## 云助手
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下的云助手命令总数量上限 | 请根据配额 ID q_axt-command-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 单个阿里云账号在特定地域下的云助手任务输出大小限制 | 请根据配额 ID q_axt-task-output-size 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | 无 |
| 单个阿里云账号在特定地域下的云助手任务输出保存时长 | 请根据配额 ID q_axt-task-output-life 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | 无 |
| 单个阿里云账号在特定地域下的云助手托管实例激活码数量上限 | 请根据配额 ID q_cloud-assistant-activation-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | 无 |
| 单个阿里云账号在特定地域下的命令执行支持实例上限数 | 请根据配额 ID q_task-instance-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 创建的 Bat、PowerShell 或者 Shell 脚本和自定义参数在 Base64 编码后，使用场景与文件大小限制 | 创建命令：文件大小（Base64 编码后的大小）不能超过 18 KB。 立即执行并保存命令：文件大小不能超过 18 KB。 立即执行但不保存命令：文件大小不能超过 24 KB。 上传文件：文件大小不能超过 32 KB。 | 无 |
| 一条命令中的自定义参数个数上限 | 20 | 无 |
| 操作系统 | 您只能在以下操作系统中运行云助手命令： Alibaba Cloud Linux CentOS 6/7/8 及更高版本 CoreOS Debian 8/9/10 及更高版本 OpenSUSE RedHat 5/6/7 及更高版本 说明 RedHat 中需要您自行下载 rpm 包安装云助手 Agent，具体操作，请参见 [安装云助手](install-the-cloud-assistant-agent.md) [Agent](install-the-cloud-assistant-agent.md) 。 SUSE Linux Enterprise Server 11/12/15 及更高版本 Ubuntu 12/14/16/18 及更高版本 FreeBSD 11/12/13/14 及更高版本 Window Server 2012/2016/2019 及更高版本 说明 使用 ECS 公共镜像创建的实例会默认安装云助手 Agent。 使用自定义镜像或者云市场镜像创建的实例需要您首先确认操作系统是否支持云助手，再自行安装云助手 Agent。具体步骤请参见 [安装云助手](install-the-cloud-assistant-agent.md) [Agent](install-the-cloud-assistant-agent.md) 。 | 无 |
关于云助手的更多内容，请参见[云助手概述](overview-10.md)。
## 网络连通性诊断
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个地域下诊断线路的最大数量 | 100 | 无 |
| 单个地域下诊断任务的最大数量 | 1,000 | 无 |
| 单个地域下同时执行的诊断任务的最大数量 | 5 | 无 |
关于网络连通性诊断的更多内容，请参见[诊断网络连通性](diagnose-network-connectivity.md)。
## API
| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| API 速率配额 | API 速率配额是指对 OpenAPI 调用频率的约束限制，根据 API 的版本及资源类型，大致分为两类： 云服务器 ECS API 速率配额：API 版本为 2014-05-26 的镜像、安全组、块存储等 API 的速率限制。 查看云服务器 ECS API 速率配额的具体操作，请参见 [查看云服务器 ECS API](quota-management.md) [速率配额](quota-management.md) 。 块存储 API 速率配额：API 版本为 2021-07-30 的块存储高阶特性 API 的速率限制。 查看块存储 API 速率配额的具体操作，请参见 [查看或提升块存储](quota-management.md) [API](quota-management.md) [速率配额](quota-management.md) 。 | 云服务器 ECS API 速率配额：该类型的 API 速率配额暂不支持申请提升。 块存储 API 速率配额：可以申请提升配额，具体操作请参见 [查看或提升块存储](quota-management.md) [API](quota-management.md) [速率配额](quota-management.md) 。 |
关于ECS API的更多内容，请参见[集成概览](../developer-reference/integration-overview.md)。
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
