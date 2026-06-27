# 函数计算场景中使用Prometheus SDK上报时序数据-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-prometheus-sdk-report-metrics-data-in-function-compute-scenarios

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 函数计算场景中使用Prometheus SDK上报时序数据

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

SLS SDK支持写入时序数据，但手动维护一系列自定义指标的方式较为繁琐。Prometheus能自动生成多种维度的监控指标并内置维护标签信息，然而，它通常要求对外暴露一个HTTP接口，通过第三方采集器以Pull模式拉取时序数据。在函数计算场景中，由于计算服务无法直接提供此类HTTP接口，无法通过前述Pull模式上报时序数据。本文介绍一种利用Prometheus SDK并基于Push模式上报时序数据的方案。

## 前提条件

- 

[已开通日志服务](products/sls/documents/resource-management-overview.md)。

- 

已创建Project和MetricStore。具体操作，请参见[管理](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)和[管理](products/sls/documents/manage-a-metricstore.md)[MetricStore](products/sls/documents/manage-a-metricstore.md)。

## 集成Prometheus

Prometheus能够自动生成多种维度的监控指标并内置维护了各种标签信息，结合Prometheus内置维护的指标信息，上报时序数据到时序库，根据不同场景，有两种模式。

- 

- 

- 

- 

- 

- 

| 方式 | 说明 |
| --- | --- |
| Pull 模式 | Pull 模式采集并上报指标数据，包含以下四个阶段： 在原项目中引入 Prometheus SDK，使用 SDK 创建并维护各种指标项。 对外暴露一个 /metrics 的 HTTP 接口，采集进程（Prometheus、VMAgent、iLogtail 等）定时访问该接口以获取编码后的指标数据。 采集进程解析从 HTTP 接口获取到的指标数据并转换成符合 Prometheus RemoteWrite PB 协议的编码数据。 采集进程请求 SLS 时序库的 RemoteWrite HTTP 接口写入时序数据。 |
| Push 模式 | Push 模式表示主动推送指标数据到时序库中。日志服务时序库支持两种主动上报时序数据的方式： 通过 [SLS SDK](products/sls/documents/use-an-sdk-to-collect-metrics.md) 以日志格式将时序数据写入到时序库中。 使用 Prometheus SDK 以开源标准格式将时序数据写入到时序库中，详细见 [代码示例](products/sls/documents/use-prometheus-sdk-report-metrics-data-in-function-compute-scenarios.md) 。 |


## 代码示例

使用Prometheus SDK，可以将Pull模式中采集进程所执行的操作全部合并到原项目进程中。

## Go语言

已[安装](products/sls/documents/developer-reference/install-log-service-sdk-for-go.md)[Go SDK](products/sls/documents/developer-reference/install-log-service-sdk-for-go.md)。通过调用Gather()接口获取所有时序指标，之后再调用Encode或Decode接口即可实现。

package main import ( "bytes" "fmt" "time" "github.com/gogo/protobuf/proto" "github.com/golang/snappy" "github.com/prometheus/client_golang/prometheus" "github.com/prometheus/common/expfmt" "github.com/prometheus/prometheus/util/fmtutil" "io/ioutil" "math/rand" "net/http" ) var durationHistogram = prometheus.NewHistogram( prometheus.HistogramOpts{ Name: "server_handling_seconds", Buckets: prometheus.DefBuckets, }, ) var requestCount = prometheus.NewCounter( prometheus.CounterOpts{ Name: "server_requests_count", }, ) func main() { prometheus.MustRegister(durationHistogram) // 分别替换 your-project-name, endpoint, your-project-name, your-metricstore-name u := fmt.Sprintf("https://%s.%s/prometheus/%s/%s/api/v1/write", "your-project-name", "endpoint", "your-project-name", "your-metricstore-name") for i := 0; i < 300; i++ { // 更新指标数据 for j := 0; j < 100; j++ { val := rand.Float64() * 10 durationHistogram.Observe(val) requestCount.Inc() } // 收集已注册的所有指标数据 mfs, err := prometheus.DefaultGatherer.Gather() if err != nil { panic(err) } // 对指标数据进行编码处理 // 注意：由于Histogram类型的指标是在Encode过程中添加 "+Inf" 这个le标签，所以此处的Encode过程不可省略。 buf := bytes.NewBuffer(nil) encoder := expfmt.NewEncoder(buf, expfmt.NewFormat(expfmt.TypeTextPlain)) for _, mf := range mfs { if err := encoder.Encode(mf); err != nil { panic(err) } } // 对编码后的指标数据做解析处理，并转化成RemoteWrite PB协议的Request // 当前示例对于错误处理直接结束进程，实际使用中需根据业务特点选择合适的处理方式，例如跳过或者退出重试等 request, err := fmtutil.MetricTextToWriteRequest(buf, nil) if err != nil { panic(err) } // 对*prompb.WriteRequest做序列化并压缩 data, _ := proto.Marshal(request) bufBody := snappy.Encode(nil, data) rwR, err := http.NewRequest("POST", u, ioutil.NopCloser(bytes.NewReader(bufBody))) if err != nil { panic(err) } rwR.Header.Add("Content-Encoding", "snappy") rwR.Header.Set("Content-Type", "application/x-protobuf") // 设置basic auth信息，即AccessKeyId和AccessKeySecret。 rwR.SetBasicAuth("yourAccessKeyID", "yourAccessKeySecret") // 往SLS时序库发送时序数据 resp, err := http.DefaultClient.Do(rwR) if err != nil { panic(err) } d, err := ioutil.ReadAll(resp.Body) if err != nil { panic(err) } fmt.Println(string(d)) time.Sleep(time.Second) } }

## 验证采集数据

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。

- 

在时序存储>时序库页签中，单击目标MetricStore。

- 

在页面右上角，设置查询和分析的时间范围。输入[PromQL](products/sls/documents/time-metric-data-query-and-analysis-syntax.md)[语句](products/sls/documents/time-metric-data-query-and-analysis-syntax.md)，计算整体耗时情况的P50百分位数值，单击立即执行。

histogram_quantile(0.5, sum by (le) (rate(server_handling_seconds_bucket[1m])))

执行后，页面将展示 P50 延迟指标的折线图，表明数据已成功采集。

[上一篇：通过SDK写入时序数据](products/sls/documents/use-an-sdk-to-collect-metrics.md)[下一篇：追加字段](products/sls/documents/append-data-to-a-field.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
