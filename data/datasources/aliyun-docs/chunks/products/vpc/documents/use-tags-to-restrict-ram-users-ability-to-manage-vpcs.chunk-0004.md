### 场景示例
企业有不同的部门（如财务部、人事部），需要通过 RAM（访问控制）实现按部门隔离 VPC 资源的管理权限，并且要求特定部门（财务部）在创建资源时必须符合特定的规范（如打上生产环境标签）。
资源划分（部门隔离）：
VPC-A （财务部）：绑定标签department:finance
VPC-B （人事部）：绑定标签department:hr
权限分配与标签鉴权
跨部门隔离（按 VPC，使用 ResourceTag）：只能在 VPC-A (department:finance) 下操作。
资源创建合规（按请求参数，使用 RequestTag）：在 VPC-A 下创建交换机或网络 ACL 时，必须携带env:prod标签。
生命周期安全管理（按子资源，使用 ResourceTag）：只能修改或删除自身带有env:prod标签的交换机和网络 ACL。
