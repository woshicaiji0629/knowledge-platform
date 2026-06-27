### 配置白名单规则
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，单击目标站点操作列的配置WAF。
在站点详情页面，选择安全防护>WAF>白名单规则。
在白名单规则页签，单击新增规则，配置以下参数。
填写规则名称，建议使用能描述放行目的的名称，例如"内部扫描工具放行"。
在如果请求匹配以下规则...区域配置匹配条件，设置识别可信请求的特征，例如客户端IP、URL路径、请求头等。请求匹配规则的详细配置方法，请参见[运算符和分组符号](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/work-with-rules-engine/)。
在则跳过…区域选择该请求需要跳过的防护规则范围。
全部规则：跳过所有WAF和Bots管理规则。适用于完全可信、需要无拦截通过的请求来源。
部分规则种类或ID：选择要跳过的规则类型和[具体规则](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/whitelist-rules#29362fb0b3ojr)[ID](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/whitelist-rules#29362fb0b3ojr)（例如Bot管理、智能限频、频次控制），推荐使用此模式，在放行可信流量的同时保留其他防护能力。
