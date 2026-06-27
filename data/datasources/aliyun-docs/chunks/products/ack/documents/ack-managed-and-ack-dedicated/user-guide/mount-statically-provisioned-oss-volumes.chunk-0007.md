## OSS只读权限策略
替换<myBucketName>为实际Bucket名称。{ "Statement": [ { "Action": [ "oss:Get*", "oss:List*" ], "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }
