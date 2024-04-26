import json
from efficient_apriori import apriori
import matplotlib.pyplot as plt
import numpy as np

    
#数据预处理

#cit-HepTh预处理
#构建稀疏矩阵
def edge2Matrix(fpath="../autodl-tmp/cit-HepTh.txt"):
    #构建稀疏图
    graph=dict()
    nodes=set()
    with open(fpath,"r") as f:
        edges=f.readlines()[4:]
        for edge in edges:
            nodes=edge.split('\t')
            fromnode,tonode=nodes[0],nodes[1][:-1]
            graph[fromnode]=graph.get(fromnode,[])
            graph[fromnode].append(tonode)

    #保存数据
    with open('../autodl-tmp/cit-HepTh.json','w') as out:
        json.dump(graph,out)
    print("finished!")
    return

def loadMatrix(fpath="../autodl-tmp/cit-HepTh.json"):        
    #加载数据
    with open(fpath,'r') as f:
        data_json=json.load(f)
        dataset=[]
        for key in data_json.keys():
            dataset.append(data_json[key])
    print("finished!")
    return dataset
    
#Yelp预处理
def yelpcategory(path="./yelp_academic_dataset_business.json",condition="True"):
    yelpdata=[]
    with open(path,'r') as f:
        datas=f.read().split('\n')
        for data in datas[:-1]:
            data=json.loads(data)
            if data['categories'] is not None and "Restaurants" in data["categories"] and (eval(condition)):
                clist=data['categories'].split(', ')
                clist.remove("Restaurants")     #不分析Restaurant类别
                yelpdata.append(clist)
    print('finished!')
    return yelpdata
    

    
#数据可视化分析    

#频繁项集
def showFreqItemSet(FreqItemSet,totals,title="",xlabel="support",ylabel="FreqItem"):
    dic=dict()
    for k in FreqItemSet:
        for item in FreqItemSet[k]:
            dic[item]=FreqItemSet[k][item]
    lis=sorted(dic.items(),key=lambda item:item[1])
    x=[i[1]/totals for i in lis]
    y=[str(i[0]) for i in lis]
    plt.barh(y,left=0, height=0.5, width=x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return
    
#关联规则
def showRules(rules,title="",xlabel="confidence",ylabel="Rules"):
    rules=sorted(rules,key=lambda item:item.confidence)
    x=[i.confidence for i in rules]
    y=[str(i.lhs)+'->'+str(i.rhs) for i in rules]
    plt.barh(y,left=0, height=0.5, width=x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return
