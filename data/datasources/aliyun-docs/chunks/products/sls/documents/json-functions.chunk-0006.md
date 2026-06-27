### 示例
返回JSON数组["a", [3, 9], "c"]下标为1的元素。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2FycmF5X2dldCgnWyJhIiwgWzMsIDldLCAiYyJdJywgMSk%3D)）
* | SELECT json_array_get('["a", [3, 9], "c"]', 1)
查询和分析结果为[3,9]。
