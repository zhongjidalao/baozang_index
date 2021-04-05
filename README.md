## 宝藏值

[![GitHub stars](https://img.shields.io/github/stars/zhongjidalao/baozang_index)](https://github.com/zhongjidalao/baozang_index/stargazers)[![GitHub license](https://img.shields.io/github/license/zhongjidalao/baozang_index)](https://github.com/zhongjidalao/baozang_index/blob/master/LICENSE)

因为经常打开一个动漫就有一大堆人刷宝藏动漫，就像这个样子

<img src="https://s2.ax1x.com/2020/02/15/1zkung.png" width="60%"/>

我就想，既然这么多番都很宝藏，到底哪个更宝藏？所以我就写了个爬虫把弹幕爬下来，看看到底有多少个宝藏，然后顺便添加了一个词云的功能。

### 第三方库

- jieba
- wordcloud
- lxml

### 用法

<img src="https://s2.ax1x.com/2020/02/15/1zkZ1f.png"/>

直接运行程序，输入网址和视频的oid，oid号应该是B站视频的唯一编码，按f12找到list.so文件，后面带的就是oid。

<img src="https://s2.ax1x.com/2020/02/15/1zkec8.png"/>

### 词云展示

<img src="https://s2.ax1x.com/2020/02/15/1zkmjS.png"/>