### ACKRestrictALBCreation
规则说明：强制复用已有ALB实例，禁止通过ALBConfig创建新的ALB资源实例。
重要等级：low。
参数说明：无
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKRestrictALBCreation metadata: name: restrict-alb-creation spec: enforcementAction: deny match: kinds: - apiGroups: ["alibabacloud.com"] kinds: ["AlbConfig"]
Allowed：
apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: reuse-alb spec: config: id: 'abcdefghijklmnopqrstuvwxyz' forceOverride: false listenerForceOverride: false
Disallowed：
apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: alb spec: config: name: alb addressType: Internet zoneMappings: - vSwitchId: vsw-uf6ccg2a9g71hx8go**** # 替换为集群所在VPC中至少两个处于不同可用区的VSwitch IDVSwitch ID allocationId: eip-asdfas**** # 替换为EIP ID，默认选项为自动分配公网IP。 - vSwitchId: vsw-uf6nun9tql5t8nh15**** # 替换为集群所在VPC中至少两个处于不同可用区的VSwitchIDID allocationId: eip-dpfmss**** # 替换为EIP ID。EIP ID。 listeners: - port: 80 protocol: HTTP
该文章对您有帮助吗？
反馈
