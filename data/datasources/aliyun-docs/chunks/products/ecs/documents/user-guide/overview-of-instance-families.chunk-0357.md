0万PPS网络收发包能力。
支持ERI（Elastic RDMA Interface），可以在VPC网络下实现RDMA直通加速互联。实例上绑定两张弹性RDMA网卡（Elastic RDMA Interface，简称ERI），每张弹性网卡连接到不同的网卡索引，可以实现160 Gbit/s的网络带宽；所有ERI连接到相同的网卡索引，实例最高可达到100 Gbit/s的网络带宽。更多信息，请参见[AttachNetworkInterface](../api-attachnetworkinterface.md)。
说明
关于ERI的使用说明，请参见[在企业级实例上启用](configure-erdma-on-a-cpu-instance.md)[eRDMA](configure-erdma-on-a-cpu-instance.md)或者[在](on-the-gpu-instance-configuration-erdma.md)[GPU](on-the-gpu-instance-configuration-erdma.md)[实例上启用](on-the-gpu-instance-configuration-erdma.md)[eRDMA](on-the-gpu-instance-configuration-erdma.md)。
ebmgn7ex包括的实例规格及指标数据如下表所示。
