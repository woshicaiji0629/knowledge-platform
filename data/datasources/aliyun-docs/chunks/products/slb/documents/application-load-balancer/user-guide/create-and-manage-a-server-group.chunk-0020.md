### API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)或[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)时，通过SlowStartConfig配置慢启动。
说明
慢启动运行机制：
服务器组内健康检查正常的已有后端服务器不会自动进入慢启动模式。为空的服务器组首次添加的后端服务器也不会进入慢启动模式；仅当至少有一个健康检查正常的后端服务器未处于慢启动状态时，新添加的后端服务器才会进入慢启动模式。
删除处于慢启动模式的后端服务器，该服务器退出慢启动模式。再次添加同一后端时，健康检查正常后重新进入慢启动模式。
处于慢启动模式的后端服务器健康检查异常时退出慢启动模式，健康检查恢复正常后重新进入慢启动模式。
健康检查开启时，后端服务器健康检查正常后慢启动生效；健康检查关闭时，慢启动立即生效。
更多信息，请参见[配置慢启动](smooth-business-start-through-alb-slow-start.md)。
