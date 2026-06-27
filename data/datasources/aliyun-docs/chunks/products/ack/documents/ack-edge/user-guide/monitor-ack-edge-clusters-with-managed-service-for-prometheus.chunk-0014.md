### 为什么GPU监控无法部署？
如GPU节点上存在污点，可能导致GPU监控无法部署。可通过以下步骤查看GPU节点的污点情况。
执行以下命令，查看目标GPU节点的污点情况。
如GPU节点拥有自定义的污点，可找到污点相关的条目。本文以key为test-key、value为test-value、effect为NoSchedule为例说明：
kubectl describe node cn-beijing.47.100.***.***
预期输出：
Taints:test-key=test-value:NoSchedule
通过以下两种方式处理GPU节点的污点。
执行以下命令，删除GPU节点的污点。
kubectl taint node cn-beijing.47.100.***.*** test-key=test-value:NoSchedule-
对GPU节点的污点进行容忍度声明，允许Pod调度到该污点的节点上。
