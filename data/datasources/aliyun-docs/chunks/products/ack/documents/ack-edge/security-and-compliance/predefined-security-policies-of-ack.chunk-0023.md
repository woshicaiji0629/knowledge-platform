### ACKEmptyDirHasSizeLimit
规则说明：要求emptyDir类型的Volume必须指定sizelimit。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKEmptyDirHasSizeLimit metadata: name: empty-dir-has-sizelimit spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: name: test-1 namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: sizeLimit: "10Mi"
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - image: k8s.gcr.io/test-webserver name: test-container volumeMounts: - mountPath: /cache name: cache-volume volumes: - name: cache-volume emptyDir: {}
