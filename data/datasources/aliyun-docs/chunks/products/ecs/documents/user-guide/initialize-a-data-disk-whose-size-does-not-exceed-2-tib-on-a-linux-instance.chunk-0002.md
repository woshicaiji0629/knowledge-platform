not-exceed-2-tib-on-a-linux-instance.md)云盘。
在云盘状态检测界面，配置挂载点后，单击手动挂载。

| 参数 | 说明 |
| --- | --- |
| 挂载点 | 应为以 / 开头的空路径，可自定义但不可重复。若目录非空，会覆盖其下内容，导致原文件无法访问，可能影响业务。 |

当界面显示云盘检测完成，可以正常使用时，表示挂载文件系统已完成。
重要
当前为临时挂载，重启后失效。为使重启后数据仍可访问，建议登录实例[配置开机自动挂载分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
