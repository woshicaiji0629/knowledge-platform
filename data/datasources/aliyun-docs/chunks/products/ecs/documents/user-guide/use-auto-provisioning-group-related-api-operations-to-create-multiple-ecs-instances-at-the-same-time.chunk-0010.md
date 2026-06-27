t( launchTemplateConfig )) .setClientToken("0c593ea1-3bea******************"); RuntimeOptions runtime = new RuntimeOptions(); CreateAutoProvisioningGroupResponse response = client.createAutoProvisioningGroupWithOptions(createAutoProvisioningGroupRequest, runtime); System.out.println(new Gson().toJson(response.getBody())); } }
JSON返回值示例如下：
{ "autoProvisioningGroupId": "apg-**************", "launchResults": { "launchResult": [ { "amount": 0, "errorCode": "NoInstanceStock", "errorMsg": "The instanceTypes are out of usage", "instanceType": "ecs.s6-c1m1.small", "spotStrategy": "NoSpot", "zoneId": "cn-heyuan-b" }, { "amount": 2, "instanceIds": { "instanceId": [ "i-f8z8**************icn5", "i-f8z8**************icn6" ] }, "instanceType": "ecs.s6-c1m1.small", "spotStrategy": "SpotAsPriceGo", "zoneId": "cn-heyuan-b" } ] }, "requestId": "CDA21119-7CFD-5B40-A2D0-******8" }
通过CreateAutoProvisioningGroup创建弹性供应组时，您只需要设置批量创建实例的相关配置项，无需关心创建过程，弹性供应组将以尽力交付的方式，完成创建。
说明
尽力交付的方式是指，当您配置的某些资源组合无法创建实例时，将自动切换到其他可用的资源组合继续进行创建。该方式创建实例需要一定的时间，并且可能导致实际创建结果与创建策略存在一定的偏差。
