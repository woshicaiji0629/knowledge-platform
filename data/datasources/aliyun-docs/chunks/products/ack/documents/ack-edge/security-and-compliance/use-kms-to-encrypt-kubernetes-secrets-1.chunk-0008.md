### 如何禁止RAM用户或RAM角色在已创建的ACK Edge集群中开启或关闭Secret落盘加密功能
您可以通过为RAM用户或RAM角色授予如下拒绝操作的RAM权限策略，禁止该RAM用户或RAM角色在已创建的ACK Edge集群中开启或关闭Secret落盘加密功能。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。
{ "Action": [ "cs:UpdateKMSEncryption" ], "Effect": "Deny", "Resource": [ "*" ] }
该文章对您有帮助吗？
反馈
