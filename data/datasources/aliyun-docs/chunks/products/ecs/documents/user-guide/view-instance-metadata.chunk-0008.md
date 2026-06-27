### 步骤一：排查并升级代码及依赖项
在切换到仅加固模式之前，实例及其中部署的应用，必须确保满足以下要求：
确保Cloud-init版本不低于23.2.2：可登录实例并执行cloud-init --version命令查看当前版本。若版本过低，切换仅加固模式后将导致实例启动异常，请先[升级](install-cloud-init.md)Cloud-init版本到23.2.2或更高版本。
所有应用代码/脚本已通过[方式一：加固模式](view-instance-metadata.md)访问实例元数据。
重要
若应用代码依赖Credentials库获取STS Token配置SDK，需将Credentials依赖升级至[支持加固模式的版本](view-instance-metadata.md)。
升级完成后，可[如何检测](view-instance-metadata.md)[ECS](view-instance-metadata.md)[实例是否存在普通模式的元数据访问？](view-instance-metadata.md)，在确定不存在普通模式访问后，开启实例的仅加固模式。
