### 调用示例
以下示例将为您展示如何使用阿里云CLI调用CDN中的DescribeUserDomains命令，查询用户名下所有的域名与状态。DescribeUserDomains命令的详细介绍，请参见[DescribeUserDomains](api-cdn-2018-05-10-describeuserdomains.md)。
执行命令。
aliyun cdn DescribeUserDomains --DomainName mxxxio.top
输出结果。
{ "Domains": { "PageData": [ { "CdnType": "web", "Cname": "mxxx.xxxp.w.kunlunq.com", "Coverage": "domestic", "Description": "", "DomainId": 201xxx553, "DomainName": "mjlxxxao.top", "DomainStatus": "online", "GlobalResourcePlan": "off", "GmtCreated": "2024-08-27T06:29:36Z", "GmtModified": "2024-08-27T06:34:04Z", "ResourceGroupId": "rg-acfmwpdflelaoai", "Sandbox": "", "Sources": { "Source": [ { "Content": "183.xxx.xxx.88.cn-hangzhou.sae.aliyuncs.com", "Port": 80, "Priority": "20", "Type": "domain", "Weight": "10" } ] } } ] }, "PageNumber": 1, "PageSize": 20, "RequestId": "E4EBD2BF-5EB0-4044-9B97-xxxxxx", "TotalCount": 1 } } ] }, "SslProtocol": "off" } ] }, "PageNumber": 1, "PageSize": 20, "RequestId": "34C9E61F-02A0-5EB5-BBCB-16B531ABB9E0", "TotalCount": 1 }
说明
如果调用CDNAPI后返回错误，您需要根据返回的错误码提示检查传入的请求参数及其取值是否正确。
您也可以记录下调用返回的RequestID或SDK报错信息，通过[阿里云](https://next.api.aliyun.com/troubleshoot)[OpenAPI](https://next.api.aliyun.com/troubleshoot)[诊断平台](https://ne
