## GPU拓扑感知调度优势
NVLink连接的单向通信带宽为25 GB/s，双向通信带宽为50 GB/s，而PCIe连接的通信带宽为16 GB/s。在训练过程中，不同的GPU组合会导致训练速度的差异，因此选择最优的GPU组合能够实现最佳的训练性能。
Kubernetes对节点的GPU拓扑信息缺乏感知，这导致调度过程中的GPU选择较为随机，不同组合的训练速度差异显著。为了解决这一问题，ACK基于[Scheduling Framework](https://developer.aliyun.com/article/766273)机制，实现了GPU拓扑感知调度，从而在节点的GPU组合中选取具有最佳训练速度的配置。
