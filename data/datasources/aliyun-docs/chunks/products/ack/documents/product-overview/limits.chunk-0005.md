### 集群配额
下表仅展示各限制项的默认配额。关于本产品支持调整的配额项以及支持调整的配置上限，可以前往[配额中心](https://quotas.console.aliyun.com)查看和申请。配额中心现已支持多个云产品，具体信息，请参见[配额中心支持的云产品](https://help.aliyun.com/zh/quota-center/product-overview/alibaba-cloud-services-that-support-quota-center#topic-2622763)。
①：如需使申请提高的单集群最大节点池数配额生效，还需同时申请弹性伸缩ESS的伸缩组总数配额，请登录[配额平台提交申请](https://quotas.console.aliyun.com/products/csk/quotas)。
②：单节点最大Pod数受集群网络插件影响。
Flannel：受集群创建时网段规划影响。可参考下表，且不支持申请提高。
Terway：依赖[ECS](../../../ecs/documents/user-guide/overview-of-instance-families.md)[实例规格](../../../ecs/documents/user-guide/overview-of-instance-families.md)所提供的弹性网卡数量，建议选择较高规格和较新类型的ECS机型。
