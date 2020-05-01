#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:03:54 2019

@author: eshaankapur
"""

from FactHelperFunctions import *

import unicodedata
from scipy import spatial
import math
import ast


import gensim

import en_core_web_md
nlp = en_core_web_md.load()

system = "Android-Lollipop"


if system == "Turbonomics":
    f = open("Wordset_Turbonomics.txt","r")
    model = gensim.models.Word2Vec.load("Model_Turbonomics_dim1000_ep7")
    filenames = ["ReleaseNotes_6.3.1_e_hierarchy.txt", "ReleaseNotes_6.3.2_e_hierarchy.txt", "ReleaseNotes_6.3.3_e_hierarchy.txt", "ReleaseNotes_6.3.4_e_hierarchy.txt", "ReleaseNotes_6.3.5_e_hierarchy.txt", "ReleaseNotes_6.3.7_e_hierarchy.txt", 
             "Turbonomic_User_Guide_6.3.0_hierarchy.txt", "TargetConfiguration_6.3.0_hierarchy.txt", "TargetConfiguration_6.3.1_hierarchy.txt"]
    QnA = [["How do I add WMI targets?","['TargetConfiguration_6.3.x', '﻿Guest OS Process Targets', '﻿WMI', '﻿Adding WMI Targets']"], 
           ["Add HyperFlex Targets","['TargetConfiguration_6.3.x', 'Hyperconverged Targets', 'Cisco HyperFlex', 'Adding HyperFlex Targets']"], 
           ["How do I set up the SMI-S provider in HPE 3PAR?","['TargetConfiguration_6.3.x', 'Storage Targets', '﻿HPE 3PAR', '﻿Setting Up the SMI-S Provider']"], 
           ["How to set up Application containers?","['TargetConfiguration_6.3.0_hierarchy.txt', 'Application Container Targets', 'Setting Up Application Containers Managed By  Kubernetes']"], 
           ["set up a deployment","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Place: Reserve and Deploy Workload', 'Setting Up a Deployment']"], 
           ["How can I view a report?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Reports: Viewing Historical Data', 'Viewing Reports']"], 
           ["Steps for updating the tomcat server","['ReleaseNotes_6.3.x_e_hierarchy.txt', 'Turbonomic 6.3.1 Release Notes', 'Configuration Requirements', 'Updating the Tomcat Server']"], 
           ["what does hybrid view present ?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'The Home Page', 'Hybrid View']"], 
           ["Hybrid view in the Home page ","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'The Home Page', 'Hybrid View']"], 
           ["How to enable SNMP?","['TargetConfiguration_6.3.0_hierarchy.txt', 'Guest OS Process Targets', 'SNMP', 'Enabling SNMP']"], 
           ["What are the steps in creating plan scenarios?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Plans: Looking to the Future', 'Setting Up User Plan Scenarios', 'Creating Plan Scenarios']"], 
           ["What can I see on action charts?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Dashboards: Focused Views', 'Chart Types', 'Actions and Impact Chart Types', 'Action Charts']"]]
    
elif system == "faq":
    f = open("Wordset_faq.txt","r")
    model = gensim.models.Word2Vec.load("Model_faq_dim1000_ep7")
    filenames = ["faq_hierarchy.txt"]
    QnA = [["Why doesn't Python have with statement",""], 
           ["Does Python have with statement",""], 
           ["Can I delete Python",""], 
           ["How to copy an object","2.2.12 How do I copy an object in Python?"], 
           ["Is there a ternary operator in Python","2.2.16 Is there an equivalent of C’s “?:” ternary operator?"],
           ["What does slash in parameter list mean","2.2.18 What does the slash(/) in the parameter list of a function mean?"]]
    
    
elif system == "AppDynamics":
    f = open("Wordset_AppDynamics.txt","r")
    model = gensim.models.Word2Vec.load("Model_AppDynamics_dim1000_ep7")
    filenames = ["4.5.7-AppDynamics-Essentials-Suite-2-25-19_hierarchy.txt"]
    QnA = [["How to download AppDynamics software", "Download AppDynamics Software"],
           ["How to view License Usage", ""],
           ["How to start the Universal Agent Linux Service", ""],
           ["How to create a Universal Agent group", ""],
           ["How to view the Metric Browser", "Using the Metric Browser"],
           ["What are Policy triggers", "Policy Triggers"],
           ]
    
elif system == "Android-Lollipop":
    f = open("Wordset_Android-Lollipop.txt","r")
    model = gensim.models.Word2Vec.load("Model_faq_dim1000_ep7")
    filenames = ["Android-Lollipop-Quick-Start-Guide_hierarchy.txt"]
    
    QnA = [["How to send a text message","Send an SMS (text message) from your phone"],
           ["How to send a message",""],
           ["How to organize home screens","Organize your Home screens"],
           ["How to add an account on the device","Add an account"],
           ["How to make payments","Tap & pay"],
           ["What is Gmail","Gmail"],
           ["What is talk back","Accessibility"],
           ]
    
"""
QnA = [["What killed the indians?", "P73"], ["What led to the downfall of the Aztec culture?", "P51"], 
       ["Who was Charlemagne?", "P8/S42"], ["What was the capital of the Incan Empire?", "P54/S345?"],
       ["Who led the exploration to greenland?", "P10 / S58"], 
       ["Did the Aztecs perform human sacrifice?", "P50/S322-323"],
       ["Who was the Joan of Arc?", "P20"], 
       ["When was Rome founded?", "P5/S31"], 
       ["When did the Mayan civilization decline?", "P47/S305"], 
       ["How did contact with European culture affect the Mayans?", "P73"],
       ["who colonized North American Continent","P3/S24"],
       ["who colonized north america","P3/S24"],
       ["what are the causes of Mayan Culture Decline",""],
       ["When was Rome built?","P5/S31"], 
       ["When was city of Rome founded?","P5/S31"],
       ["When did Mayan culture see a decline?","P47/S305"],
       ["When did Mayan culture evolve into a complex civilization?", "P44/S295"],
       ["Why did Mayan Culture Decline?",""]]

QnA = [["How do I add WMI targets?","['TargetConfiguration_6.3.x', '﻿Guest OS Process Targets', '﻿WMI', '﻿Adding WMI Targets']"], 
       ["Add HyperFlex Targets","['TargetConfiguration_6.3.x', 'Hyperconverged Targets', 'Cisco HyperFlex', 'Adding HyperFlex Targets']"], 
       ["How do I set up the SMI-S provider in HPE 3PAR?","['TargetConfiguration_6.3.x', 'Storage Targets', '﻿HPE 3PAR', '﻿Setting Up the SMI-S Provider']"], 
       ["How to set up Application containers?","['TargetConfiguration_6.3.0_hierarchy.txt', 'Application Container Targets', 'Setting Up Application Containers Managed By  Kubernetes']"], 
       ["set up a deployment","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Place: Reserve and Deploy Workload', 'Setting Up a Deployment']"], 
       ["How can I view a report?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Reports: Viewing Historical Data', 'Viewing Reports']"], 
       ["Steps for updating the tomcat server","['ReleaseNotes_6.3.x_e_hierarchy.txt', 'Turbonomic 6.3.1 Release Notes', 'Configuration Requirements', 'Updating the Tomcat Server']"], 
       ["what does hybrid view present ?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'The Home Page', 'Hybrid View']"], 
       ["Hybrid view in the Home page ","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'The Home Page', 'Hybrid View']"], 
       ["How to enable SNMP?","['TargetConfiguration_6.3.0_hierarchy.txt', 'Guest OS Process Targets', 'SNMP', 'Enabling SNMP']"], 
       ["What are the steps in creating plan scenarios?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Plans: Looking to the Future', 'Setting Up User Plan Scenarios', 'Creating Plan Scenarios']"], 
       ["What can I see on action charts?","['Turbonomic_User_Guide_6.3.0_hierarchy.txt', 'Dashboards: Focused Views', 'Chart Types', 'Actions and Impact Chart Types', 'Action Charts']"]]


QnA = [["Why doesn't Python have with statement",""], 
       ["Does Python have with statement",""], 
       ["Can I delete Python",""], 
       ["How to copy an object","2.2.12 How do I copy an object in Python?"], 
       ["Is there a ternary operator in Python","2.2.16 Is there an equivalent of C’s “?:” ternary operator?"],
       ["What does slash in parameter list mean","2.2.18 What does the slash(/) in the parameter list of a function mean?"]]


