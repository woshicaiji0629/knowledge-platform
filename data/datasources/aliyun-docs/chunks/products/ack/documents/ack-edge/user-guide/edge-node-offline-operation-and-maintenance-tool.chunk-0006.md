### 场景二：修改指定Pod的ConfigMap
在Pod所在的边缘节点上执行如下命令，打开编辑界面。
edgeadm -n {namespace} -p {pod-name} edit configmap {configmap-name}
进入编辑模式，修改ConfigMap模板内容，保存并退出。
修改成功后，指定的Pod会自动重启并使用修改后的ConfigMap。如果节点上还有其他Pod使用该ConfigMap，您可以通过如下命令手动重启Pod使修改生效。
crictl stopp {pod-id}
说明
该命令只会停止Pod，Pod停止后会被kubelet自动重启。
