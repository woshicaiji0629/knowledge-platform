### 场景三：修改指定Pod的Secret
在Pod所在的边缘节点上执行如下命令，打开编辑界面。
edgeadm -n {namespace} -p {pod-name} edit secret {secret-name}
进入编辑模式，修改Secret模板内容，保存并退出。
修改成功后，指定的Pod会自动重启并使用修改后的Secret。如果节点上还有其他Pod使用该Secret，您可以通过如下命令手动重启Pod使修改生效。
crictl stopp {pod-id}
该文章对您有帮助吗？
反馈
