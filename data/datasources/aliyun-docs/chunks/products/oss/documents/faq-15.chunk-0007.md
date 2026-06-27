et设置基于时间的合规保留策略。当策略锁定后，用户可以在Bucket中上传和读取Object，但是在Object的保留时间到期之前，任何用户都无法删除Object和策略。Object的保留时间到期后，才可以删除Object。
当您需要长期存储且不允许修改或删除重要数据时，例如医疗档案、技术文件、合同文书等，可以将此类数据存放在指定的Bucket内，并通过开启合规保留策略保护您的重要数据。
OSS是否支持在线修改文件？
OSS不支持对已上传的文件进行在线修改。如果您需要对文件进行修改，您可以先将已上传的文件下载到本地，修改后重新上传。
OSS是三副本吗？
不是。OSS采用的是纠删码（erasure coding，EC），而不是三副本。纠删码在性能和可靠性方面并不会比三副本差。
可用性99.995%是怎么计算的？
OSS的可用性SLA的定义不同于实例型产品，其服务可用性将根据服务周期内每5分钟错误率之和除以服务周期内5分钟的总个数计算出每5分钟错误率的平均值，按照如下方式计算：
每5分钟错误率=每5分钟失败请求数/每5分钟有效总请求数x100%
服务可用性=（1-服务周期内∑每5分钟错误率/服务周期内5分钟总个数×100%
更多信息，请参见[对象存储](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201803021527_93160.html?spm=a2c4g.11186623.0.0.47a350f9jxxAM0)[OSS](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201803021527_93160.html?spm=a2c4g.11186623.0.0.47a350f9jxxAM0)[服务等级协议](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201803021527_93160.html?spm=a2c4g.11186623.0.0.47a350f9jxxAM0)
