# import json

# api_titles = set()
# api_dict = json.load(open('../data/dataset/connected_api_dict.json'))
# print(len(api_dict))
# for api in api_dict:
#     api_titles.add(api)

from gensim.models import Word2Vec
import nltk

# 定义两个文本
text1 = "The Data API allows users to integrate their program with YouTube and allow it to perform many of the operations available on the website. It provides the capability to search for videos, retrieve standard feeds, and see related content. A program can also authenticate as a user to upload videos, modify user playlists, and more. This integration can be used for a variety of uses such as developing a web application allowing users to upload video to YouTube, or a device or desktop application that brings the YouTube experience to a new platform. The Data API gives users programmatic access to the video and user information stored on YouTube. This can be used to personalize a web site or application with the user's existing information as well as perform actions like commenting on and rating videos. This RESTful API provides responses in XML format"

text2 = "What was formerly the ECS - eCommerce Service - has been renamed the Product Advertising API. Through this API developers can retrieve product information. The API exposes Amazon's product data and e-commerce functionality. This allows developers, web site publishers and others to leverage the Amazon Product Discovery features that Amazon uses to power its own business, and potentially make money as an Amazon affiliate. Additionally, the API has features allowing developers to advertise proucts, let users search for Amazon products and help users discover Amazon products. Both REST and SOAP APIs are provided, this profile is for the REST API"

# 将文本分成单词
tokens1 = nltk.word_tokenize(text1)
tokens2 = nltk.word_tokenize(text2)

# 训练Word2Vec模型
model = Word2Vec([tokens1, tokens2], min_count=1)

# 计算两个文本的语义相似度
similarity = model.wv.n_similarity(tokens1, tokens2)

print("语义相似度：", similarity)
        