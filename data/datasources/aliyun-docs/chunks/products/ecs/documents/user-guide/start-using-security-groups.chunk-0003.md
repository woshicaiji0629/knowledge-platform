ty-group-rules.md)。安全组规则为有状态规则，只需配置入方向，系统自动放行对应出方向响应流量。常用端口与授权建议见下表，完整示例见[安全组应用指导和案例](security-groups-for-different-use-cases.md)。
一键放行 Web 常见端口（22/80/443/8888）

| 端口 | 协议 | 用途 | 授权对象建议 | 延伸阅读 |
| --- | --- | --- | --- | --- |
| 22 | TCP | SSH 远程连接（Linux） | 办公网或固定公网 IP； 不建议 长期使用 0.0.0.0/0 | [案例](security-groups-for-different-use-cases.md) [2](security-groups-for-different-use-cases.md) |
| 3389 | TCP | RDP 远程桌面（Windows） | 办公网或固定公网 IP； 不建议 长期使用 0.0.0.0/0 | [案例](security-groups-for-different-use-cases.md) [2](security-groups-for-different-use-cases.md) |
| 80 | TCP | HTTP | 公网建站可使用 0.0.0.0/0 | [案例](security-groups-for-different-use-cases.md) [1](security-groups-for-different-use-cases.md) |
| 443 | TCP | HTTPS | 公网建站可使用 0.0.0.0/0 | [案例](security-groups-for-different-use-cases.md) [1](security-groups-for-different-use-cases.md) |
| 8888 | TCP | 宝塔等管理面板（以面板实际端口为准） | 仅管理员 IP；按面板安装提示放行对应端口 | - |
| 3306 等 | TCP | 应用访问 VPC 内数据库 | 在数据库安全组 入方向 授权 源安全组 ，不对公网开放 | [案例](security-groups-for-different-use-cases.md) [3](security-groups-for-different-use-cases.md) |
| 业务端口 | TCP | 跨安全组内网互访（如 8080、3306） | 在 目标 安全组入方向授权 源安全组 ID | [案例](security-groups-for-different-use-cases.md) [5](security-groups-for-different-use-cases.md) |
