## 验证结果
手动查询
操作记录页签可查看资源刷新或预热的详细记录和进度。进度为100%表示任务执行完成。刷新或预热的数量过多会影响任务的完成进度，请耐心等待。
接口查询
调用[查询刷新预热任务-按](../developer-reference/api-cdn-2018-05-10-describerefreshtaskbyid.md)[ID](../developer-reference/api-cdn-2018-05-10-describerefreshtaskbyid.md)接口，查询刷新或预热任务是否完成。
命令行验证
执行命令curl -I <资源链接>，系统显示结果如下：
存在X-Cache的情况：
X-Cache为HIT，说明此次请求命中缓存，预热成功。
X-Cache为MISS，说明此次请求未命中缓存，预热任务未完成或预热失败，请重新预热。
不存在X-Cache的情况：
如果不存在X-Cache，说明该资源未接入CDN，请参照[快速接入阿里云](../getting-started/quick-access-to-alibaba-cloud-cdn.md)[CDN](../getting-started/quick-access-to-alibaba-cloud-cdn.md)，先将该URL的域名接入阿里云CDN，再进行资源的预热。
