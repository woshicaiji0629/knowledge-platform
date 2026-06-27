### 声明matchpolicy
使用Gang scheduling时，您可以通过声明match-policy以使PodGroup在对Pod进行计数时考虑不同类型的。
当您使用Label方式时，可以在Pod上使用以下Label。
pod-group.scheduling.sigs.k8s.io/match-policy: "waiting-and-running"
当您使用PodGroup方式时，可以在PodGroup自定义资源上使用以下Label。
pod-group.scheduling.sigs.k8s.io/match-policy: "waiting-and-running"
如果您使用的是Annotation方式，目前仅支持once-satisfied匹配。
支持的各种匹配方式以及功能如下表所示。

| 匹配方式取值 | 说明 |
| --- | --- |
| only-waiting | 匹配时只关注完成资源预占的 Pod。 |
| waiting-and-running | 匹配时关注状态为 Running 的 Pod 以及完成资源预占的 Pod。 |
| waiting-running-succeed | 匹配时关注状态为 Succeed、Running 的 Pod 以及完成资源预占的 Pod。 |
| once-satisfied | 匹配时只关注完成资源预占的 Pod，匹配成功后该 PodGroup 不再生效。 |