QnA = [["How to download AppDynamics software", "Download AppDynamics Software"],
       ["How to view License Usage", ""],
       ["How to start the Universal Agent Linux Service", ""],
       ["How to create a Universal Agent group", ""],
       ["How to view the Metric Browser", "Using the Metric Browser"],
       ["What are Policy triggers", "Policy Triggers"],
       ]

QnA = [["How to send a text message","Send an SMS (text message) from your phone"],
       ["How to send a message",""],
       ["How to organize home screens","Organize your Home screens"],
       ["How to add an account on the device","Add an account"],
       ["How to make payments","Tap & pay"],
       ["What is Gmail","Gmail"],
       ["What is talk back","Accessibility"],
       ]


#f = open("Wordset_Turbonomics.txt","r")
#f = open("Wordset_faq.txt","r")
f = open("Wordset_Android-Lollipop.txt","r")
#f = open("Wordset_ReleaseNotes_6.3.7.txt","r")
#print(word_set)

#model= gensim.models.Word2Vec.load("Model_faq_dim1000_ep7")
model= gensim.models.Word2Vec.load("Model_AppDynamics_dim1000_ep7")
model= gensim.models.Word2Vec.load("Model_Android-Lollipop_dim1000_ep7")
#model= gensim.models.Word2Vec.load("ReleaseNotes_6.3.7_model")
    
filenames = ["ReleaseNotes_6.3.1_e_hierarchy.txt", "ReleaseNotes_6.3.2_e_hierarchy.txt", "ReleaseNotes_6.3.3_e_hierarchy.txt", "ReleaseNotes_6.3.4_e_hierarchy.txt", "ReleaseNotes_6.3.5_e_hierarchy.txt", "ReleaseNotes_6.3.7_e_hierarchy.txt", 
             "Turbonomic_User_Guide_6.3.0_hierarchy.txt", "TargetConfiguration_6.3.0_hierarchy.txt", "TargetConfiguration_6.3.1_hierarchy.txt"]

