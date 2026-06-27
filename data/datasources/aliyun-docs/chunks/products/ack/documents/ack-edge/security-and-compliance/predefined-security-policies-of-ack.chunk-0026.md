：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| mode | string | 是否采用白名单模式，默认值 allowlist 为白名单模式，其他值为黑名单模式。 |
| regions | array | 指定的阿里云 Region ID 列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKOSSStorageLocationConstraint metadata: name: restrict-oss-location annotations: description: "Restricts location of oss storage in cluster." spec: match: kinds: - apiGroups: [""] kinds: ["PersistentVolume", "Pod"] namespaces: - "test-gatekeeper" parameters: mode: "allowlist" regions: - "cn-beijing"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-oss-csi-good namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test csi: driver: ossplugin.csi.alibabacloud.com volumeAttributes: bucket: "oss" url: "oss-cn-beijing.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pod-oss-csi namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test csi: driver: ossplugin.csi.alibabacloud.com nodePublishSecretRef: name: oss-secret volumeAttributes: bucket: "oss" url: "oss-cn-hangzhou.aliyuncs.com" otherOpts: "-o max_stat_cache_size=0 -o allow_other" path: "/"
