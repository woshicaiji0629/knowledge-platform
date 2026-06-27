使用的是第三方服务商签发的证书，请选择自定义上传（证书+私钥），您需要在设置证书名称后，上传证书（公钥）和私钥，该证书将在阿里云数字证书管理服务中保存。您可以在[我的证书](https://yundun.console.aliyun.com/?spm=5176.2020520110.all.12.16df56a1u1IhI6&p=cas#/cas/home)中查看。
Referer黑/白名单
Referer黑/白名单基于HTTP请求头中的Referer字段，通过设置黑名单/白名单来控制访问，防止资源盗用。黑白名单互斥。详情可以参考[配置](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
说明
您可以提前打开[定制和订阅运营报表](../user-guide/customize-an-operations-report-template-and-create-a-tracking-task.md)功能，运营报表会统计并展示用户访问的PV/UV、地区和运营商、域名排行、热门Referer、热门URL、回源热门URL和Top客户端IP等内容。然后根据热门Referer再来配置Referer黑/白名单。
