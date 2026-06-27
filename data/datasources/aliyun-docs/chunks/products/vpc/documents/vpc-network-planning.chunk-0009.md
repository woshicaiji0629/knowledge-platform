fc |  |  |
| 2001:XXXX:XXXX:1a00:ffff:ffff:ffff:fffd |  |  |
| 2001:XXXX:XXXX:1a00:ffff:ffff:ffff:fffe |  |  |
| 2001:XXXX:XXXX:1a00:ffff:ffff:ffff:ffff |  |  |

规划多个VPC的场景下，如果交换机所属私有子网与其他私有子网或本地IDC有网络互通需求，请避免交换机网段与对端网段重叠，否则无法实现网络互通。
ClassicLink功能允许经典网络的ECS和10.0.0.0/8、172.16.0.0/12或192.168.0.0/16三个VPC网段的ECS通信。如果要和经典网络通信的VPC网段是10.0.0.0/8，则该VPC下的交换机网段必须是10.111.0.0/16。更多信息，请参见[ClassicLink](overview-2.md)[概述](overview-2.md)。
