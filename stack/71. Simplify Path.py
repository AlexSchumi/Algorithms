class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path or len(path) == 0:
            return " "
        flag = 0
        res = []
        for i in range(len(path)):
            if path[i] == '/' and i < len(path) - 1: # search for another possible '/'
                flag = i
                j = i + 1
                while j <= len(path) - 1:
                    if path[j] == '/': break # jump out of loop if we find another '/'
                    j += 1
                if j > len(path) - 1: break # if j is out of range, jump out of loop

                if j - i == 1: continue # multiple '/' together
                else:
                    if j - i == 2:
                        if path[i+1] == '.': continue
                        else: res.append(path[i+1])
                    elif j - i == 3:
                        if path[i+1:j] == '..':
                            if len(res) > 0:
                                res.pop()
                        else:
                            if path[i+1:j] != res[-1]:
                                res.append(path[i+1:j])
                    else:
                        if path[i+1:j] != res[-1]:
                            res.append(path[i+1:j])
                    i = j

        # find the last j
        if flag < len(path)-1:
            if path[flag+1:len(path)] == '..':
                if len(res) > 0:
                    res.pop()
            elif path[flag+1:len(path)] == '.': pass
            else:
                res.append(path[flag+1:len(path)])


        if len(res) == 0:
            return '/'
        else:
            dir = ""
            for r in res:
                dir += '/' + r
        return dir

    def simplifyPath2(self, path):
        if not path or len(path) == 0:
            return " "
        res = []

        for i in range(len(path)):
            if path[i] == '/': # find another 1
                j = i + 1
                while j <= len(path)-1 and path[j] != '/':
                    j += 1
                if j > len(path) - 1:
                    if j - i > 1:
                        if path[i+1:] == '..':
                            if len(res) > 0:
                                res.pop()
                        elif path[i+1:] == '.': pass
                        else: res.append(path[i+1:j])

                    else: break
                else:
                    if j - i > 1:
                        if path[i+1:j] == '.': pass
                        elif path[i+1:j] == '..':
                            if len(res) > 0:
                                res.pop()
                        else: res.append(path[i+1:j])
            i = j

        if len(res) == 0:
            return '/'
        else:
            dir = "/" + res[0]
            for i in range(1,len(res)):
                if res[i] != res[i-1]:
                    dir += '/' + res[i]
        return dir

    def simplifyPath3(self, path):
        if not path or len(path) == 0:
            return " "
        res = []
        places = [p for p in path.split('/') if p != '' and p != '.'] #be familiar with .split()
        for dir in places:
            if dir =='..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(dir)

        return "/" + "/".join(res) # 'str'.join(string list) (add str in after every element in list)



if __name__ == '__main__':
    print(Solution().simplifyPath3("/a//b////c/d//././/.."))
    #print(Solution().simplifyPath3("/home/home"))
