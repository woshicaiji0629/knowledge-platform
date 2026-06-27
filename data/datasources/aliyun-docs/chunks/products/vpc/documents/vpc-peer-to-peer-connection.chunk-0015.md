### 选择限制策略
实际配置时，请将示例中的资源目录 ID、路径或账号 ID 替换为您组织实际的取值，资源目录 ID 与路径可在[资源管理控制台](https://resourcemanager.console.aliyun.com/)获取。
基于资源目录 ID
仅允许 RAM 用户与指定资源目录内的账号建立 VPC 对等连接。将rd-xxxxxx替换为您的资源目录 ID。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": [ "vpc:CreateVpcPeerConnection", "vpc:AcceptVpcPeerConnection" ], "Resource": "*", "Condition": { "StringNotEquals": { "acs:TargetRDId": ["rd-xxxxxx"] } } } ] }
基于资源目录路径
仅允许 RAM 用户与指定资源夹（Folder）路径下的账号建立 VPC 对等连接，适用于精细化分层治理。将示例中的路径替换为您的实际路径。
{ "Version": "1", "Statement": [ { "Effect": "Deny", "Action": [ "vpc:CreateVpcPeerConnection", "vpc:AcceptVpcPeerConnection" ], "Resource": "*", "Condition": { "StringNotLike": { "acs:TargetRDPath": ["rd-xxxxxx/r-xxxxxx/fd-xxxxxx/*"] } } } ] }
