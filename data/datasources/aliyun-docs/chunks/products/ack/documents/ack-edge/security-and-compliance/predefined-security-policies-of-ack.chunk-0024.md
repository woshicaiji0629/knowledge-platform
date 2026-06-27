### ACKLocalStorageRequireSafeToEvict
规则说明：限制部署在集群指定范围内的Pod必须具有"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"注释标签。集群自动伸缩时不会删除没有此注释标签的Pod。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKLocalStorageRequireSafeToEvict metadata: name: local-storage-require-safe-to-evict spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: name: test-1 namespace: test-gatekeeper annotations: 'cluster-autoscaler.kubernetes.io/safe-to-evict': 'true' spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /test-pd name: test-volume volumes: - name: test-volume hostPath: # directory location on host path: /data # this field is optional type: Directory
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: {}
