### 示例
将JSON数组[1,2,3]转换为字符串[1, 2, 3]。
查询和分析语句（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log?encode%3Dbase64%26queryString%3DKiB8IFNFTEVDVCBqc29uX2Zvcm1hdChqc29uX3BhcnNlKCdbMSwgMiwgM10nKSk%3D)）
* | SELECT json_format(json_parse('[1, 2, 3]'))
查询和分析结果为[1,2,3]。
