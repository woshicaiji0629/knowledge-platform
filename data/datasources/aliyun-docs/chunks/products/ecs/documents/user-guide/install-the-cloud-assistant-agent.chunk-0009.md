## 常见问题
如果我的操作系统不支持安装云助手Agent，该怎么办？
[迁移操作系统](migrate-the-operating-system-of-an-ecs-instance.md)：将当前系统升级或迁移到受支持的版本。
[更换操作系统（更换系统盘）](replace-the-operating-system-of-an-instance.md)：通过更换系统盘功能，为实例安装一个受支持的操作系统。
为什么操作系统支持但无法安装最新版本的云助手Agent？
部分内核在安装云助手时存在最高可安装版本的限制。
执行uname -r查看内核版本。

| 实例的内核版本号 | 云助手 Agent 可升级的最高版本 |
| --- | --- |
| Linux 内核版本 < 2.6.32 | X86/X64 架构：2.2.3.398 ARM 架构：2.4.3.398 |
| FreeBSD 内核版本 < 12.x | 2.3.3.529 |
