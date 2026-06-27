unctionID/FuncId）：212。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ali_origin_dns_host | String | 是 | 回源查询 DNS 使用的域名。 | example.com |

配置示例：通过设置parentid来引用已经使用规则引擎功能（功能函数：condition，功能ID：250）创建好的某个规则条件（通过添加配置时生成的configid来引用），实现在用户请求命中这个规则条件的情况下，回源到指定的源站地址。
{ "Functions": [{ "functionArgs": [{ "argName": "ali_origin_dns_host", "argValue": "example.com" }], "functionName": "origin_dns_host", "parentId":30119730104**** }], "DomainNames": "example.com" }
origin_host
功能说明：配置指定源站回源HOST，可以对指定源站设置指定的回源HOST，该功能详细介绍请参见控制台配置说明[指定源站回源](../user-guide/specify-an-origin-host-for-each-origin.md)[HOST](../user-guide/specify-an-origin-host-for-each-origin.md)。
功能ID（FunctionID/FuncId）：242。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin | String | 是 | 指定源站地址（也可以不指定源站地址，不指定源站地址时，参数 origin 的值设置为 all，代表所有源站）。 | example.com |
| host | String | 是 | 指定 HOST（也可以不指定 HOST，参数 host 的值设置为 ali_follow_origin 代表跟随源站地址作为 host 值）。 | host.example.com |
