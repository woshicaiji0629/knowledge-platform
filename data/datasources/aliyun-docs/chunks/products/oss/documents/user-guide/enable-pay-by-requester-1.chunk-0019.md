## 应用于生产环境
RAM 角色访问的计费归属：当请求者通过扮演阿里云RAM角色来访问数据时，该角色所属的账户将为此请求付费。
错误做法：让请求者扮演Bucket 拥有者账号下的 RAM 角色来获取访问数据的权限。此场景下，所有请求是以 Bucket 拥有者的身份执行，产生的请求和流量费用仍将由 Bucket 拥有者支付，无法实现成本转移。
正确做法：通过Bucket Policy 直接为请求者授予访问数据的权限。
预签名 URL 陷阱：
错误做法：由 Bucket 拥有者使用身份凭证（AccessKey 或 STS 临时凭证）生成预签名 URL 并对外分享，此时请求是以Bucket 拥有者身份发起，相关费用由Bucket 拥有者承担。
正确做法：由请求方使用身份凭证（AccessKey 或 STS 临时凭证）来生成预签名 URL，并在生成时包含x-oss-request-payer=requester参数，签名的计算方法见[在](../developer-reference/add-signatures-to-urls.md)[URL](../developer-reference/add-signatures-to-urls.md)[中包含签名](../developer-reference/add-signatures-to-urls.md)。请求方将此 URL 对外分享使用时，费用由请求方承担。
兼容性风险：开启请求者付费会影响静态网站托管依赖的匿名访问机制，导致网站无法正常工作，建议将网站前端资源（HTML/CSS/JS）与需要请求者付费的数据分别部署在不同的Bucket中。
