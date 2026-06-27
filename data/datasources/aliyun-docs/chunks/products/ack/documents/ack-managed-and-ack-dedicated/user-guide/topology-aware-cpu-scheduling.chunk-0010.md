## 检查Pod Annotation
Pod调度至目标节点后，ack-koordinator会根据Pod的 Annotation 并修改其对应Cgroup的cpuset.cpus文件，以完成物理核心的绑定。
查看Podcpuset信息。
