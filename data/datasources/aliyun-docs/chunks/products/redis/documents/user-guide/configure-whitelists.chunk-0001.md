## 白名单设置方法介绍

| 设置方法 | 说明 | 适用场景 |
| --- | --- | --- |
| 添加白名单 | 手动添加客户端所属的 IP 地址到实例的白名单，以允许该客户端访问实例。 | [相同](configure-whitelists.md) [VPC](configure-whitelists.md) [的](configure-whitelists.md) [ECS](configure-whitelists.md) [实例访问](configure-whitelists.md) [Redis](configure-whitelists.md) [不同](configure-whitelists.md) [VPC](configure-whitelists.md) [的](configure-whitelists.md) [ECS](configure-whitelists.md) [实例访问](configure-whitelists.md) [Redis](configure-whitelists.md) [本地设备访问](configure-whitelists.md) [Redis](configure-whitelists.md) |
| 添加安全组 | [安全组](../../../ecs/documents/user-guide/overview-44.md) 是一种虚拟防火墙，用于控制安全组中的 ECS 的出入流量。 如果需要授权多个 ECS 访问实例，您可以为实例绑定 ECS 所属安全组的方式，绑定后安全组内所有 ECS 都可以访问该实例（无需手动填写 ECS 的 IP 地址）。 | [通过安全组批量添加](configure-whitelists.md) [ECS](configure-whitelists.md) [私网和公网](configure-whitelists.md) [IP](configure-whitelists.md) |
| [通过阿里云](configure-whitelists.md) [App](configure-whitelists.md) [设置白名单](configure-whitelists.md) （手机端） | [阿里云](https://help.aliyun.com/zh/document_detail/52854.html) [App](https://help.aliyun.com/zh/document_detail/52854.html) 是阿里云官方出品的移动应用，为您提供随时随地触达阿里云的能力。通过阿里云 App，您可以在手机端快速完成 IP 白名单的设置，同时还支持云资源监控、了解产品动态、购买云产品等功能。 | 通过手机 App 添加专有网络 IP 或公网 IP 到白名单 |
