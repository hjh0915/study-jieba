# -*- coding: utf-8 -*-

import jieba.analyse

seg_extract_tags = jieba.analyse.extract_tags("中国是一个伟大的国家，中国人人会越来越好！")
print(seg_extract_tags)

seg_extract_tags = jieba.analyse.extract_tags("中国是一个伟大的国家，中国人人会越来越好！", topK=3)
print(seg_extract_tags)

seg_extract_tags = jieba.analyse.extract_tags("中国是一个伟大的国家，中国人人会越来越好！", topK=5, withWeight=True)
print(seg_extract_tags)

seg_extract_tags = jieba.analyse.extract_tags("中国是一个伟大的国家，中国人人会越来越好！", topK=5, allowPOS=('n'))
print(seg_extract_tags)