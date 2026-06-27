### 示例3：授权不支持限制集群的OpenAPI的操作权限
部分OpenAPI不支持限制集群的授权（例如，DescribeEvents），如果您需要给RAM用户或RAM角色授权这些OpenAPI不支持限制集群的OpenAPI的操作权限，请勿在Resource中限定集群ID。修改前后的RAM权限策略对比如下：

| 修改前 RAM 权限策略 | 修改后 RAM 权限策略 |
| --- | --- |
| { "Statement" : [ { "Action" : [ "cs:Get*" , "cs:List*" , "cs:Describe*" ] , "Effect" : "Allow" , "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] } ] , "Version" : "1" } | { "Statement" : [ { "Action" : [ "cs:DescribeEvents" ] , "Effect" : "Allow" , "Resource" : [ "*" ] } , { "Action" : [ "cs:Get*" , "cs:List*" , "cs:Describe*" ] , "Effect" : "Allow" , "Resource" : [ "acs:cs:*:*:cluster/ YOUR_CLUSTER_ID " ] } ] , "Version" : "1" } |
