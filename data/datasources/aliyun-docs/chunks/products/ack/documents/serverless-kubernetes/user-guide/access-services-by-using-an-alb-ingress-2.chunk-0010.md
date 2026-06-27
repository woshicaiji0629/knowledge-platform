## 步骤四：访问服务
利用获取的ALB实例地址，通过命令行方式访问coffee服务。
curl -H Host:demo.domain.ingress.top http://alb-lhwdm5c9h8lrcm****.cn-hangzhou.alb.aliyuncs.com/coffee
利用获取的ALB实例地址，通过命令行方式访问tea服务。
curl -H Host:demo.domain.ingress.top http://alb-lhwdm5c9h8lrcm****.cn-hangzhou.alb.aliyuncs.com/tea
