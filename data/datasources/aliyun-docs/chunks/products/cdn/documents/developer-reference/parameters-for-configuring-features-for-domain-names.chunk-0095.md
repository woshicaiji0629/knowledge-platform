## 安全配置
ali_location
功能说明：区域封禁，该功能详细介绍请参见控制台配置说明[区域封禁](../user-guide/configure-a-region-blacklist-or-whitelist.md)。
功能ID（FunctionID/FuncId）：57。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| location | String | 是 | 用于设置封禁策略应用的区域，输入的值包含两种格式： 支持设置区域为某个国家，使用两位大写英文字母组成的国家编码（遵循 ISO3166 标准规范），支持同时输入多个值（不同值之间使用空格分隔）。 支持设置区域为全球（global）。 | CN |
| type | String | 是 | 用于设置封禁策略的类型，取值范围： black：黑名单，封禁对应区域的客户端 IP white：白名单，封禁对应区域以外的客户端 IP | black |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "location", "argValue": "CN" }, { "argName": "type", "argValue": "black" }], "functionName": "ali_location" }], "DomainNames": "example.com" }
