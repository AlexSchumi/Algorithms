#d={'a':'apple','b':'ball'}
#d.keys()  # displays all keys in list
#['a','b']
#d.values() # displays you values in list
#['apple','ball']
#d.items() # displays you pair tuple of key and value
#[('a','apple'),('b','ball')
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
