### 注意事项
为保障DAS可正常访问云数据库的相关资源，开启该功能后，系统会将名为[AliyunServiceRoleForDAS](https://help.aliyun.com/zh/das/user-guide/aliyunservicerolefordas-role#task-1930737)的关联角色授权给DAS使用。
若实例为云原生版读写分离架构时，实例将以实际使用带宽最高的节点为主，并统一扩缩容所有节点。
若实例为集群架构或经典版读写分离架构时，带宽观测和扩缩容的粒度为数据分片或只读节点，各节点独立进行扩缩容，不会彼此影响。
