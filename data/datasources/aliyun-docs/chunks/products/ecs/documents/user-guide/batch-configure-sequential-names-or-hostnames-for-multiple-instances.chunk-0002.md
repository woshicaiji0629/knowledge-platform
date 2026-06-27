值， bits 会默认取值为 6 。 假如 [begin_number,bits] 只设置了 begin_number ，例如 [99] 或 [99,] ，则 bits 会默认取值为 6 。 | [0,6] |
| name_suffix | 指定实例名称或主机名称的后缀。 | -ecshost |

指定排序参数示例

| 输入参数示例 | 生成名称（以 3 台 ECS 实例为例） |
| --- | --- |
| k8s-node-[]-ecshost 或 k8s-node-[,]-ecshost | k8s-node-000000-ecshost k8s-node-000001-ecshost k8s-node-000002-ecshost |
| k8s-node-[99]-ecshost 或 k8s-node-[99,]-ecshost | k8s-node-000099-ecshost k8s-node-000100-ecshost k8s-node-000101-ecshost |
| k8s-node-[99,1]-ecshost | k8s-node-000099-ecshost k8s-node-000100-ecshost k8s-node-000101-ecshost |
| k8s-node-[999998]-ecshost | k8s-node-999998-ecshost k8s-node-999999-ecshost k8s-node-999999-ecshost |
| k8s-node-[0,4] | k8s-node-0000 k8s-node-0001 k8s-node-0002 |
