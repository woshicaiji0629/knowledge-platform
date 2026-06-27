### 在线调试
CDN在OpenAPI门户提供API调试等功能。在调用前，您需要了解CDN提供的版本、接入点说明、集成方式等信息。
以AddCdnDomain（添加域名）接口为例，在 OpenAPI 门户左侧导航栏选择域名管理>添加/删除域名>添加域名 AddCdnDomain，在中间参数配置区域填写必填参数CdnType（加速域名的业务类型）、DomainName（需要接入CDN的加速域名）、Sources（回源地址列表），以及可选参数ResourceGroupId、CheckUrl、Scope、TopLevelDomain等，然后单击发起调用。调用前需注意：需先开通 CDN 服务；加速域名必须完成备案；每次只能添加一个域名；每个用户最多添加 50 个域名；单个用户调用频率限制为 30 次/秒。
