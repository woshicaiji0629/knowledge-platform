### Cluster management
Cluster命令族的命令不适用于标准架构。
通过代理节点连接实例时，会兼容支持部分Cluster命令族的命令，具体为CLUSTER INFO、CLUSTER KEYSLOT、CLUSTER NODES、CLUSTER SLAVES、CLUSTER SLOTS。
Redis开源版5.0版自5.1.3版本、Redis开源版6.0版自0.1.14版本开始支持READONLY与READWRITE命令，之前版本不支持。
