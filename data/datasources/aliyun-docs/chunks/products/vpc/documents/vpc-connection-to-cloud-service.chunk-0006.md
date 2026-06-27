败。
使用授权账号，在授权VPC访问授权Bucket时，访问成功。
若账号、VPC或Bucket任意一个未授权，则访问失败。
修改权限策略
可以通过修改权限策略，调整授权VPC、授权Bucket或授权账号范围。
调整授权VPC：前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Condition字段，增减可访问Bucket的VPC。
调整授权Bucket：
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID，选择终端节点策略页签，调整现有授权策略的Resource字段，增减VPC可访问的Bucket。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Resource字段，增减可被访问的Bucket资源。如果涉及多个Bucket，在每个Bucket里均需要进行操作。
调整授权账号：
注意如果访问OSS的账号是RAM账号，则RAM账号本身需要授予OSS相关Bucket的操作权限，否则可能导致访问失败。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID，选择终端节点策略页签，调整现有授权策略的Principal字段，增减可在VPC内访问Bucket的账号。
前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整现有授权策略的Principal字段，增减可在VPC内访问Bucket的账号。如果涉及多个Bucket，在每个Bucket里均需要进行操作。
绑定/解绑路由表
可以通过网关终端节点绑定/解绑路由表，控制VPC内哪些交换机通过网关终端节点访问云服务。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoin
