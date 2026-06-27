## 通过命令查看kubelet参数
[登录节点](overview-of-node-management.md)，查看kubelet参数。
ps -ef | grep kubelet
预期输出：
--enable-controller-attach-detach=true
true：存储插件为CSI。
false：存储插件为Flexvolume。
