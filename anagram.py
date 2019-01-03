def anagram(s1, s2):
    str1 = s1.replace(' ', '')
    str2 = s2.replace(' ', '')
    arr1 = list(str1)
    arr2 = list(str2)
    siz1 = len(arr1)
    siz2 = len(arr2)

    if siz1 == siz2:
        for inc1 in range(len(arr1)):
                for inc2 in range(len(arr2)):
                    #print("{0} and {1} are {2} and {3}".format(inc1, inc2, arr1[inc1], arr2[inc2]))
                    if arr1[inc1] == arr2[inc2]:
                        arr2.pop(inc2)
                        break

    if len(arr2) == 0:
        return True

    return False

def anagram_using_sort(s1, s2):
    str1 = s1.replace(' ', '').lower()
    str2 = s2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)