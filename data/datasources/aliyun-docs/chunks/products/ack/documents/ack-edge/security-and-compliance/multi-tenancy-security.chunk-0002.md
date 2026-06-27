于您希望提供Kubernetes即服务 (KaaS) 的场景之中。使用KaaS，您的应用程序与提供一组PaaS服务的控制器和CRD集合一起托管在共享集群中。租户直接与Kubernetes API服务器交互，并被允许对非策略对象执行CRUD操作。还有自助功能，例如允许租户创建和管理他们自己的命名空间。在类似此种环境中，租户被假定正在运行不可信代码。
要在此类环境中隔离租户，您可能需要实施严格的Network Policies以及Pod Sandboxing。具体操作，请参见[安全容器](https://www.aliyun.com/solution/cloudnative/securecontainer?spm=5176.21213303.1391245.1.4f323edayDJh1a)。
软件即服务 (SaaS)
在此环境中，每个租户都与在集群中运行的应用程序的特定实例相关联。每个实例通常都有自己的数据，并使用通常独立于Kubernetes RBAC的单独的访问控制。
与其他场景不同，SaaS环境中的租户不直接与Kubernetes API交互。而是SaaS应用程序负责与Kubernetes API交互以创建每个租户所需要的对象。
