## 应用于生产环境
禁止随意删除或禁用密钥。
一旦删除或禁用密钥，所有依赖该密钥的加密资源（如云盘、快照、镜像）将无法解密，可能导致数据不可恢复。请在操作前进行[密钥关联检测](../../../kms/documents/key-management-service/user-guide/manage-keys-2.md)。
重要
因用户主动操作导致密钥失效而引起的数据不可恢复损失，由用户自行承担。
限制RAM用户仅能创建加密云盘。
为满足特定的安全合规要求，防止因云盘未加密而导致数据泄露，可为账号下的所有RAM用户配置自定义权限策略，[限制其只能创建加密云盘](custom-policies-for-ecs.md)，保护数据的机密性。
禁止RAM用户管理密钥。
为防止密钥被误删除或禁用，可仅授予RAM用户只读访问密钥管理服务（KMS）的权限：AliyunKMSReadOnlyAccess。
批量加密已有系统盘
可使用OOS公共模板[ACS-ECS-BulkyEncryptSystemDisk](https://oos.console.aliyun.com/cn-hangzhou/template/public/detail/ACS-ECS-BulkyEncryptSystemDisk)，通过更换操作系统方式，[加密多台](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)[ECS](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)[实例的系统盘](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)。
