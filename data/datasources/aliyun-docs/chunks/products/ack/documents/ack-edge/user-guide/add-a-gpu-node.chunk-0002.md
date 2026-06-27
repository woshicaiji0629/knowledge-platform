## 1.26及以上版本集群
ACK Edge集群从1.26版本开始，接入Nvidia GPU时，无需配置gpuVersion参数直接接入，由接入工具自动检查GPU型号并安装相关组件。
添加GPU节点的操作与其他边缘节点操作一致，具体操作，请参见[添加边缘节点](add-an-edge-node.md)。
说明
1.26及以上版本的ACK Edge集群支持全系列NVIDIA官方发布的生产级（Production Grade）GPU显卡，包括Tesla系列、Hopper（H系列）、Ada Lovelace（A系列）以及L系列。
