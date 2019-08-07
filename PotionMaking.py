# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:15:05 2016

@author: Samuel Sellberg
"""
from  scipy import *
from  pylab import *

class Dice:
    def __init__(self,amount,size):
        self.amount=amount
        self.size=size
    def __repr__(self):
        if self.amount==1:
            am=''
        else:
            am=self.amount
        return '%sD%s' %(am,self.size)

class Effect:
    def __init__(self,name,dice,anti=None,invis=False):
        self.name=name
        self.dice=dice
        self.anti=anti
        self.invis=invis
    def save(self,dic):
        if not isinstance(dic,dict):
            raise TypeError("Does not recognize dic as dict.")
        dic[self]=self.name
    def __repr__(self):
        return """Name: %s
Strength: %s""" %(self.name,self.dice)
    
class SideEffect:
    def __init__(self,name,strength,anti=None,noadd=False,invis=False):
        self.name=name
        self.str=strength
        self.anti=anti
        self.noadd=noadd
        self.invis=invis
    def save(self,dic):
        if not isinstance(dic,dict):
            raise TypeError("Does not recognize dic as dict.")
        dic[self]=self.name
    def __repr__(self):
        return """Name: %s
Strength: %s""" %(self.name,self.str)

class Ingredient:
    def __init__(self,Name,Level,Description,E=None,S=None,Necessity=1,Process=False,altName=None):
        if not isinstance(Name,str):
            raise TypeError("Does not recognize Name as str.")
        if not isinstance(E,Effect):
            if not isinstance(E,(tuple,list)):
                raise TypeError("Does not recognize E.")
        if isinstance(E,(tuple,list)):
            for i in range(len(E)):
                if not isinstance(E[i],Effect):
                    raise TypeError("Does not recognize element in E as Effect.")
        if not isinstance(S,SideEffect):
            if not isinstance(S,(tuple,list)):
                raise TypeError("Does not recognize S.")
        if isinstance(S,(tuple,list)):
            for i in range(len(S)):
                if not isinstance(S[i],SideEffect):
                    raise TypeError("Does not recognize element in S as SideEffect.")
        if not isinstance(Level,int):
            raise TypeError("Does not recognize Level as int.")
        if not 0<=Level<=5:
            raise ValueError("Level must be within 0 to 5.")
        if not isinstance(Description,str):
            raise TypeError("Does not recognize Description as str.")
        if not isinstance(Necessity,int):
            raise TypeError("Does not recognize Necessity as int.")
        if Necessity<0:
            raise ValueError("Necessity cannot be negative.")
        if not isinstance(altName,str):
            if not altName==None:
                raise TypeError("Does not recognize altName as str.")
        if Process==True and altName==None:
            raise Exception("You need to enter an altName if Process is True.")
        self.name=Name
        self.effect=E
        self.sideEffect=S
        self.level=Level
        self.desc=Description
        self.nec=Necessity
        self.process=Process
        self.altname=altName
    def save(self,dic):
        if not isinstance(dic,dict):
            raise TypeError("Does not recognize dic as dict.")
        dic[self]=self.name
    def Process(self):
        if self.process==False:
            return 'This ingredient does not need to be processed.'
        if self.process==True:
            self.process=False
            self.name=self.altname
            return self
    def __repr__(self):
        if isinstance(self.effect,(tuple,list)):
            effect=''
            for i in range(len(self.effect)):
                eff='%s %s' %(self.effect[i].name,self.effect[i].dice)
                if not i==0:
                    effect+=', '
                effect+=eff
        else:
            effect='%s %s' %(self.effect.name,self.effect.dice)
        if isinstance(self.sideEffect,(tuple,list)):
            sidee=''
            for i in range(len(self.sideEffect)):
                sid='%s:%s' %(self.sideEffect[i].name,self.sideEffect[i].str)
                if not i==0:
                    sidee+=', '
                sidee+=sid
        else:
            sidee='%s:%s' %(self.sideEffect.name,self.sideEffect.str)
        if self.level==0:
            level='Very Easy'
        if self.level==1:
            level='Easy'
        if self.level==2:
            level='Medium'
        if self.level==3:
            level='Hard'
        if self.level==4:
            level='Very Hard'
        if self.level==5:
            level='Nearly Impossible'
        return """%s
