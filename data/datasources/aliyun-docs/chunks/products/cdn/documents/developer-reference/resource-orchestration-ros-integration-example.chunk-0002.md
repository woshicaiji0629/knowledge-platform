## 操作步骤
登录[资源编排](https://rosnext.console.aliyun.com/cn-shanghai/stacks)[ROS](https://rosnext.console.aliyun.com/cn-shanghai/stacks)[控制台](https://rosnext.console.aliyun.com/cn-shanghai/stacks)，单击顶部导航栏地域下拉框，选择您需要的地域。
单击左侧菜单栏中的资源栈，选择创建资源栈>使用ROS。
指定模板：选中选择已有模板。
模板录入方式：选中输入模板。
模板内容选择ROS，并输入代码。
添加加速域名的语法、说明及示例，请参见[ALIYUN::CDN::Domain](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domain)。
YAML格式
ROSTemplateFormatVersion: '2015-09-01' Parameters: CdnType: AllowedValues: - video - download - web - liveStream Description: 'The business type. Valid values: web, download, video, livestream, and httpsdelivery. web: acceleration of images and small files download. download: acceleration of large file downloads. video: live streaming acceleration. httpsdelivery: SSL acceleration for HTTPS.' Type: String CheckUrl: Description: The validation of the origin. Type: String DomainName: Description: The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com. Type: String ResourceGroupId: Description: The ID of the resource group. If this is left blank, the system automatically fills in the ID of the default resource group. Type: Strin
