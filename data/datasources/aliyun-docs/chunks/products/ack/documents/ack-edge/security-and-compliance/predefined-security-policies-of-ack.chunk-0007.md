### ACKNoEnvVarSecrets
规则说明：限制Secret以secretKeyRef的形式挂载到应用Pod环境变量中使用。
重要等级：medium。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKNoEnvVarSecrets metadata: name: no-env-var-secrets spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["test-gatekeeper"]
Allowed：
apiVersion: v1 kind: Pod metadata: name: mypod namespace: test-gatekeeper spec: containers: - name: mypod image: redis volumeMounts: - name: foo mountPath: "/etc/foo" volumes: - name: foo secret: secretName: mysecret items: - key: username path: my-group/my-username
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad namespace: test-gatekeeper spec: containers: - name: mycontainer image: redis env: - name: SECRET_USERNAME valueFrom: secretKeyRef: name: mysecret key: username - name: SECRET_PASSWORD valueFrom: secretKeyRef: name: mysecret key: password restartPolicy: Never
