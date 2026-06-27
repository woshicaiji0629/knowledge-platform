st EIP实例会被分配一个可在整个接入区域内发布、不受地域限制的公网IP地址。在将此IP地址与后端资源进行绑定后，接入区域内的用户流量将通过该IP地址从就近接入点进入阿里云网络。进入阿里云网络后，Anycast EIP可以智能选择路由并自动完成网络调度，将用户的网络访问请求送达至后端资源节点，提升用户的公网访问体验。

| 对比项 | 弹性公网 IP（BGP 多线） | 弹性公网 IP（BGP 多线-精品） | 任播弹性公网 IP（Anycast EIP） |
| --- | --- | --- | --- |
| 适用场景 | 通用低成本公网访问 | 海外回中国内地流量 | 全球多地域使用相同 IP |
| 限制说明 | 业务部署在某地域（不限） 终端用户使用互联网，从任意地区访问 | 业务仅限部署在 [海外部分地域](../../eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md) 终端用户使用互联网，从中国内地访问 | 业务仅限部署在 [海外部分地域](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-8ea-s1r-s8b) 终端用户使用互联网，从海外地区 [Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-f48-q88-8mz) [接入点位置](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#title-f48-q88-8mz) 就近访问 |
| 质量 | 一般（流量经过运营商普通线路） | 较高（流量经过运营商精品线路） | 较高（流量经过运营商普通线路、阿里云优质全球骨干网络） |
| 成本 | 低 | 中 | 高 |
