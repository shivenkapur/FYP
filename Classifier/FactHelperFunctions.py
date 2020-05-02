#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import en_core_web_sm
nlp = en_core_web_sm.load()
#import en_core_web_md
#nlp = en_core_web_md.load()

import json


def inDataset(dataset, item):
    for x in dataset:
        if x.lower()==item.lower():
            return True
    return False

def inList(dataset, item):
    for x in dataset:
        if x[0]==item:
            return True
    return False

def inList2(dataset, item):
    for x in dataset:
        if x==item:
            return True
    return False

def inList3(dataset, item):
    for x in dataset:
        if x[0]==item[0]:
            return True
    return False

def takeFirst(elem):
        return elem[0]
def takeSecond(elem):
        return elem[1]
def takeThird(elem):
        return elem[2]
def takeFourth(elem):
        return elem[3]
    
def compareElements(item1, item2, n):
    result = True
    for i in range(n):
        if item1[i]!=item2[i]:
            result = False
            break
    return result
    
def compareLists(list1, list2, n):
    change_list = []
    #print(len(list1))
    if len(list1)==len(list2):
        for i in range(len(list1)):
            if not(compareElements(list1[i], list2[i], n)):
                found = False
                for j in range(len(list2)):
                    if compareElements(list1[i], list2[j], n):
                        change_list.append([list1[i],i-j])
                        #print(list1[i], i, j)
                        found = True
                        break
                if found==False:
                    change_list.append([list1[i], "NA -" + str(len(list1)-i)])
    return change_list

def termSimilarities(term, nouns_list, verbs_list, model, num=3):
    print(term)
    term_list = []
    for verb in verbs_list:
            similarity = abs(model.similarity(term,verb))
            term_list.append([verb,similarity])
            #print(verb,similarity)
    for noun in nouns_list:
            similarity = abs(model.similarity(term,noun))
            term_list.append([noun,similarity])
    
    
    
    term_list.sort(key=takeSecond, reverse=True)
    
    #for x in term_list:
        #print(x)
        
    
    max_value = -1
    max_verb = ""
    for verb in verbs_list:
            similarity = abs(model.similarity(term, verb))
            if similarity>max_value:
                max_value = similarity
                max_verb = verb
    
    max_value = -1
    max_noun = ""
    for noun in nouns_list:
            similarity = abs(model.similarity(max_verb ,noun))
            if similarity>max_value:
                max_value = similarity
                max_noun = noun
                
    print(term, max_verb, max_noun)
    
    
    
    #term = "computer science"
    #term = "scientist"
    #num = 4
    
    max_verb_list = []
    for verb in verbs_list:
            similarity = abs(model.similarity(term, verb))
            max_verb_list.append([verb,similarity])
    max_verb_list.sort(key=takeSecond, reverse=True)
    
    print(max_verb_list)
    
    max_noun_list = []
    for i in range(num):
        max_noun_list.append([])
    
    for noun in nouns_list:
        for i in range(num):
            similarity = abs(model.similarity(max_verb_list[i][0] ,noun))
            max_noun_list[i].append([noun,similarity])
    
         
    for i in range(num):
        max_noun_list[i].sort(key=takeSecond, reverse=True)
        for j in range(num):
            print(term, max_verb_list[i],max_noun_list[i][j])
    


def getCombinations(model, nouns_list, verbs_list):
    #print("------------  Embedding ------------")
    
    #Noun X Verb
    nv_matrix = []
    
    max_nv_list =[]
    
    for noun in nouns_list:
        temp =[]
        #print(noun)
        for verb in verbs_list:
            similarity = abs(model.similarity(noun,verb))
            temp.append(similarity)
            if noun!=verb:
                max_nv_list.append([noun,verb,similarity])
            #print(noun,verb,similarity)
            #print(verb,similarity)
        nv_matrix.append(temp)
        
    
    #for line in nv_matrix:
        #print(line)
    #print(nv_matrix)
    """
    max_value = -1
    max_index =[-1,-1]
    for n in range(len(nouns_list)):
        for v in range(len(verbs_list)):
            if nv_matrix[n][v]>max_value and nouns_list[n]!=verbs_list[v]:
                max_value = nv_matrix[n][v]
                max_index = [n, v]
            
    print(nouns_list[max_index[0]], verbs_list[max_index[1]])
    """
    
    max_nv_list.sort(key=takeThird, reverse=True)
    
    #for i in range(20):
        #print(max_nv_list[i])
            
    #print("")
    #print("")
    
    # Verb X Verb
    vv_matrix = []
    
    max_vv_list =[]
    
    for verb1 in verbs_list:
        for verb2 in verbs_list:
            similarity = abs(model.similarity(verb1,verb2))
            temp.append(similarity)
            if verb1!=verb2:
                max_vv_list.append([verb1,verb2,similarity])
            #print(verb1,verb2,similarity)
            #print(verb2,similarity)
        
    #for line in vv_matrix:
        #print(line)
    #print(nv_matrix)
    """
    max_value = -1
    max_index =[-1,-1]
    for v1 in range(len(verbs_list)):
        for v2 in range(len(verbs_list)):
            if vv_matrix[v1][v2]>max_value and v1!=v2:
                max_value = vv_matrix[v1][v2]
                max_index = [v1, v2]
            
    print(verbs_list[max_index[0]], verbs_list[max_index[1]])
    """
    max_vv_list.sort(key=takeThird, reverse=True)
    
    new_max_vv_list = []
    for i in range(40):
        if i%2==0:
            new_max_vv_list.append(max_vv_list[i])
            
            
    max_nvn_list = []
    
    for noun1 in nouns_list:
        for verb in verbs_list:
            for noun2 in nouns_list:
                if (noun1!=noun2 and noun1!=verb and verb!=noun2):
                    similarity1 = abs(model.similarity(noun1,verb))
                    similarity2 = abs(model.similarity(verb,noun2))
                    similarity = similarity1 * similarity2
                    max_nvn_list.append([noun1, verb, noun2, similarity])
            
    max_nvn_list.sort(key=takeFourth, reverse=True)        
    
    new_max_nvn_list = []
    for i in range(40):
        if i%2==0:
            new_max_nvn_list.append(max_nvn_list[i])
    
    return [max_nv_list, new_max_vv_list, new_max_nvn_list]


