| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启回源 302 跟随： on：开启。 off：关闭。 | on |
| max_tries | Integer | 否 | 302 跟随次数上限。 默认值：2。 取值范围：[1,5]。 说明 回源次数-1（次）=302 跟随次数，即默认的回源次数上限为 3，可配置范围是[2,6]。 | 2 |
| retain_args | String | 否 | 302 跟随时是否保留原请求参数返回目标源： on：保留。 off（默认）：不保留。 | off |
| retain_header | String | 否 | 302 跟随时是否保留原请求头回目标源： on：保留。 off（默认）：不保留。 | off |
| response_header | String | 否 | 302 跟随响应头，表示源站给 CDN 的 302 跟随响应头的名称，该响应头名称默认为 Location。 | X-Alicdn-Redirect |
| retain_host | String | 否 | 302 跟随保留回源域名，当开启时，表示 CDN 在 302 跟随时保留回源域名，只在跟随到目标域名时生效。可以配置的值为： on：开启 off（默认）：关闭 | off |
| modify_host | String | 否 | 302 跟随修改回源域名，表示 CDN 在 302 跟随时修改回源域名，只在跟随到目标域名时生效。默认情况下不修改回源域名。 | example.com |
| cache | String | 否 | 302 跟随缓存跟随结果，当开启时，表示 CDN 在 302 跟随时缓存同 URL 的跟随结果，提升 CDN 的响应性能。可以配置的值为： on：开启 off（默认）：关闭 | off |
| expired_time | Integer | 否 | 302 跟随缓存跟随结果的超时时间，表示 CDN 在 302 跟随时缓存同 URL 的跟随结果的超时时间，需要配合缓存功能一起使用，单位秒，默认：3600 秒 | 7200 |
| follow_origin_host | String | 否 | 302 跟随回源 host 使用源站域名，当开启时，表示 CDN 会使用源站域名作为回源 host（即使主备切换也会使用最新的源站域名）。可以配置的值为： on：开启 off（默认）：关闭 | off |
| follow_5xx_retry_origin | String | 否 | 源站主备切换，当开启时，表示 CDN 如果收到源站响应的 5xx 状态码，会切换到下一个可用的源站。
