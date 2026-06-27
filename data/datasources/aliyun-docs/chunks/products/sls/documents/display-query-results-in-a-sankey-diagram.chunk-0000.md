## 简介
桑基图 (Sankey Diagram)，是一种特定类型的流图，用于描述一组值到另一组值的流向。适合网络流量等场景，通常包含3组值source、target以及value。source和target描述了节点的关系，而value描述了该source和target之间边的关系。
基本构成如下：
节点
边
例如以下数据可以用桑基图表示。

| source | target | value |
| --- | --- | --- |
| node1 | node2 | 14 |
| node1 | node3 | 12 |
| node3 | node4 | 5 |
| … | .. | … |

使用如下桑基图描述上述数据的关系。
