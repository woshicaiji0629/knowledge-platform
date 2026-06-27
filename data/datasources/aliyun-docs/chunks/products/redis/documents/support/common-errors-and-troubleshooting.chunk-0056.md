### ERR Unknown sentinel subcommand 'master'
可能原因：Lettuce在[master-replica](https://github.com/lettuce-io/lettuce-core/wiki/Master-Replica)Sentinel模式下会向Redis实例发送Sentinel master/slave命令，而Tair实例在Sentinel兼容模式下仅支持Sentinel get-master-addr-by-name命令，故产生该报错。
解决方法：修改代码为普通模式（非Sentinel），Tair采用自研的高可用服务HA组件，无需Sentinel。
