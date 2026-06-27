## 1.19版本之前集群
apiVersion: networking.k8s.io/v1beta1 kind: IngressClass metadata: name: alb spec: controller: ingress.k8s.alibabacloud/alb parameters: apiGroup: alibabacloud.com kind: AlbConfig name: alb-demo
执行以下命令，创建IngressClass。
kubectl apply -f alb.yaml
预期输出：
ingressclass.networking.k8s.io/alb created
