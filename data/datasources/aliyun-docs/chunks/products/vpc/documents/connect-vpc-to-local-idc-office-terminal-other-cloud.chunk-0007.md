## 专线连接多云
建议双专线、双接入点等方式，提升专线链路可靠性。
多云环境下，往往有多个VPC需要互通，人工配置路由相对繁琐，您可以通过将专有网络VPC与专线网关ECR均连接至[转发路由器](../../cen/documents/product-overview/how-transit-routers-work.md)[TR](../../cen/documents/product-overview/how-transit-routers-work.md)，结合BGP动态路由实现全网高效互联。动态路由能够根据网络拓扑的变化自动调整路由表，减少人工配置的工作量，降低组网配置复杂度。
