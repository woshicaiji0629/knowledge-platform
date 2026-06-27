## 常见问题
实例ping不通怎么办？
无法ping通ECS实例，通常是因为安全组中入方向ICMP协议（ping 命令所使用的协议）的默认规则被移除。可以使用安全组规则诊断工具快速定位问题。
前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)找到目标实例并记录实例ID。
单击一键诊断进入自助问题排查页面，并切换至目标地域。
选择安全组规则诊断，单击发起诊断。
选择记录的实例 ID及对应的网卡。单击开始检测。
多数情况下，一台实例只有一张网卡。
查看检测结果。如果结果显示ICMP协议未放行，单击开通端口即可快速开通。
除ICMP外，诊断工具还会检测以下常用端口是否放行：80、443、22、3389和8080。
如果检测后发现还是ping不通可以根据[无法](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ping](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[通](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[ECS](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[实例公网](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[IP](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)[的排查方法](../troubleshooting-for-ping-attempts-to-pass-the-server-and-port-disconnection.md)更进一步排查。
实例连不上、服务访问不通怎么办？
服务无法访问，通常是由于安全组未放行端口。可以使用安全组规则诊断工具快速定位问题。
前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)
