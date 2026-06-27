# 配置CNAME常见问题-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/support/cname-faq

# 配置CNAME常见问题
添加 CDN 加速域名后，CDN 会分配一个 CNAME 地址。将加速域名的解析记录指向该 CNAME 地址后，CDN 加速服务即可生效。本文介绍配置CNAME过程中的常见问题。
## 如何测试 CNAME 解析是否生效？
在CDN控制台完成CNAME配置后，使用nslookup或dig等查询工具验证。不推荐使用ping命令，其返回的解析信息可能不准确。
Windowsnslookup -type=CNAME <加速域名>
如果返回的结果和CDN提供的CNAME值相等，则证明CNAME解析生效。
Linux/Mac OS
在Linux或Mac OS系统的终端（Terminal）中，使用dig命令验证：
仅查询CNAME目标地址（推荐）：
dig +short <加速域名> CNAME
如果返回的结果和CDN提供的CNAME值相等，则证明CNAME解析生效。结果示例如下：
dig +short cdn.example.com CNAME cdn.example.com.w.alikunlun.com.
查询域名详细信息：
dig <加速域名> CNAME
如果ANSWER SECTION的CNAME值和CDN提供的CNAME值相等，则证明CNAME解析生效。
### 查询结果显示NXDOMAIN或找不到记录怎么办？
按以下步骤排查：
检查域名拼写：确认查询命令中输入的域名无误。
检查DNS配置：登录DNS解析控制台，检查CNAME记录是否存在、主机记录是否正确。主机记录应填写加速域名的前缀部分，而非完整域名。例如，加速域名为cdn.example.com时，主机记录应填写cdn，而非cdn.example.com。
等待DNS生效：DNS记录修改后，全局生效需要时间，可等待后重试。
说明
DNS记录的全球生效时间取决于其TTL。例如，如果旧记录的TTL是10分钟，那么新记录的生效时间至少为10分钟。在修改CNAME前，建议将原记录的TTL设置为较短时间（如60秒）。
## 查询到了A记录，但没有CNAME记录，或配置 CNAME 时提示与 A 记录冲突怎么办？
同一主机记录不能同时存在 A 记录和 CNAME 记录。冲突提示说明该主机记录下已存在 A 记录或其他类型记录，解决方法如下：
登录 DNS 解析控制台，找到冲突的 A 记录（或 MX、TXT 等记录）。
删除或暂停该冲突记录。
重新添加 CNAME 记录，将记录值指向 CDN 分配的 CNAME 地址。
说明
删除 A 记录后，原解析流量将中断。建议先用子域名测试验证 CDN 加速正常后再切换主域名。
建议在业务低峰期操作。
如果域名已开启全局流量管理（GTM）的健康检查，GTM 可能自动创建解析记录导致冲突，需先在 GTM 中处理后再添加 CNAME。
## CDN 域名配置完成后，控制台状态仍显示"待配置"或"验证不通过"怎么办？
配置完成后，通常需要 5~30 分钟生效，实际以配置域名解析时选择的TTL为准。全网解析生效后，CDN控制台状态将显示正常。请等待后刷新控制台页面查看状态。
如果等待后域名状态未更新，请按以下步骤排查：
检查主机记录是否正确：须与加速域名前缀一致，例如a.example.com对应a，example.com对应@。常见错误是填写了www但加速域名并非www.example.com。
检查 CNAME 记录值是否匹配：须与 CDN 控制台显示的 CNAME 地址完全一致，建议直接从控制台复制。
使用 nslookup 或dig命令验证：确认返回的 CNAME 指向 CDN 分配的地址。
检查是否有冲突记录：确认已删除同一主机记录下的 A 记录或其他冲突记录。
## 控制台显示 CNAME 未配置但实际已解析
在以下场景中，CDN 控制台可能显示CNAME状态为未配置，但实际加速功能已正常运行，不影响实际使用：
加速区域不含中国内地：如果在添加加速域名时将加速区域设置为全球（不包含中国内地）（对应 API 参数Scope取值为overseas），在中国内地网络环境下检测 CNAME 时会提示未配置。这是正常现象，不影响目标加速区域的正常使用。可以通过以下方式验证境外加速是否生效：
使用nslookup或dig命令或在 CDN 控制台确认域名已解析到 CDN 分配的 CNAME 地址。
在非中国内地网络环境下访问加速资源，通过浏览器开发者工具查看响应头，若X-Cache字段值为HIT，则表示 CDN 缓存命中，加速已生效。
配置了分线路 DNS 解析：如果在 DNS 服务商处配置了按解析线路区分的记录（例如中国内地线路解析到 CDN 的 CNAME 地址、非中国内地线路解析到源站 IP），CDN 控制台可能因检测到部分线路未解析到 CDN 而显示"CNAME 未配置"。只要目标区域的用户能正常访问加速资源，即可忽略该提示。
DNS 解析延迟：新配置或修改 CNAME 记录后，DNS 解析全网生效通常需要几分钟到数小时（取决于 TTL 设置）。在此期间控制台可能显示未配置，请稍后再检查。
## 一个域名是否可以配置多个 CNAME 记录指向不同的 CDN 地址？
不支持。同一主机记录只能配置一个 CNAME 记录值，配置多个可能导致访问报错（如返回 403 错误）。
解决方法：确保同一主机记录下只保留一条 CNAME 记录，记录值指向当前使用的 CDN 加速域名对应的 CNAME 地址。如有多余记录请删除。
## 泛域名 CNAME 解析对子域名的影响？
配置泛域名（如*.example.com）的 CNAME 解析后，所有未单独配置解析的子域名（如a.example.com、b.example.com）将自动继承泛域名解析。如果某些子域名不需要 CDN 加速，需为其单独配置 A 记录或其他类型记录。具体子域名的解析记录优先级高于泛域名，不会被覆盖。
说明
解析优先级规则可能因 DNS 服务商而异。
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
