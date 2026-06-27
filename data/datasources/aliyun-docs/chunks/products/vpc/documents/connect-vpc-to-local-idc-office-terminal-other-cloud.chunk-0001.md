### 使用专线连接
本地数据中心使用专线连接到阿里云，您需要使用到[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)产品。
连接过程中您需要进行的操作：
申请物理专线端口，并完成您本地数据中心设备到阿里云接入点机房设备的[物理专线连接](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-physical-connection/)。物理专线类型分为独享专线和共享专线，会涉及到运营商工勘、专线铺设、布线施工等工作，整个施工周期预计按月为单位，建议您提前做好时间与预算规划。
独享专线：运营商从您的本地数据中心机房，新增一条专线并连接到阿里云接入点机房，整个施工周期预计需要1至3个月。该条专线及对应端口为您独有。
共享专线：部分运营商会预先与阿里云接入点建立连接，使用共享专线需要运营商从运营商的接入点新增专线，并连接到您的本地数据中心机房，整个施工周期一般在1个月内。在这种连接方式下，运营商接入点和阿里云接入点之间的连接是多租户共享。
配置[边界路由器](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)[VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)、[专线网关](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)[ECR](https://help.aliyun.com/zh/express-connect/user-guide/ecr/)实例，并完成与VPC的连接。
其他建议：
为了避免单条物理专线可能因外界不可抗力导致网络中断（例如专线某处被误挖断），您可以通过双专线、双接入点的方式，提升物理专线链路可靠性。对于非核心业务，您可考虑[使用专线+VPN](https://help.aliyun.com/zh/cloud-network-well-architected-design/dedicated-line-to-build-hybrid-cloud-multi-cloud-network#b47123fe77xk2)[做主备](https://help.aliyun.com/zh/cloud-network-well-architected-design/dedicated-line-to-build-hybrid-cl
