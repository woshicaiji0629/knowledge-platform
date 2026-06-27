## 1.19版本之前集群
apiVersion: networking.k8s.io/v1beta1 kind: Ingress metadata: name: cafe-ingress spec: ingressClassName: alb rules: - host: demo.domain.ingress.top http: paths: # 配置Context Path。 - path: /tea backend: serviceName: tea-svc servicePort: 80 # 配置Context Path。 - path: /coffee backend: serviceName: coffee-svc servicePort: 80
执行以下命令，配置coffee和tea服务对外暴露的域名和path路径。
kubectl apply -f cafe-ingress.yaml
预期输出：
ingress.networking.k8s.io/cafe-ingress created
执行以下命令获取ALB实例地址。
kubectl get ing
预期输出：
NAME CLASS HOSTS ADDRESS PORTS AGE cafe-ingress alb demo.domain.ingress.top alb-m551oo2zn63yov****.cn-hangzhou.alb.aliyuncs.com 80 50s
