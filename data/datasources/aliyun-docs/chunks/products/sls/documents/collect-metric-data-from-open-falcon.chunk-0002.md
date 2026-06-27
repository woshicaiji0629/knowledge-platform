## 使用限制
您所使用的Open-Falcon版本需包含[Influxdb support](https://github.com/open-falcon/falcon-plus/commit/df7a2f80e27902a7e081c595bd1a24080cc624e7)功能。
只有Linux Logtail 0.16.44及以上版本的Logtail支持采集Open-Falcon数据。如果您已在服务器上安装旧版本的Logtail，需先升级。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
出于性能和可靠性考虑，推荐将Logtail和Open-Falcon的transfer模块安装在相同服务器上。
