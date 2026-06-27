### 无心跳/心跳为FAIL如何解决
心跳为FAIL时，可能是初次建立心跳需要花费一些时间，请等待两分钟左右后刷新心跳状态，若仍为FAIL，请按如下步骤检查：
请确认服务器与日志服务Project的关联关系，不同关系对应不同的安装流程。
若发现流程选择错误，在服务器上执行chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;卸载命令，再重新选择正确的流程执行即可。
若流程选择正确但心跳为FAIL，请查看安装LoongCollector的服务器上/usr/local/ilogtail/ilogtail_config.json文件中region信息是否与日志服务Project地域的[RegionID](loongcollector-installation-linux.md)一致。
若不一致，请替换安装命令中的${region_id}后重新执行安装命令，LoongCollector将更新上述文件中内容。
此方式将会执行覆盖安装，丢失原配置，慎用于已经进行采集配置的服务器。
若信息一致或重新安装后心跳仍为FAIL，请继续执行后续检查步骤。
若流程中需要设置用户ID文件（即跨账号情况），请检查：
用户ID的值必须为主账号ID，否则请修改。
该主账号ID应为日志服务Project所属的主账号ID，而非ECS服务器所属的主账号ID。
请检查日志服务控制台的机器组中配置的用户自定义标识内容，与服务器用户自定义标识文件中的内容是否一致。若不一致，修改任意一处的内容以保持一致。
若心跳仍然为FAIL，请检查是否满足[前提条件](loongcollector-installation-linux.md)中的网络要求。
