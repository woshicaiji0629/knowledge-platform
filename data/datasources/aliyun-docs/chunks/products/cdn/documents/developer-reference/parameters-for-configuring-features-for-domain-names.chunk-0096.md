## QUIC
iquic
功能说明：QUIC基础参数，该功能详细介绍请参见控制台配置说明[配置](../user-guide/what-is-the-quic-protocol.md)[QUIC](../user-guide/what-is-the-quic-protocol.md)[协议](../user-guide/what-is-the-quic-protocol.md)。
功能ID（FunctionID/FuncId）：281。
参数说明：

| 参数 | 类型 | 是否必填 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| iquic_enable | String | 是 | 是否开启 QUIC 协议： on：开启 off：关闭 | on |

配置示例
{ "Functions": [{ "functionArgs": [{ "argName": "iquic_enable", "argValue": "on" }], "functionName": "iquic" }], "DomainNames": "example.com" }
该文章对您有帮助吗？
反馈
