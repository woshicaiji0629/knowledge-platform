### 操作步骤
控制台
使用阿里云主账号（管理员）完成：
前往[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，[创建](../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../ram/documents/user-guide/create-a-ram-user.md)。
为 VPC 绑定标签：前往[VPC 控制台](https://vpc.console.aliyun.com/vpc/)，将鼠标悬停在目标 VPC标签列的图标，单击气泡框中的绑定或编辑。
VPC-A：department:finance。
VPC-B：department:hr。
在[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)VpcTagAccessPolicy。
本示例中为 VPC 和交换机使用了不同的标签键：
department:finance用于acs:ResourceTag条件：控制可以在哪个VPC下操作。
env:prod用于acs:RequestTag条件：控制创建子资源时必须携带的标签。
在实际使用中，您也可以为两者使用相同的标签键，根据业务需要灵活配置。
{ "Version": "1", "Statement": [ { // Statement 1：仅允许在绑定了标签 department:finance 的VPC中创建交换机和网络ACL。 // 使用 acs:ResourceTag，检查被操作的VPC（父资源）上是否绑定了指定标签。 "Effect": "Allow", "Action": [ "vpc:CreateVSwitch", "vpc:CreateNetworkAcl" ], "Resource": "acs:vpc:*:*:vpc/*", "Condition": { "StringEquals": { "acs:ResourceTag/department": [ "finance" ] } } }, { // Statement 2：创建交换机时，请求中必须携带标签 env:prod。 // 使用 acs:RequestTag，检查API请求参数中是否包含指定标签。 "Effect": "Allow", "Action": [ "vpc:Cre
