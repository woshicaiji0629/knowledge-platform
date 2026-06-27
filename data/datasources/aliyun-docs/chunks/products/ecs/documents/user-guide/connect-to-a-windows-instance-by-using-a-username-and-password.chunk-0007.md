## 常见问题
- 如何配置安全组规则以放行3389端口？
在实例所在安全组[添加](start-using-security-groups.md)如下安全组规则：

| 授权策略 | 协议 | 访问来源 | 访问目的(本实例) |
| --- | --- | --- | --- |
| 允许 | 自定义 TCP | 填写本地客户端的公网 IP 地址。 重要 若使用 0.0.0.0/0 ，表示允许任意 IP 访问远程服务端口，存在安全风险，请谨慎使用。 | RDP(3389) 如果修改了实例的 RDP 服务的端口，需调整为实际端口。 |

- 发起连接后，等待一段时间后，提示无法连接？
表示客户端无法连接到服务器。排查顺序：
检查公网IP是否正确。
检查安全组是否放行端口。
检查实例是否处于运行状态。
使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。
- 使用远程桌面（MSTSC）或Windows App如何传输文件？
[在本地](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[Windows](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[中使用远程桌面连接（MSTSC）传输文件](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)
[在本地](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[macOS](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[中使用](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[Windows APP](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[向实例传输文件](use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)
该文章对您有帮助吗？
反馈
