# 58, 59, 60 - Udemy Chapter No

#   No of Occurances  [10, 2, 5, 10, 1, 5, 10]

# test = [10,2,5,10,1,5,10]
# def nooflist(list, element):
#     occurance = 0
#     for e in list:
#         if e == element:
#             occurance +=1
#     return occurance
# print(nooflist(test, 10))


#  Reverse of a string  abcd

# def reverse(string):
#     result = ""
#     for c in string:
#         result = c + result
#     return result

# print(reverse("abcd"))



#  Sum of List  [1, 5, 8, 6, 7, 2]

# def sumofList(list):
#     result = 0
#     for el in list:
#         result += el
#     return result

# print(sumofList([1,5,8,6,7,2]))


#  Biggest no in the list [10, 2, 5, 7, 15, 12]

# def sumofList(list):
#     result = 0
#     for el in list:
#         result += el
#     return result

# def biggestval(list):
#     biggest = list[0]
#     i = 1    
#     while i < len(list):
#         if biggest < list[i]:
#             biggest = list[i]
#             i=+1
#     return biggest


# #big = print(biggest([10, 2, 5, 7, 15, 12]))
# # print(big)
# print(biggestval([10, 2, 5, 7, 15, 12]))
# print()


#  Number of words in a string

# def noofWords(input):
#     if len(input) == 0:
#         return 0
#     count = 1
#     for c in input:
#         if c == " ":
#             count+=1
#     if input[len(input) - 1] == " ":
#         count -= 1
#     return count

# print(noofWords("asfd dfsdf df fdd sdfsd"))



# is prefix
# "abcde", "ab" => True
# "abcde", "bc" => False

# def isPrefix(input, prefix):
#     if len(input) < len(prefix):
#         return False
#     i = 0
#     while i < len(prefix):
#         if prefix[i] != input[i]:
#             return False
#         i += 1
#     return True

# print(isPrefix("abcde","ab"))
# print(isPrefix("abcdef","bc"))
        
        
# List is sorted or not
# [14, 12, 10, 9, 6] => True
# [10, 12, 9, 6, 14] => False

def isSorted(list):
    i = 0
    while i < len(list) - 1:
        if list[i] > list[i+1]:
            return False
        i += 1
    return True            
print(isSorted([10,6,9,8]))