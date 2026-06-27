### ACKPSPFlexVolumes
规则说明：限制在集群指定范围内部署Pod的FlexVolume驱动配置。
重要等级：medium。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedFlexVolumes | array | 允许配置的 FlexVolume 驱动列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPFlexVolumes metadata: name: psp-flexvolume-drivers spec: match: kinds: - apiGroups: [""] kinds: ["Pod", "PersistentVolume"] namespaces: - "test-gatekeeper" parameters: allowedFlexVolumes: #[] - driver: "alicloud/disk" - driver: "alicloud/nas" - driver: "alicloud/oss" - driver: "alicloud/cpfs"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pv-nas namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/nas"
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pv-oss-flexvolume namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/ossxx"
