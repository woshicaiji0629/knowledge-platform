## OSS读写权限策略
替换<myBucketName>为实际Bucket名称。{ "Statement": [ { "Action": "oss:*", "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }
（可选）使用KMS托管的指定CMK ID加密OSS Object时，还需为该角色配置KMS权限，详见[使用](encrypt-an-oss-volume.md)[KMS](encrypt-an-oss-volume.md)[托管的指定](encrypt-an-oss-volume.md)[CMK ID](encrypt-an-oss-volume.md)[加密](encrypt-an-oss-volume.md)。
将该策略授权给RAM角色。
访问[RAM](https://ram.console.aliyun.com/roles)[控制台-角色](https://ram.console.aliyun.com/roles)页面，在RAM角色列表的操作列，单击目标角色对应的新增授权。
在权限策略区域，按照页面提示搜索并选择上一步创建的权限策略，并完成授权的新增。
