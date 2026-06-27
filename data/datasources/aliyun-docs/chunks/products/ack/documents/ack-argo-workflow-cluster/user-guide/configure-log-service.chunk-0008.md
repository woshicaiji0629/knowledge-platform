### 通过Argo CLI直接访问SLS（推荐）
执行以下命令，配置访问权限。
argo config init #按照提示配置相关信息,包括ak、sk等。
执行以下命令获取对应Pod的日志。
argo logs <workflow-name> <pod-name> --sls # 获取对应Pod日志。 argo logs <workflow-name> --sls # 获取对应workflow日志ZIP包。
