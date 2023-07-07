jieba
======
安装
----
pip3 install jieba

分词的三种常见模式
---------------
jieba.lcut(s) 精确模式，返回一个列表类型，一般分词就用这个方法 
jieba.lcut(s, cut_all=True) 全模式，返回一个列表类型 
jieba.lcut_for_search(s) 搜索引擎模式，返回一个列表类型 
