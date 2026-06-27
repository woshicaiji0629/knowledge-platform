## 注意事项
edge-hub组件版本使用v0.11.0及以上版本。
您在创建Service时需要确定好是否添加注解nodeport.openyurt.io/listen。若Service创建后再添加该注解，需要重启所有kube-proxy，该功能才能生效。
新增节点池后，需要在未接入节点之前，把新创建的节点池增加到Service的注解中，该功能才能在后续接入的节点上生效。
由于节点池名称支持变更，所以请使用节点池ID来指定节点池。节点池ID可通过[容器服务管理控制台](https://cs.console.aliyun.com)查看，格式一般为npxxxx。
