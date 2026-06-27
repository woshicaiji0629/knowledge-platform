确。
- 配置源站信息
源站是指您运行业务的网站服务器。CDN 缓存未命中时从源站获取资源。
配置源站信息
完成域名业务信息配置后，在源站信息区域单击新增源站信息。
在对话框中，选择源站的类型，并填写源站地址。
根据您源站的实际情况填写端口，默认使用HTTP协议的80端口。
在新增源站信息对话框中，源站信息支持OSS域名、IP、源站域名、函数计算域名四种类型。优先级取值范围0~127，主源站优先级为20，备源站优先级为30。权重取值范围1~100。端口还支持HTTPS默认443端口及自定义端口（范围1~65535），填写完成后单击确定。
说明
本示例以10.10.10.1作为源站服务器的IP来[配置源站](../user-guide/configure-an-origin-server.md)。
如果您要加速OSS的资源，源站信息请选择OSS域名；
如果您要加速的资源部署在ECS，源站信息请选择IP，IP请填写ECS服务器的公网IP。
如果您要加速的资源在服务器上并且不能使用IP访问，源站信息请选择源站域名，域名填写源站服务器的域名。但请注意，源站域名不能和加速域名相同，否则会造成循环解析。
如果您要加速的资源是阿里云的函数计算，源站信息请选函数计算域名，区域和域名根据您账号的函数计算资源进行选择。
如果您的源站上托管了多个网站，还需要配置[指定源站回源](../user-guide/specify-an-origin-host-for-each-origin.md)[HOST](../user-guide/specify-an-origin-host-for-each-origin.md)。
更多关于源站配置项的说明，请见[配置源站](../user-guide/configure-an-origin-server.md)。
关于CDN与OSS的最佳实践，请见[CDN 加速 OSS 资源](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)。
- 验证加速域名
成功添加加速域名后，为保证DNS解析可以顺利切换而不影响现有业务，建议您先在本地测试加速域名，验证加速域名访问正常后，再将加速域名的DNS解析记录指向CNAME域名。
说明
模拟访问会产生正常的CDN费用。详细信息，请参见[计费组成](../product-overview/billing-overview.md)。
验证加速域名
获取加速域名的CNAME地址。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管
