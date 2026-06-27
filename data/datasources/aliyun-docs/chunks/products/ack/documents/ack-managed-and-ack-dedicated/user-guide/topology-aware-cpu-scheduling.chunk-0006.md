# 将 <your-pod-name> 替换为Pod实际名称 kubectl describe pod <your-pod-name> -n default
在输出的Containers字段下定位Container ID，并删去前缀（如containerd://）。
预期输出：
Containers: nginx: Container ID: containerd://b8b88a70096aabb0aea197dd2aba78d15bcbe9145198ef46a0474b31*****
确认节点的cgroup版本。
stat -fc %T /sys/fs/cgroup/
输出为cgroup_root：系统使用 cgroup v1。
输出为cgroup2fs：系统使用 cgroup v2。
根据cgroup版本执行对应的验证命令，查看CPU绑核情况。
在cgroup路径中，Pod UID中的-需替换为_。如原始Pod UID为a78a02b5-c87f-4e74-9ddd-254c163*****，则路径中使用的格式为a78a02b5_c87f_4e74_9ddd_254c163*****。
cgroup v1：
