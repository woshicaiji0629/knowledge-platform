普通模式
Linux实例
curl http://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称
Windows实例（Powershell）
Invoke-RestMethodhttp://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称
<实例RAM角色名称>需替换为实际的实例RAM角色名称。例如EcsRamRoleDocumentTesting。
返回示例如下：
{ "AccessKeyId" : "STS.*******6YSE", "AccessKeySecret" : "aj******jDU", "Expiration" : "2017-11-01T05:20:01Z", "SecurityToken" : "CAISng********", "LastUpdated" : "2023-07-18T14:17:28Z", "Code" : "Success" }
AccessKeyId、AccessKeySecret、SecurityToken共同构成了临时访问令牌。
Expiration：临时授权访问凭证的有效期。
方式二：通过阿里云CLI获取
CLI支持通过实例元数据服务获取临时访问凭证STS Token的逻辑，且支持周期性自动刷新。
若使用加固模式获取临时身份凭证，CLI的版本不低于3.0.248。
安装CLI。
[安装](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)[CLI（Linux）](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)
[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows)
[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos)
配置身份凭据。
aliyun configure --profile EcsProfile --mode EcsRamRole
该命令为交互式命令，需要根据提示输入相应信息。更多信息请参见[配置凭证](https://help.aliyun.com/zh/cli/configu
