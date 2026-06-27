ACK专有集群：配置kubectl，使用insecure-skip-tls-verify配置忽略此错误。
重要
此方式将导致客户端不再校验API Server证书，不建议在生产环境中使用。建议[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)，然后再将新IP加入到API Server证书SAN中来解决此问题。
方式一：执行kubectl命令时指定--insecure-skip-tls-verify参数。
kubectl -s https://<IP>:6443 --insecure-skip-tls-verify get ns
方式二：修改KubeConfig文件内容，新增insecure-skip-tls-verify: true配置，然后删除certificate-authority-data配置。
apiVersion: v1 clusters: - cluster: server: https://<IP>:6443 insecure-skip-tls-verify: true name: kubernetes contexts: ...
ACK托管集群能否提供集群根证书密钥用于自助生成KubeConfig证书？
ACK托管集群不对外提供集群根证书密钥，建议通过控制台或OpenAPI获取集群KubeConfig。
