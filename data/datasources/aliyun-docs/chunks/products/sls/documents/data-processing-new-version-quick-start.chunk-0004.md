动态目标](processing-result-output-configuration.md) [Project/LogStore](processing-result-output-configuration.md) [输出](processing-result-output-configuration.md) 。如果 SPL 中动态指定，则使用该 LogStore，否则使用当前配置的默认 LogStore。 重要 SPL 规则动态指定的 LogStore 须与当前配置的 Region、授权、以及 Project 相匹配。禁止目标 LogStore 与源 LogStore 相同。 警告 请勿将目标库配置为当前源库（即同源配置），否则可能导致日志被循环写入，产生额外的存储与流量费用。由此造成的资源消耗及相关费用，将由用户自行承担。 |
| 授权方式 | 您可以通过如下方式授予数据加工任务写目标 LogStore 的权限。 默认角色 ：授予数据加工任务使用阿里云系统角色 AliyunLogETLRole 将数据加工结果写入目标 LogStore。 单击 授权系统角色 AliyunLogETLRole ，根据页面提示完成授权。更多信息，请参见 [通过默认角色访问数据](access-data-by-using-a-default-role.md) 。 重要 如果您使用的是 RAM 用户，需要由阿里云账号先完成授权。 已完成授权的阿里云账号，无需再次授权。 自定义角色 ：授予数据加工任务使用自定义角色将数据加工结果写入目标 LogStore。您需先授予自定义角色写数据到目标 LogStore 的权限，然后在 角色 ARN 中输入您自定义角色的 ARN。如何授权，请参见 [通过自定义角色访问数据](access-data-by-using-a-custom-role.md) 。 密钥 ：根据集团安全要求，不再支持 AK/SK 创建任务。 |
| 写入结果集 | 需要写入至当前目标 LogStore 的数据集，数据加工（新版）处理结果的数据集详情请参见 [加工结果输出配置](processing-result-output-configuration.md) 。一个输出目标可配置多个数据集，单个数据集也可被多个目标选中。 |
| 加工范围 |  |
| 时间范围 （数据接收时间） | 指定数据加工任务的时间范围，详细说明如下： 所有 ：从 LogStore 接收到第一条日志的时间点开始数据加工任务，直到加工任务被手动停止。 某时间开始 ：指定数据加工任务的开始时间，从该时间点开始加工，直到加工任务被手动停止。 特定时间范围 ：指定数据加工任务的起止时间，加工任务执行到指定时间后自动停止。 |
| 高级选项 |  |
| 高级参数配置 | 对于加工语句中需要使用的密码