filenames = ["faq_hierarchy.txt"]
filenames = ["4.5.7-AppDynamics-Essentials-Suite-2-25-19_hierarchy.txt"]
filenames = ["Android-Lollipop-Quick-Start-Guide_hierarchy.txt"]
"""

word_set = []
for line in f:
    word_set.append(line.replace("\n",""))
    
alpha = 0.5

document_json =[]
sentences_json =[]
    
dataset =[]
nouns_list = []
verbs_list = []

p=1
s=1



d=1


def formatText(contents):
    contents = contents.replace("\n\n", "!@#$%^&*()")
    contents = contents.replace("\n", " ")   
    contents = contents.replace("!@#$%^&*()", "\n\n") 
                                
    #contents = contents.replace("•", " ")
    #contents = contents.replace("◦", " ")
    
    return contents

def AddVectors(A,B):
    C = []
    if len(A) == len(B):
        for i in range(len(A)):
            C.append(A[i]+B[i])
        return C
    else:
        #print("Unequal Matrices")
        return []

def DivideVector(A,n):
    if n!=0:
        for i in range(len(A)):
            A[i] = A[i]/n
    return A

def CombineVectors(A,B,nA, nB):
    C = []
    if len(A) == len(B):
        for i in range(len(A)):
            C.append((nA*A[i])+(nB*B[i]))
        return C
    else:
        #print("Unequal Matrices")
        return []

def PrintTopic(topic, level):
    space = ""
    for i in range(0,level+1):
        space = space + "  "
    if level == -1:
        print(space + "-- Chapter: " + topic["Doc Heading"])
        space = space + "  "
        for para in topic["Paras"]:
            print(space + para)
        for subtopic in topic["Topics"]:
            PrintTopic(subtopic, level+1)
    else:
        try:
            print(space + "-- Topic lv"+ str(level) +": " + topic["Heading"])
        except:
            print(space + "-- Topic lv"+ str(level) +": " + topic["Doc Heading"])
        space = space + "  "
        for para in topic["Paras"]:
            print(space + para)
        try:  
            for subtopic in topic["Sub Topics"]:
                PrintTopic(subtopic, level+1)
        except:  
            for subtopic in topic["Topics"]:
                PrintTopic(subtopic, level+1)
    

def getChildrenText(topic):
    text = "" 
    try:
        text = topic["Heading"]
    except:
        text = topic["Doc Heading"]
    for para in topic["Paras"]:
        text = text + " " + para
    try:  
        for subtopic in topic["Sub Topics"]:
            temp_text = getChildrenText(subtopic)
            text = text + " " + temp_text
    except:  
        for subtopic in topic["Topics"]:
            temp_text = getChildrenText(subtopic)
            text = text + " " + temp_text
    return text
    


def getVectors(para, model):
    #print(para)
    doc = nlp(para)
           
    spacy_vector = doc.vector
    avg_vector = []
    nv_avg_vector = []
    nvp_avg_vector = []
    avg_vector2 = []
    nvpa_avg_vector = []
    
    noun_verb_vector = []
    noun_verb_term = ""
    noun_verb_pronoun_term = ""
    noun_verb_pronoun_adj_term = ""
    
    
    vector_list = []
    nv_vector_list = []
    nvp_vector_list = []
    vector_list2 = []
    nvpa_vector_list = []
    
    for token in doc:
        if (token.pos_=="PUNCT"):
            continue
        try:
            if (token.lemma_=="-PRON-"):
                if inDataset(word_set,token.text.lower()):
                    vector_list.append(model.wv.__getitem__(token.text.lower()))
                    vector_list2.append(model.wv.__getitem__(token.text.lower()))
            else:
                if inDataset(word_set,token.lemma_.lower()):
                    vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                    vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
            if (token.pos_=="NOUN" or token.pos_=="VERB" ): #or token.pos_=="PROPN"
                noun_verb_term = noun_verb_term + " " + token.text
                noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
                if inDataset(word_set,token.lemma_.lower()):
                    nv_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                    vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
                    nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                    nvpa_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
            elif token.pos_=="PROPN": #or 
                noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
                if inDataset(word_set,token.lemma_.lower()):
                    nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                    nvpa_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
            elif token.pos_=="ADJ":
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
                if inDataset(word_set,token.lemma_.lower()):
                    nvpa_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
        except:
            if (token.pos_=="NOUN" or token.pos_=="VERB" ): #or token.pos_=="PROPN"
                noun_verb_term = noun_verb_term + " " + token.text
                noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
            elif token.pos_=="PROPN": #or 
                noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
            elif token.pos_=="ADJ":
                noun_verb_pronoun_adj_term = noun_verb_pronoun_adj_term + " " + token.text
            #print("Model Exception: " + token.text)
        
        
    if vector_list != []:
        avg_vector = vector_list[0]
        for i in range(1,len(vector_list)):
            #avg_vector = avg_vector + vector_list[i]
            avg_vector = AddVectors(avg_vector, vector_list[i])
        avg_vector = [x / len(vector_list) for x in avg_vector]
    
    if nv_vector_list != []:
        nv_avg_vector = nv_vector_list[0]
        for i in range(1,len(nv_vector_list)):
            #nv_avg_vector = nv_avg_vector + nv_vector_list[i]
            nv_avg_vector = AddVectors(nv_avg_vector, nv_vector_list[i])
        #avg_vector = avg_vector /len(vector_list)
        nv_avg_vector = [x / len(nv_vector_list) for x in nv_avg_vector]
    
    if nvp_vector_list != []:
        nvp_avg_vector = nvp_vector_list[0]
        for i in range(1,len(nvp_vector_list)):
            #nvp_avg_vector = nvp_avg_vector + nvp_vector_list[i]
            nvp_avg_vector = AddVectors(nvp_avg_vector, nvp_vector_list[i])
        #avg_vector = avg_vector /len(vector_list)
        nvp_avg_vector = [x / len(nvp_vector_list) for x in nvp_avg_vector]
        
    if vector_list2 != []:
        avg_vector2 = vector_list2[0]
        for i in range(1,len(vector_list2)):
            #avg_vector2 = avg_vector2 + vector_list2[i]
            avg_vector2 = AddVectors(avg_vector2, vector_list2[i])
        #avg_vector = avg_vector /len(vector_list)
        avg_vector2 = [x / len(vector_list2) for x in avg_vector2]
    
    if nvpa_vector_list != []:
        nvpa_avg_vector = nvpa_vector_list[0]
        for i in range(1,len(nvpa_vector_list)):
            #nvp_avg_vector = nvp_avg_vector + nvp_vector_list[i]
            nvpa_avg_vector = AddVectors(nvpa_avg_vector, nvpa_vector_list[i])
        #avg_vector = avg_vector /len(vector_list)
        nvpa_avg_vector = [x / len(nvpa_vector_list) for x in nvpa_avg_vector]
    
    noun_verb_vector = nlp(noun_verb_term).vector
    noun_verb_pronoun_vector = nlp(noun_verb_pronoun_term).vector
    noun_verb_pronoun_adj_vector = nlp(noun_verb_pronoun_adj_term).vector
    
    result = {"Avg Vector": avg_vector, "Avg Vector2": avg_vector2,"Spacy Vector": spacy_vector, "NV Spacy Vector": noun_verb_vector, "NV Avg Vector": nv_avg_vector, 
              "NVP Spacy Vector": noun_verb_pronoun_vector, "NVP Avg Vector": nvp_avg_vector, "NVPA Spacy Vector": noun_verb_pronoun_adj_vector, "NVPA Avg Vector": nvpa_avg_vector}
    
    return result



def AddTopicData(topic, level, document, parents, parent_vectors):
    result =[]
    parent_text = ""
    """
    for x in parents:
        parent_text = parent_text + x + " "
    parent_text = parent_text + ". "
    """
    
    children_vectors = {"Avg Vector": [], "Avg Vector2": [],"Spacy Vector": [], "NV Spacy Vector": [], "NV Avg Vector": [], "NVP Spacy Vector": [], "NVP Avg Vector": []}
    #children_vectors = getVectors(getChildrenText(topic), model)
    
    
    if level == -1:
        #print(space + "-- Chapter: " + topic["Doc Heading"][:100])
        temp_result = getVectors(parent_text + topic["Doc Heading"], model)
        #result.append({"Document":document, "Parents": parents + [topic["Doc Heading"]], "Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"]})
        result.append({"Text": topic["Doc Heading"], "Document":document, "Parents": parents + [topic["Doc Heading"]], "Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"], "NVPA Spacy Vector": temp_result["NVPA Spacy Vector"], "NVPA Avg Vector": temp_result["NVPA Avg Vector"], 
                       "Parent Avg Vector": temp_result["Avg Vector"], "Parent Avg Vector2": temp_result["Avg Vector2"],"Parent Spacy Vector": temp_result["Spacy Vector"], "Parent NV Spacy Vector": temp_result["NV Spacy Vector"], "Parent NV Avg Vector": temp_result["NV Avg Vector"], "Parent NVP Spacy Vector": temp_result["NVP Spacy Vector"], "Parent NVP Avg Vector": temp_result["NVP Avg Vector"],
                       "Children Avg Vector": children_vectors["Avg Vector"], "Children Avg Vector2": children_vectors["Avg Vector2"],"Children Spacy Vector": children_vectors["Spacy Vector"], "Children NV Spacy Vector": children_vectors["NV Spacy Vector"], "Children NV Avg Vector": children_vectors["NV Avg Vector"], "Children NVP Spacy Vector": children_vectors["NVP Spacy Vector"], "Children NVP Avg Vector": children_vectors["NVP Avg Vector"]})
        
        current_vectors = {"Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"]}
        
        for para in topic["Paras"]:
            #print(space + para[:100])
            temp_result = getVectors(parent_text + para, model)
            result.append({"Text": para, "Document":document, "Parents": parents + [topic["Doc Heading"]], "Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"], "NVPA Spacy Vector": temp_result["NVPA Spacy Vector"], "NVPA Avg Vector": temp_result["NVPA Avg Vector"], 
                       "Parent Avg Vector": temp_result["Avg Vector"], "Parent Avg Vector2": temp_result["Avg Vector2"],"Parent Spacy Vector": temp_result["Spacy Vector"], "Parent NV Spacy Vector": temp_result["NV Spacy Vector"], "Parent NV Avg Vector": temp_result["NV Avg Vector"], "Parent NVP Spacy Vector": temp_result["NVP Spacy Vector"], "Parent NVP Avg Vector": temp_result["NVP Avg Vector"],
                       "Children Avg Vector": temp_result["Avg Vector"], "Children Avg Vector2": temp_result["Avg Vector2"],"Children Spacy Vector": temp_result["Spacy Vector"], "Children NV Spacy Vector": temp_result["NV Spacy Vector"], "Children NV Avg Vector": temp_result["NV Avg Vector"], "Children NVP Spacy Vector": temp_result["NVP Spacy Vector"], "Children NVP Avg Vector": temp_result["NVP Avg Vector"]})
        
        for subtopic in topic["Topics"]:
            temp_result = AddTopicData(subtopic, level+1, document, parents + [topic["Doc Heading"]],current_vectors)
            for temp in temp_result:
                result.append(temp)
    else:
        #print(space + "-- Topic lv"+ str(level) +": " + topic["Heading"][:100])
        temp_result = getVectors(parent_text + topic["Heading"], model)
        
        #current_vectors = {"Avg Vector": (temp_result["Avg Vector"] + parent_vectors["Avg Vector"]), "Avg Vector2": (temp_result["Avg Vector2"] + parent_vectors["Avg Vector2"]),"Spacy Vector": (temp_result["Spacy Vector"] + parent_vectors["Spacy Vector"]), "NV Spacy Vector": (temp_result["NV Spacy Vector"] +  parent_vectors["NV Spacy Vector"]), "NV Avg Vector": (temp_result["NV Avg Vector"] + parent_vectors["NV Avg Vector"]), "NVP Spacy Vector": (temp_result["NVP Spacy Vector"] + parent_vectors["NVP Spacy Vector"]), "NVP Avg Vector": (temp_result["NVP Avg Vector"] + parent_vectors["NVP Avg Vector"])}
        #current_vectors = {"Avg Vector": DivideVector(AddVectors(temp_result["Avg Vector"], parent_vectors["Avg Vector"]),2), "Avg Vector2": DivideVector(AddVectors(temp_result["Avg Vector2"], parent_vectors["Avg Vector2"]),2),"Spacy Vector": DivideVector(AddVectors(temp_result["Spacy Vector"], parent_vectors["Spacy Vector"]),2), "NV Spacy Vector": DivideVector(AddVectors(temp_result["NV Spacy Vector"],  parent_vectors["NV Spacy Vector"]),2), "NV Avg Vector": DivideVector(AddVectors(temp_result["NV Avg Vector"], parent_vectors["NV Avg Vector"]),2), "NVP Spacy Vector": DivideVector(AddVectors(temp_result["NVP Spacy Vector"], parent_vectors["NVP Spacy Vector"]),2), "NVP Avg Vector": DivideVector(AddVectors(temp_result["NVP Avg Vector"], parent_vectors["NVP Avg Vector"]),2)}
        
        current_vectors = {"Avg Vector": CombineVectors(temp_result["Avg Vector"], parent_vectors["Avg Vector"],alpha, 1-alpha), "Avg Vector2": CombineVectors(temp_result["Avg Vector2"], parent_vectors["Avg Vector2"],alpha, 1-alpha),"Spacy Vector": CombineVectors(temp_result["Spacy Vector"], parent_vectors["Spacy Vector"],alpha, 1-alpha), "NV Spacy Vector": CombineVectors(temp_result["NV Spacy Vector"],  parent_vectors["NV Spacy Vector"],alpha, 1-alpha), "NV Avg Vector": CombineVectors(temp_result["NV Avg Vector"], parent_vectors["NV Avg Vector"],alpha, 1-alpha), "NVP Spacy Vector": CombineVectors(temp_result["NVP Spacy Vector"], parent_vectors["NVP Spacy Vector"],alpha, 1-alpha), "NVP Avg Vector": CombineVectors(temp_result["NVP Avg Vector"], parent_vectors["NVP Avg Vector"],alpha, 1-alpha)}
        
        
        result.append({"Text": topic["Heading"], "Document":document, "Parents": parents + [topic["Heading"]], "Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"], "NVPA Spacy Vector": temp_result["NVPA Spacy Vector"], "NVPA Avg Vector": temp_result["NVPA Avg Vector"], 
                       "Parent Avg Vector": current_vectors["Avg Vector"], "Parent Avg Vector2": current_vectors["Avg Vector2"],"Parent Spacy Vector": current_vectors["Spacy Vector"], "Parent NV Spacy Vector": current_vectors["NV Spacy Vector"], "Parent NV Avg Vector": current_vectors["NV Avg Vector"], "Parent NVP Spacy Vector": current_vectors["NVP Spacy Vector"], "Parent NVP Avg Vector": current_vectors["NVP Avg Vector"],
                       "Children Avg Vector": children_vectors["Avg Vector"], "Children Avg Vector2": children_vectors["Avg Vector2"],"Children Spacy Vector": children_vectors["Spacy Vector"], "Children NV Spacy Vector": children_vectors["NV Spacy Vector"], "Children NV Avg Vector": children_vectors["NV Avg Vector"], "Children NVP Spacy Vector": children_vectors["NVP Spacy Vector"], "Children NVP Avg Vector": children_vectors["NVP Avg Vector"]})
        
        
        
        for para in topic["Paras"]:
            #print(space + para[:100])
            temp_result = getVectors(parent_text + para, model)
            result.append({"Text": para, "Document":document, "Parents": parents + [topic["Heading"]], "Avg Vector": temp_result["Avg Vector"], "Avg Vector2": temp_result["Avg Vector2"],"Spacy Vector": temp_result["Spacy Vector"], "NV Spacy Vector": temp_result["NV Spacy Vector"], "NV Avg Vector": temp_result["NV Avg Vector"], "NVP Spacy Vector": temp_result["NVP Spacy Vector"], "NVP Avg Vector": temp_result["NVP Avg Vector"], "NVPA Spacy Vector": temp_result["NVPA Spacy Vector"], "NVPA Avg Vector": temp_result["NVPA Avg Vector"], 
                       "Parent Avg Vector": current_vectors["Avg Vector"], "Parent Avg Vector2": current_vectors["Avg Vector2"],"Parent Spacy Vector": current_vectors["Spacy Vector"], "Parent NV Spacy Vector": current_vectors["NV Spacy Vector"], "Parent NV Avg Vector": current_vectors["NV Avg Vector"], "Parent NVP Spacy Vector": current_vectors["NVP Spacy Vector"], "Parent NVP Avg Vector": current_vectors["NVP Avg Vector"],
                       "Children Avg Vector": temp_result["Avg Vector"], "Children Avg Vector2": temp_result["Avg Vector2"],"Children Spacy Vector": temp_result["Spacy Vector"], "Children NV Spacy Vector": temp_result["NV Spacy Vector"], "Children NV Avg Vector": temp_result["NV Avg Vector"], "Children NVP Spacy Vector": temp_result["NVP Spacy Vector"], "Children NVP Avg Vector": temp_result["NVP Avg Vector"]})
        
        for subtopic in topic["Sub Topics"]:
            #AddTopicData(subtopic, level+1)
            temp_result = AddTopicData(subtopic, level+1, document, parents + [topic["Heading"]], current_vectors)
            for temp in temp_result:
                result.append(temp)
    
    #for res in result:
        
    
    return result


document_json = []
k=1
for file in filenames:
    chapters_dict = []
    #doc = ""
    f = open(file,"r")
    for line in f:
        hier_doc = ast.literal_eval(line)
        chapters_dict.append(hier_doc)
    
    #for hier_doc in chapters_dict:
    #    for chap in hier_doc:
    for chap in chapters_dict:     
        temp_result = AddTopicData(chap, -1, file, [file],[])
        for temp in temp_result:
            document_json.append(temp)
        print(k)
        k+=1
      




#document_json = document_json + sentences_json

"""
f = open("Turbonomics_vectors.txt", "w")
for x in document_json:
    f.write(str(x))
    f.write("\n")
