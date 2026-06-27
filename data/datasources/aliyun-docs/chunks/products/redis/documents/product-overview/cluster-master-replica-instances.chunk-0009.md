e/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
集群架构实例变配后，数据是否会自动均衡？
在标准架构升级至集群架构，或在集群架构中增减分片时，实例将自动分析数据的分布情况，并执行数据重平衡。您无需执行额外操作。
此外，Proxy模式额外支持[无感扩缩容](imperceptible-scaling.md)。而直连模式在客户端正确处理MOVED重定向的情况下，也能实现无感扩缩容。
该文章对您有帮助吗？
反馈
