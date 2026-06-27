流量费+ 数据存储费”。 根据实际业务情况，可能还会存在“OSS 请求费用”等其他费用。详细计费项，请参见 [OSS](../../../oss/documents/billing-overview.md) [计量计费概述](../../../oss/documents/billing-overview.md) 。 |

流量费说明
当OSS作为CDN源站时，可能会产生CDN下行流量费（由CDN计费）和OSS流出到CDN流量费（由OSS计费）。
CDN下行流量费：用户从CDN节点请求资源，节点将资源下发给客户端时产生的流量费用；流量从CDN流向客户端，消耗的流量由CDN计费。价格详见[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.5be031c9TyAAu1#/cdn/detail/cdn)[定价-按流量计费](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.5be031c9TyAAu1#/cdn/detail/cdn)。
CDN节点回源到OSS产生的流量，不计费。
OSS流出到CDN节点产生的流量费：流量从OSS流向CDN，由OSS计费。价格详见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[定价-流量费用-OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[流出到](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)[流量](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.26443048xzpfk5#/oss/detail/ossbag)。
说明
阿里云CDN回源阿里云OSS的流量优惠说明：
用户需要在控制台上把源站类型设置为“OSS域名”，这样阿里云OSS产品会将来自阿里云CDN产品的回源流量识别为“CDN回源流出流量”，从而享受到更优惠的价格。
如果用户在控制台上把源站类型误设为“源站域名”，阿里云OSS产品会将来自阿里云CDN产品的回源流量识别为“外网流出流量”，这种情况下就享受不到优惠价格。
当CDN回源节点和回源的OSS的存储空间均在非中国内地区域时，OSS流出到CDN的流量免费。
