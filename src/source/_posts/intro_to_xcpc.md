---
title: 如何入门程序设计竞赛
date: 2025-06-30 17:57:21
tags:
  - 入门
  - 蓝桥杯
  - 天梯赛
  - XCPC
  - 百度之星
categories:
  - 教程
sticky: 
thumbnail: 
excerpt: 本文为程序设计竞赛学习指南，涵盖从入门到进阶的完整路径。内容包括必备学习态度、推荐软件工具（如Dev-C++）、高质量学习资源（OI-Wiki、洛谷、牛客、Codeforces等）及刷题策略。文章介绍C++ STL使用、高频考点知识树（队列、栈、排序、图论等），并提供各平台使用方法与比赛技巧。附带标准C++模板，帮助选手高效备战各类赛事，适合新手和进阶选手参考学习。
cover: 
expires:
---

## 准备
首先要端正态度，除了少部分天赋异鼎的天才以外，大部分选手都需要巨量的练习，这意味着你需要牺牲自己的一部分娱乐和休息时间进行高强度的训练。平时训练时也不能过度依赖AI，赛时是肯定不给你用AI的。
软件方面，建议使用 Devc++ 5.11，大部分赛站都会提供这个软件，能够满足你基本的编译运行需求。
## 知识平台
- [OI-Wiki](https://oi-wiki.org/) 程序设计竞赛的百科全书，在上面有大量的算法和解析
- [Hello 算法](https://www.hello-algo.com/) 绘图精美，详细解析几个基础的数据结构和算法，对入门有帮助
- [cppreference](https://cppreference.cn/w/) 查询 C/C++ 函数的具体定义和实现，算竟只用到其中很小一部分
## 刷题平台
- [洛谷](https://www.luogu.com.cn/) 中国最大的刷题网站，有完善的知识点分类和难度分类，题解丰富，适合刷知识点
- [牛客](https://ac.nowcoder.com/) 经常举办高质量比赛，每周都有牛客周赛，适合新手参与，难度相对较低，结束后在 B站有视频讲解
- [Codeforces](https://codeforces.com/) 世界最大的刷题网站，主要锻炼思维，比赛时间一般在晚上10点半-12点半，纯英文题目，有文字解析
- [Atcoder](https://atcoder.jp/) Atcoder的ABC(AtCoder Beginner Contest) 经常会出经典题，时间在晚上8点-9点40，纯英文题目，有文字解析
- [Vjudge](https://vjudge.net/)Vjudge并不是刷题平台，但它能抓取其他平台的题目并免费翻译，里面也有一些高质量题单
## 书籍
- 洛谷的 深入浅程序设计竞赛（基础篇/进阶篇），经典例题，可配合题单 [https://vjudge.net/article/4196](https://vjudge.net/article/4196) 使用
- 俞勇的 算法竞赛
- 挑战程序设计竞赛
没有必要非要卖一本书，网络上也有很多高质量资源。
## 怎么学

![知识树](https://img1.parksi.cn/ShareX/2025/06/pItA2phQp3.webp)
常用算法/数据结构：队列，栈，二叉堆（优先队列），哈希表，排序，简单贪心思想，前缀和，差分，字符串，图论基础，并查集，bfs，dfs，最短路，dijkstra堆优化，快速幂，位运算，倍增，简单构造算法，st表，三分，高精度，单调栈，单调队列，树状数组，线段树。
### 学C++的STL
这里注意到一个问题，像栈这样的数据结构，它的功能是确定的，如果使用C语言每次都要自己实现，但C++提供了STL库，其中包含了很多基础数据结构，能够直接拿来用。
[OI-Wiki介绍](https://oi-wiki.org/lang/csl/)，但不要有心理负担，C是C++的子集，所有C语言的代码在C++依然成立，但C++提供了更多方便的扩展功能，文章的结尾会给出一个C++标准模板。
### 高频基础考点
队列，栈，二叉堆（优先队列），哈希表，排序，简单贪心思想，前缀和，差分，字符串，图论基础，并查集，bfs，dfs，最短路，dijkstra堆优化，快速幂，高精度这些都算是比较高频的考点，要先学会这些知识点，一般的流程是在 OI-Wiki 上学这个知识点的理论和实现然后到洛谷去刷这个知识点的题目（从简单开始刷），不会做的看题解。
### 尽早开始刷题
不要觉得自己什么都不会就不去参加比赛，建议新手至少每周都要参与牛客周赛和ABC，这两类比赛都是着重考察基础知识点的，随着练习量的提高，进步也会很明显。随后就要积极参与CF的比赛。
## 各平台怎么用
首先建议大家使用系统自带的 Edge 浏览器
### Codeforces
官网：[Codeforces](https://codeforces.com/)
#### 比赛

| 名称                           | 难度                  |              |
| ---------------------------- | ------------------- | ------------ |
| Codeforces Round Div 1,2,3,4 | 数字越大越简单             | 新手简易先刷DIv4和3 |
| Educational Codeforces Round | 一般对标Div2，但稍微简单，会出典题 | 建议做          |

#### 插件
##### CF better
CF是英文网站，CF better可以提供界面和内容的汉化
首先安装 篡改猴，这是用户脚本的管理器
使用 Edge 浏览器打开 [篡改猴 - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/%E7%AF%A1%E6%94%B9%E7%8C%B4/iikmkjmpaadaobahmlepeloendndfphd) 点击右侧的获取
![篡改猴的安装](https://img1.parksi.cn/ShareX/2025/06/%25kloxr26Iom.webp)
安装之后还需要打开 开发人员模式才能使脚本生效
找到扩展-管理扩展或在地址栏输入 `edge://extensions/` 打开开发人员模式
点击此链接安装脚本 ：[https://greasyfork.org/zh-CN/scripts/465777-codeforces-better](https://greasyfork.org/zh-CN/scripts/465777-codeforces-better)
如果打不开可以使用 [ https://ghfast.top/https://github.com/beijixiaohu/OJBetter/raw/main/script/release/codeforces-better.user.js](https://ghfast.top/https://github.com/beijixiaohu/OJBetter/raw/main/script/release/codeforces-better.user.js)
再次进入Codeforces即可显示CF better页面

![](https://img1.parksi.cn/ShareX/2025/06/%25QoKNIBDcXG.webp)


#### 功能
![](https://img1.parksi.cn/ShareX/2025/06/%25q3y0D3YrrU.webp)
在右上角进行登录和注册，比赛中有CF未来和过去的比赛，训练营有往年XCPC真题

随便进入一场比赛，点击题目即可查看题目，提交代码时选择的编译器一般为G++，右下角的小框就是翻译工具，点击即可翻译那个方格的内容，当然更推荐点击题目里的Vjudge跳转，Vjudge的翻译一般更好（当然以原文为准，Vjudge也能可能出错），点击榜单可以查看当期榜单。
![](https://img1.parksi.cn/ShareX/2025/06/%25db2BBDZCDo.png)
![](https://img1.parksi.cn/ShareX/2025/06/%25pr4Y6qekWA.webp)

### Atcoder
官网：[https://atcoder.jp/](https://atcoder.jp/)
和CF一样，Atcoder也有翻译插件
[https://greasyfork.org/zh-CN/scripts/471106-atcoder-better](https://greasyfork.org/zh-CN/scripts/471106-atcoder-better)
[https://ghfast.top/https://github.com/beijixiaohu/OJBetter/raw/main/script/release/atcoder-better.user.js](https://ghfast.top/https://github.com/beijixiaohu/OJBetter/raw/main/script/release/atcoder-better.user.js)
![](https://img1.parksi.cn/ShareX/2025/06/%252SFE4lmQP8.webp)
首页会显示即将进行的比赛，和CF不同的是，Atcoder如果报名没做的话也是会扣分的。剩下的和CF差不多
### 牛客
官网：[牛客竞赛OJ_ACM/NOI/CSP/CCPC/ICPC_信息学编程算法训练平台](https://ac.nowcoder.com/)
先做牛客周赛、小白月赛和各高校的校赛（群里一般都会转发）
中文题面没啥好说的，官方比赛结束后会在B站上传视频解析

### 洛谷
官网：[https://www.luogu.com.cn/](https://www.luogu.com.cn/)
点击左侧题库可以筛选知识点和难度进行刷题![](https://img1.parksi.cn/ShareX/2025/06/%25e7Zr0XGoUh.webp)
题目题解非常丰富

### Vjudge
官网：[https://vjudge.net/](https://vjudge.net/)
![](https://img1.parksi.cn/ShareX/2025/06/%25cxW4YcqAv3.webp)
一般使用插件跳转过来，需要登录才能查看翻译，选择左侧的Deepseek_zh或者Chatgpt-zh查看翻译。

## 一般题目结构
```cpp
// 引入标准头文件，包含大部分常用 STL 容器和算法  
#include <bits/stdc++.h>  
  
// 定义 endl 为换行符，通常用于输出后刷新缓冲区，原理是 \n 比 endl快，但在交互题中注意刷新缓冲区  
#define endl '\n'  
  
// 使用类型别名，将 long long 类型定义为 ll，便于书写大整数类型  
typedef long long ll;  
  
// 使用标准命名空间 std，避免每次调用标准库函数时都要加 std::  
using namespace std;  
  
  
// solve 函数是解决问题的核心逻辑所在  
// 用于像CF这样一个测试点有多组数据的情况  
void solve() {  
    }  
  
// 主函数 main 是程序的入口点  
signed main() {  
    // 提高输入输出效率：关闭 C 和 C++ 标准流的同步  
    // 这样可以加快程序运行速度，尤其在处理大量输入输出时  
    ios::sync_with_stdio(0);  
        // 解除 cin 和 cout 的绑定，进一步提升输入效率  
    cin.tie(0);  
        // 设置测试用例数量 T，默认为 1  
    int T = 1;  
        // 如果需要多组测试用例，可以取消下面这一行的注释，从输入读取 T 的值  
    // cin >> T;  
        // 循环执行 T 次 solve 函数  
    while (T--) {  
        solve();  
    }  
        // 程序正常结束，返回 0 表示成功退出  
    return 0;  
}
```
