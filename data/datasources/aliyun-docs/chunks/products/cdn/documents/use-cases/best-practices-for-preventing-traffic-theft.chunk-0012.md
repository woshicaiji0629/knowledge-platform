### 配置IP访问规则
在ESA控制台，选择[站点管理](https://esa.console.aliyun.com/siteManage/list)，在站点列单击目标站点。
在站点详情页面，选择安全防护>WAF>IP访问规则。
选择并填写需要防护的IP/IP段、[ASN](https://help.aliyun.com/zh/edge-security-acceleration/esa/support/what-is-asn)、区域信息，并设置执行动作，单击添加规则。执行动作详情参考[执行动作说明](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/ip-access-rules#56609e4e27ghb)。
可选：创建的规则默认对站点下所有HTTP（7层）请求生效。如需在TCP/UDP（4层代理）请求中生效需在站点详情页面，选择四层代理>配置，在配置页面点击创建应用，在创建应用页面中开启IP访问控制。
