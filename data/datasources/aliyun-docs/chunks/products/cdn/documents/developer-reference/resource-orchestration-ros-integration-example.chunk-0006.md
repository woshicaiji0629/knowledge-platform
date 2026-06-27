ame" }, "CdnType": { "Ref": "CdnType" }, "TopLevelDomain": { "Ref": "TopLevelDomain" }, "Sources": { "Ref": "Sources" }, "Tags": { "Ref": "Tags" } } } }, "Outputs": { "DomainName": { "Description": "The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com.", "Value": { "Fn::GetAtt": [ "Domain", "DomainName" ] } }, "Cname": { "Description": "The CNAME generated for the CDN domain.You must add a CNAME record with your DNS provider to map the CDN domain name to the CNAME.", "Value": { "Fn::GetAtt": [ "Domain", "Cname" ] } } } }
单击下一步，执行操作栈。
在配置参数页面配置参数，单击创建。
输出结果。
资源栈的状态显示为创建成功，状态描述为Stack CREATE completed successfully，表示资源栈已成功创建。
创建完成后，您可以通过OpenAPI、SDK或者在CDN控制台，可以查看到。
在CDN控制台的域名管理页面中，可以看到新添加的加速域名，其状态显示为正常运行，CNAME状态为已配置。
该文章对您有帮助吗？
反馈
