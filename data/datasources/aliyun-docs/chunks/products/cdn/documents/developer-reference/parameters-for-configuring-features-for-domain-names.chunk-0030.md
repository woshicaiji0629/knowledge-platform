", "argValue": "ali_follow_host" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }
source_group
功能说明：源站组设置。
功能ID（FunctionID/FuncId）：294。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| source_group_name | String | 是 | 源站组名称，支持小写英文字母、数字和下划线，最大长度不超过 128 个字节。 | example_origin |
| source_info | String | 是 | 源站信息，格式为 源站地址_优先级_权重_端口 ，不同参数值之间用下划线分隔，多个源站之间用英文逗号（,）分隔。 源站地址：支持 IPv4、IPv6、域名。 优先级：支持 1~65535（值越小优先级越高）。 权重：支持 1~100（CDN 回源的时候将按照源站权重来分配发送给不同源站的请求比例）。 端口：支持 1~65535。 | 单个源站：192.168.0.1_10_33_80 多个源站：192.168.0.1_10_33_80,192.0.2.1_10_67_80 |
| retry_times | Integer | 否 | 回源重试次数。 | 3 |
| retry_status_rule | Integer | 否 | 回源重试状态码，目前仅支持配置以下五种：4xx、5xx、404、404-or-5xx、4xx-or-5xx，配置其中一个即可。 | 404-or-5xx |
| failback_source | String | 否 | 备份使用基础源信息，取值： on：在源站组内的所有源站都不可用的情况下，将会使用 基本配置-源站信息 里面的源站地址。 off：在源站组内的所有源站都不可用的情况下，将会直接给客户端返回表示源站不可用的 5xx 状态码。 | on |
