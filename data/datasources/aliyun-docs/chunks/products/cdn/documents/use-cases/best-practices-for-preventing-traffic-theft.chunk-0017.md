### 使用高级模式
通过高级模式，您可以为站点配置针对特定请求的防护规则集，并对不同的防护行为单独设置生效时间。高级模式还支持防护移动应用，也可以将规则集跨域配置到您账户下的其他站点中。您可以参考下面的步骤配置 Bots 规则集：
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>Bots。
在Bots页面，选择高级模式，单击创建规则集。
填写规则集名称，选择防护目标类型为网页/浏览器，选择SDK集成方式为自动集成（推荐）。
根据您需要过滤的请求条件在如果请求匹配以下规则...中配置规则表达式，例如针对来自中国内地的请求进行Bots防护，可配置为：(ip.geoip.country in {"CN"})。更多支持的字段可参考[Bots](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/rules-match-fields-available-for-bots)[可用的规则匹配字段](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/rules-match-fields-available-for-bots)。
选择需要添加的防护执行动作。
针对搜索引擎的Bots：
[合法](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[Bot](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[管理](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)：建议您可以配置您信赖的指定搜索引擎Bots直接放行。
伪造爬虫拦截：用于快速拦截所有搜索引擎的Bots，可结合[合法](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/identify-and-handle-bots-traffic#458e1fa445hit)[Bot](https:/
