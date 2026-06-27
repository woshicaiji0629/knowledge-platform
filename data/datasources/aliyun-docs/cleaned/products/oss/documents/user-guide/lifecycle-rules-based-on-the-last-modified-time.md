# 基于最后一次修改时间配置生命周期规则以降低OSS存储成本-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time

# 基于最后一次修改时间配置生命周期规则以降低OSS存储成本
并不是所有上传至OSS的数据都需要频繁访问，但基于数据合规或者存档等原因，部分数据仍需要继续保存。或者基于业务使用场景，希望批量删除Bucket内不再需要保存的数据。您可以配置基于最后一次修改时间（Last Modified Time）的生命周期规则，定期将Object从热存储类型转为冷存储类型，或者删除Object，以降低存储成本。
## 使用场景
某医疗机构的医疗档案，上传至OSS后半年内偶尔访问，半年后基本不再访问。可以通过设置生命周期规则，将已上传180天的医疗档案转为归档存储。
某公司服务热线的录音文件，上传至OSS后2个月内用于数据统计及核查，2个月后偶尔访问，半年后基本不再访问，2年后数据不再需要存储。可以通过设置生命周期规则，设置60天后转为低频访问存储，180天后转为归档存储，730天后删除。
某Bucket内有大量文件需要全部删除，可以配置一条匹配整个Bucket的生命周期规则，设置一天后删除所有文件。
关于存储类型的介绍，请参见[存储类型](overview-53.md)。
## 使用限制
### 地域属性限制
由于无地域属性存储空间仅支持标准存储类型文件，因此基于最后一次修改时间的生命周期规则作用于无地域属性存储空间时，仅执行删除操作，不涉及存储类型转换操作。
### 匹配条件
生命周期规则目前仅支持根据前缀和标签进行匹配，不支持通配符匹配、后缀匹配以及正则匹配。
### 碎片过期限制
不支持对重叠前缀的Object设置两条或两条以上包含碎片过期策略的生命周期规则。示例如下：
示例一
您对整个Bucket设置了一条包含碎片过期策略的生命周期规则，则不支持对Bucket中任意前缀的Object再设置一条包含碎片过期策略的生命周期规则。
示例二
您对某个Bucket中前缀为dir1设置了一条包含碎片过期策略的生命周期规则，则不支持对该Bucket中包含重叠前缀（例如dir1/dir2）的Object再设置一条包含碎片过期策略的生命周期规则。
### 存储类型转换限制
不支持通过生命周期规则将Appendable类型Object转为冷归档或深度冷归档存储。需先通过[SealAppendObject](../developer-reference/sealappendobject.md)将Object变为非追加状态，然后再使用生命周期规则完成转换。
不支持通过生命周期规则将软链接（symlink）转换为低频访问、归档、冷归档以及深度冷归档存储类型。
## 注意事项
### 规则数量
单个Bucket最多支持配置1000条生命周期规则，单条生命周期规则中可同时包含最后一次修改时间以及最后一次访问时间的策略。
### 覆盖语义
PutBucketLifecycle为覆盖语义。例如，某个Bucket已配置了生命周期规则Rule1，您需要在Rule1基础上继续追加生命周期规则Rule2，您需要执行以下操作。
获取Rule1。
叠加Rule2。
更新规则为（Rule1+Rule2）。
### 生效时间
生命周期规则创建后的24小时内，OSS会加载规则。规则加载完成后，OSS会在每天的北京时间8:00开始执行规则。
如果生命周期规则指定的时间策略是按指定天数（Days），则Object的最后修改时间与规则开始执行时间（8:00）必须间隔24小时以上。例如规则指定Object上传1天后删除，则2020年7月20日上传的文件删除时间如下：
北京时间8:00前上传的文件会在2020年7月21日8:00开始删除，并在7月22日8:00前删除完毕。
北京时间8:00后上传的文件会在2020年7月22日8:00开始删除，并在7月23日8:00前删除完毕。
更新生命周期规则可能会中止当天的生命周期任务，请不要频繁更新生命周期规则。
### 执行完成时间
规则生效后，华东1（杭州）、华东2（上海）、华北2（北京）、华北 3（张家口）、华北6（乌兰察布）、华南1（深圳）、新加坡地域，执行 Object 数在 10 亿以内的生命周期相关操作（包括 Object 删除、 Object 存储类型转换以及碎片过期），通常情况下在 24 小时内完成；其他地域，执行 Object 数在 1 亿以内的生命周期相关操作（包括 Object 删除、 Object 存储类型转换以及碎片过期），通常情况下在 24 小时内完成。
如出现以下情况，则可能使任务执行时间超过 24 小时，甚至持续数天到数周：扫描 Object 数过多、待执行生命周期的 Object 数过多、标签数较多、单 Object 的历史版本数量过多、生命周期任务执行时新上传的 Object 过多等。
说明
如果存储空间开启了版本控制，则对Object的每个版本均记为一次操作。
### 费用说明
关于通过生命周期规则转换Object存储类型或者删除Object时可能涉及的存储和请求费用说明，请参见[生命周期费用说明](fees-related-to-lifecycle-rules.md)。
### 在开通了OSS-HDFS服务的Bucket中配置生命周期规则
在开通了OSS-HDFS服务的Bucket中配置基于OSS文件的生命周期规则
如果您对开通了OSS-HDFS服务的Bucket设置或更新为匹配整个Bucket的生命周期规则，需通过NOT元素排除.dlsdata/，避免因生命周期规则触发的Object删除或存储类型转换行为影响OSS-HDFS数据读写。
在开通了OSS-HDFS服务的Bucket中配置基于HDFS文件的生命周期规则
如果您需要对经常访问的数据以标准类型进行存储，对于较少访问的数据以低频、归档以及冷归档类型进行存储，您可以使用基于生命周期规则的冷热分层存储功能实现这一场景。具体操作，请参见[使用冷热分层存储](enable-the-automatic-storage-tiering-feature-for-the-oss-hdfs-service.md)。
## 开启版本控制时配置生命周期规则
通过生命周期转换存储类型时，不会产生历史版本。
## 组成元素
### 匹配元素
按前缀匹配：按指定前缀匹配Object和碎片。可创建多条规则匹配不同的前缀，前缀不能重复。前缀的命名规范与Object命名规范相同，详情请参见[对象（Object）](../terms-2.md)。
按[标签](object-tagging-8.md)匹配：按指定标签的Key和Value匹配Object。单条规则可配置多个标签，仅当Object包含所有标签时执行生命周期规则。
| 生命周期规则设置的标签 | Object 携带的标签 | 生命周期规则是否作用于该 Object |
| --- | --- | --- |
| a:1,b:2 | a:1 | 否 |
| a:1,b:3 | 否 |  |
| a:1,b:2 | 是 |  |
| a;1,b:2,c:3 | 是 |  |
说明
标签匹配规则不作用于碎片。
按前缀+标签匹配：按指定前缀和标签的筛选条件匹配对象。
配置到整个Bucket：匹配整个Bucket内的所有Object和碎片。
NOT元素：如果您希望按照生命周期规则对与前缀和标签匹配的Object进行相应处理的同时，跳过不需要处理的Object，您可以通过NOT元素对不需要处理的Object指定前缀和标签。关于NOT元素的配置示例，请参见[NOT](lifecycle-rules-based-on-the-last-modified-time.md)[示例](lifecycle-rules-based-on-the-last-modified-time.md)。
重要
生命周期规则现支持多 NOT 元素配置，但该功能处于邀测状态，尚未对所有用户开放使用，可联系[技术支持](https://selfservice.console.aliyun.com/ticket/createIndex)申请使用。
单个 Bucket 的 NOT 元素总数上限为 1000；单条规则的 NOT 元素上限为 100，所有规则中的Prefix元素总数上限为2000。
使用多 NOT 元素后，后续的生命周期规则操作请使用控制台管理。
如果多 NOT 元素配置功能尚未开通，请勿通过配置多条规则分别 NOT 不同子目录的方式来替代。不同规则的 NOT 元素互不影响——若 rule1 仅排除了 dir/p1/，dir/p2/ 仍会被 rule1 匹配删除；若 rule2 仅排除了 dir/p2/，dir/p1/ 仍会被 rule2 匹配删除，最终导致 dir/ 下所有文件被删除。
### Object的过期时间及操作
过期天数：指定一个过期天数N，并指定非版本状态下的所有Object、以及版本控制状态下的当前版本Object过期后执行什么操作。Object会在其最后修改时间的N天后过期，并执行指定的操作。
过期日期：指定一个过期日期，并指定非版本状态下的所有Object、以及版本控制状态下的当前版本Object过期后执行什么操作。最后修改时间在该日期之前的Object全部过期，并执行指定的操作。
Object成为非当前版本天数：指定一个过期天数N，并指定非当前版本Object过期后执行什么操作。Object会在其成为非当前版本的N天后过期，并执行指定的操作。
您可以转换过期Object的存储类型或将其删除。详情请参见[生命周期配置元素](configuration-elements.md)。
### 碎片的过期时间及操作
过期天数：可指定一个过期天数N，文件碎片会在其最后修改时间的N天后被删除。
过期日期：指定一个过期日期，最后修改时间在该日期之前的文件碎片会被全部删除。
## 规则说明
### 不同前缀
例如，某个Bucket包含以下Object：
logs/programl/log1.txt logs/program2/log2.txt logs/program3/log3.txt doc/readme.txt
如果生命周期规则指定的前缀是logs/，则仅作用于以logs/开头的Object；如果指定的前缀是doc/readme.txt，则仅作用于doc/readme.txt。
说明
您可以为生命周期规则指定中文前缀。
对过期策略匹配的Object执行GET或HEAD操作时，OSS会在响应Header中加入x-oss-expiration头。expiry-date表示Object的过期日期；rule-id表示相匹配的规则ID。
### 相同前缀和标签
当不同生命周期规则作用于相同前缀和标签的Object时，删除操作优先于存储类型转换操作。rule1用于指定所有前缀为abc，标签为a=1的Object 20天后删除，rule2规则不生效。
| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule1 | abc | a=1 | 20 天后删除 |
| rule2 | abc | a=1 | 20 天后转为 Archive |
### 前缀重叠+标签相同
rule1用于指定所有标签为a=1的Object 10天后转为IA。rule2用于指定前缀为abc且标签为a=1的Object 120天后删除。
| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule1 | - | a=1 | 10 天后转为 IA |
| rule2 | abc | a=1 | 120 天后被删除 |
rule3用于指定所有标签为a=1的Object 20天后转为Archive。由于Archive类型文件无法转换为IA类型，因此rule4指定的前缀为abc且标签为a=1的Object 30天后转为IA的规则不生效。
| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule3 | - | a=1 | 20 天后转为 Archive |
| rule4 | abc | a=1 | 30 天后转为 IA |
### NOT
对同一个Bucket配置多条生命周期规则，且某条生命周期规则涉及NOT元素时，NOT元素指定的行为只对本条生命周期规则生效。具体示例如下：
示例一
通过生命周期规则1，指定examplebucket中前缀为dir/的Object 100天后删除。
通过生命周期规则2，通过NOT元素指定examplebucket中除前缀为dir/以外的所有Object 50天后删除。
以生命周期规则生效时间为起点，examplebucket中Object的删除行为如下表所示。
| Object | 删除行为 |
| --- | --- |
| 前缀为 dir/的 Object | 100 天后删除 |
| 前缀不为 dir/的 Object | 50 天后删除 |
示例二
通过生命周期规则1，通过NOT元素指定examplebucket内除标签（key1:value1）以外的所有Object 30天后删除。
通过生命周期规则2，指定examplebucket内包含标签（key2:value2）的所有Object 50天后删除。
以生命周期规则生效时间为起点，examplebucket内Object的删除行为如下表所示：
| Object | 删除行为 |
| --- | --- |
| 对于未包含以上标签的所有 Object | 30 天后删除 |
| 对于仅包含 key1:value1 标签的 Object | 不删除 |
| 对于仅包含 key2:value2 标签的 Object | 30 天后删除 |
| 对于同时包含 key1:value1 以及 key2:value2 标签的 Object | 50 天后删除 |
## 操作方式
### 使用OSS控制台
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏， 选择数据管理>生命周期。
在生命周期页面，单击创建规则。
说明
如果您仅需要创建基于最后一次修改时间策略的生命周期规则，不需要在生命周期页面打开启用访问跟踪开关。开启访问跟踪会产生额外费用。访问跟踪适用于创建基于最后一次访问时间策略的生命周期规则。更多信息，请参见[基于最后一次访问时间的生命周期规则](lifecycle-rules-based-on-the-last-access-time.md)。
在创建生命周期规则面板，按如下说明配置生命周期规则。
存储空间未开启版本控制
| 区域 | 配置项 | 说明 |
| --- | --- | --- |
| 基础设置 | 状态 | 设置生命周期规则的状态，可选择 启动 或 禁用 。 启动生命周期规则后，将按照配置的生命周期规则转换数据存储类型或删除数据。 禁用生命周期规则后，将中断生命周期任务。 |
| 策略 | 选择生命周期规则作用的 Object。您可以选择 按前缀匹配 或 配置到整个 Bucket 。 说明 选择按前缀匹配时，需要填写前缀的完整路径。例如，您希望仅作用于 src/dir1 下的所有文件，则前缀需要填写为 src/dir1，仅填写 dir1 则不生效。 |  |
| 是否允许前缀重叠 | OSS 默认会检查各个生命周期规则的前缀是否重叠。例如，您设置了以下两条包含重叠前缀的生命周期规则： 规则 1 指定该 Bucket 内所有前缀为 dir1/ 的 Object 在距离最后一次修改时间 180 天后删除。 规则 2 指定该 Bucket 内所有前缀为 dir1/dir2/ 的 Object 在距离最后一次修改时间 30 天后转低频访问类型，60 天后删除。 在配置规则 2 时未选中该选项的情况下，因后台检测到 dir1/dir2/ 目录下的 Object 同时匹配两条删除规则，因此会拒绝设置规则 2，并报错 Overlap for same action type Expiration. 。 在配置规则 2 时选中该选项的情况下， dir1/dir2/ 下的 Object 会在 30 天后转低频访问类型，60 天后删除。 dir1/ 下的其他 Object 会在 180 天删除。 说明 如果配置了多条规则，且其中一条为基于整个 Bucket 的规则时，会被视为前缀重叠的情况。 |  |
| 前缀 | 输入规则要匹配的 Object 名称的前缀。 前缀设置为 img ，表示匹配名称以 img 开头的所有 Object，例如 imgtest.png、img/example.jpg 等。 前缀设置为 img/ ，表示匹配名称以 img/开头的所有 Object，例如 img/example.jpg、img/test.jpg 等。 |  |
| 标签 | 生命周期规则仅针对拥有指定标签 Object 生效。 如果没有设置前缀，只设置了标签，且标签的 key 为 a，value 为 1。则该规则将匹配 Bucket 内所有标签为 a=1 的 Object。 如果设置了前缀，前缀设置为 img，同时设置了标签，标签的 key 为 a，value 为 1，则该规则将匹配 Bucket 内所有名称以 img 开头，标签为 a=1 的 Object。 更多信息，请参见 [对象标签](object-tagging-8.md) 。 |  |
| NOT | NOT 选项用于设置生命周期规则对指定前缀和标签的 Object 不生效。 重要 开启 NOT 选项时，前缀和标签必须至少存在一项，即同时设置前缀和标签或者只设置前缀或标签。 NOT 语义定义标签中的 key 不支持与 标签 配置项中定义的 key 相同。 开启 NOT 选项后，不支持设置碎片过期策略。 |  |
| 文件大小 | 指定生命周期规则生效的文件大小。 指定最小文件 ：生命周期规则对大于该值的文件大小生效。取值大于 0 B，小于 5 TB。 指定最大文件 ：生命周期规则对小于该值的文件大小生效。取值大于 0 B，小于等于 5 TB。 重要 如果在同一条生命周期中，同时配置了指定最小文件和指定最大文件： 确保指定最大文件的值大于指定最小文件的值。 不支持配置碎片执行策略。 不支持配置清除删除标记策略。 |  |
| 文件执行策略设置 | 文件时间策略 | 选择 Object 过期策略，可选择 指定天数 、 指定日期 和 不启用 。选择 不启用 时，文件过期策略不生效。 |
| 生命周期管理规则 | 配置转换 Object 存储类型或者删除过期 Object 的规则，可选择 低频访问 、 归档存储 、 冷归档存储 、 深度冷归档存储 和 数据删除 。 例如，当您将 文件时间策略 设置为 指定日期 ，并将日期设置为 2023 年 9 月 24 日，则最后一次修改时间在 2023 年 9 月 24 日之前的 Object 会被自动删除，且删除后不可恢复。 |  |
| 碎片执行策略设置 | 碎片过期策略 | 配置碎片执行策略。如果选中了 标签 ，则无法配置该选项。您可以选择按 指定天数 或 指定日期 执行碎片过期策略，也可以选择 不启用 碎片过期策略。当选择 不启用 时，碎片过期策略不生效。 重要 生命周期规则至少包含文件过期策略或碎片过期策略。 |
| 碎片规则 | 根据碎片过期策略选择的过期天数或过期日期设定碎片何时过期，碎片过期后会被自动删除，且删除后不可恢复。 |  |
存储空间已开启版本控制
开启版本控制后，基础设置与碎片执行策略设置区域涉及的配置项，与未开启版本控制的配置方法相同。以下表格仅介绍与未开启版本控制相比，开启版本控制后配置项存在的差异。
重要
在配置生命周期规则前，请确认：如果Bucket已开启了版本控制并作为跨区域复制的目标端，从源端同步过来的删除标记（Delete Marker）会将本Bucket内的同名对象从当前版本转变为历史版本。因此，请谨慎配置针对历史版本的清理规则，避免当前Bucket中的数据被非预期删除。
| 区域 | 配置项 | 说明 |
| --- | --- | --- |
| 当前版本文件执行策略设置 | 清理对象删除标记 | 开启版本控制后，清除策略中增加了 清理对象删除标记 选项，其他选项与未开启版本控制时相同。 选择此选项后，如果当前 Object 仅有一个版本且为删除标记时，则 OSS 将删除过期 Object 的删除标记。如果当前 Object 有多个版本，且 Object 的最新版本为删除标记时，则 OSS 将保留该删除标记。关于删除标记的更多信息，请参见 [删除标记](delete-marker.md) 。 重要 当有历史版本存在时，该规则不会清理对象删除标记。因此建议及时清理对象删除标记和非必要的历史版本，否则 Bucket 内因存储过多的删除标记，导致 List 性能下降。 |
| 历史版本文件执行策略设置 | 文件时间策略 | 设置历史版本文件的过期策略，可选择 指定天数 和 不启用 。当选择 不启用 时，文件过期策略不生效。 |
| 生命周期管理规则 | 设定一个过期天数 N，历史版本的 Object 会在其被转换为历史版本的 N 天后过期，并在过期的第二天执行指定操作。例如设置为 30，则在 2023 年 09 月 01 日被转为历史版本的 Object 会在 2023 年 10 月 01 日被转换为指定存储类型或被删除。 重要 您可以通过 Object 下一个版本的最后一次修改时间确定 Object 被转为历史版本的时间。 |  |
单击确定。
生命周期规则保存成功后，您可以在策略列表中查看已设置的生命周期规则。
### 使用阿里云SDK
以下仅列举常见SDK的配置生命周期规则的代码示例。关于其他SDK的配置生命周期规则的代码示例，请参见[SDK](../developer-reference/overview-21.md)[简介](../developer-reference/overview-21.md)。
## Java
import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.common.utils.DateUtil; import com.aliyun.oss.model.LifecycleRule; import com.aliyun.oss.model.SetBucketLifecycleRequest; import com.aliyun.oss.model.StorageClass; import java.util.ArrayList; import java.util.HashMap; import java.util.List; import java.util.Map; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 创建SetBucketLifecycleRequest。 SetBucketLifecycleRequest request = new SetBucketLifecycleRequest(bucketName); // 设置规则ID。 String ruleId0 = "rule0"; // 设置文件匹配前缀。 String matchPrefix0 = "A0/"; // 设置要匹配的标签。 Map<String, String> matchTags0 = new HashMap<String, String>(); // 依次填写要匹配标签的键（例如owner）和值（例如John）。 matchTags0.put("owner", "John"); String ruleId1 = "rule1"; String matchPrefix1 = "A1/"; Map<String, String> matchTags1 = new HashMap<String, String>(); matchTags1.put("type", "document"); String ruleId2 = "rule2"; String matchPrefix2 = "A2/"; String ruleId3 = "rule3"; String matchPrefix3 = "A3/"; String ruleId4 = "rule4"; String matchPrefix4 = "A4/"; String ruleId5 = "rule5"; String matchPrefix5 = "A5/"; String ruleId6 = "rule6"; String matchPrefix6 = "A6/"; // 距最后修改时间3天后过期。 LifecycleRule rule = new LifecycleRule(ruleId0, matchPrefix0, LifecycleRule.RuleStatus.Enabled, 3); rule.setTags(matchTags0); request.AddLifecycleRule(rule); // 指定日期之前创建的文件过期。 rule = new LifecycleRule(ruleId1, matchPrefix1, LifecycleRule.RuleStatus.Enabled); rule.setCreatedBeforeDate(DateUtil.parseIso8601Date("2022-10-12T00:00:00.000Z")); rule.setTags(matchTags1); request.AddLifecycleRule(rule); // 分片3天后过期。 rule = new LifecycleRule(ruleId2, matchPrefix2, LifecycleRule.RuleStatus.Enabled); LifecycleRule.AbortMultipartUpload abortMultipartUpload = new LifecycleRule.AbortMultipartUpload(); abortMultipartUpload.setExpirationDays(3); rule.setAbortMultipartUpload(abortMultipartUpload); request.AddLifecycleRule(rule); // 指定日期之前的分片过期。 rule = new LifecycleRule(ruleId3, matchPrefix3, LifecycleRule.RuleStatus.Enabled); abortMultipartUpload = new LifecycleRule.AbortMultipartUpload(); abortMultipartUpload.setCreatedBeforeDate(DateUtil.parseIso8601Date("2022-10-12T00:00:00.000Z")); rule.setAbortMultipartUpload(abortMultipartUpload); request.AddLifecycleRule(rule); // 距最后修改时间10天后转低频访问存储类型，距最后修改时间30天后转归档存储类型。 rule = new LifecycleRule(ruleId4, matchPrefix4, LifecycleRule.RuleStatus.Enabled); List<LifecycleRule.StorageTransition> storageTransitions = new ArrayList<LifecycleRule.StorageTransition>(); LifecycleRule.StorageTransition storageTransition = new LifecycleRule.StorageTransition(); storageTransition.setStorageClass(StorageClass.IA); storageTransition.setExpirationDays(10); storageTransitions.add(storageTransition); storageTransition = new LifecycleRule.StorageTransition(); storageTransition.setStorageClass(StorageClass.Archive); storageTransition.setExpirationDays(30); storageTransitions.add(storageTransition); rule.setStorageTransition(storageTransitions); request.AddLifecycleRule(rule); // 指定最后修改日期在2022年10月12日之前的文件转为归档存储。 rule = new LifecycleRule(ruleId5, matchPrefix5, LifecycleRule.RuleStatus.Enabled); storageTransitions = new ArrayList<LifecycleRule.StorageTransition>(); storageTransition = new LifecycleRule.StorageTransition(); storageTransition.setCreatedBeforeDate(DateUtil.parseIso8601Date("2022-10-12T00:00:00.000Z")); storageTransition.setStorageClass(StorageClass.Archive); storageTransitions.add(storageTransition); rule.setStorageTransition(storageTransitions); request.AddLifecycleRule(rule); // rule6针对版本控制状态下的Bucket。 rule = new LifecycleRule(ruleId6, matchPrefix6, LifecycleRule.RuleStatus.Enabled); // 设置Object相对最后修改时间365天之后自动转为归档文件。 storageTransitions = new ArrayList<LifecycleRule.StorageTransition>(); storageTransition = new LifecycleRule.StorageTransition(); storageTransition.setStorageClass(StorageClass.Archive); storageTransition.setExpirationDays(365); storageTransitions.add(storageTransition); rule.setStorageTransition(storageTransitions); // 设置自动移除过期删除标记。 rule.setExpiredDeleteMarker(true); // 设置非当前版本的object距最后修改时间10天之后转为低频访问类型。 LifecycleRule.NoncurrentVersionStorageTransition noncurrentVersionStorageTransition = new LifecycleRule.NoncurrentVersionStorageTransition().withNoncurrentDays(10).withStrorageClass(StorageClass.IA); // 设置非当前版本的Object距最后修改时间20天之后转为归档类型。 LifecycleRule.NoncurrentVersionStorageTransition noncurrentVersionStorageTransition2 = new LifecycleRule.NoncurrentVersionStorageTransition().withNoncurrentDays(20).withStrorageClass(StorageClass.Archive); // 设置非当前版本Object 30天后删除。 LifecycleRule.NoncurrentVersionExpiration noncurrentVersionExpiration = new LifecycleRule.NoncurrentVersionExpiration().withNoncurrentDays(30); List<LifecycleRule.NoncurrentVersionStorageTransition> noncurrentVersionStorageTransitions = new ArrayList<LifecycleRule.NoncurrentVersionStorageTransition>(); noncurrentVersionStorageTransitions.add(noncurrentVersionStorageTransition2); rule.setStorageTransition(storageTransitions); rule.setNoncurrentVersionExpiration(noncurrentVersionExpiration); rule.setNoncurrentVersionStorageTransitions(noncurrentVersionStorageTransitions); request.AddLifecycleRule(rule); // 发起设置生命周期规则请求。 ossClient.setBucketLifecycle(request); // 查看生命周期规则。 List<LifecycleRule> listRules = ossClient.getBucketLifecycle(bucketName); for(LifecycleRule rules : listRules){ System.out.println("ruleId="+rules.getId()+", matchPrefix="+rules.getPrefix()); } } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }
## PHP
<?php // 引入自动加载文件 加载依赖库 require_once __DIR__ . '/../vendor/autoload.php'; use AlibabaCloud\Oss\V2 as Oss; use AlibabaCloud\Oss\V2\Models\LifecycleConfiguration; // 定义命令行参数描述 $optsdesc = [ "region" => ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域 "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名 "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项 ]; // 生成长选项列表 用于解析命令行参数 $longopts = \array_map(function ($key) { return "$key:"; // 每个参数后面加冒号 表示需要值 }, array_keys($optsdesc)); // 解析命令行参数 $options = getopt("", $longopts); // 检查必填参数是否缺失 foreach ($optsdesc as $key => $value) { if ($value['required'] === True && empty($options[$key])) { $help = $value['help']; echo "Error: the following arguments are required: --$key, $help"; // 提示用户缺少必填参数 exit(1); } } // 获取命令行参数值 $region = $options["region"]; // 存储空间所在区域 $bucket = $options["bucket"]; // 存储空间名称 // 使用环境变量加载凭证信息 AccessKeyId 和 AccessKeySecret $credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 使用SDK的默认配置 $cfg = Oss\Config::loadDefault(); // 设置凭证提供者 $cfg->setCredentialsProvider($credentialsProvider); // 设置区域 $cfg->setRegion($region); // 如果提供了终端节点 则设置终端节点 if (isset($options["endpoint"])) { $cfg->setEndpoint($options["endpoint"]); } // 创建OSS客户端实例 $client = new Oss\Client($cfg); // 定义生命周期规则 将前缀为log/的对象在30天后转换为低频存储类型 $lifecycleRule = new Oss\Models\LifecycleRule( prefix: 'log/', // 对象前缀 transitions: array( new Oss\Models\LifecycleRuleTransition( days: 30, // 转换时间为30天 storageClass: 'IA' // 转换为目标存储类型为低频访问 ) ), id: 'rule', // 规则ID status: 'Enabled' // 规则状态为启用 ); // 创建生命周期配置对象 并添加生命周期规则 $lifecycleConfiguration = new LifecycleConfiguration( rules: array($lifecycleRule) ); // 创建设置存储空间生命周期的请求对象 并将生命周期配置传入 $request = new Oss\Models\PutBucketLifecycleRequest( bucket: $bucket, lifecycleConfiguration: $lifecycleConfiguration ); // 调用putBucketLifecycle方法设置存储空间的生命周期规则 $result = $client->putBucketLifecycle($request); // 打印返回结果 printf( 'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码 'request id:' . $result->requestId . PHP_EOL // 请求的唯一标识 );
## Node.js
const OSS = require('ali-oss') const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: 'yourregion', // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, authorizationV4: true, // 填写存储空间名称。 bucket: 'yourbucketname' }); async function putBucketLifecycle(lifecycle) { try { const result = await client.putBucketLifecycle('yourbucketname', [ lifecycle ]); console.log(result); } catch (e) { console.log(e); } } const lifecycle1 = { id: 'rule1', status: 'Enabled', prefix: 'foo/', expiration: { // 指定当前版本Object距其最后修改时间3天后过期。 days: 3 } } putBucketLifecycle(lifecycle1) const lifecycle2 = { id: 'rule2', status: 'Enabled', prefix: 'foo/', expiration: { // 指定日期之前创建的文件过期。 createdBeforeDate: '2020-02-18T00:00:00.000Z' }, } putBucketLifecycle(lifecycle2) const lifecycle3 = { id: 'rule3', status: 'Enabled', prefix: 'foo/', abortMultipartUpload: { // 指定分片3天后过期。 days: 3 }, } putBucketLifecycle(lifecycle3) const lifecycle4 = { id: 'rule4', status: 'Enabled', prefix: 'foo/', abortMultipartUpload: { // 指定日期之前创建的分片过期。 createdBeforeDate: '2020-02-18T00:00:00.000Z' }, } putBucketLifecycle(lifecycle4) const lifecycle5 = { id: 'rule5', status: 'Enabled', prefix: 'foo/', transition: { // 指定当前版本Object距其最后修改时间20天后转归档存储类型。 days: 20, storageClass: 'Archive' }, expiration: { // 指定当前版本Object距其最后修改时间21天后过期。 days: 21 }, } putBucketLifecycle(lifecycle5) const lifecycle6 = { id: 'rule6', status: 'Enabled', prefix: 'foo/', transition: { // 指定日期之前修改的文件转为归档类型。 createdBeforeDate: '2023-02-19T00:00:00.000Z', storageClass: 'Archive' }, expiration: { // 指定日期之前修改的文件删除。 createdBeforeDate: '2023-01-18T00:00:00.000Z' }, } putBucketLifecycle(lifecycle6) const lifecycle7 = { id: 'rule7', status: 'Enabled', prefix: 'foo/', expiration: { // 设置自动移除过期删除标记。 expiredObjectDeleteMarker: true } } putBucketLifecycle(lifecycle7) const lifecycle8 = { id: 'rule8', status: 'Enabled', prefix: 'foo/', // 设置非当前版本的Object距其最后修改时间10天之后转为低频访问类型。 noncurrentVersionTransition: { noncurrentDays: '10', storageClass: 'IA' } } putBucketLifecycle(lifecycle8) const lifecycle9 = { id: 'rule9', status: 'Enabled', prefix: 'foo/', // 设置非当前版本的Object距其最后修改时间10天之后转为低频访问类型。 noncurrentVersionTransition: { noncurrentDays: '10', storageClass: 'IA' }, // 指定规则所适用的对象标签。 tag: [{ key: 'key1', value: 'value1' }, { key: 'key2', value: 'value2' }] } putBucketLifecycle(lifecycle9)
## Python
import argparse import alibabacloud_oss_v2 as oss # 创建命令行参数解析器，用于接收用户输入的参数 parser = argparse.ArgumentParser(description="put bucket lifecycle sample") # 添加命令行参数 --region，表示存储空间所在的地域，必填项 parser.add_argument('--region', help='The region in which the bucket is located.', required=True) # 添加命令行参数 --bucket，表示存储空间的名称，必填项 parser.add_argument('--bucket', help='The name of the bucket.', required=True) # 添加命令行参数 --endpoint，表示其他服务访问 OSS 时使用的域名，可选项 parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS') def main(): # 解析命令行参数 args = parser.parse_args() # 从环境变量中加载凭证信息（AccessKeyId 和 AccessKeySecret） credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 加载 SDK 的默认配置 cfg = oss.config.load_default() # 设置凭证提供者 cfg.credentials_provider = credentials_provider # 设置存储空间所在的地域 cfg.region = args.region # 如果用户提供了自定义的 endpoint，则设置到配置中 if args.endpoint is not None: cfg.endpoint = args.endpoint # 使用配置对象初始化 OSS 客户端 client = oss.Client(cfg) result = client.put_bucket_lifecycle(oss.PutBucketLifecycleRequest( bucket=args.bucket, lifecycle_configuration=oss.LifecycleConfiguration( rules=[oss.LifecycleRule( # 指定生命周期规则rule1。规则中指定前缀为foo、标签键为k1、标签值为v1的文件，在距离最后一次修改时间30天后转为低频访问类型 id='rule1', status='Enabled', prefix='foo/', transitions=[oss.LifecycleRuleTransition( days=30, storage_class=oss.StorageClassType.IA, is_access_time=False, # 设置为false，基于最后一次修改时间策略 )], tags=[oss.Tag( key='k1', value='v1', )], ), oss.LifecycleRule( # 指定生命周期规则rule2。规则中指定前缀为dir，在受版本控制状态下的Object仅有删除标记的情况下自动删除删除标记，非当前版本Object超过30天后过期删除，非当前版本Object超过10天后转为IA存储类型 id='rule2', status='Enabled', prefix='dir/', expiration=oss.LifecycleRuleExpiration( expired_object_delete_marker=True ), noncurrent_version_expiration=oss.NoncurrentVersionExpiration( noncurrent_days=30, ), noncurrent_version_transitions=[oss.NoncurrentVersionTransition( noncurrent_days=10, storage_class=oss.StorageClassType.IA, is_access_time=False, )], )] ), )) # 打印操作结果的状态码和请求 ID print(f'status code: {result.status_code}, ' # HTTP 状态码，表示请求是否成功 f'request id: {result.request_id}') # 请求 ID，用于追踪请求日志和调试 if __name__ == "__main__": # 程序入口，调用 main 函数执行逻辑 main()
## C#
using Aliyun.OSS; using Aliyun.OSS.Common; // 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket"; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); client.SetRegion(region); try { var setBucketLifecycleRequest = new SetBucketLifecycleRequest(bucketName); // 创建第1条生命周期规则。 LifecycleRule lcr1 = new LifecycleRule() { ID = "delete obsoleted files", Prefix = "obsoleted/", Status = RuleStatus.Enabled, ExpriationDays = 3, Tags = new Tag[1] }; // 设置标签。 var tag1 = new Tag { Key = "project", Value = "projectone" }; lcr1.Tags[0] = tag1; // 创建第2条生命周期规则。 LifecycleRule lcr2 = new LifecycleRule() { ID = "delete temporary files", Prefix = "temporary/", Status = RuleStatus.Enabled, ExpriationDays = 20, Tags = new Tag[1] }; // 设置标签。 var tag2 = new Tag { Key = "user", Value = "jsmith" }; lcr2.Tags[0] = tag2; // 设置碎片在距最后修改时间30天后过期。 lcr2.AbortMultipartUpload = new LifecycleRule.LifeCycleExpiration() { Days = 30 }; LifecycleRule lcr3 = new LifecycleRule(); lcr3.ID = "only NoncurrentVersionTransition"; lcr3.Prefix = "test1"; lcr3.Status = RuleStatus.Enabled; lcr3.NoncurrentVersionTransitions = new LifecycleRule.LifeCycleNoncurrentVersionTransition[2] { // 设置非当前版本的Object距最后修改时间90天之后转为低频访问类型。 new LifecycleRule.LifeCycleNoncurrentVersionTransition(){ StorageClass = StorageClass.IA, NoncurrentDays = 90 }, // 设置非当前版本的Object距最后修改时间180天之后转为归档类型。 new LifecycleRule.LifeCycleNoncurrentVersionTransition(){ StorageClass = StorageClass.Archive, NoncurrentDays = 180 } }; setBucketLifecycleRequest.AddLifecycleRule(lcr1); setBucketLifecycleRequest.AddLifecycleRule(lcr2); setBucketLifecycleRequest.AddLifecycleRule(lcr3); // 设置生命周期规则。 client.SetBucketLifecycle(setBucketLifecycleRequest); Console.WriteLine("Set bucket:{0} Lifecycle succeeded ", bucketName); } catch (OssException ex) { Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}", ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId); } catch (Exception ex) { Console.WriteLine("Failed with error info: {0}", ex.Message); }
## Android-Java
PutBucketLifecycleRequest request = new PutBucketLifecycleRequest(); request.setBucketName("examplebucket"); BucketLifecycleRule rule1 = new BucketLifecycleRule(); // 设置规则ID和文件前缀。 rule1.setIdentifier("1"); rule1.setPrefix("A"); // 设置是否执行生命周期规则。如果值为true，则OSS会定期执行该规则；如果值为false，则OSS会忽略该规则。 rule1.setStatus(true); // 距最后修改时间200天后过期。 rule1.setDays("200"); // 30天后自动转为归档存储类型（Archive） rule1.setArchiveDays("30"); // 未完成分片3天后过期。 rule1.setMultipartDays("3"); // 15天后自动转为低频存储类型（IA）。 rule1.setIADays("15"); BucketLifecycleRule rule2 = new BucketLifecycleRule(); rule2.setIdentifier("2"); rule2.setPrefix("B"); rule2.setStatus(true); rule2.setDays("300"); rule2.setArchiveDays("30"); rule2.setMultipartDays("3"); rule2.setIADays("15"); ArrayList<BucketLifecycleRule> lifecycleRules = new ArrayList<BucketLifecycleRule>(); lifecycleRules.add(rule1); lifecycleRules.add(rule2); request.setLifecycleRules(lifecycleRules); OSSAsyncTask task = oss.asyncPutBucketLifecycle(request, new OSSCompletedCallback<PutBucketLifecycleRequest, PutBucketLifecycleResult>() { @Override public void onSuccess(PutBucketLifecycleRequest request, PutBucketLifecycleResult result) { OSSLog.logInfo("code::"+result.getStatusCode()); } @Override public void onFailure(PutBucketLifecycleRequest request, ClientException clientException, ServiceException serviceException) { OSSLog.logError("error: "+serviceException.getRawMessage()); } }); task.waitUntilFinished();
## C++
#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /*初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ std::string Region = "yourRegion"; /*填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /*初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); SetBucketLifecycleRequest request(BucketName); std::string date("2022-10-12T00:00:00.000Z"); /*设置标签。*/ Tagging tagging; tagging.addTag(Tag("key1", "value1")); tagging.addTag(Tag("key2", "value2")); /*指定生命周期规则。*/ auto rule1 = LifecycleRule(); rule1.setID("rule1"); rule1.setPrefix("test1/"); rule1.setStatus(RuleStatus::Enabled); rule1.setExpiration(3); rule1.setTags(tagging.Tags()); /*指定过期时间。*/ auto rule2 = LifecycleRule(); rule2.setID("rule2"); rule2.setPrefix("test2/"); rule2.setStatus(RuleStatus::Disabled); rule2.setExpiration(date); /*rule3为针对版本控制状态下的Bucket的生命周期规则。*/ auto rule3 = LifecycleRule(); rule3.setID("rule3"); rule3.setPrefix("test3/"); rule3.setStatus(RuleStatus::Disabled); /*设置Object距其最后修改时间365天之后自动转为归档类型。*/ auto transition = LifeCycleTransition(); transition.Expiration().setDays(365); transition.setStorageClass(StorageClass::Archive); rule3.addTransition(transition); /*设置自动移除过期删除标记。*/ rule3.setExpiredObjectDeleteMarker(true); /*设置非当前版本的Object距最后修改时间10天之后转为低频访问类型。*/ auto transition1 = LifeCycleTransition(); transition1.Expiration().setDays(10); transition1.setStorageClass(StorageClass::IA); /*设置非当前版本的Object距最后修改时间20天之后转为归档类型。*/ auto transition2 = LifeCycleTransition(); transition2.Expiration().setDays(20); transition2.setStorageClass(StorageClass::Archive); /*设置Object在其成为非当前版本30天之后删除。*/ auto expiration = LifeCycleExpiration(30); rule3.setNoncurrentVersionExpiration(expiration); LifeCycleTransitionList noncurrentVersionStorageTransitions{transition1, transition2}; rule3.setNoncurrentVersionTransitionList(noncurrentVersionStorageTransitions); /*设置生命周期规则。*/ LifecycleRuleList list{rule1, rule2, rule3}; request.setLifecycleRules(list); auto outcome = client.SetBucketLifecycle(request); if (!outcome.isSuccess()) { /*异常处理 */ std::cout << "SetBucketLifecycle fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /*释放网络等资源。*/ ShutdownSdk(); return 0; }
## C
#include "oss_api.h" #include "aos_http_io.h" /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ const char *endpoint = "yourEndpoint"; /* 填写Bucket名称，例如examplebucket。*/ const char *bucket_name = "examplebucket"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ const char *region = "yourRegion"; void init_options(oss_request_options_t *options) { options->config = oss_config_create(options->pool); /* 用char*类型的字符串初始化aos_string_t类型。*/ aos_str_set(&options->config->endpoint, endpoint); /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID")); aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET")); //需要额外配置以下两个参数 aos_str_set(&options->config->region, region); options->config->signature_version = 4; /* 是否使用cname域名访问OSS服务。0表示不使用。*/ options->config->is_cname = 0; /* 用于设置网络相关参数，比如超时时间等。*/ options->ctl = aos_http_controller_create(options->pool, 0); } int main(int argc, char *argv[]) { /* 在程序入口调用aos_http_io_initialize方法来初始化网络、内存等全局资源。*/ if (aos_http_io_initialize(NULL, 0) != AOSE_OK) { exit(1); } /* 用于内存管理的内存池（pool），等价于apr_pool_t。其实现代码在apr库中。*/ aos_pool_t *pool; /* 重新创建一个内存池，第二个参数是NULL，表示没有继承其它内存池。*/ aos_pool_create(&pool, NULL); /* 创建并初始化options，该参数包括endpoint、access_key_id、acces_key_secret、is_cname、curl等全局配置信息。*/ oss_request_options_t *oss_client_options; /* 在内存池中分配内存给options。*/ oss_client_options = oss_request_options_create(pool); /* 初始化Client的选项oss_client_options。*/ init_options(oss_client_options); /* 初始化参数。*/ aos_string_t bucket; aos_table_t *resp_headers = NULL; aos_status_t *resp_status = NULL; aos_str_set(&bucket, bucket_name); aos_list_t lifecycle_rule_list; aos_str_set(&bucket, bucket_name); aos_list_init(&lifecycle_rule_list); /* 指定过期天数。*/ oss_lifecycle_rule_content_t *rule_content_days = oss_create_lifecycle_rule_content(pool); aos_str_set(&rule_content_days->id, "rule-1"); /* 设置文件前缀。*/ aos_str_set(&rule_content_days->prefix, "dir1"); aos_str_set(&rule_content_days->status, "Enabled"); rule_content_days->days = 3; aos_list_add_tail(&rule_content_days->node, &lifecycle_rule_list); /* 指定过期时间。*/ oss_lifecycle_rule_content_t *rule_content_date = oss_create_lifecycle_rule_content(pool); aos_str_set(&rule_content_date->id, "rule-2"); aos_str_set(&rule_content_date->prefix, "dir2"); aos_str_set(&rule_content_date->status, "Enabled"); /* 过期时间格式为UTC。 aos_str_set(&rule_content_date->date, "2023-10-11T00:00:00.000Z"); aos_list_add_tail(&rule_content_date->node, &lifecycle_rule_list); /* 设置生命周期规则。*/ resp_status = oss_put_bucket_lifecycle(oss_client_options, &bucket, &lifecycle_rule_list, &resp_headers); if (aos_status_is_ok(resp_status)) { printf("put bucket lifecycle succeeded\n"); } else { printf("put bucket lifecycle failed, code:%d, error_code:%s, error_msg:%s, request_id:%s\n", resp_status->code, resp_status->error_code, resp_status->error_msg, resp_status->req_id); } /* 释放内存池，相当于释放了请求过程中各资源分配的内存。*/ aos_pool_destroy(pool); /* 释放之前分配的全局资源。*/ aos_http_io_deinitialize(); return 0; }
## Ruby
require 'aliyun/oss' client = Aliyun::OSS::Client.new( # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 endpoint: 'https://oss-cn-hangzhou.aliyuncs.com', # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 access_key_id: ENV['OSS_ACCESS_KEY_ID'], access_key_secret: ENV['OSS_ACCESS_KEY_SECRET'] ) # 填写Bucket名称。 bucket = client.get_bucket('examplebucket') # 设置生命周期规则。 bucket.lifecycle = [ Aliyun::OSS::LifeCycleRule.new( :id => 'rule1', :enable => true, :prefix => 'foo/', :expiry => 3), Aliyun::OSS::LifeCycleRule.new( :id => 'rule2', :enable => false, :prefix => 'bar/', :expiry => Date.new(2016, 1, 1)) ]
## Go
package main import ( "context" "flag" "log" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) // 定义全局变量 var ( region string // 存储区域 bucketName string // 存储空间名称 ) // init函数用于初始化命令行参数 func init() { flag.StringVar(&region, "region", "", "The region in which the bucket is located.") flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.") } func main() { // 解析命令行参数 flag.Parse() // 检查bucket名称是否为空 if len(bucketName) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, bucket name required") } // 检查region是否为空 if len(region) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, region required") } // 加载默认配置并设置凭证提供者和区域 cfg := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion(region) // 创建OSS客户端 client := oss.NewClient(cfg) // 创建设置存储空间生命周期规则的请求 request := &oss.PutBucketLifecycleRequest{ Bucket: oss.Ptr(bucketName), // 存储空间名称 LifecycleConfiguration: &oss.LifecycleConfiguration{ Rules: []oss.LifecycleRule{ { // 指定生命周期规则rule1。规则中指定前缀为foo、标签键为k1、标签值为v1的文件，在距离最后一次修改时间30天后转为低频访问类型 Status: oss.Ptr("Enabled"), ID: oss.Ptr("rule1"), Prefix: oss.Ptr("foo/"), Transitions: []oss.LifecycleRuleTransition{ { Days: oss.Ptr(int32(30)), StorageClass: oss.StorageClassIA, IsAccessTime: oss.Ptr(false), // 设置为false，基于最后一次修改时间策略 }, }, Tags: []oss.Tag{ { Key: oss.Ptr("k1"), Value: oss.Ptr("v1"), }, }, }, { // 指定生命周期规则rule2。规则中指定前缀为dir，在受版本控制状态下的Object仅有删除标记的情况下自动删除删除标记，非当前版本Object超过30天后过期删除，非当前版本Object超过10天后转为IA存储类型 ID: oss.Ptr("rule2"), Prefix: oss.Ptr("dir/"), Status: oss.Ptr("Enabled"), Expiration: &oss.LifecycleRuleExpiration{ Days: oss.Ptr(int32(10)), ExpiredObjectDeleteMarker: oss.Ptr(true), }, NoncurrentVersionExpiration: &oss.NoncurrentVersionExpiration{ NoncurrentDays: oss.Ptr(int32(30)), }, NoncurrentVersionTransitions: []oss.NoncurrentVersionTransition{{ NoncurrentDays: oss.Ptr(int32(10)), StorageClass: oss.StorageClassIA, IsAccessTime: oss.Ptr(false), // 设置为false，基于最后一次修改时间策略 }}, }, }, }, } // 执行设置存储空间生命周期规则的操作 result, err := client.PutBucketLifecycle(context.TODO(), request) if err != nil { log.Fatalf("failed to put bucket lifecycle %v", err) } // 打印设置存储空间生命周期规则的结果 log.Printf("put bucket lifecycle result:%#v\n", result) }
### 使用命令行工具ossutil
您可以使用命令行工具ossutil来设置生命周期规则，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下示例展示了如何为存储空间examplebucket设置生命周期信息。
ossutil api put-bucket-lifecycle --bucket examplebucket --lifecycle-configuration "{\"Rule\":{\"ID\":\"rule1\",\"Prefix\":\"tmp/\",\"Status\":\"Enabled\",\"Expiration\":{\"Days\":\"10\"},\"Transition\":{\"Days\":\"5\",\"StorageClass\":\"IA\"},\"AbortMultipartUpload\":{\"Days\":\"10\"}}}"
关于该命令的更多信息，请参见[put-bucket-lifecycle](../developer-reference/put-bucket-lifecycle.md)。
## 相关API
以上操作方式底层基于API实现，如果您的程序自定义要求较高，您可以直接发起REST API请求。直接发起REST API请求需要手动编写代码计算签名。更多信息，请参见[PutBucketLifecycle](../developer-reference/putbucketlifecycle.md)。
## 常见问题
### 如何通过生命周期快速清理Bucket下的所有文件
Bucket未开启版本控制
对于未开启版本控制的Bucket，只需要配置一条生命周期规则，即可自动快速清理所有文件和碎片（Multipart Upload产生的未合并碎片）。
登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。
在左侧导航栏，选择数据安全>版本控制，确认Bucket未开启版本控制。
在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。
Bucket已开启版本控制
Bucket开启版本控制后，会产生当前版本文件、历史版本文件、碎片文件和删除标记。只需要配置一条生命周期规则，即可自动快速清理这些文件。
登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。
在左侧导航栏，选择数据安全>版本控制，确认Bucket已开启版本控制。
在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有当前版本、历史版本文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。该规则会同步清理删除标记。
### 报错Set bucket lifecycle error, InvalidArgument, Days in the Transition action for StorageClass Archive must be more than the Transition action for StorageClass IA怎么办？
出现该报错是因为不同存储类型的转储时间不满足要求。Bucket配置的转换周期必须满足：低频访问 < 归档 < 冷归档 < 深度冷归档。
### 生命周期规则是否作用于Bucket内已有的存量Object？
生命周期规则同时作用于配置前的存量Object和配置后新上传Object。例如，10月07日配置规则，指定30天后删除，则10月5日上传的Object在11月6日删除，10月08日上传的Object在11月09日删除。
### 如何修改其中一条或多条生命周期规则配置？
假设您的Bucket配置了两条生命周期规则，分别为Rule1和Rule2，您希望修改Rule1的某个配置项，您需要执行以下操作。
调用GetBucketLifecycle接口获取当前Bucket配置的所有生命周期规则，即Rule1和Rule2。
修改Rule1生命周期规则的配置项。
调用PutBucketLifecycle接口更新生命周期规则为Rule1+Rule2。
### 如何删除其中一条或多条生命周期规则？
调用DeleteBucketLifecycle时会一键删除Bucket配置的所有生命周期规则。假设您的Bucket配置了两条生命周期规则，分别为Rule1和Rule2，您仅希望删除Rule1，您需要执行以下操作。
调用GetBucketLifecycle接口获取当前Bucket配置的所有生命周期规则，即Rule1和Rule2。
删除Rule1。
调用PutBucketLifecycle接口更新生命周期规则为Rule2。
### 通过生命周期规则进行的类型转换、过期删除操作，是否有日志记录？
所有成功通过生命周期规则进行的类型转换、过期删除操作都会有日志记录，日志记录字段如下：
Operation
CommitTransition：转换存储类型。
ExpireObject：删除过期Object。
Sync Request
lifecycle：触发的转换和删除操作。
关于OSS日志字段的更多信息，请参见[日志字段详情](../../../sls/documents/log-fields-13.md)。关于日志查询的费用说明，请参见[计费说明](real-time-log-query.md)。
### 是否支持创建一条生命周期规则同时清理对象删除标记和当前版本对象？
不支持。您可以先创建规则清理对象删除标记，再创建规则删除当前版本对象。
### 基于最后一次修改时间的生命周期规则是否支持将Object从低频访问类型转换为标准类型？
不支持。您可以通过以下方式将Object从低频访问类型转为标准类型：
通过CopyObject的方式
CopyObject接口支持将单个Object从低频访问类型转为标准类型。
通过ossutil工具
ossutil支持通过set-meta命令添加X-Oss-Storage-Class选项的方式将单个或多个Object从低频访问类型转换为标准类型。具体操作，请参见[设置或更新元数据](../developer-reference/set-meta.md)。
## 相关文档
默认情况下，OSS会将Object的上传时间置为其最后一次修改时间。通过生命周期转换文件存储类型的操作不会更新Object的最后一次修改时间。具体哪些操作会影响Object的LastModified，请参见[哪些操作会更新](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[Object](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[的](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)[LastModified？](what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects.md)。
当低频访问、归档、冷归档或者深度冷归档存储类型Object在存储不足规定时长时转换了存储类型并提前删除时，需要收取不足规定时长容量费用。更多信息，请参见[Object](../billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)[在存储不足规定时长时如何计费？](../billing-method-for-objects-whose-storage-duration-is-less-than-the-minimum-storage-duration.md)。
生命周期规则仅支持对整个Bucket或与前缀匹配的数据进行批量转储或者删除，如果您希望批量删除指定后缀的数据，您可以使用[ossutil rm](../developer-reference/rm.md)[命令](../developer-reference/rm.md)。
如果您希望OSS自动监测数据的访问模式并识别冷数据，然后转换其存储类型以降低存储成本，请配置[基于最后一次访问时间的生命周期规则](lifecycle-rules-based-on-the-last-access-time.md)。
如果您希望查看Bucket内所有Object的存储类型，请参见[列举文件](list-objects-18.md)。
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
