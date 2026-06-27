## 工作流程
VPC 对等连接通过私网连通两个VPC，使部署在两端 VPC 中的资源可以使用私网 IP 互访。
创建VPC对等连接：同账号VPC，系统会自动接受请求并建立连接。跨账号VPC，需要接收端账号接受连接请求。
双向路由配置：为两端VPC分别配置指向对端VPC的路由，才能实现资源互访。
当有大量 VPC 互连、大带宽、低成本的综合需求时，可同时使用 VPC 对等连接和云企业网。二者区别，可参考[VPC](cross-vpc-interconnection-overview.md)[互连](cross-vpc-interconnection-overview.md)。
