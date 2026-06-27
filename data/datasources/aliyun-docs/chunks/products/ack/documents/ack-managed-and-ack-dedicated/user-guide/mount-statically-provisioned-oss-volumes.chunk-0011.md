## OSS读写权限策略
替换mybucket为实际Bucket名称。{ "Statement": [ { "Action": "oss:*", "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }
使用控制台创建PV时，还需拥有oss:ListBuckets权限。
{ "Effect": "Allow", "Action": "oss:ListBuckets", "Resource": "*" }
（可选）使用KMS托管的指定CMK ID加密OSS Object时，还需为该RAM用户配置KMS权限，详见[使用](encrypt-an-oss-volume.md)[KMS](encrypt-an-oss-volume.md)[托管的指定](encrypt-an-oss-volume.md)[CMK ID](encrypt-an-oss-volume.md)[加密](encrypt-an-oss-volume.md)。
将该策略授权给RAM用户。
访问[RAM](https://ram.console.aliyun.com/users)[控制台-用户](https://ram.console.aliyun.com/users)页面，在RAM用户列表的操作列，单击目标用户对应的添加权限。
在权限策略区域，按照页面提示搜索并选择上一步创建的权限策略，并完成授权的新增。
为RAM用户创建AccessKey，以便后续将其存储为Secret，供PV使用。
访问[RAM](https://ram.console.aliyun.com/users)[控制台-用户](https://ram.console.aliyun.com/users)页面，在RAM用户列表单击目标用户，然后在AccessKey区域，单击创建 AccessKey。
按照页面提示，在对话框进行AccessKey的创建，获取并妥善保管其AccessKey ID和AccessKey Secret。
