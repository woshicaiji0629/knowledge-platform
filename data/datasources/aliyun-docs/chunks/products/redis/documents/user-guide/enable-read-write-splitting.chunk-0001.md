## 影响
秒级连接闪断：开启或关闭读写分离操作会导致实例发生秒级连接闪断。请在业务低峰期执行，并确保实例写入流量较低且应用具备重连机制。
命令限制增加：由于读写分离不支持部分命令，在实例开启读写分离时，请评估命令限制对业务的影响，更多信息，请参见[读写分离的命令限制](../developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
