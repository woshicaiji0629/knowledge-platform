## 相关文档
可通过CNFS托管OSS存储卷，以提升其性能和QoS控制，请参见[管理](manage-the-lifecycle-of-oss-buckets.md)[OSS](manage-the-lifecycle-of-oss-buckets.md)[生命周期](manage-the-lifecycle-of-oss-buckets.md)。
为保护OSS中的静态敏感数据，建议开启服务端加密，请参见[加密](encrypt-an-oss-volume.md)[ossfs 1.0](encrypt-an-oss-volume.md)[存储卷](encrypt-an-oss-volume.md)。
关于ossfs和OSS的常见问题，请参见[ossfs 1.0](ossfs1-0.md)、[ossfs 1.0](faq-about-oss-volumes-1.md)[存储卷](faq-about-oss-volumes-1.md)[FAQ](faq-about-oss-volumes-1.md)。
启用[容器存储监控](use-csi-plugin-to-monitor-storage-resources-at-the-node-side.md)配置告警，及时发现存储卷的异常或性能瓶颈。
与[ossfs 2.0](ossfs-2-0.md)相比，ossfs 1.0在随机写和并发写场景下能提供更可靠的数据一致性保障。但对于顺序读写场景，ossfs 2.0性能更优。
该文章对您有帮助吗？
反馈
