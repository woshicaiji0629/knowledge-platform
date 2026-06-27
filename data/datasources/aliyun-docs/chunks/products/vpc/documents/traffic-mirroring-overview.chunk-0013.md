### 将非VPC内部流量镜像到跨VPC的镜像目的
配置以下筛选条件，可以监控来自VPC外部的流量和流出VPC的流量。
例如，按照入方向规则的优先级，所有源IP在VPC CIDR地址段内的入方向流量就不采集，但会采集其他所有流量。
由于镜像目的与镜像源位于不同VPC，默认网络隔离。需要使用[VPC](vpc-peer-to-peer-connection.md)[对等连接](vpc-peer-to-peer-connection.md)并在两端VPC配置路由，确保镜像目的路由可达。
