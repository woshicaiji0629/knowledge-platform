# 实例元数据
运行于ECS实例的应用，可通过元数据服务动态查询实例ID、IP等实例元数据信息，避免硬编码。为防范[SSRF](view-instance-metadata.md)[攻击](view-instance-metadata.md)导致元数据泄露，建议通过加固模式访问元数据（需先获取访问令牌），并配置实例仅允许加固模式访问，以有效规避普通模式下的安全风险。
