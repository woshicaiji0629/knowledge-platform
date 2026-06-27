### 示例1：授予指定集群的只读权限
{"Statement":[{"Action":["cs:Get*","cs:List*","cs:Describe*"],"Effect":"Allow","Resource":["acs:cs:*:*:cluster/YOUR_CLUSTER_ID"]}],"Version":"1"}
