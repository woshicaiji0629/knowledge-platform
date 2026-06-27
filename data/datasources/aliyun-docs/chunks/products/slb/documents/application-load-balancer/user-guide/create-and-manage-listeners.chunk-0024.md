## 配额

| 配额名称 | 描述 | 默认值 | 最大支持提升至 | 是否支持申请 |
| --- | --- | --- | --- | --- |
| alb_quota_loadbalancer_listeners_num_basic_edition | 一个基础版 ALB 实例可添加的监听数 | 50 个 | 80 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_listeners_num) |
| alb_quota_loadbalancer_listeners_num_standard_edition | 一个标准版 ALB 实例可添加的监听数 | 50 个 | 100 个 |  |
| alb_quota_loadbalancer_listeners_num_standardwithwaf_edition | 一个 WAF 增强版 ALB 实例可添加的监听数 | 50 个 | 100 个 |  |
| alb_quota_max_idle_timeout | 创建监听时连接空闲最大超时时间 | 600 秒 | 3600 秒 |  |
| alb_quota_max_request_timeout | 创建监听时连接请求最大超时时间 | 600 秒 | 3600 秒 |  |

仅[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)支持将alb_quota_max_request_timeout和alb_quota_max_idle_timeout配额提升至最大3600秒；未升级实例仅支持提升至最大900秒。
该文章对您有帮助吗？
反馈
