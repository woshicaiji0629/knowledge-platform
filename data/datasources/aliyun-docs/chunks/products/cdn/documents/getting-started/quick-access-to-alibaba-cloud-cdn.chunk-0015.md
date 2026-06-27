user-guide/set-an-alert-rule.md)。
请根据网站的历史流量、历史带宽和历史HTTPS请求数来设置阈值。如果不清楚网站的流量、带宽和HTTPS请求数信息，您可以先行跳过该配置，待系统稳定运行之后，使用CDN的[用量查询](../user-guide/query-resource-usage-1.md)查看加速域名的用量信息，然后再来[配置用量封顶](../user-guide/configure-usage-cap.md)。
流量封顶
如果计费方式是默认的按流量计费，推荐配置该功能。可以根据历史流量来设置阈值，系统会统计域名在指定周期内产生的总流量。当累计流量超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
带宽封顶
如果计费方式是按带宽峰值计费，推荐配置该功能，能有效控制计费带宽的上限。当系统实时监控到的带宽值超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
HTTPS请求数封顶
如果加速域名需要开启HTTPS访问，并且对HTTPS请求量有明确预算控制，推荐配置该功能。当加速累计请求数超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
提升访问安全
HTTPS证书
如域名需要 HTTPS 访问，请配置证书，否则 HTTPS 不可用。
不需要 HTTPS 时可跳过。
重要
开启HTTPS将产生HTTPS请求数，静态HTTPS请求数每月前500万次免费，超过500万次后，开始计费。HTTPS请求数计费不能使用CDN流量包抵扣，请确保您的账户余额充足，或购买HTTPS请求包，避免欠费导致CDN停止服务。详情请见[静态](../product-overview/billing-of-https-requests-for-static-content.md)[HTTPS](../product-overview/billing-of-https-requests-for-static-content.md)[请求数](../product-overview/billing-of-https-requests-for-static-content.md)。
已在阿里云数字证书管理服务中购买了证书，请选择云盾（SSL）证书中心，并在证书名称中选择已购买的证书，如果无法选择您购买的证书，请检查已购买证书绑定的域名和加速域名是否相同。
使用的是第三方服务商签发的证书，请选择自定义上传（证书+私钥），您需要在设置证书名称后，上传证书（公钥）和私钥，该证书将在阿里云数字证书管理服务中保存。您可以在[我的证书](https://yundun.console.aliyun.com/?spm=5176.2020520110.all.12.16df56a1u1
