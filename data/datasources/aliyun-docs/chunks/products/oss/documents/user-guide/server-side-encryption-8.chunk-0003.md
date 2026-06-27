## 权限说明
RAM用户在不同场景中使用服务端加解密的权限说明如下：
说明
关于为RAM用户授权的具体操作，请参见[为](../common-examples-of-ram-policies.md)[RAM](../common-examples-of-ram-policies.md)[用户授予自定义的权限策略](../common-examples-of-ram-policies.md)。
设置Bucket加密方式
具有对目标Bucket的管理权限。
具有PutBucketEncryption和GetBucketEncryption权限。
如果设置加密方式为SSE-KMS，且指定了CMK ID，还需要ListKeys、Listalias、ListAliasesByKeyId以及DescribeKey权限。此场景下的RAM Policy授权策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:List*", "kms:DescribeKey" ], "Resource": [ "acs:kms:*:141661496593****:*" //表示允许调用该阿里云账号ID下所有的KMS密钥，如果仅允许使用某个CMK，此处可输入对应的CMK ID。 ] } ] }
上传文件至设置了加密方式的Bucket
具有目标Bucket的上传文件权限。
如果设置加密方式为KMS，并指定了CMK ID，还需要ListKeys、ListAliases、ListAliasesByKeyId、DescribeKey、GenerateDataKey以及Decrypt权限。此场景下的RAM Policy授权策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:List*", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ], "Resource": [ "acs:kms:*:141661496593****:*"//表示允许调用该阿里云账号ID下所有的KMS密钥，如果仅允许使用某个CMK，此处可输入对应的CMK ID。 ] } ] }
从设置了加密方式的Bucket中下载文件
具有目标Bucket的文件访问权限。
如果设置加密方式为KMS，并指定了CMK ID，还需要Decrypt权限。此场景下的RAM Policy授权策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:Decrypt" ], "Resource": [
