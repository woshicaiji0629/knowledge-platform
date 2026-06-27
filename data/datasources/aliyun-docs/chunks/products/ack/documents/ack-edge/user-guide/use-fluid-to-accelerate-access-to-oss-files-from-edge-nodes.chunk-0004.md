yRef: name: mysecret key: fs.oss.accessKeySecret --- apiVersion: data.fluid.io/v1alpha1 kind: JindoRuntime metadata: name: hadoop spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxxx replicas: 2 tieredstore: levels: - mediumtype: MEM path: /dev/shm volumeType: emptyDir quota: 2Gi high: "0.99" low: "0.95"
说明
在ACK Edge集群中，您需要通过nodeAffinity和nodeSelector将Dataset和JindoRuntime部署到同一个节点池中，确保节点池内的节点网络互通。
由于边缘节点管控和OSS的访问都需要通过云边网络访问云上，建议您保证足够的网络带宽，以免影响到管控通道的稳定性。
相关参数解释如下表所示：
