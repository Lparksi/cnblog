---
title: 并查集
date: 2025-07-01 15:43:08
tags:
  - 并查集
categories:
  - 算法
sticky: 
thumbnail: ""
excerpt: 介绍并查集，一种用于解决动态连通性问题的数据结构
cover: ""
expires:
---
Union Found aka DSU.
用于解决动态连通性问题。
最差时间复杂度(`UF 4`) 
`N + M lg* N` 近线性阶，效率很高。
## 构造
`UF uf(size);` 
复杂度 O(n)
## 方法

| 名称        | 参数      | 返回值类型 | 作用      |
| --------- | ------- | ----- | ------- |
| connected | int p,q | bool  | 检查是否连接  |
| UFunion   | int p,q | void  | 将两个节点连接 |
此处不使用 `union` 是为了避免与 `stdc++.h` 发生冲突。
## 原理
首先初始化一个大小为 `n` 的 `id数组` 表示最多有n种可能，即每个节点都是独立的。
如果要联通两个节点，就把这两个节点的 `id`  更新为一样的（例如要把 `a` 和 `b` 联通，就需要把所有 id 为 b 的节点都更新为 a） 
![](https://img0.parksi.top/ShareX/2025/02/%25gO9JwQS2FO.webp)

## 优化方法
### Lazy approach 懒处理
在合并时执行较少的操作，在查询时解读

相对于 `Version1` 把 `id` 视为森林。
*Union* `p,q` 使 p 成为 q 的子节点
![](https://img0.parksi.top/ShareX/2025/02/%259GBbIMBlLU.webp)
### Weight 加权（避免树劣化）
观察得到，树的高度越高，时间复杂度越劣，因此避免得到更高的树。
当两个树合并时，永远将大的树放在前面，小的树放在后面。

### path compression 路径压缩
将树扁平化，这会减少 `root` 函数回溯的次数，较少时间复杂度
只需要改动 root 函数，使其在找寻根节点的过程中将该子树直接移到上一层节点上。
经过加权和路径压缩优化后，UF的时间复杂度可以达到==近线性==。
```cpp
    int root(int i) {  
        while (i != id[i]) {  
            id[i] = id[id[i]];  
            i = id[i];  
        }  
        return i;  
    }
```
## 实现
Version 1
```cpp
class UF {  
  private:  
    vector<int> id;  
  public:  
    UF(int n) {  
        id.resize(n);  
        for (int i = 0; i < n; i++) id[i] = i;  
    }  
    bool connected(int p, int q) {  
        return id[p] == id[q];  
    }  
    void UFunion(int p, int q) {  
        int pid = id[p];  
        int qid = id[q];  
        for (int i = 0; i < id.size(); i++) {  
            if (id[i] == pid) id[i] = qid;  
        }  
    }  
};
```
Version 2 Lazy approach 优化
```cpp
class UF {  
  private:  
    vector<int> id;  
    int root(int i) {  
        while (i != id[i]) i = id[i];  
        return i;  
    }  
  public:  
    UF(int n) {  
        id.resize(n);  
        for (int i = 0; i < n; i++) id[i] = i;  
    }  
    bool connected(int p, int q) {  
        return root(p) == root(q);  
    }  
    void UFunion(int p, int q) {  
        int i = root(p);  
        int j = root(q);  
        id[i] = j;  
    }  
};
```
Version 3 Weight 优化
```cpp
class UF {  
  private:  
    vector<int> id;  
    vector<int> sz;  
    int root(int i) {  
        while (i != id[i]) i = id[i];  
        return i;  
    }  
  public:  
    UF(int n) {  
        id.resize(n);  
        sz.resize(n);  
        for (int i = 0; i < n; i++) id[i] = i, sz[i] = 1;  
    }  
    bool connected(int p, int q) {  
        return root(p) == root(q);  
    }  
    void UFunion(int p, int q) {  
        int i = root(p);  
        int j = root(q);  
        if (i == j) return;  
        if (sz[i] < sz[j]) {  
            id[i] = j;  
            sz[j] += sz[i];  
        } else {  
            id[j] = i;  
            sz[i] += sz[j];  
        }  
    }  
};
```
Version 4 path compression 路径压缩优化
```cpp
class UF {  
  private:  
    vector<int> id;  
    vector<int> sz;  
    int root(int i) {  
        while (i != id[i]) {  
            id[i] = id[id[i]];  
            i = id[i];  
        }  
        return i;  
    }  
  public:  
    UF(int n) {  
        id.resize(n);  
        sz.resize(n);  
        for (int i = 0; i < n; i++) id[i] = i, sz[i] = 1;  
    }  
    bool connected(int p, int q) {  
        return root(p) == root(q);  
    }  
    void UFunion(int p, int q) {  
        int i = root(p);  
        int j = root(q);  
        if (i == j) return;  
        if (sz[i] < sz[j]) {  
            id[i] = j;  
            sz[j] += sz[i];  
        } else {  
            id[j] = i;  
            sz[i] += sz[j];  
        }  
    }  
};
```

## 应用
- 动态联通性问题
- Kruskal 最小路问题
### Percolation 渗流
![](https://img0.parksi.top/ShareX/2025/02/%25KJpFf6tvTV.webp)
在图中，存在一条贯穿上下的白色路径即认为该图是渗流的
左侧是渗流的，右侧不是。
此处白色方块有概率 *p* 是打开的。
![](https://img0.parksi.top/ShareX/2025/02/%25OPSEEK4L8t.webp)
存在一个 `p` 使得渗流的可能性发生突变。

![](https://img0.parksi.top/ShareX/2025/02/%25QUXCNTUFP3.webp)
可以通过新增一个虚拟上根和一个虚拟下根，每次只需要检查这两个虚拟根是否连接就能判断是否渗流
#### 实际应用
- 电力
- 水流
- 社交网络
