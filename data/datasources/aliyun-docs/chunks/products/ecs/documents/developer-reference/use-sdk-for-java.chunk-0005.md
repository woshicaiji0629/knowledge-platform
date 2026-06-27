### 3. 发起调用
通过客户端调用OpenAPI时，支持设置运行时参数，例如超时配置、代理配置等，更多信息请查看[进阶配置](https://help.aliyun.com/zh/sdk/developer-reference/advanced-configuration/)。
说明
接口返回对象命名规则：{API名称}Response，例如DescribeInstances该接口的返回对象为DescribeInstancesResponse。
// 设置运行时参数 RuntimeOptions runtime = new RuntimeOptions(); // 调用 DescribeInstances 接口 DescribeInstancesResponse response = client.describeInstancesWithOptions(request, runtime); System.out.println(response.body.toMap());
