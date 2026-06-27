rted/purchase-a-dts-instance)。
说明
数据同步作业为计费项，详细价格请参见[数据传输](https://cn.aliyun.com/price/product#/dts/detail)。
在数据传输控制台左侧单击数据同步。
找到已购买的数据同步实例，在右侧单击配置同步链路。
配置如下参数。

| 类别 | 参数 | 说明 |
| --- | --- | --- |
| 源实例信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例 ID | 选择需要切换引擎的 RDS 实例。 |  |
| 连接方式 | 有 非加密传输 和 SSL 安全连接 两种连接方式。选择 SSL 安全连接 ，需要提前开启 [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) ，会显著增加 CPU 消耗。 |  |
| 目标实例信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例 ID | 选择需要切换引擎的 RDS 实例。 |  |
| 连接方式 | 有 非加密传输 和 SSL 安全连接 两种连接方式。选择 SSL 安全连接 ，需要提前开启 [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) ，会显著增加 CPU 消耗。 |  |

单击授权白名单并进入下一步。
等待创建同步账号，然后单击下一步。
将左侧的表testfs移动到右侧，并单击编辑。
修改数据库名为之前创建的testfs_tmp，并单击确定。
单击下一步。
仅勾选全量数据初始化，并单击预检查并启动。
等待预检查完成，单击关闭。
等待数据同步延迟为0ms。
在DMS的SQL窗口执行切换表名命令：
rename table `testfs` to `testfs_del`,`testfs_tmp` to `testfs`;
说明
切换后DTS同步会报错，属于正常现象。
验证数据后请尽快释放同步作业，避免继续产生计费。
