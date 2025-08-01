---
title: 在校大学生如何获取 Jetbrains 免费教育授权
date: 2025-07-22 13:46:42
tags:
  - Jetbrains
categories:
  - 正版软件
sticky: 
thumbnail: ""
excerpt: Jetbrains是著名的IDE开发公司，旗下有IDEA、pycharm等广受好评的IDE，作为大学生可以免费申请其授权。
cover: ""
expires: 
mathjax: false
---
## 背景
Jetbrains 是著名的IDE开发公司，旗下有IDEA、pycharm等广受好评的IDE，作为大学生可以免费申请其教育授权。
## 方式

前往 [申请页面](https://www.jetbrains.com/shop/eform/students) ，通过人机验证后，使用 大学电子邮件地址 方式验证身份。
随后在校期间均可免费获取其授权，只需要在每年点击邮箱内的续费链接即可。

## 学校域名不被认可？

Jetbrains 的域名验证存放于[JetBrains/swot](https://github.com/JetBrains/swot)仓库，可以像该仓库提交 PR 来让自己的学校被许可。

域名以 txt 格式逆序存放于 lib/domains 文件夹内
例如，我校学生域名 **stu.aynu.edu.cn** 即需要在 */lib/domains/cn/edu/aynu/* 路径下创建一个名为 stu.txt 的文件，文件内写上学校的官方名称（中英文均可）
![reop pic](https://img0.parksi.top/ShareX/2025/07/chrome_odea8vos9u.webp)
可以参考 PR： [https://github.com/JetBrains/swot/pull/26610](https://github.com/JetBrains/swot/pull/26610)
