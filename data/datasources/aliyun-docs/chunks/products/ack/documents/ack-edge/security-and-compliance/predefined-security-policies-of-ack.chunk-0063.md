### ACKPSPSELinuxV2
规则说明：限制在集群指定范围内部署的Pod必须使用allowedSELinuxOptions参数中规定的SELinux配置。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedSELinuxOptions | object | 允许的 SELinux 配置白名单。更多信息，请参见 [SELinuxOptions v1 core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#selinuxoptions-v1-core) 。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPSELinuxV2 metadata: name: psp-selinux-v2 spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedSELinuxOptions: - level: s0:c123,c456 role: object_r type: svirt_sandbox_file_t user: system_u
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: securityContext: seLinuxOptions: level: "s0:c123,c456" containers: - image: test name: test
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: seLinuxOptions: level: "s0:c123,c455"
