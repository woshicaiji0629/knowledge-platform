的回源端口，例如：80。 scheme_origin 取值为 https 时，只需要配置一个 HTTPS 协议的回源端口，例如：443。 scheme_origin 取值为 follow 时，需要同时配置 HTTP 协议和 HTTPS 协议的回源端口，中间用半角冒号（:）分隔，例如：80:443。 | 80:443 |

配置示例一：CDN跟随客户端的请求协议回源，回源访问的端口为协议默认端口，即HTTP协议对应80端口，HTTPS协议对应443端口。
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "scheme_origin", "argValue": "follow" }], "functionName": "forward_scheme" }], "DomainNames": "example.com" }
配置示例二：CDN跟随客户端的请求协议回源，回源访问的端口为自定义端口，HTTP协议对应8080端口，HTTPS协议对应443端口。
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "scheme_origin", "argValue": "follow" }, { "argName": "scheme_origin_port", "argValue": "8080:4433" }], "functionName": "forward_scheme" }], "DomainNames": "example.com" }
l2_oss_key
功能说明：配置私有Bucket回源。注意，首次使用该功能时，需要进行默认权限策略的一键开启操作，开启后将会授予CDN产品对您同账号下OSS产品的所有Bucket的只读访问权限。该功能详细介绍请参见控制台配置说明[OSS](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](../user-guide/grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。
功能ID（FunctionID/FuncId）：85。
参数说明：