f.close()
"""
"""
k=1
document_json = []
f = open("Turbonomics_vectors.txt", "r")
for x in f:
    document_json.append(ast.literal_eval(x))
    print(k)
    k+=1
f.close()
"""

print("Saved")

#document_json = sentences_json
def getTopic(sequence):
    for file in filenames:
        if file==sequence[0]:
            f = open(file,"r")
            for line in f:
                hier_doc = ast.literal_eval(line)
                chapters_dict.append(hier_doc)
            for chap in chapters_dict:  
                if chap["Doc Heading"]==sequence[1]:
                    curr_topic = chap
                    for i in range (2,len(sequence)):
                        try:
                            for st in curr_topic["Sub Topics"]:
                                if st["Heading"]==sequence[i]:
                                    curr_topic = st
                                    break
                        except:
                            for st in curr_topic["Topics"]:
                                if st["Heading"]==sequence[i]:
                                    curr_topic = st
                                    break
                    return curr_topic

temp_sim = 0

for qa in QnA:#, QnA[12]]:#[QnA[0], QnA[11]]:#, QnA[3], QnA[10]]:
    doc = nlp(qa[0])
    #print(qa[0])
    
    """
    new_qa = ""
    for token in doc:
        if (token.lemma_=="-PRON-"):
            new_qa = new_qa + " " + token.text
        else:
            new_qa = new_qa + " " + token.lemma_
    doc = nlp(new_qa[1:])
    """
    """
    spacy_vector = doc.vector
    
    vector_list = []
    nv_vector_list = []
    nvp_vector_list = []
    vector_list2 = []
    
    noun_verb_term = ""
    noun_verb_pronoun_term = ""
    
    for token in doc:
        if (token.pos_=="PUNCT"):
            continue
        if (token.lemma_=="-PRON-"):
            if inDataset(word_set,token.text.lower()):
                vector_list.append(model.wv.__getitem__(token.text.lower()))
                vector_list2.append(model.wv.__getitem__(token.text.lower()))
        else:
            if inDataset(word_set,token.lemma_.lower()):
                vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
        if (token.pos_=="NOUN" or token.pos_=="VERB" ): # or token.pos_=="PROPN"
            noun_verb_term = noun_verb_term + " " + token.text
            noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
            if inDataset(word_set,token.lemma_.lower()):
                nv_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
                nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
        if token.pos_=="PROPN": #or 
            noun_verb_pronoun_term = noun_verb_pronoun_term + " " + token.text
            if inDataset(word_set,token.lemma_.lower()):
                nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
    #print(vector_list)
    
    avg_vector = []
    nv_avg_vector = []
    nvp_avg_vector = []
    avg_vector2 = []
    
    if vector_list != []:
        avg_vector = vector_list[0]
        for i in range(1,len(vector_list)):
            avg_vector = avg_vector + vector_list[i]
        #avg_vector = avg_vector /len(vector_list)
        avg_vector = [x / len(vector_list) for x in avg_vector]
    #print(len(vector_list))
    
    
    if nv_vector_list != []:
        nv_avg_vector = nv_vector_list[0]
        for i in range(1,len(nv_vector_list)):
            nv_avg_vector = nv_avg_vector + nv_vector_list[i]
            #avg_vector = avg_vector /len(vector_list)
        nv_avg_vector = [x / len(nv_vector_list) for x in nv_avg_vector]
        
    if nvp_vector_list != []:
        nvp_avg_vector = nvp_vector_list[0]
        for i in range(1,len(nvp_vector_list)):
            nvp_avg_vector = nvp_avg_vector + nvp_vector_list[i]
            #avg_vector = avg_vector /len(vector_list)
        nvp_avg_vector = [x / len(nvp_vector_list) for x in nvp_avg_vector]
        
    if vector_list2 != []:
        avg_vector2 = vector_list2[0]
        for i in range(1,len(vector_list2)):
            avg_vector2 = avg_vector2 + vector_list2[i]
        #avg_vector = avg_vector /len(vector_list)
        avg_vector2 = [x / len(vector_list2) for x in avg_vector2]
    
    noun_verb_vector = nlp(noun_verb_term).vector
    noun_verb_pronoun_vector = nlp(noun_verb_pronoun_term).vector
    """
    
    result = getVectors(qa[0], model)
    
    spacy_vector = result["Spacy Vector"]
    noun_verb_vector = result["NV Spacy Vector"]
    noun_verb_pronoun_vector = result["NVP Spacy Vector"]
    noun_verb_pronoun_adj_vector = result["NVPA Spacy Vector"]
    avg_vector = result["Avg Vector"]
    nv_avg_vector = result["NV Avg Vector"]
    nvp_avg_vector = result["NVP Avg Vector"]
    nvpa_avg_vector = result["NVPA Avg Vector"]
    avg_vector2 = result["Avg Vector2"]
    
    
    max_sim = 0 
    max_sim_para = ""
    max_sim_text = ""
    
    avg_vector_list = []
    nv_avg_vector_list = []
    nvp_avg_vector_list = []
    nvpa_avg_vector_list = []
    avg_vector_list2 = []
    spacy_vector_list = []
    noun_verb_vector_list = []
    noun_verb_pronoun_vector_list = []
    noun_verb_pronoun_adj_vector_list = []
    
    p_avg_vector_list = []
    p_nv_avg_vector_list = []
    p_nvp_avg_vector_list = []
    p_avg_vector_list2 = []
    p_spacy_vector_list = []
    p_noun_verb_vector_list = []
    p_noun_verb_pronoun_vector_list = []
    
    c_avg_vector_list = []
    c_nv_avg_vector_list = []
    c_nvp_avg_vector_list = []
    c_avg_vector_list2 = []
    c_spacy_vector_list = []
    c_noun_verb_vector_list = []
    c_noun_verb_pronoun_vector_list = []
    
    comb_vector_list = []
    comb_vector_list1 = []
    comb_vector_list2 = []
    comb_vector_list3 = []
    comb_vector_list4 = []
    
    comb_vector_list5 = []
    comb_vector_list6 = []
    comb_vector_list7 = []
    comb_vector_list8 = []
    
    comb_vector_list9 = []
    comb_vector_list10 = []
    comb_vector_list11 = []
    comb_vector_list12 = []
    comb_vector_list13 = []
    comb_vector_list14 = []
    comb_vector_list15 = []
    comb_vector_list16 = []
    comb_vector_list17 = []
    
    comb_vector_list18 = []
    comb_vector_list19 = []
    comb_vector_list20 = []
    comb_vector_list21 = []
    comb_vector_list22 = []
    comb_vector_list23 = []
    
    comb_vector_list24 = []
    comb_vector_list25 = []
    comb_vector_list26 = []
    comb_vector_list27 = []
    comb_vector_list28 = []
    comb_vector_list29 = []
    comb_vector_list30 = []
    
    
    for para in document_json:
        
        if para["Avg Vector"] != []:
            similarity1 = 1-spatial.distance.cosine(para["Avg Vector"],avg_vector)
        else:
            similarity1 = 0
            
        similarity2 = 1-spatial.distance.cosine(para["Spacy Vector"],spacy_vector)
        if math.isnan(similarity2):
            similarity2 = 0 
        
        similarity3 = 1-spatial.distance.cosine(para["NV Spacy Vector"],noun_verb_vector)
        if math.isnan(similarity3):
            similarity3 = 0 
        
        if para["NV Avg Vector"] != []:
            similarity4 = 1-spatial.distance.cosine(para["NV Avg Vector"],nv_avg_vector)
        else:
            similarity4 = 0
        
        if para["Avg Vector2"] != []:
            similarity5 = 1-spatial.distance.cosine(para["Avg Vector2"],avg_vector2)
        else:
            similarity5 = 0
        
        similarity6 = 1-spatial.distance.cosine(para["NVP Spacy Vector"],noun_verb_pronoun_vector)
        if math.isnan(similarity6):
            similarity6 = 0 
        
        if para["NVP Avg Vector"] != []:
            similarity7 = 1-spatial.distance.cosine(para["NVP Avg Vector"],nvp_avg_vector)
        else:
            similarity7 = 0
        
        similarity8 = 1-spatial.distance.cosine(para["NVPA Spacy Vector"],noun_verb_pronoun_adj_vector)
        if math.isnan(similarity8):
            similarity8 = 0 
        
        if para["NVPA Avg Vector"] != []:
            similarity9 = 1-spatial.distance.cosine(para["NVPA Avg Vector"],nvpa_avg_vector)
        else:
            similarity9 = 0
            
        
        
        
        if para["Parent Avg Vector"] != []:
            similarity1p = 1-spatial.distance.cosine(para["Parent Avg Vector"],avg_vector)
        else:
            similarity1p = 0
            
        similarity2p = 1-spatial.distance.cosine(para["Parent Spacy Vector"],spacy_vector)
        if math.isnan(similarity2p):
            similarity2p = 0 
        
        similarity3p = 1-spatial.distance.cosine(para["Parent NV Spacy Vector"],noun_verb_vector)
        if math.isnan(similarity3p):
            similarity3p = 0 
        
        if para["Parent NV Avg Vector"] != []:
            similarity4p = 1-spatial.distance.cosine(para["Parent NV Avg Vector"],nv_avg_vector)
        else:
            similarity4p = 0
        
        if para["Parent Avg Vector2"] != []:
            similarity5p = 1-spatial.distance.cosine(para["Parent Avg Vector2"],avg_vector2)
        else:
            similarity5p = 0
        
        similarity6p = 1-spatial.distance.cosine(para["Parent NVP Spacy Vector"],noun_verb_pronoun_vector)
        if math.isnan(similarity6p):
            similarity6p = 0 
        
        if para["Parent NVP Avg Vector"] != []:
            similarity7p = 1-spatial.distance.cosine(para["Parent NVP Avg Vector"],nvp_avg_vector)
        else:
            similarity7p = 0
        
        
        
        """
        if para["Children Avg Vector"] != []:
            similarity1c = 1-spatial.distance.cosine(para["Children Avg Vector"],avg_vector)
        else:
            similarity1c = 0
            
        similarity2c = 1-spatial.distance.cosine(para["Children Spacy Vector"],spacy_vector)
        if math.isnan(similarity2c):
            similarity2c = 0 
        
        similarity3c = 1-spatial.distance.cosine(para["Children NV Spacy Vector"],noun_verb_vector)
        if math.isnan(similarity3c):
            similarity3c = 0 
        
        if para["Children NV Avg Vector"] != []:
            similarity4c = 1-spatial.distance.cosine(para["Children NV Avg Vector"],nv_avg_vector)
        else:
            similarity4c = 0
        
        if para["Children Avg Vector2"] != []:
            similarity5c = 1-spatial.distance.cosine(para["Children Avg Vector2"],avg_vector2)
        else:
            similarity5c = 0
        
        similarity6c = 1-spatial.distance.cosine(para["Children NVP Spacy Vector"],noun_verb_pronoun_vector)
        if math.isnan(similarity6c):
            similarity6c = 0 
        
        if para["Children NVP Avg Vector"] != []:
            similarity7c = 1-spatial.distance.cosine(para["Children NVP Avg Vector"],nvp_avg_vector)
        else:
            similarity7c = 0
        """
        
            
        """
        if para["Paragraph Seq"] in ["P73", "P11", "P27", "P51", "P24", "P42"]:#,"P160","P127","P214","P152","P220"]:#(para["Paragraph Seq"]=="P3"):
            temp_sim = similarity1 + similarity2 + similarity3
            print(para["Paragraph Seq"])
            print(similarity1)
            print(similarity2)
            print(similarity3)
            print(similarity4)
            print(similarity5)
            print(similarity6)
            print(similarity7)
        """
        
        
        
        
        
        
        avg_vector_list.append([para["Parents"],similarity1, para["Document"], para["Text"]])
        spacy_vector_list.append([para["Parents"],similarity2, para["Document"], para["Text"]])
        noun_verb_vector_list.append([para["Parents"],similarity3, para["Document"], para["Text"]])
        nv_avg_vector_list.append([para["Parents"],similarity4, para["Document"], para["Text"]])
        avg_vector_list2.append([para["Parents"],similarity5, para["Document"], para["Text"]])
        noun_verb_pronoun_vector_list.append([para["Parents"],similarity6, para["Document"], para["Text"]])
        nvp_avg_vector_list.append([para["Parents"],similarity7, para["Document"], para["Text"]])
        noun_verb_pronoun_adj_vector_list.append([para["Parents"],similarity8, para["Document"], para["Text"]])
        nvpa_avg_vector_list.append([para["Parents"],similarity9, para["Document"], para["Text"]])
        
        p_avg_vector_list.append([para["Parents"],similarity1p, para["Document"], para["Text"]])
        p_spacy_vector_list.append([para["Parents"],similarity2p, para["Document"], para["Text"]])
        p_noun_verb_vector_list.append([para["Parents"],similarity3p, para["Document"], para["Text"]])
        p_nv_avg_vector_list.append([para["Parents"],similarity4p, para["Document"], para["Text"]])
        p_avg_vector_list2.append([para["Parents"],similarity5p, para["Document"], para["Text"]])
        p_noun_verb_pronoun_vector_list.append([para["Parents"],similarity6p, para["Document"], para["Text"]])
        p_nvp_avg_vector_list.append([para["Parents"],similarity7p, para["Document"], para["Text"]])
        nvp_avg_vector_list.append([para["Parents"],similarity7, para["Document"], para["Text"]])
        """
        c_avg_vector_list.append([para["Parents"],similarity1c, para["Document"], para["Text"]])
        c_spacy_vector_list.append([para["Parents"],similarity2c, para["Document"], para["Text"]])
        c_noun_verb_vector_list.append([para["Parents"],similarity3c, para["Document"], para["Text"]])
        c_nv_avg_vector_list.append([para["Parents"],similarity4c, para["Document"], para["Text"]])
        c_avg_vector_list2.append([para["Parents"],similarity5c, para["Document"], para["Text"]])
        c_noun_verb_pronoun_vector_list.append([para["Parents"],similarity6c, para["Document"], para["Text"]])
        c_nvp_avg_vector_list.append([para["Parents"],similarity7c, para["Document"], para["Text"]])
        """
        """
        comb_vector_list.append([para["Parents"],similarity1 + similarity2 + similarity3 + similarity4, para["Document"], para["Text"]])
        comb_vector_list1.append([para["Parents"],similarity1 + similarity2 + similarity3, para["Document"], para["Text"]]) # 1 +2 +3
        comb_vector_list2.append([para["Parents"],similarity2 + similarity3, para["Document"], para["Text"]]) # 2 + 3
        comb_vector_list3.append([para["Parents"],similarity1 * similarity2 * similarity3 * similarity4 , para["Document"], para["Text"]]) #1*2*3
        comb_vector_list4.append([para["Parents"],similarity1 + 2* similarity2 + 2*similarity3 , para["Document"], para["Text"]])#1 +2(2) +2(3)
        comb_vector_list5.append([para["Parents"],similarity1 + similarity2 + similarity3 + similarity5, para["Document"], para["Text"]])
        comb_vector_list6.append([para["Parents"],similarity5 + similarity2 + similarity3, para["Document"], para["Text"]]) # 1 +2 +3
        comb_vector_list7.append([para["Parents"],similarity5 * similarity2 * similarity3, para["Document"], para["Text"]]) # 1 *2 *3
        comb_vector_list8.append([para["Parents"],similarity5 + 2* similarity2 + 2*similarity3 , para["Document"], para["Text"]])#5 +2(2) +2(3)
        
        comb_vector_list9.append([para["Parents"],similarity1 + similarity2 + similarity6 + similarity7, para["Document"], para["Text"]])
        comb_vector_list10.append([para["Parents"],similarity1 + similarity2 + similarity6, para["Document"], para["Text"]]) # 1 +2 +3
        comb_vector_list11.append([para["Parents"],similarity2 + similarity6, para["Document"], para["Text"]]) # 2 + 3
        comb_vector_list12.append([para["Parents"],similarity1 * similarity2 * similarity6 , para["Document"], para["Text"]]) #1*2*3
        comb_vector_list13.append([para["Parents"],similarity1 + 2* similarity2 + 2*similarity6 , para["Document"], para["Text"]])#1 +2(2) +2(3)
        comb_vector_list14.append([para["Parents"],similarity1 + similarity2 + similarity3 + similarity6 + similarity7, para["Document"], para["Text"]])
        comb_vector_list15.append([para["Parents"],similarity1 * similarity2 * similarity6 * similarity7 , para["Document"], para["Text"]]) #1*2*3
        
        comb_vector_list16.append([para["Parents"],similarity1 + similarity2 + similarity3 + similarity4 +similarity5 + similarity6 + similarity7, para["Document"], para["Text"]])
        """
        
        
        
        comb_vector_list17.append([para["Parents"],similarity1 * similarity2 * similarity3 * similarity4 *similarity5 * similarity6 * similarity7, para["Document"], para["Text"]])
        comb_vector_list18.append([para["Parents"],similarity1p * similarity2p * similarity3p * similarity4p *similarity5p * similarity6p * similarity7p, para["Document"], para["Text"]])
        comb_vector_list19.append([para["Parents"],(similarity1 * similarity2 * similarity3 * similarity4 *similarity5 * similarity6 * similarity7) + 0.2*(similarity1p * similarity2p * similarity3p * similarity4p *similarity5p * similarity6p * similarity7p), para["Document"], para["Text"]])
        comb_vector_list20.append([para["Parents"],(similarity1 * similarity2 * similarity3 * similarity4 *similarity5 * similarity6 * similarity7) * (similarity1p * similarity2p * similarity3p * similarity4p *similarity5p * similarity6p * similarity7p), para["Document"], para["Text"]])
        
        comb_vector_list21.append([para["Parents"],similarity6 + similarity7, para["Document"], para["Text"]])
        comb_vector_list22.append([para["Parents"],similarity6 * similarity7, para["Document"], para["Text"]])
        comb_vector_list23.append([para["Parents"],similarity6 * similarity7 * similarity6p * similarity7p, para["Document"], para["Text"]])
        
        #comb_vector_list24.append([para["Parents"],similarity6c + similarity7c, para["Document"], para["Text"]])
        #comb_vector_list25.append([para["Parents"],similarity6c * similarity7c, para["Document"], para["Text"]])
        #comb_vector_list26.append([para["Parents"],similarity6 * similarity7 * similarity6c * similarity7c, para["Document"], para["Text"]])
        
        comb_vector_list27.append([para["Parents"],similarity8 + similarity9, para["Document"], para["Text"]])
        comb_vector_list28.append([para["Parents"],similarity8 * similarity9, para["Document"], para["Text"]])
        comb_vector_list29.append([para["Parents"],similarity6 + similarity7 + similarity8 + similarity9, para["Document"], para["Text"]])
        comb_vector_list30.append([para["Parents"],similarity6 * similarity7 * similarity8 * similarity9, para["Document"], para["Text"]])
        
    avg_vector_list.sort(key=takeSecond, reverse=True)
    nv_avg_vector_list.sort(key=takeSecond, reverse=True)
    avg_vector_list2.sort(key=takeSecond, reverse=True)
    spacy_vector_list.sort(key=takeSecond, reverse=True)
    noun_verb_vector_list.sort(key=takeSecond, reverse=True)
    noun_verb_pronoun_vector_list.sort(key=takeSecond, reverse=True)
    nvp_avg_vector_list.sort(key=takeSecond, reverse=True)
    noun_verb_pronoun_adj_vector_list.sort(key=takeSecond, reverse=True)
    nvpa_avg_vector_list.sort(key=takeSecond, reverse=True)
    
    p_avg_vector_list.sort(key=takeSecond, reverse=True)
    p_nv_avg_vector_list.sort(key=takeSecond, reverse=True)
    p_avg_vector_list2.sort(key=takeSecond, reverse=True)
    p_spacy_vector_list.sort(key=takeSecond, reverse=True)
    p_noun_verb_vector_list.sort(key=takeSecond, reverse=True)
    p_noun_verb_pronoun_vector_list.sort(key=takeSecond, reverse=True)
    p_nvp_avg_vector_list.sort(key=takeSecond, reverse=True)
    
    """
    c_avg_vector_list.sort(key=takeSecond, reverse=True)
    c_nv_avg_vector_list.sort(key=takeSecond, reverse=True)
    c_avg_vector_list2.sort(key=takeSecond, reverse=True)
    c_spacy_vector_list.sort(key=takeSecond, reverse=True)
    c_noun_verb_vector_list.sort(key=takeSecond, reverse=True)
    c_noun_verb_pronoun_vector_list.sort(key=takeSecond, reverse=True)
    c_nvp_avg_vector_list.sort(key=takeSecond, reverse=True)
    """
    """
    comb_vector_list.sort(key=takeSecond, reverse=True)
    comb_vector_list1.sort(key=takeSecond, reverse=True)
    comb_vector_list2.sort(key=takeSecond, reverse=True)
    comb_vector_list3.sort(key=takeSecond, reverse=True)
    comb_vector_list4.sort(key=takeSecond, reverse=True)
    comb_vector_list5.sort(key=takeSecond, reverse=True)
    comb_vector_list6.sort(key=takeSecond, reverse=True)
    comb_vector_list7.sort(key=takeSecond, reverse=True)
    comb_vector_list8.sort(key=takeSecond, reverse=True)
    comb_vector_list9.sort(key=takeSecond, reverse=True)
    comb_vector_list10.sort(key=takeSecond, reverse=True)
    comb_vector_list11.sort(key=takeSecond, reverse=True)
    comb_vector_list12.sort(key=takeSecond, reverse=True)
    comb_vector_list13.sort(key=takeSecond, reverse=True)
    comb_vector_list14.sort(key=takeSecond, reverse=True)
    comb_vector_list15.sort(key=takeSecond, reverse=True)
    comb_vector_list16.sort(key=takeSecond, reverse=True)
    comb_vector_list17.sort(key=takeSecond, reverse=True)
    """
    
    comb_vector_list17.sort(key=takeSecond, reverse=True)
    comb_vector_list18.sort(key=takeSecond, reverse=True)
    comb_vector_list19.sort(key=takeSecond, reverse=True)
    comb_vector_list20.sort(key=takeSecond, reverse=True)
    comb_vector_list21.sort(key=takeSecond, reverse=True)
    comb_vector_list22.sort(key=takeSecond, reverse=True)
    comb_vector_list23.sort(key=takeSecond, reverse=True)
    comb_vector_list24.sort(key=takeSecond, reverse=True)
    comb_vector_list25.sort(key=takeSecond, reverse=True)
    comb_vector_list26.sort(key=takeSecond, reverse=True)
    comb_vector_list27.sort(key=takeSecond, reverse=True)
    comb_vector_list28.sort(key=takeSecond, reverse=True)
    comb_vector_list29.sort(key=takeSecond, reverse=True)
    comb_vector_list30.sort(key=takeSecond, reverse=True)
    
    """
    rank_list= []
    temp_rank_list = []
    for x in avg_vector_list[:10]:
        if inList3(spacy_vector_list[:10],x):
            if inList3(noun_verb_vector_list[:10],x):
                temp_rank_list.append(x)
    print(temp_rank_list)
    
    def ranker(i):
        return i
    
    for x in temp_rank_list:
        rank = 0
        i = 1
        for y in avg_vector_list[:10]:
            if (x==y):
                rank = rank + ranker(i)
                break
            i =i +1
        i = 1
        for y in spacy_vector_list[:10]:
            if (x==y):
                rank = rank + ranker(i)
                break
            i =i +1
        i = 1
        for y in noun_verb_vector_list[:10]:
            if (x==y):
                rank = rank + ranker(i)
                break
            i =i +1
        rank_list.append([x,rank])
    rank_list.sort(key=takeSecond)
    """
    
    
    
        #if max_sim<similarity:
            #max_sim = similarity
            #max_sim_para = para["Paragraph Seq"]
            #max_sim_text = para["Text"]
    print("Question: " + qa[0])
    print("Correct Answer: " + qa[1])
    #print("Predicted Answer: " + max_sim_para)
    #print(max_sim_text)
    
    
    #topset.clear()
    
    """
    topset = {''}
    i=0
    print("Spacy Prediction: ")
    for item in spacy_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Noun Verb Spacy Prediction: ")
    for item in noun_verb_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Noun Verb Pronoun Spacy Prediction: ")
    for item in noun_verb_pronoun_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    
    
    topset = {''}
    i=0
    print("Avg Prediction: ")
    #for i in range(5):
    for item in avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Noun Verb Avg Prediction: ")
    for item in nv_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Noun Verb Pronoun Avg Prediction: ")
    for item in nvp_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Avg2 Prediction: ")
    for item in avg_vector_list2[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    
    topset = {''}
    i=0   
    print("Noun Verb Pronoun Adj Spacy Prediction: ")
    for item in noun_verb_pronoun_adj_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    print("Noun Verb Pronoun AdjAvg Prediction: ")
    for item in nvpa_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    
    print("Parent Avg Prediction: ")
    #for i in range(5):
    for item in p_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Parent Spacy Prediction: ")
    for item in p_spacy_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Parent Noun Verb Spacy Prediction: ")
    for item in p_noun_verb_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Parent Noun Verb Pronoun Spacy Prediction: ")
    for item in p_noun_verb_pronoun_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Parent Noun Verb Avg Prediction: ")
    for item in p_nv_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Parent Noun Verb Pronoun Avg Prediction: ")
    for item in p_nvp_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Parent Avg2 Prediction: ")
    for item in p_avg_vector_list2[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    """
    
    
    """
    print("Children Avg Prediction: ")
    #for i in range(5):
    for item in c_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Children Spacy Prediction: ")
    for item in c_spacy_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Children Noun Verb Spacy Prediction: ")
    for item in c_noun_verb_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0   
    print("Children Noun Verb Pronoun Spacy Prediction: ")
    for item in c_noun_verb_pronoun_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Children Noun Verb Avg Prediction: ")
    for item in c_nv_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
        
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Children Noun Verb Pronoun Avg Prediction: ")
    for item in c_nvp_avg_vector_list[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    
    topset = {''}
    i=0
    print("Children Avg2 Prediction: ")
    for item in c_avg_vector_list2[:5]:
        print(item[0])
        print(item[3])
    
    print("")
    print("")
    """
    
    
    """
    topset = {''}
    i=0
    print("Combined 1+2+3+4 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list[i][0] in topset:
            topset.add(comb_vector_list[i][0])
            print(comb_vector_list[i][0])
            #print(comb_vector_list[i][2])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1+2+3 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list1[i][0] in topset:
            topset.add(comb_vector_list1[i][0])
            print(comb_vector_list1[i][0])
            #print(comb_vector_list1[i][2])
        i = i + 1
        
        
    topset = {''}
    i=0
    print("Combined 2+3 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list2[i][0] in topset:
            topset.add(comb_vector_list2[i][0])
            print(comb_vector_list2[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1*2*3 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list3[i][0] in topset:
            topset.add(comb_vector_list3[i][0])
            print(comb_vector_list3[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1+ 2(2) + 2(3) Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list4[i][0] in topset:
            topset.add(comb_vector_list4[i][0])
            print(comb_vector_list4[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1+2+3+6 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list5[i][0] in topset:
            topset.add(comb_vector_list5[i][0])
            print(comb_vector_list5[i][0])
            #print(comb_vector_list5[i][2])
        i = i + 1
    
    
    
    topset = {''}
    i=0
    print("Combined 6+2+3 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list6[i][0] in topset:
            topset.add(comb_vector_list6[i][0])
            print(comb_vector_list6[i][0])
        i = i + 1
    
    
    topset = {''}
    i=0
    print("Combined 6*2*3 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list7[i][0] in topset:
            topset.add(comb_vector_list7[i][0])
            print(comb_vector_list7[i][0])
        i = i + 1
     
    
    topset = {''}
    i=0
    print("Combined 1+ 2(2) + 2(3) Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list8[i][0] in topset:
            topset.add(comb_vector_list8[i][0])
            print(comb_vector_list8[i][0])
        i = i + 1
    
    
    topset = {''}
    i=0
    print("Combined 1+2+6+7 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list9[i][0] in topset:
            topset.add(comb_vector_list9[i][0])
            print(comb_vector_list9[i][0])
        i = i + 1
    
    
    topset = {''}
    i=0
    print("Combined 1+2+6 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list10[i][0] in topset:
            topset.add(comb_vector_list10[i][0])
            print(comb_vector_list10[i][0])
        i = i + 1
    
     
    topset = {''}
    i=0
    print("Combined 2+6 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list11[i][0] in topset:
            topset.add(comb_vector_list11[i][0])
            print(comb_vector_list11[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1*2*6 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list12[i][0] in topset:
            topset.add(comb_vector_list12[i][0])
            print(comb_vector_list12[i][0])
        i = i + 1
    
    
    topset = {''}
    i=0
    print("Combined 1+ 2(2) + 2(6) Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list13[i][0] in topset:
            topset.add(comb_vector_list13[i][0])
            print(comb_vector_list13[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1+2+3+6+7 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list14[i][0] in topset:
            topset.add(comb_vector_list14[i][0])
            print(comb_vector_list14[i][0])
        i = i + 1
        
    
    topset = {''}
    i=0
    print("Combined 1*2*6*7 Prediction: ")
    while len(topset)<=5:
        if not comb_vector_list15[i][0] in topset:
            topset.add(comb_vector_list15[i][0])
            print(comb_vector_list15[i][0])
        i = i + 1
     
    
    topset = {''}
    i=0
    print("Combined 1+2+3+4+5+6+7 Prediction: ")
    while len(topset)<=10:
        if not comb_vector_list16[i][0] in topset:
            topset.add(comb_vector_list16[i][0])
            print(comb_vector_list16[i][0])
        i = i + 1
    
    
    
    
    topset = {''}
    i=0
    print("Combined 1*2*3*4*5*6*7 Prediction: ")
    
    while len(topset)<=5:
        if not comb_vector_list17[i][0] in topset:
            topset.add(comb_vector_list17[i][0])
            print(comb_vector_list17[i][0])
            #print(comb_vector_list17[i][1])
            print(comb_vector_list17[i][2])
        i = i + 1
    
    
    for item in comb_vector_list17[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    
    for x in comb_vector_list17:
        if x[0] =="P73":
            print(x[0])
            print(x[1])
            break
    
    
    print("Rank Prediction: ")
    for i in range(5):
        if i>len(rank_list):
            print(rank_list[i][0])
        else:
            break
    """
    
    
    """
    print(" ")
    print("Combined 1p*2p*3p*4p*5p*6p*7p Prediction: ")
    for item in comb_vector_list18[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    print(" ")
    print("Combined N+Np Prediction: ")
    for item in comb_vector_list19[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
        
    print(" ")
    print("Combined N*Np Prediction: ")
    for item in comb_vector_list20[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    
    print(" ")
    print("Combined 6+7 Prediction: ")
    for item in comb_vector_list21[:5]:
        print(item[0])
        print(item[3])
        tpic = getTopic(item[0])
        PrintTopic(tpic,0)
    """
    print(" ")
    print("Combined 6*7 Prediction: ")
    for item in comb_vector_list22[:3]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
        print(" ")
        
    """
    print(" ")
    print("Combined 6*7*6p*7p Prediction: ")
    for item in comb_vector_list23[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    """
    
    """
    print(" ")
    print("Combined 6c+7c Prediction: ")
    for item in comb_vector_list24[:5]:
        print(item[0])
        print(item[3])
        tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    
    print(" ")
    print("Combined 6c*7c Prediction: ")
    for item in comb_vector_list25[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    print(" ")
    print("Combined 6*7*6c*7c Prediction: ")
    for item in comb_vector_list26[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    """
    print(" ")
    print("Combined 8+9 Prediction: ")
    for item in comb_vector_list27[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    print(" ")
    print("Combined 8*9 Prediction: ")
    for item in comb_vector_list28[:3]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    print(" ")
    print("Combined 6+7+8+9 Prediction: ")
    for item in comb_vector_list29[:5]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    
    print(" ")
    print("Combined 6*7*8*9 Prediction: ")
    for item in comb_vector_list30[:3]:
        print(item[0])
        print(item[3])
        #tpic = getTopic(item[0])
        #PrintTopic(tpic,0)
    print(" ")
    
    
    """
    sent_list = []
    
    for x in comb_vector_list17:
        if x[0]==comb_vector_list17[0][0]:
            sent_list.append(x[2])
            
    print(sent_list[0])
    print(sent_list[1])
    """
    
    """
    doc_para = nlp(comb_vector_list17[0][2])
    sentence_data = [sent.string.strip() for sent in doc_para.sents]
    
    #print(sentence_data)
    
    top_para_list=[]
    
    top_para_json =[]
    s=1
    for sent in sentence_data:
        if sent!="":
            doc = nlp(sent)
            
            sent_spacy_vector = doc.vector
            sent_avg_vector = []
            sent_nv_avg_vector = []
            sent_nvp_avg_vector = []
            sent_avg_vector2 = []
            
            sent_noun_verb_vector = []
            sent_noun_verb_term = ""
            sent_noun_verb_pronoun_term = ""
            
            
            sent_vector_list = []
            sent_nv_vector_list = []
            sent_nvp_vector_list = []
            sent_vector_list2 = []
            
            for token in doc:
                if (token.pos_=="PUNCT"):
                    continue
                
                if (token.lemma_=="-PRON-"):
                    if inDataset(word_set,token.text.lower()):
                        sent_vector_list.append(model.wv.__getitem__(token.text.lower()))
                        sent_vector_list2.append(model.wv.__getitem__(token.text.lower()))
                else:
                    if inDataset(word_set,token.lemma_.lower()):
                        sent_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                        sent_vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
                if (token.pos_=="NOUN" or token.pos_=="VERB" ): #or token.pos_=="PROPN"
                    sent_noun_verb_term = sent_noun_verb_term + " " + token.text
                    sent_noun_verb_pronoun_term = sent_noun_verb_pronoun_term + " " + token.text
                    if inDataset(word_set,token.lemma_.lower()):
                        sent_nv_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                        sent_vector_list2.append(model.wv.__getitem__(token.lemma_.lower()))
                        sent_nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                if token.pos_=="PROPN": #or 
                    sent_noun_verb_pronoun_term = sent_noun_verb_pronoun_term + " " + token.text
                    if inDataset(word_set,token.lemma_.lower()):
                        sent_nvp_vector_list.append(model.wv.__getitem__(token.lemma_.lower()))
                    
            if sent_vector_list != []:
                sent_avg_vector = sent_vector_list[0]
                for i in range(1,len(sent_vector_list)):
                    sent_avg_vector = sent_avg_vector + sent_vector_list[i]
                sent_avg_vector = [x / len(sent_vector_list) for x in sent_avg_vector]
                    
            #print(len(vector_list), s)
                        
            if sent_nv_vector_list != []:
                sent_nv_avg_vector = sent_nv_vector_list[0]
                for i in range(1,len(sent_nv_vector_list)):
                    sent_nv_avg_vector = sent_nv_avg_vector + sent_nv_vector_list[i]
                sent_nv_avg_vector = [x / len(sent_nv_vector_list) for x in sent_nv_avg_vector]
                    
            if sent_nvp_vector_list != []:
                sent_nvp_avg_vector = sent_nvp_vector_list[0]
                for i in range(1,len(sent_nvp_vector_list)):
                    sent_nvp_avg_vector = sent_nvp_avg_vector + sent_nvp_vector_list[i]
                sent_nvp_avg_vector = [x / len(sent_nvp_vector_list) for x in sent_nvp_avg_vector]
                        
                    
            if sent_vector_list2 != []:
                sent_avg_vector2 = sent_vector_list2[0]
                for i in range(1,len(sent_vector_list2)):
                    sent_avg_vector2 = sent_avg_vector2 + sent_vector_list2[i]
                sent_avg_vector2 = [x / len(sent_vector_list2) for x in sent_avg_vector2]
                    
                    
            sent_noun_verb_vector = nlp(sent_noun_verb_term).vector
            sent_noun_verb_pronoun_vector = nlp(sent_noun_verb_pronoun_term).vector
                    
            #print(avg_vector)
                             
            sent_seq_text = "S"+str(s) # para_seq_text
            top_para_json.append({"Sentence Text":sent, "Sentence Seq": sent_seq_text,"Avg Vector": sent_avg_vector, "Avg Vector2": sent_avg_vector2, "Spacy Vector": sent_spacy_vector, "NV Spacy Vector": sent_noun_verb_vector, "NV Avg Vector": sent_nv_avg_vector, "NVP Spacy Vector": sent_noun_verb_pronoun_vector, "NVP Avg Vector": sent_nvp_avg_vector})
            s=s+1
            
            
            if sent_avg_vector != []:
                similarity1 = 1-spatial.distance.cosine(sent_avg_vector,avg_vector)
            else:
                similarity1 = 0
                
            similarity2 = 1-spatial.distance.cosine(sent_spacy_vector,spacy_vector)
            if math.isnan(similarity2):
                similarity2 = 0 
            
            similarity3 = 1-spatial.distance.cosine(sent_noun_verb_vector,noun_verb_vector)
            if math.isnan(similarity3):
                similarity3 = 0 
            
            if sent_nv_avg_vector != []:
                similarity4 = 1-spatial.distance.cosine(sent_nv_avg_vector, nv_avg_vector)
            else:
                similarity4 = 0
            
            if sent_avg_vector2 != []:
                similarity5 = 1-spatial.distance.cosine(sent_avg_vector2,avg_vector2)
            else:
                similarity5 = 0
            
            similarity6 = 1-spatial.distance.cosine(sent_noun_verb_pronoun_vector,noun_verb_pronoun_vector)
            if math.isnan(similarity6):
                similarity6 = 0 
            
            if sent_nvp_avg_vector != []:
                similarity7 = 1-spatial.distance.cosine(sent_nvp_avg_vector,nvp_avg_vector)
            else:
                similarity7 = 0
                
            top_para_list.append([sent_seq_text, similarity1 * similarity2 * similarity3 * similarity4 *similarity5 * similarity6 * similarity7, sent])
    
    
    top_para_list.sort(key=takeSecond, reverse=True)
    
    for x in top_para_list:
        print(x[0])
        print(x[2])
    """
    
    print("")
    print("")
    print("")
    print("")
    print("")
    
    
