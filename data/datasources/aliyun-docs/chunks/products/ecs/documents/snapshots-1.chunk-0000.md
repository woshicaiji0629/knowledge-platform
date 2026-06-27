### 计费项说明
在初次使用快照前，需要先开通快照服务，[开通快照](user-guide/activate-ecs-snapshot.md)不收费，创建快照后才开始计费。创建的[手动快照](user-guide/create-a-snapshot.md)和[自动快照策略](user-guide/automatically-create-snapshots.md)默认是标准快照，阿里云在各地域会根据标准快照容量和使用时长收取标准快照存储费。
在使用标准快照过程中如果需要将标准快照归档以降低快照存储成本，标准快照会转换为[归档快照](user-guide/archive-snapshots.md)，阿里云在各地域会根据归档快照容量和使用时长收取归档快照存储费。
重要
归档快照的最短保留时间为60天（1,440小时），如果在60天内提前删除归档快照，除了需要支付归档快照存储费，还需支付归档快照不足规定时长费。
使用[复制快照](user-guide/copy-a-snapshot.md)功能将标准快照复制到目标地域实现跨地域数据备份，在目标地域会产生复制快照流量费和标准快照存储费。归档快照不支持复制。
使用[（公测）快照预热](user-guide/public-preview-snapshot-prefetch.md)功能将数据先从对象存储OSS中加载，以消除首次数据访问时的延迟，需要收取快照预热费。
