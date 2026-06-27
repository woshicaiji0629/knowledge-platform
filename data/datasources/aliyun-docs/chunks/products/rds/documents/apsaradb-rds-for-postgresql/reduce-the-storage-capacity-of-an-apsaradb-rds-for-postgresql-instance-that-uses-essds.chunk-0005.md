### Serverless实例
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在实例资源区域，单击存储空间后的修改。
在修改页签中，滑动滑块或单击减号按钮，调整存储空间，然后单击确定。
说明
缩容后的最小空间由公式min{使用量*1.3，使用量+400 GB}计算，不得低于当前规格允许的最小存储空间，存储空间调整步长5 GB。
在弹出的调整弹性设置对话框中确认变配信息后单击确认。
当实例运行状态变为升降配中时，表示正在进行缩容。
