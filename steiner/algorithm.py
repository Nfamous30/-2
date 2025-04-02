# -*- coding: utf-8 -*-
"""

"""
import queue
import numpy as np
import time
import json
from apiGraph import apiGraph
from steinerTree import STree
from steinerTree import SteinerTreeQueue

MAX_WEIGHT = 999

class MinimalSteinerTree:
    def __init__(self, graph, categories):
        self.graph = graph
        self.numOfNodes = graph.dimension
        self.categories = categories
        self.trees_dict = {}
        
    def run(self, keywords):
        '''
        寻找包含keywords的最小斯坦纳树，返回满足条件的最小斯坦纳树列表
        graph: 图的邻接矩阵
        keywords: 关键字的list
        categories: 各api包含的categories的list
        '''
        num_of_keywords = len(keywords)
        que = queue.PriorityQueue()
        res_que = queue.PriorityQueue()
        

        all_in = (1 << num_of_keywords) - 1
        
        for v in range(self.numOfNodes):
            #先查看v是否为包含keywords的节点，如果是存入队列
            keySet = self.calcKeySet(v, keywords, num_of_keywords)

            if keySet > 0:
                tree = STree(keySet, v)
                que.put(tree)
                self.addTree(v, tree)
#                print('first match:', v)
        
#        test_count = 0
        while not que.empty():
            tree = que.get()
#            print('=====dequeue:', tree.root, ',keySet:', tree.keySet, ',remain:', que.qsize())
            
            if tree.keySet == all_in:
                # res_que.put(tree)
                if res_que.qsize() < 100:
                    res_que.put(tree)
            #    print('test_count:', test_count)
                # return tree

            
            #grow 操作
            v = tree.root
            neighbors = self.graph.neighbors(v)
 
            for u in neighbors:
                t = self.getTree(u, tree.keySet)
                u_weight = MAX_WEIGHT if t is None \
                    else t.weight
                if (tree.weight + 1) < u_weight:
                    newTree = tree.grow(u, self.calcKeySet(u, keywords, num_of_keywords))
                    que.put(newTree)
                    self.addTree(u, newTree)
                    
                    #因为tree的根节点没变，所以不需要更新steiner_trees
            #merge操作
            trees = self.trees_dict.get(v)
            if trees is None:
                continue
            newTrees = [] #在遍历时直接添加新合并的树到字典会报错，
            #这里采用的方法是先保存下来，合并完再统一更新
            for key in trees.keys():
                t = trees[key]
            # for t in trees:
                if t.keySet & tree.keySet == 0:
                    union_keySet = t.keySet | tree.keySet
                    union_tree = self.getTree(v, union_keySet)
                    union_weight = MAX_WEIGHT \
                        if union_tree is None \
                        else union_tree.weight
                    
                    if t.weight + tree.weight - 1 < union_weight:
                        newTree = tree.merge(t)
                        que.put(newTree)
                        # print('=====enqueue merge:', newTree.root, ',keySet:', newTree.keySet, ',remain:', que.qsize())
                        newTrees.append(newTree)
            for t in newTrees:
                self.addTree(v, t)


        return res_que
        
    def calcKeySet(self, v, keywords, num_of_keywords):
        '''计算给定节点v包含的keywords对应的二进制位串'''
        category_set = set(self.categories[v])
        category_set = set(map(tuple, category_set))
            
        keySet = 0
        for i in range(num_of_keywords):
            if tuple(keywords[i]) in category_set:
                keySet |= (1 << i)
                
        return keySet
    
    def addTree(self, root, tree):
        ''' 添加新生成的树到steiner_trees词典 '''
        trees = self.trees_dict.get(root)
        
        if trees is None:
           # trees = []
           trees = {}
           self.trees_dict[root] = trees

        # trees.append(tree)
        trees[tree.keySet] = tree

        
    def getTree(self, root, keySet):
        '''获取指定根节点和keySet的树,没有返回None'''
        trees = self.trees_dict.get(root)
        
        if trees is None:
            return None

        # for t in trees:
        #     if t.keySet == keySet:
        #         return t
        # return None
        return trees.get(keySet)

def test():
    graph = apiGraph(json.load(open('../dataset/graph.json')))

    categories = json.load(open('../dataset/api_categories.json'))

    category_list = json.load(open('../dataset/category_list.json'))

    minimal_steiner = MinimalSteinerTree(graph, categories)

    count_options = [2, 3, 4, 5, 6]
    num_of_options = len(count_options)
    # keywords = ['England', 'Home Automation', 'Barcodes', 'Web Site Management', 'Metadata', 'Classifieds']

    keywords = ['England', 'Travel', 'Mapping', 'Hotels']
    begin = time.time()

    min_tree_queue = minimal_steiner.run(keywords)

    # if min_tree_queue is None:
    #     print('weight:%d, time:%fs' % (0, time.time() - begin))

    # print('weight:%d, time:%fs' % (min_tree.weight, time.time() - begin))
    # with open('../dataset/min_tree_que.json', 'w') as f:
    #     json.dump(min_tree_queue, f)
    while min_tree_queue.qsize()>0:
        temp_tree = min_tree_queue.get()
        temp_tree.display()

test()

def self_test():
    '''自己构造测试数据，检查算法运行是否正确'''
              #v1 v2 v3 v4 v5 v6 v7 v8 v9 v10v11v12v13v14
    matrix = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], #v1
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], #v2
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #v3
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], #v4
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], #v5
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], #v6
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #v7
              [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #v8
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0], #v9
              [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], #v10
              [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], #v11
              [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1], #v12
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1], #v13
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]  #v14
              ]
    graph = apiGraph(matrix)
    #category数据写在了文件中
    categories = []
    with open('../data/dataset/test_category.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line[:-1] #去除换行符
            fields = line.split('\t')
            categories.append(fields[1:])
            
    keywords = ['k1', 'k5']
    begin = time.time()
    minimal_steiner = MinimalSteinerTree(graph,  categories)
    min_tree = minimal_steiner.run(keywords)

    if min_tree is None:
        print('weight:%d, time:%fs' % (0, time.time() - begin))

    print('weight:%d, time:%fs' % (min_tree.weight, time.time() - begin))
    # weight, nodes = minimal_steiner.run(keywords)
    # print(min_tree.keyset)
    min_tree.display()
 
    
# self_test()