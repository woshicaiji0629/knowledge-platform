## 性能优化
tesla
功能说明：配置页面优化加速，该功能详细介绍请参见控制台配置说明[页面优化](../user-guide/enable-html-optimization.md)。
功能ID（FunctionID/FuncId）：16。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面优化加速： on：开启。 off：关闭。 | on |
| trim_js | String | 否 | 是否优化 HTML 中内嵌的 JS 代码： on：开启。 off（默认）：关闭。 | off |
| trim_css | String | 否 | 是否优化 HTML 中内嵌的 CSS 代码： on：开启。 off（默认）：关闭。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "trim_css", "argValue": "off" }, { "argName": "trim_js", "argValue": "off" }], "functionName": "tesla" }], "DomainNames": "example.com" }
gzip
功能说明：页面Gzip优化，该功能详细介绍请参见控制台配置说明[Gzip](../user-guide/use-the-gzip-compression-feature.md)[压缩](../user-guide/use-the-gzip-compression-feature.md)。
功能ID（FunctionID/FuncId）：35。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启页面 Gzip 优化： on：开启。 off：关闭。 | on |
