### ERR 'xxx' command keys must in same slot
可能原因：在Tair集群架构实例执行的事务或脚本中，存在跨Slot的Key。
解决方法：改造事务或脚本，您可以通过CLUSTER KEYSLOT命令获取目标Key的Hash Slot。
重要
Tair集群架构实例会根据CRC算法将Key均匀的写入不同Slot中。若您希望将多个Key写入到一个Slot中，您可以使用Hash Tags，但该方法若使用不当容易造成数据倾斜，请谨慎使用。
