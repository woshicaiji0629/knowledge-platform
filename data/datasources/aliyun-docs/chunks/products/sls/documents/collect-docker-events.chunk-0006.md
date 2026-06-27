## 日志样例
Docker事件样例如下所示。
样例1：镜像拉取事件
__source__: 10.10.10.10 __tag__:__hostname__: logtail-ds-77brr __topic__: _action_: pull _id_: registry.cn-hangzhou.aliyuncs.com/ringtail/eventer:v1.6.1.3 _time_nano_: 1547910184047414271 _type_: image name: registry.cn-hangzhou.aliyuncs.com/ringtail/eventer
样例2：Kubernetes中容器的销毁事件
__source__: 10.10.10.10 __tag__:__hostname__: logtail-ds-xnvz2 __topic__: _action_: destroy _id_: af61340b0ac19e6f5f32be672d81a33fc4d3d247bf7dbd4d3b2c030b8bec4a03 _time_nano_: 1547968139380572119 _type_: container annotation.kubernetes.io/config.seen: 2019-01-20T15:03:03.114145184+08:00 annotation.kubernetes.io/config.source: api annotation.scheduler.alpha.kubernetes.io/critical-pod: controller-revision-hash: 2630731929 image: registry-vpc.cn-hangzhou.aliyuncs.com/acs/pause-amd64:3.0 io.kubernetes.container.name: POD io.kubernetes.docker.type: podsandbox io.kubernetes.pod.name: logtail-ds-44jbg io.kubernetes.pod.namespace: kube-system io.kubernetes.pod.uid: 6ddcf598-1c81-11e9-9ddf-00163e0c7cbe k8s-app: logtail-ds kubernetes.io/cluster-service: true name: k8s_POD_logtail-ds-44jbg_kube-system_6ddcf598-1c81-11e9-9ddf-00163e0c7cbe_0 pod-template-generation: 9 version: v1.0
D
