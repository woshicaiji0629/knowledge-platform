### ERR READONLY you can't write against a read only instance
可能原因：Tair实例在主备切换、升降配或小版本升级时，将出现秒级的连接闪断和30秒以内的只读状态。
解决方法：属于正常现象，实例会自动恢复，您无需进行任何操作。请提前为您的应用设计重连机制和异常处理的能力，更多信息请参见[升级实例配置](../user-guide/change-the-configurations-of-an-instance.md)。
