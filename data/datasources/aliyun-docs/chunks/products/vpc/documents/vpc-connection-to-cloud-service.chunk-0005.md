ucket授权策略：语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
策略示例
下面的示例表示：
策略1：拒绝所有账号，从除了实例ID为vpc-bp******的VPC外的其他VPC，访问名称为examplebucket的Bucket，进行OSS相关操作。
OSS的Action汇总请参见[RAM Policy](../../oss/documents/ram-policy-overview.md)[概述](../../oss/documents/ram-policy-overview.md)。Deny策略建议尽量避免配置Action为*，以免导致Bucket所有者在OSS控制台也无法访问Bucket。
策略2：仅允许账号ID为1746xxxxxx的用户，从实例ID为vpc-bp******的VPC，访问名称为examplebucket的Bucket，进行OSS相关操作。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": ["oss:ListObjects","oss:GetObject","oss:PutObject","oss:DeleteObject"], "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["*"], "Condition": { "StringNotEquals": { "acs:SourceVpc": [ "vpc-bp******" ] } } },{ "Effect": "Allow", "Action": ["oss:*"], "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["1746xxxxxx"], "Condition": { "StringEquals": { "acs:SourceVpc": [ "vpc-bp******" ] } } } ] }
策略配置完成后单击保存。
验证访问策略。
注意如果访问OSS的账号是RAM账号，则RAM账号本身需要授予OSS相关Bucket的操作权限，否则可能导致访问失败。
使用授权账号，在授权VPC访问授权Bucket时，访问成功。
若账号、VPC或Bucket任意一个未授权，则访问失败。
修改权限策略
可以通过修改权限策略，调整授权VPC、授权Bucket或授权账号范围。
调整授权VPC：前往[OSS](https://oss.console.aliyun.com/bucket)