def getSpaCyCombinations(nouns_list, verbs_list):
    #print("------------  Embedding ------------")
    
    #Noun X Verb
    
    max_nv_list =[]
    
    for noun in nouns_list:
        for verb in verbs_list:
            dn = nlp(noun)
            dv = nlp(verb)
            similarity = dn[0].similarity(dv[0])
            #similarity = 1-spatial.distance.cosine(embedded_matrix[noun[1]-1][0],embedded_matrix[verb[1]-1][0])
            if noun!=verb:
                max_nv_list.append([noun,verb,similarity])
    
    max_nv_list.sort(key=takeThird, reverse=True)
    
    
    vv_matrix = []
    
    max_vv_list =[]
    
    for verb1 in verbs_list:
        for verb2 in verbs_list:
            dv1 = nlp(verb1)
            dv2 = nlp(verb2)
            similarity = dv1[0].similarity(dv2[0])
            if verb1!=verb2:
                max_vv_list.append([verb1,verb2,similarity])
        #vv_matrix.append(temp)
        
    
    max_vv_list.sort(key=takeThird, reverse=True)
    
    new_max_vv_list = []
    for i in range(40):
        if i%2==0:
            new_max_vv_list.append(max_vv_list[i])
            
            
    max_nvn_list = []
    
    for noun1 in nouns_list:
        for verb in verbs_list:
            for noun2 in nouns_list:
                if (noun1!=noun2 and noun1!=verb and verb!=noun2):     
                    dn1 = nlp(noun1)
                    dv = nlp(verb)
                    dn2 = nlp(noun2)
                    similarity1 = dn1[0].similarity(dv[0])
                    similarity2 = dv[0].similarity(dn2[0])
                    similarity = similarity1 * similarity2
                    max_nvn_list.append([noun1, verb, noun2, similarity])
            
    max_nvn_list.sort(key=takeFourth, reverse=True)        
    
    new_max_nvn_list = []
    for i in range(40):
        if i%2==0:
            new_max_nvn_list.append(max_nvn_list[i])
    
    return [max_nv_list, new_max_vv_list, new_max_nvn_list]



def termHypergraphs(model, total, tree_word_terms, tree_num, compare_terms):
    tree_word_list = [[],[],[]]
    i=0
    for term in tree_word_terms:
        for word in total:
            tree_word_list[i].append([word, abs(model.similarity(term,word))])
            #tree_word_list[i].append([word, model.similarity(term,word)])
        i=i+1
        
    
    for i in range(tree_num):
        print(tree_word_terms[i])
        tree_word_list[i].sort(key=takeSecond, reverse=True)
        for x in tree_word_list[i][:10]:
            print(x)
        
    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for x in tree_word_list[0][:10]:
        if inList(tree_word_list[1][:10], x[0]):
            if inList(tree_word_list[2][:10], x[0]):
                list1.append(x[0])
            else:
                list2.append(x[0])
        elif inList(tree_word_list[2][:10], x[0]):
            list4.append(x[0])
    
    for x in tree_word_list[1][:10]:
        if not(inList2(list1, x[0])):
            if inList(tree_word_list[2][:10], x[0]):
                list3.append(x[0])
    
    print(" ------ List 1 ------")
    for x in list1:
        print(x)
    
    print(" ------ List 2 ------")
    for x in list2:
        print(x)
        
    print(" ------ List 3 ------")
    for x in list3:
        print(x)
        
    print(" ------ List 4 ------")
    for x in list4:
        print(x)
        
    for com_word in compare_terms:
        print(com_word + " -->")

        term_list = []
        for word in total:
            term_list.append([word, abs(model.similarity(com_word, word))])
            #term_list.append([word, model.similarity(com_word, word)])
        
        term_list.sort(key=takeSecond, reverse=True)
            
        for term in tree_word_terms:
            i=1
            for x in term_list:
                if x[0]==term:
                    break
                i = i + 1
                
            print(term, abs(model.similarity(term, com_word)), ", Rank: " + str(i))
        
        
        
        print(" ")
        #for x in term_list[:10]:
            #print(x[0],x[1])
            
    print("Total ", len(term_list))
        
            
    """
    print("Erik -->")
    for term in tree_word_terms:
        print(term, abs(model.similarity(term,"erik")))
    
    print(" ")
    term_list = []
    for word in total:
        term_list.append([word, abs(model.similarity("erik",word))])
    
    term_list.sort(key=takeSecond, reverse=True)
    for x in term_list[:20]:
        print(x)
    """
    
def saveToFile(filename, data):
    f = open(filename, "w")
    for line in data:
        f.write(line)
        f.write("\n")
    f.close()
    
def saveToJson(filename, data):
    with open(filename, 'w') as outfile: 
        for line in data:
            json.dump(line, outfile)