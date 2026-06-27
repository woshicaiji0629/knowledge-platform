限。
如果设置加密方式为KMS，并指定了CMK ID，还需要Decrypt权限。此场景下的RAM Policy授权策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:Decrypt" ], "Resource": [ "acs:kms:*:141661496593****:*"//表示具有该阿里云账号ID下所有KMS的解密权限。若要针对某个KMS密钥进行解密，此处可输入对应的CMK ID。 ] } ] }
