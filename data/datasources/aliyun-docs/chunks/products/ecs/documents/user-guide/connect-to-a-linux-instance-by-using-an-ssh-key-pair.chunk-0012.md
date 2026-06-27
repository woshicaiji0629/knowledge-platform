## 控制台
进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在左上角选择地域与资源组。
找到对应实例后，单击>获取实例系统日志，然后找到BEGIN SSH HOST KEY FINGERPRINTS，会显示所有主机指纹。
请仔细核对本地客户端提示的指纹（如上例中的 SHA256:******）是否与日志中显示的指纹完全一致。若不一致，则可能正在遭受中间人攻击，需切换至安全网络环境后重试连接。
若找不到BEGIN SSH HOST KEY FINGERPRINTS，需进入实例内查看主机指纹。
