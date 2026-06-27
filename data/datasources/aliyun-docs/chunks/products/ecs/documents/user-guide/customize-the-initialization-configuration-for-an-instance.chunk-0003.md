## Linux实例
Linux实例使用cloud-init组件实现实例初始化动作。根据实例是否首次启动，执行不同的配置内容（一些使用较早版本镜像的实例也采用Upstart Job进行初始化工作）。
cloud-init工具支持的自定义数据类型包括可直接配置实例的User-Data和Cloud Config格式，同时还支持其他用户数据格式，最常见的为include文件和Gzip压缩内容。除cloud-init初始化工具外，一些使用较早版本镜像的实例也采用Upstart Job进行初始化工作。
说明
自定义数据格式的详细说明，可参见cloud-init文档[User-Data Formats](https://cloudinit.readthedocs.io/en/latest/topics/format.html)。
如果您的User-Data脚本、Cloud Config数据或Include文件内容的大小超过32 KB，数据类型建议选择Gzip压缩内容。
如果任务需要在实例每次启动时都执行，数据类型建议选择Cloud Config数据或Upstart Job。
