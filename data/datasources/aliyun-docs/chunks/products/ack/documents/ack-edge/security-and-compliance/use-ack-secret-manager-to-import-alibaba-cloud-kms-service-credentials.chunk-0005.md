## 步骤一：安装ack-secret-manager组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击创建，在Chart区域搜索并选中ack-secret-manager，其他设置保持默认，然后单击下一步。
根据弹出的页面提示确认，组件将被安装在默认的kube-system命名空间中，并以组件名称发布应用。如果需要自定义应用名和命名空间，请根据页面提示设置。
在参数配置页面，选择Chart版本为最新版本，并设置相应参数，然后单击确定。
如需开启RRSA认证功能，需要将参数rrsa.enable设置为true。
如需开启定时同步凭据功能，需要配置如下参数。
command.disablePolling：是否关闭凭据的自动轮询功能，设置为false，开启凭据自动轮询功能。
command.pollingInterval：凭据同步的频率，设置为120s，此处以两分钟同步一次凭据为例，可以根据实际需求调整。
配置限流参数：如果集群中具有较多的ExternalSecret（待同步的 KMS 凭据），配置不当可能会引发KMS或RAM侧的限流，因此，需要配置以下限流参数避免发生限流。command.maxConcurrentKmsSecretPulls：每秒可以同步的最大KMS凭据数量，默认为10。
如需指定KMS服务Endpoint地址，需要配置kmsEndpoint参数。
command.kmsEndpoint：参数支持KMS服务的共享网关和专属网关，可按需配置，该参数是全局配置，当前也支持凭据级的配置，具体的配置说明请参见下文[配置](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[KMS](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[服务](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[Endpoint](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[地址](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
创建成功后，会自动跳转到目标集群的ack-secret-manager页面，检查安
