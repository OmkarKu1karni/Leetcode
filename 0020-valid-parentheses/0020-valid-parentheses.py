class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        St = [] 
        for i in s :
            if i in ["{","(","["] :
                St.append(i)
            else:
                if len(St)==0:
                    return False
                else:
                    match i :
                        case ")":
                            if St[-1]=="(" :
                                St.pop()
                            else:
                                return False
                        case "}":
                            if St[-1]=="{" :
                                St.pop()
                            else:
                                return False
                        case "]":
                            if St[-1]=="[" :
                                St.pop()
                            else:
                                return False
        return len(St)==0