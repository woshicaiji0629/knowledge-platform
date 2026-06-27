## API
说明
仅Linux实例支持通过API绑定、换绑或解绑密钥对。
创建实例时设置密钥对：在调用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)创建实例时，将KeyPairName设置为对应的密钥对名称。
绑定/换绑密钥对：调用[AttachKeyPair](../developer-reference/api-ecs-2014-05-26-attachkeypair.md)，并指定密钥对名称KeyPairName和实例IDInstanceIds。
解绑密钥对：调用[DetachKeyPair](../developer-reference/api-ecs-2014-05-26-detachkeypair.md)，并指定密钥对名称KeyPairName和实例IDInstanceIds。
