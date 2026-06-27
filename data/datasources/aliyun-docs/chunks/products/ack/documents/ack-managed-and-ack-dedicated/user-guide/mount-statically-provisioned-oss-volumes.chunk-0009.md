## AccessKey方式
创建具有OSS访问权限的RAM用户并获取其AccessKey，使其拥有OSS Bucket的操作权限。
创建RAM用户（如有，可跳过）。
访问[RAM](https://ram.console.aliyun.com/users/create)[控制台-创建用户](https://ram.console.aliyun.com/users/create)页面，按照页面提示完成RAM用户的创建，如登录名称、密码等。
创建权限策略。
本示例遵循最小权限原则，[创建一个自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)，授予访问目标OSS Bucket的权限（OSS只读权限或OSS读写权限）。
访问[RAM](https://ram.console.aliyun.com/policies/create)[控制台-创建权限策略](https://ram.console.aliyun.com/policies/create)页面，切换为脚本编辑，按照页面提示配置策略脚本。
