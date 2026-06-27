## 变配实例功能版本
ALB实例包含基础版、标准版、WAF增强版和扩展版。ALB实例功能版本支持平滑升级，升级期间仍可正常使用ALB实例，业务不受影响。
关于功能版本支持的功能特性，请参见[功能特性](../product-overview/functional-characteristics.md)。
关于资源使用的配额限制，请参见[配额与限制](../product-overview/quotas-and-limits.md)。
变配实例功能版本的变配限制、生效时间、计费影响等相关信息请参见下表。

| 变配限制 | 生效时间 | 计费影响 | 适用场景 |
| --- | --- | --- | --- |
| 标准版 ALB 实例不支持变配为基础版。 WAF 增强版 ALB 实例仅支持变配为标准版，不支持变配为基础版。 WAF 增强版的相关限制和管理操作，请参见 [为 ALB 开启 WAF 防护](../use-cases/enable-waf-protection-for-alb.md) 。 扩展版 ALB 实例不支持变配实例功能版本。 | 通常变配实例功能版本会立即生效，但可能由于网络等原因有一定的延时，请您耐心等待几分钟。 | ALB 实例功能版本变配，对应的实例费会变更，具体费用以实际结算为准。更多信息，请参见 [ALB](../product-overview/alb-billing-rules.md) [计费规则](../product-overview/alb-billing-rules.md) 。 升级为 ALB WAF 增强版实例后，会产生 WAF 3.0 的防护费用。更多信息，请参见 [WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/billing-description.md) [包年包月计费说明](../../../../waf/documents/web-application-firewall-3-0/billing-description.md) 和 [WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/billing-description-v3.md) [按量付费计费说明](../../../../waf/documents/web-application-firewall-3-0/billing-description-v3.md) 。若您的当前账号没有 WAF 实例，您购买 ALB WAF 增强版后，开通的是按量付费 WAF 3.0 实例。 | 当前 ALB 实例功能版本不满足您的业务需求或超出您的业务需求时，您可以变配实例功能版本。 |
