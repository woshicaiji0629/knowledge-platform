## 创建安全组
购买 ECS 实例时可一并创建安全组，详见[为新建实例配置安全组](start-using-security-groups.md)。如需独立于实例创建安全组并关联至已有实例，按下方控制台或API步骤操作。
控制台
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)页面，单击创建安全组。
设置安全组名称及专有网络 VPC。
选择安全组类型为普通安全组或企业级安全组。
为安全组配置[安全组规则](security-group-rules.md)。安全组规则为有状态规则，只需配置入方向，系统自动放行对应出方向响应流量。常用端口与授权建议见下表，完整示例见[安全组应用指导和案例](security-groups-for-different-use-cases.md)。
一键放行 Web 常见端口（22/80/443/8888）
