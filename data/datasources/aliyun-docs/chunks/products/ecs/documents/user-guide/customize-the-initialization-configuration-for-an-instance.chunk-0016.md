### 2. 创建实例时使用自定义数据
通过控制台创建实例
在[实例购买页](https://ecs-buy.aliyun.com/wizard/#/)展开高级选项区域，在自定义数据区域输入实例自定义数据。
重要
如果实例自定义数据已进行Base64编码，请勾选输入已采用Base64编码，且在进行Base64编码前自定义数据内容的大小不能超过32 KB。否则，无需勾选，系统会自动对内容进行Base64编码。
通过API创建实例
如果您通过API方式创建实例，请在[RunInstances - 批量创建实例](../developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance - 创建实例](../developer-reference/api-ecs-2014-05-26-createinstance.md)接口指定UserData字段。
