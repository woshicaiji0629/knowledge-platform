### 示例
判断JSON数组[1, 2, 3]中是否包含2。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2FycmF5X2NvbnRhaW5zKCdbMSwgMiwgM10nLCAyKQ%3D%3D)）
* | SELECT json_array_contains('[1, 2, 3]', 2)
查询和分析结果为true，表示JSON数组[1, 2, 3]中包含2。
