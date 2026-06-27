## 基本信息
ipv6
功能说明：IPv6访问配置，该功能详细介绍请参见控制台配置说明[IPv6](../user-guide/configure-ipv6.md)[配置](../user-guide/configure-ipv6.md)。
功能ID（FunctionID/FuncId）：194。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| switch | String | 是 | 是否开启 IPv6 访问： on：开启。 off：关闭。 | on |
| region | String | 是 | 开启 IPv6 功能的地区，支持星号（*）。 说明 星号（*）表示所有区域都开启 IPv6（目前仅支持针对所有区域都开启 IPv6，如果需要仅针对某个特定区域开启 IPv6，请 [填写信息](https://page.aliyun.com/form/act2017566026/index.htm) 申请）。 不传该参数，表示默认所有区域都开启 IPv6。 | * |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "switch", "argValue": "on" }, { "argName": "region", "argValue": "*" }], "functionName": "ipv6" }], "DomainNames": "example.com" }
