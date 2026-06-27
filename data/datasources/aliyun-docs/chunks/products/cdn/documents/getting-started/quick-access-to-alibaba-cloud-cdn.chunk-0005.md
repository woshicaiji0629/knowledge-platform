### 一、添加域名和源站
- 配置域名
为了使您的域名享受到加速服务，需要将您的域名作为加速域名配置在阿里云CDN里。只有完成这一步骤，阿里云CDN才能识别并加速您配置的域名。
添加域名
[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)
在左侧导航栏，单击域名管理。
单击添加域名，配置加速区域、加速域名和业务类型，其他参数均可保持默认。
说明
加速域名是指接入阿里云CDN、用于加速的网站域名或资源域名，也是终端用户实际访问的域名。在上述示例的场景下，此处填写www.example.com。
www.example.com和example.com是两个不同的域名，CDN需要分别添加为加速域名。如果您同时需要加速这两个域名，需在CDN控制台中分别添加www.example.com和example.com，并分别完成CNAME配置。不能将裸域名的CNAME直接解析到带www域名的CDN CNAME地址。
加速区域请根据[加速区域](../user-guide/change-the-accelerated-region.md)的描述，选择合适自身业务的区域，本次演示选择仅中国内地作为加速区域。当加速区域包含中国内地时，域名必须进行[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，否则域名无法正常访问。
业务类型根据[应用场景](../product-overview/scenarios.md)的描述，选择适合您自身业务的场景，本次演示选择图片小文件。
当加速区域为全球（不包含中国内地）时，可以开启全球资源计划。开启后，您的域名可以享受更丰富的节点资源，但是支持的功能会受到限制，请查看[开启全球资源计划后支持的配置功能](../user-guide/configure-global-resource-planning.md)，谨慎评估之后使用。
- Q：配置CDN统一加速域名时有哪些注意事项？
配置统一加速域名时，请注意以下事项：
业务类型选择：建议选择「图片小文件」，以适配静态资源的加速场景。
共享缓存：若多个加速域名的源站内容完全一致，可开启共享缓存功能，提升缓存命中率。
HTTPS支持：如需支持HTTPS访问，需为每个加速域名单独配置SSL证书。
回源HOST设置：回源HOST建议设置为对应的实际源
