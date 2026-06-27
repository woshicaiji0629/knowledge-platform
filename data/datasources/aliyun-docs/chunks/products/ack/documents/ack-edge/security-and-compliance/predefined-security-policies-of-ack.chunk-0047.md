### RatifyVerification
规则说明：您在集群中安装应用市场组件Ratify后，可以验证在集群指定范围内部署的Pod镜像中的签名或SBOM等安全元数据。
重要等级：high。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: RatifyVerification metadata: name: ratify-constraint spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: ["default"]
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/signed # 部署合法签名的镜像。 name: test-container
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: test-gatekeeper spec: containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/unsigned # 部署不满足Ratify签名校验的非法镜像。 name: test-container
