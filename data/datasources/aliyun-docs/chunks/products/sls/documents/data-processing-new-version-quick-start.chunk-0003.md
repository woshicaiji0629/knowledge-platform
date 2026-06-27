| 参数 | 说明 |
| --- | --- |
| 任务名称 | 数据加工任务的名称。 |
| 显示名称 | 数据加工显示的名称。 |
| 任务描述 | 数据加工任务的描述。 |
| 授权方式 | 您可以通过如下方式授予数据加工任务读取源 LogStore 中数据的权限。 默认角色 ：授予数据加工任务使用阿里云系统角色 AliyunLogETLRole 来读取源 LogStore 中的数据。单击 授权系统角色 AliyunLogETLRole ，根据页面提示完成授权。更多信息，请参见 [通过默认角色访问数据](access-data-by-using-a-default-role.md) 。 重要 如果您使用的是 RAM 用户，需要由阿里云账号先完成授权。 已完成授权的阿里云账号，无需再次授权。 自定义角色 ：授予数据加工任务使用自定义角色来读取源 LogStore 中的数据。您需先授予自定义角色读取源 LogStore 数据的权限，然后在 角色 ARN 中输入您自定义角色的 ARN。如何授权，请参见 [通过自定义角色访问数据](access-data-by-using-a-custom-role.md) 。 密钥 ：根据集团安全要求，不再支持 AK/SK 创建任务。 |
| 存储目标 |  |
| 目标名称 | 存储目标的名称。存储目标中包括 Project、LogStore 等配置。 |
| 目标 Region | 选择目标 Project 所在地域。 |
| 目标 Project | 用于存储数据加工结果的目标 Project 名称。目标 Project 可以通过 SPL 规则动态指定，详情请参见 [动态目标](processing-result-output-configuration.md) [Project/LogStore](processing-result-output-configuration.md) [输出](processing-result-output-configuration.md) 。如果 SPL 中动态指定，则使用该 Project，否则使用当前配置的默认 Project。 重要 SPL 规则动态指定的 Project 须与当前配置的 Region、授权相匹配。 |
| 目标库 | 用于存储数据加工结果的目标 LogStore 名称。目标 LogStore 可以通过 SPL 规则动态指定，详情请参见 [动态目标](processing-result-output-configuration.md) [Project/LogStore](processing-result-output-configuration.md) [输出](processing-result-output-configuration.md) 。
