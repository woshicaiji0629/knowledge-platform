### 控制台
创建网关终端节点并配置授权策略
开启网关终端节点的VPC、授权Bucket、在VPC内访问OSS的用户，可以分别归属于不同的阿里云账号。
注意网关终端节点[仅在部分地域支持](vpc-connection-to-cloud-service.md)。
创建网关终端节点并配置终端节点策略。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击创建终端节点。
选择地域并自定义终端节点名称，终端节点类型保持为网关终端节点。
终端节点服务选中阿里云服务，并选中对象存储OSS的终端节点服务。
选中VPC并勾选路由表。
网关终端节点完成创建后，系统会自动在选中的路由表里，增加一个自定义路由条目：目标网段为一个系统前缀列表（里面包含[OSS 在该地域的 VIP 网段](../../oss/documents/user-guide/regions-and-endpoints.md)），下一跳为创建的网关终端节点。
配置终端节点策略：语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
策略示例
下面的示例表示：VPC仅允许账号ID为1746xxxxxx的用户，访问名称为examplebucket的Bucket，进行OSS相关操作。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "oss:*", "Resource": ["acs:oss:*:*:examplebucket", "acs:oss:*:*:examplebucket/*"], "Principal": ["1746xxxxxx"] } ] }
创建完成后，可以在关联路由表的自定义路由条目中，查看到一条系统自动添加的、下一跳指向网关终端节点的路由条目。
配置OSS的bucket授权策略。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击需要配置授权的Bucket名称。
左侧导航选择权限控制 > Bucket授权策略。单击按语法策略添加，单击编辑。
配置Bucket授权策略：语法与访问控制RAM产品的[权限策略语言](../../ram/documents/policy-elements.md)相同。
策略示例
下面的示例表示：
策略1：拒绝所有账号，从除了实例ID为vpc-bp******的VPC外的其他VPC，访问名称为examplebucket的Bucket，进行
