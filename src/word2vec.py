from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 加载预训练的Word2Vec模型
import gensim.downloader as api

# 加载预训练模型
model = api.load('word2vec-google-news-300')

# 定义两个文本
text1 = "The Data API allows users to integrate their program with YouTube and allow it to perform many of the operations available on the website. It provides the capability to search for videos, retrieve standard feeds, and see related content. A program can also authenticate as a user to upload videos, modify user playlists, and more.\nThis integration can be used for a variety of uses such as developing a web application allowing users to upload video to YouTube, or a device or desktop application that brings the YouTube experience to a new platform. The Data API gives users programmatic access to the video and user information stored on YouTube. This can be used to personalize a web site or application with the user's existing information as well as perform actions like commenting on and rating videos. This RESTful API provides responses in XML format"
text2 = "What was formerly the ECS - eCommerce Service - has been renamed the Product Advertising API. Through this API developers can retrieve product information. The API exposes Amazon's product data and e-commerce functionality. This allows developers, web site publishers and others to leverage the Amazon Product Discovery features that Amazon uses to power its own business, and potentially make money as an Amazon affiliate. Additionally, the API has features allowing developers to advertise proucts, let users search for Amazon products and help users discover Amazon products. Both REST and SOAP APIs are provided, this profile is for the REST API"

# 分词并去除停用词
stopwords = ["a", "an", "the", "and", "or", "with", "to", "of", "in", "on"]
tokens1 = [token for token in text1.lower().split() if token not in stopwords]
tokens2 = [token for token in text2.lower().split() if token not in stopwords]

# 将单词向量相加，得到文本向量
vector1 = np.mean([model.get_vector(token) for token in tokens1], axis=0)
vector2 = np.mean([model.get_vector(token) for token in tokens2], axis=0)

# 计算余弦相似度
similarity = cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))[0][0]
print("相似度：", similarity)

