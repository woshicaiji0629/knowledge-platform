# 将 <your-pod-name> 替换实际Pod名称 kubectl get pod <your-pod-name> -n default -o yaml | grep "cpuset:"
预期输出：
cpuset: '{"nginx":{"0":{"elems":{"0":{},"1":{},"2":{},"3":{}}}}}'
输出结果说明：
"nginx":{...}：针对名为nginx的容器的配置。
"0":{...}：最外层的键"0"代表NUMA节点ID。本示例表示所有绑定的核都位于同一NUMA Node 0上，避免了跨NUMA访存的性能损耗。
"elems":{"0":{},"1":{},"2":{},"3":{}}：键代表被绑定的物理CPU核心ID。此示例中，容器被成功绑定到了0、1、2、3这四个核心上，与limits.cpu: 4相符。
