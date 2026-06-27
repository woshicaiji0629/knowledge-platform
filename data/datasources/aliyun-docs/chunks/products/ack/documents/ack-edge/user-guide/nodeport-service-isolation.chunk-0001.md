## 架构原理
edge-hub组件中内置可编程数据过滤框架，可以对边缘发起请求的响应数据（云端kube-apiserver返回）实现无感知和按需转换，以满足云边协同场景的特定需求。架构如下图所示。
edge-hub中引入一个名为nodeportisolation的新过滤器来实现NodePort Service的隔离能力，同时NodePort Service添加了一个新的注解（Annotaion）nodeport.openyurt.io/listen。
