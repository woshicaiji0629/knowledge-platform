Python
安装Credentials工具。
若使用加固模式获取临时身份凭证，alibabacloud_credentials的版本应不低于0.3.6。pip install alibabacloud_credentials
配置ECS的RAM角色作为访问凭证。
fromalibabacloud_credentials.clientimportClientasCredClientfromalibabacloud_credentials.modelsimportConfigasCredConfig credentialsConfig = CredConfig(type='ecs_ram_role',# 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置role_namerole_name='ROLE_NAME',# 选填，默认值：False。True：表示强制使用加固模式。False：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。disable_imds_v1=True) credentialsClient = CredClient(credentialsConfig)﻿
以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。
RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。importoss2fromalibabacloud_credentials.clientimportClientfromalibabacloud_credentials.modelsimportConfigfromoss2importCredentialsProviderfromoss2.credentialsimportCredentials# 1. 定义凭证适配器：将 Credentials 工具获取的 Token 转换为 OSS SDK 可用的格式classCredentialProviderWrapper(CredentialsProvider):def__init__(self, client): self.client = clientdefget_credentials(self):# SDK 自动请求 http://100.100.100.200 获取临时凭证access_key_id = self.client.get_access_key_id() access_key_secret = self.client.get_access_key_secret() security_token = self.client.get_security_token()returnCredentials(
