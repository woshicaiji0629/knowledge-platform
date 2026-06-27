### 导入/导出规则
如果需要备份、恢复和迁移规则，可以使用导入导出功能。
导入规则
导入的安全组规则需遵循以下要求：
文件格式：JSON或CSV。
规则数量：单次导入不超过200条。
规则优先级：1到100之间。优先级高于100的规则将被忽略。
在跨地域导入规则时，不支持安全组规则中授权对象为安全组和前缀列表，不支持安全组规则中端口范围为端口列表。
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)在目标安全组详情页面访问规则区域，单击导入安全组规则。
在导入安全组规则页面，单击选择文件并选中本地的JSON或CSV文件，单击确认。
导入失败时，将鼠标悬停在警告图标上可查看原因。
导出规则
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，在目标安全组详情页访问规则区域，单击导出。导出的规则文件的命名格式：
JSON格式：ecs_${region_id}_${groupID}.json。
示例：如果Region ID为cn-qingdao，安全组ID为sg-123，则导出的文件名为ecs_cn-qingdao_sg-123.json。
CSV格式：ecs_sgRule_${groupID}_${region_id}_${time}.csv。
示例：如果Region ID为cn-qingdao，安全组ID为sg-123，导出日期为2020-01-20，则导出的文件名为ecs_sgRule_sg-123_cn-qingdao_2020-01-20.csv。
