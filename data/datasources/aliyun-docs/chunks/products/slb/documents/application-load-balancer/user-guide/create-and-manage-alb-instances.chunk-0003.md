verview/migrate-a-waf-instance-to-waf-3.md)。ALB 默认不开启 X-Forwarded-Proto 头字段。释放 WAF 2.0 实例后，直接访问 ALB 可能会因后端服务无法正确识别协议（HTTP/HTTPS）而导致业务异常（例如，无限重定向）。为避免此问题，务必在 ALB 监听配置中手动开启X-Forwarded-Proto请求头。
（仅当实例网络类型为公网）加入共享带宽：双可用区ALB实例默认公网带宽峰值为400Mbps，可加入[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#ea9cb55b4ambt)以获取更大带宽峰值。
（仅当实例网络类型为公网，且未选择加入共享带宽）公网计费方式：默认为[按流量计费](../../../../eip/documents/pay-as-you-go.md)且无法修改。
按流量计费模式下，带宽峰值不作为业务承诺指标，仅作为参考值和带宽上限峰值。当出现资源争抢时，带宽峰值可能会受到限制。
实例名称和[资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)：建议合理设置以简化管理。购买实例后，支持在[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面修改实例名称及使用[标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)管理实例。
