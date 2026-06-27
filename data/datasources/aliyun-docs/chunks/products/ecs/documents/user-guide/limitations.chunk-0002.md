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
| 多播协议 | 不支持多播协议。如需实现类似多播
