## 验证P2P加速
启用P2P加速后，P2P组件会自动为Pod注入P2P相关annotation、P2P加速镜像地址以及对应的镜像拉取凭证。
重要
P2P镜像拉取凭证与您原先配置的非P2P镜像地址拉取凭证仅镜像仓库域名不一样，其他凭证信息一致。因此，若您原先镜像拉取凭证用户信息配置错误，也会导致P2P镜像拉取失败。
执行以下命令，查看Pod。
kubectl get po <Pod的名称> -oyaml
预期输出：
apiVersion: v1 kind: Pod metadata: annotations: # inject p2p-annotations automatically k8s.aliyun.com/image-accelerate-mode: p2p k8s.aliyun.com/p2p-config: '...' spec: containers: # inject image to p2p endpoint - image: test-registry-vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001/docker-builder/nginx:latest imagePullSecrets: - name: test-registry # inject image pull secret for p2p endpoint - name: acr-credential-test-registry-p2p
可以看到，Pod已注入P2P相关annotation、P2P加速镜像地址以及对应的镜像拉取凭证，说明启用P2P加速成功。
