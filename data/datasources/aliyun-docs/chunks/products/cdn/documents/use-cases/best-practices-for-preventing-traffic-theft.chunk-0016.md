### 使用简易模式
简易模式是面向安全入门级用户的机器流量、爬虫管理功能，适用于所有套餐版本的用户，但是对于部分功能使用会有一些套餐限制。相比于需要专业配置能力配置复杂规则的高级模式，简易模式默认将流量划分为了3类，您只需要快速选择对某类爬虫的处置动作即可实现对爬虫的管理。
配置全局策略
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在左侧导航栏，选择安全防护>Bots。
在Bots页面，选择简易模式，根据下列说明选择合适的配置项进行配置。
绝对是Bot：包含大量恶意爬虫请求。通常建议您配置拦截或滑块挑战。
可能是Bot：这类的请求风险较绝对是Bot相对较低，有可能包含恶意爬虫以及其他流量。通常建议您配置观察或在风险较高时期做滑块挑战。
已通过验证的Bot：这类通常是各类搜索引擎的爬虫，有利于您网站的SEO优化。一般建议放行，如您不希望任何搜索引擎爬虫访问您的站点时可做拦截操作。
为静态资源请求配置Bots检测
若您购买了企业版套餐，可以[配置静态资源免受恶意 Bots 的攻击](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/protect-static-resources)。
重要
如果您启用静态资源保护，可能会阻止定期获取静态资源的正常Bots（例如邮件客户端）。启用此功能之前，请确保您了解现有的基础架构。
启用JavaScript检测
若您购买了企业版套餐，可以使用轻量隐性的[JavaScript](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/javascript-detection)[检测](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/javascript-detection)采集浏览器指纹以提升Bots识别结果。