Effects: %s
Side Effects: %s
Required Level of Handeling: %s
Description:
%s""" %(self.name,effect,sidee,level,self.desc)
        
        

class Potion:
    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError("Does not recognize name as str.")
        self.name=name
        self.effects=[]
        self.sideEffects=[]
    def Add(self,Ingredient):
        if not isinstance(Ingredient,Ingredient):
            raise TypeError("You can only add an ingredient to a potion.")
        if Ingredient.process==True:
            return 'This ingredient needs to be processed first.'
        for i in range(len(self.effects)):
            if isinstance(Ingredient.effect,(tuple,list)):
                ninc=[]
                for j in range(len(Ingredient.effect)):
                    if self.effects[i].name==Ingredient.effect[j].name:
                        if isinstance(self.effects[i].dice,list):
                            for k in range(len(self.effects[i].dice)):
                                if self.effects[i].dice[k].size==Ingredient.effect[j].dice.size:
                                    am=self.effects[i].dice[k].amount+Ingredient.effect[j].dice.amount
                                    self.effects[i].dice[k].amount=am
                                if self.effects[i].dice[k].size!=Ingredient.effect[j].dice.size:
                                    self.effects[i].dice[k].append(Ingredient.effect[j].dice)
                        else:
                            if self.effects[i].dice.size==Ingredient.effect[j].dice.size:
                                am=self.effects[i].dice.amount+Ingredient.dice.effect[j].amount
                                self.effects[i].dice.amount=am
                            if self.effects[i].dice.size!=Ingredient.effect[j].dice.size:
                                self.effects[i].dice=[self.effects[i].dice,Ingredient.effect[j].dice]
                    if self.effects[i].name==Ingredient.effect[j].anti:
                        #      Kolla på Side Effect
                        ninc.append(j)
            else:
                ninc=False
                if self.effects[i].name==Ingredient.effect.name:
                    if isinstance(self.effects[i].dice,list):
                        for k in range(len(self.effects[i].dice)):
                            if self.effects[i].dice[k].size==Ingredient.effect.dice.size:
                                am=self.effects[i].dice[k].amount+Ingredient.effect.dice.amount
                                self.effects[i].dice[k].amount=am
                            if self.effects[i].dice[k].size!=Ingredient.effect.dice.size:
                                self.effects[i].dice[k].append(Ingredient.effect.dice)
                    else:
                        if self.effects[i].dice.size==Ingredient.effect.dice.size:
                            am=self.effects[i].dice.amount+Ingredient.dice.effect.amount
                            self.effects[i].dice.amount=am
                        if self.effects[i].dice.size!=Ingredient.effect.dice.size:
                            self.effects[i].dice=[self.effects[i].dice,Ingredient.effect.dice]
                if self.effects[i].name==Ingredient.effect.anti:
                    #      Kolla på Side Effect
                    ninc=True
        if isinstance(Ingredient.effect,(tuple,list)):
            for i in range(len(Ingredient.effect)):
                if not ninc.count(i)==1:
                    self.effects.append(Ingredient.effect[i])
        else:
            if ninc==False:
                self.effects.append(Ingredient.effect)
        #----------------------------------------------------------------------
        for i in range(len(self.sideEffects)):
            if isinstance(Ingredient.sideEffect,(tuple,list)):
                ninc=[]
                for j in range(len(Ingredient.sideEffect)):
                    if self.sideEffects[i].name==Ingredient.sideEffect[j].name:
                        if self.sideEffects[i].noadd==True or Ingredient.sideEffect[j].noadd==True:
                            None
                        else:
                            size=self.sideEffects[i].str+Ingredient.sideEffect[j].str
                            self.sideEffects[i].str=size
                        ninc.append(j)
                    if self.sideEffects[i].name==Ingredient.sideEffect[j].anti:
                        if self.sideEffects[i].noadd==True or Ingredient.sideEffect[j].noadd==True:
                            self.sideEffects.remove(self.sideEffects[i])
                        elif self.sideEffects[i].str==Ingredient.sideEffect[j].str:
                            self.sideEffects.remove(self.sideEffects[i])
                        elif self.sideEffects[i].str>Ingredient.sideEffect[j].str:
                            size=self.sideEffects[i].str-Ingredient.sideEffect[j].str
                            self.sideEffects[i].str=size
                        elif self.sideEffects[i].str<Ingredient.sideEffect[j].str:
                            size=Ingredient.sideEffect[j].str-self.sideEffects[i].str
                            index=self.sideEffects.index(self.sideEffects[i])
                            self.sideEffects.remove(self.sideEffects[i])
                            self.sideEffects.insert(index,SideEffect(Ingredient.sideEffect[j].name,size,Ingredient.sideEffect[j].anti,Ingredient.sideEffect[j].invis))
                        ninc.append(j)
            else:
                ninc=False
                if self.sideEffects[i].name==Ingredient.sideEffect.name:
                    if self.sideEffects[i].noadd==True or Ingredient.sideEffect.noadd==True:
                        None
                    else:
                        size=self.sideEffects[i].str+Ingredient.sideEffect.str
                        self.sideEffects[i].str=size
                    ninc=True
                if self.sideEffects[i].name==Ingredient.sideEffect.anti:
                    if self.sideEffects[i].noadd==True or Ingredient.sideEffect.noadd==True:
                        self.sideEffects.remove(self.sideEffects[i])
                    elif self.sideEffects[i].str==Ingredient.sideEffect.str:
                        self.sideEffects.remove(self.sideEffects[i])
                    elif self.sideEffects[i].str>Ingredient.sideEffect.str:
                        size=self.sideEffects[i].str-Ingredient.sideEffect.str
                        self.sideEffects[i].str=size
                    elif self.sideEffects[i].str<Ingredient.sideEffect.str:
                        size=Ingredient.sideEffect.str-self.sideEffects[i].str
                        index=self.sideEffects.index(self.sideEffects[i])
                        self.sideEffects.remove(self.sideEffects[i])
                        self.sideEffects.insert(index,SideEffect(Ingredient.sideEffect.name,size,Ingredient.sideEffect.anti,Ingredient.sideEffect.invis))
                    ninc=True
        if isinstance(Ingredient.sideEffect,(tuple,list)):
            for i in range(len(Ingredient.sideEffect)):
                if not ninc.count(i)==1:
                    self.sideEffects.append(Ingredient.sideEffect[i])
        else:
            if ninc==False:
                self.sideEffects.append(Ingredient.sideEffect)
    def __repr__(self):
        effect=''
        for i in range(len(self.effect)):
            if isinstance(self.effect[i].dice,(list)):
                for j in range(len(self.effect[i].dice)):
                    ef='%s %s' %(self.effect[i].name,self.effect[i].dice[j])
                    if not j==0:
                        eff+=' + '
                    eff+=ef
            else:
                eff='%s %s' %(self.effect[i].name,self.effect[i].dice)
            if not i==0:
                effect+=', '
            effect+=eff
        sidee=''
        for i in range(len(self.sideEffect)):
            sid='%s:%s' %(self.sideEffect[i].name,self.sideEffect[i].str)
            if not i==0:
                sidee+=', '
            sidee+=sid
        return """%s
Effects: %s
Side Effects: %s""" %(self.name,effect,sidee)
        
                








strength=Effect('Strength',Dice(2,6))
acidity=SideEffect('Acidity',3)
salt=Ingredient('Salt',0,'This is a salty item!',strength,acidity,Process=True,altName='Purified Salt')
supersalt=Ingredient('Salt',0,'This is a salty item!',(strength,strength),(acidity,acidity))