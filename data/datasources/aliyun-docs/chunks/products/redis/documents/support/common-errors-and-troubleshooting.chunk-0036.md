### ERR eval/evalsha command keys must be in same slot
可能原因：Lua脚本操作的Key不在同一个Slot（槽）中，该报错通常产生于集群实例中。
解决方法：改造Lua脚本，您可以通过CLUSTER KEYSLOT命令获取目标Key的Hash Slot，更多信息请参见[集群架构特殊限制](usage-of-lua-scripts.md)。
