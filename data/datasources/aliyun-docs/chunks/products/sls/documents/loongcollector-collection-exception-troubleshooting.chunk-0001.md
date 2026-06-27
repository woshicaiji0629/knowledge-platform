### 日志未采集
采集日志时若查询页面无数据，可能原因如下：
在控制台日志库的消费预览中查看，是否采集到日志，若采集到日志但查询无数据，一般由于未[创建索引](create-indexes.md)。
无新增日志：待采集日志文件无更新，则不会采集。
机器组心跳异常：[心跳异常问题汇总排查](troubleshooting-of-abnormal-heartbeat-problems.md)。
无采集配置：采集配置需创建并应用到机器组，然后才能下发到服务器生效，详情参考[机器组与采集配置关联指南](machine-group-and-collection-configuration-association-guide.md)。
采集配置路径错误：检查采集配置中待采集日志文件路径是否正确。
容器场景下还可以开启元容器信息预览查看采集匹配的容器情况。
如果是容器采集场景还需注意：
路径是否有挂载和软链接：不支持软链接，挂载优先级：EmptyDir > hostpath > NAS(不推荐)。更多请参考[日志源与挂载点要求（重要）](kubernetes-cluster-container-log-collection-instructions.md)。
EmptyDir挂载：性能最优，可登录容器查看看日志；hostpath挂载：可登录主机和容器查看日志，容器奔溃日志仍保留；NAS挂载：不推荐，采集NAS文件性能极低且易采集失败，且查询只能简单grep。
采集配置的label和env与容器是否一致：注意docker label需要进宿主机 docker inspect 容器id 查询。
发生采集错误：若上述检查通过，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)。
