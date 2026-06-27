### 可申请提升的配额
一个ALB实例可添加的转发规则数（不计入默认规则）配额如下：

| 配额名称 | 描述 | 默认值 | 最大支持提升至 | 是否支持申请 |
| --- | --- | --- | --- | --- |
| alb_quota_loadbalancer_rules_num_basic_edition | 一个基础版 ALB 实例可添加的转发规则数（不计入默认规则） | 40 个 | 100 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_basic_edition) |
| alb_quota_loadbalancer_rules_num_standard_edition | 一个标准版 ALB 实例可添加的转发规则数（不计入默认规则） | 100 个 | 200 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_standard_edition) |
| alb_quota_loadbalancer_rules_num_standardwithwaf_edition | 一个 WAF 增强版 ALB 实例可添加的转发规则数（不计入默认规则） | 100 个 | 200 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_standardwithwaf_edition) |

当转发规则数接近或达到上限时，您可以：
在配额中心申请提升转发规则数配额。
合并条件相似的转发规则，利用同一条件多值的"或"关系减少规则数量。
基础版实例可[升级](modify-the-configurations-of-alb-instances.md)至标准版或WAF增强版以获得更高的配额上限。
