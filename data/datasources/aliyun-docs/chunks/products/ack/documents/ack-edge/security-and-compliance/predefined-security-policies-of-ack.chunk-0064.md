### ACKPSPVolumeTypes
规则说明：限制在集群指定范围内部署的Pod使用指定Volume挂载类型。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| volumes | array | 允许使用的 Volume 挂载类型列表。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPVolumeTypes metadata: name: psp-volume-types spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: volumes: # - "*" # * may be used to allow all volume types - configMap # - emptyDir - projected - secret - downwardAPI - persistentVolumeClaim # - hostPath #required for allowedHostPaths - flexVolume #required for allowedFlexVolumes
Allowed：
apiVersion: v1 kind: Pod metadata: name: pv-oss namespace: test-gatekeeper spec: containers: - name: test image: test volumes: - name: test flexVolume: driver: "alicloud/oss"
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: containers: - image: test name: test volumes: - name: test-volume hostPath: path: /data
