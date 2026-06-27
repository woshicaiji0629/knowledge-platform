### 场景一：修改Pod模板
在Pod所在的边缘节点上执行如下命令，打开编辑界面。
edgeadm -n {namespace} edit pod {pod-name}
进入编辑模式，修改Pod模板内容，保存并退出。
修改成功后，Pod会自动重启，可以通过如下命令查询Pod配置，验证修改是否生效。
crictl inspectp {pod-id}
