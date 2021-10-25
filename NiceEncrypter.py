from random import sample

class Encrypter():
    def __init__(self, Key=None):
        self.__ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.__abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
        self.__Key = str
        self.regenerateKey(Key)

    def getKey(self) -> str:
        '''Devuelve la key actual'''
        return self.__Key

    def __setKey(self, key:str):
        self.__Key = key

    def __validateKey(self, key:str) -> bool:
        if type(key) != str:                                                
            return False
        if len(key) != 27:                  
            return False   
        for l in key:   
            if not l.isalpha():                                   
                return False
        for l in self.__abc:
            if key.count(l) > 1:                                            
                return False
        return True

    def regenerateKey(self, key=None) -> str:
        '''Regenera la key, si es invalida o no existente genera una al azar'''
        newKey = "".join(sample(self.__abc, len(self.__abc)))
        if key==None or self.__validateKey(key)==False:
            self.__setKey(newKey)
        else:
            self.__setKey(key.lower())
        return newKey
        

    def encrypt(self, text:str, veces:int) -> str:
        '''Cifra el texto ingresado x veces'''
        result = ''
        for _ in range(veces):
            for l in text:                                       
                if l.isalpha() and l.lower()!='á' and l.lower()!='é' and l.lower()!='í' and l.lower()!='ó' and l.lower()!='ú':
                    if l.isupper():                                      
                        ind = self.__ABC.index(l)                               
                        result += self.__Key[ind].upper()                 
                    elif l.islower():                                               
                        ind = self.__abc.index(l)                                          
                        result += self.__Key[ind]                                          
                else:                                                               
                    result += l     
            text = result
            result = ''
        return text

    def decrypt(self, text:str, veces:int) -> str:
        '''Descifra el texto ingresado x veces'''
        result = ''
        for _ in range(veces):
            for l in text:                                 
                if l.isalpha() and l.lower()!='á' and l.lower()!='é' and l.lower()!='í' and l.lower()!='ó' and l.lower()!='ú':                                             
                    if l.isupper():                                      
                        ind = self.__Key.index(l.lower())
                        result += self.__ABC[ind]
                    elif l.islower():                                               
                        ind = self.__Key.index(l)
                        result += self.__abc[ind]
                else:                                              
                    result += l 
            text = result
            result = ''
        return text
    
