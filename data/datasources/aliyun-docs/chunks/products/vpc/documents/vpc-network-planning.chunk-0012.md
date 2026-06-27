## 规划多个路由表
当VPC内不同交换机的流量路由存在明显差异，例如需要约束某些云服务访问公网的行为时，系统路由表无法满足业务需求。您可根据业务类型划分公有交换机与私有交换机，根据云服务是否需要直接访问公网将其部署到不同交换机中，私有交换机部署的资源可以通过公网NAT网关访问公网，实现公网访问的集中控制，满足安全隔离需求。
说明
单个VPC支持创建的自定义路由表的数量为9个，您可以前往[配额管理页面](https://vpc.console.aliyun.com/quota)或[配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=vpc_quota_vswitches_num)提升配额。
