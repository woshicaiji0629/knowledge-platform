# 实例登录凭证管理（登录名/密码/密钥对）
实例无默认密码，如忘记密码可[重置](instance-logon-credential-management.md)。创建实例时如未设置登录名，则会使用默认登录名。

| 操作系统 | 默认登录名 | 说明 |
| --- | --- | --- |
| Linux | root | 对应 Linux 系统的超级管理员用户。 |
| Windows | Administrator | 对应 Windows 系统的超级管理员用户。 |

重要
root用户权限较高，直接使用存在安全风险。建议使用ecs-user，通过sudo获取临时root权限执行敏感操作。
