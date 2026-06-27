ainNames": "example.com" }
image_transform
功能说明：配置CDN图片转换，该功能详细介绍请参见控制台配置说明[图片处理概述](../user-guide/image-editing-overview.md)。
功能ID（FunctionID/FuncId）：239。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启图片转换： on：开启。 off：关闭。 | on |
| filetype | String | 是 | 支持转码的图片格式，以竖线分割符号分隔。支持以下参数值： JPEG：JPEG 图片格式。 JPG：JPG 图片格式。 PNG：PNG 图片格式。 WEBP：WEBP 图片格式。 BMP：BMP 图片格式。 GIF：GIF 图片格式。 TIFF：TIFF 图片格式。 JP2：JPEG 2000 图片格式。 | jpg|jpeg|png |
| webp | String | 否 | 是否开启自适应转换 WEBP： on：开启。 off：关闭。 | on |
| orient | String | 否 | 是否开启图片自旋转： on：开启。 off：关闭。 说明 只对有自旋转属性的图片生效。 | on |
| slim | Integer | 否 | 图片瘦身，设置瘦身的百分比，可配置范围是[0,100]。在不改变分辨率、尺寸、格式的前提下，缩小图片质量达到省流目的。 | 10 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "filetype", "argValue": "jpg|jpeg|png" }, { "argName": "webp", "argValue": "on" }, { "argName": "orient", "argValue": "on" }, { "argName": "slim", "argValue": "" }, { "argName": "enable", "argValue": "on" }], "functionName": "image_transform" }], "DomainNames": "example.com" }
