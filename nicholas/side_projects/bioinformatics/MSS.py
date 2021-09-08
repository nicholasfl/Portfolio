import numpy
import re
from numpy import random

def MSS_naive(a):
    MSS_naive_a_n(a,len(a))

def MSS_naive_a_n(a, n):
    max_score = 0
    l = 1
    r = 0 
    array_additions = 0
    for i in range(n):
        for j in range(i,n+1):
            s = 0
            for k in range(i,j):
                s = s + a[k]
                array_additions += 1
            if (s > max_score):
                max_score = s
                l = i
                r = j
        
    print("Maximal Scoring Subsequence is from: {}-{} which gives a score of {}".format(l,r-1,max_score))
    print("array_additions:", array_additions)
    
def mod_MSS_naive(a,n):
    max_score = 0
    results = []
    l = 1
    r = 0 
    array_additions = 0
    for i in range(n):
        for j in range(i,n+1):
            s = 0
            for k in range(i,j):
                s = s + a[k]
                array_additions += 1
            if (s > max_score):
                max_score = s
                l = i
                r = j
    global_max_score = max_score
    for i in range(n):
        for j in range(i,n+1):
            s = 0
            for k in range(i,j):
                s = s + a[k]
                array_additions += 1
            if (s == global_max_score):
                results.append(i)
                results.append(j-1)
        
    return(results,global_max_score)

def maxsubseq(seq):
  return max((seq[begin:end] for begin in range(len(seq)+1)
                             for end in range(begin, len(seq)+1)),
             key=sum)

def SMSS_clever(a):
    return SMSS_clever_a_n(a, len(a))
            
def SMSS_clever_a_n(a,n):
    print ("FINDING THE SHORTEST MAXIMAL SCORING SUBSEQUENCE")
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
    min_length = 100
    shortest_results = []
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

            if((i - rstart + 1) < min_length):
                min_length = i - rstart + 1

    if (len(results) != 0):
        for i in range(0,len(results)):
            if(i % 2 == 0):
                length = results[i+1] - results[i] + 1
                if(length == min_length):
                    shortest_results.append(results[i])
                    shortest_results.append(results[i+1])

    print("SMSS: {}".format(shortest_results))

def linear_MSS(a,n):
    operationen = 0
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
            operationen += 1
        else:
            rmax = a[i]
            rstart = i 
            operationen += 1
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
            operationen += 1
    print("{}, {}, {}".format(l,r,max))
    print("operationen :", operationen)


def all_MSS_a_c(a, n):
    print("FINDING ALL MAXIMAL SCORING SUBSEQUENCES")
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
   
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

    print(results)

def all_MSS(a):
    return all_MSS_a_c(a, len(a))
    
def all_MSS_file(a):
    return all_MSS_file_a_n(a, len(a))

def all_MSS_file_a_n(a,n):
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
   
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

    f = open("C:/Users/N0009/Documents/VisualStudioCode/nicholas/AlgBio/MSS/results.txt","a")
    for elem in results:
        f.write(str(elem))
        f.write("\t")
    f.write(str(max))
    f.write("\n")
    f.close()
    print("file writing complete")
    print(results)

def dyn_MSS_a_n(a,n):
    operationen = 0
    matrix = [0] * n
    for i in range (n):
        matrix[i] = [0] * n
    maxscore = 0
    l = 1
    r = 0
    for i in range(0,n):
        for j in range(i,n):
            if(i == j):
                matrix[i][i] = a[i]
                operationen += 1
            else:
                matrix[i][j] = matrix[i][j-1] + a[j]
                operationen += 1
            if(matrix[i][j] > maxscore):
                maxscore = matrix[i][j]
                l = i
                r = j
                operationen += 1
    print("operationen: ",operationen)
    return (maxscore, l, r)

def dyn_MSS(a):
    return dyn_MSS_a_n(a, len(a))

def dc_MSS_a_n(a,i,j):
    if(i == j):
        if(a[i] > 0):
            return(a[i],i,i)
        else:
            return(0,i,i-1)
    else:
        m = int((i+j-1)/2)
        (s1,i1,j1) = dc_MSS_a_n(a,i,m)
        (s2,i2,j2) = dc_MSS_a_n(a,m+1,j)
        i3 = m
        s = a[i3]
        simax = s 
        for k in range((i3-1),i-1,-1):
            s = s + a[k]
            if(s > simax):
                simax = s
                i3 = k
        j3 = m + 1
        s = a[j3]
        sjmax = s
        for k in range((j3+1), j+1):
            s = s + a[k]
            if(s > sjmax):
                sjmax = s
                j3 = k
        s3 = simax + sjmax
        if(max([s1,s2,s3]) == s1):
            return (s1,i1,j1)
        elif(max([s1,s2,s3]) == s2):
            return(s2,i2,j2)
        else:
            return(s3,i3,j3)

def dc_MSS(a):
    print(dc_MSS_a_n(a,0,len(a)-1))

calculations = 0

def dc_MSS_count(a,i,j):
    global calculations
    if(i == j):
        if(a[i] > 0):
            return(a[i],i,i)
            calculations += 1
        else:
            return(0,i,i-1)
            calculations += 1
    else:
        m = int((i+j-1)/2)
        calculations += 1
        (s1,i1,j1) = dc_MSS_a_n(a,i,m)
        calculations += 1
        (s2,i2,j2) = dc_MSS_a_n(a,m+1,j)
        calculations += 1
        i3 = m
        s = a[i3]
        simax = s 
        for k in range((i3-1),i-1,-1):
            s = s + a[k]
            calculations += 1
            if(s > simax):
                simax = s
                i3 = k
        j3 = m + 1
        s = a[j3]
        sjmax = s
        for k in range((j3+1), j+1):
            s = s + a[k]
            calculations += 1
            if(s > sjmax):
                sjmax = s
                j3 = k
        s3 = simax + sjmax
        calculations += 1
        if(max([s1,s2,s3]) == s1):
            return (s1,i1,j1)
            calculations += 1
        elif(max([s1,s2,s3]) == s2):
            return(s2,i2,j2)
            calculations += 1
        else:
            return(s3,i3,j3)
            calculations += 1

def aLMSS_file(a):
    return aLMSS_file_a_n(a,len(a))

def aLMSS_file_a_n(a,n):
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
    max_length = 0
    longest_results = []
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

            if((i - rstart + 1) > max_length):
                max_length = i - rstart + 1

    if (len(results) != 0):
        for i in range(0,len(results)):
            if(i % 2 == 0):
                length = results[i+1] - results[i] + 1
                if(length == max_length):
                    longest_results.append(results[i])
                    longest_results.append(results[i+1])

    print("LMSS: {}".format(longest_results))
    f = open("C:/Users/N0009/Documents/VisualStudioCode/nicholas/AlgBio/MSS/results.txt","a")
    for elem in longest_results:
        f.write(str(elem))
        f.write("\t")
    f.write(str(max))
    f.write("\n")
    f.close()
    print("aLMSS file writing complete")
    print(longest_results)

def LMSS_file(a):
    return LMSS_file_a_n(a,len(a))

def LMSS_file_a_n(a,n):
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
    max_length = 0
    longest_results = []
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

            if((i - rstart + 1) > max_length):
                max_length = i - rstart + 1

    if (len(results) != 0):
        for i in range(0,len(results)):
            if(i % 2 == 0):
                length = results[i+1] - results[i] + 1
                if(length == max_length):
                    longest_results.append(results[i])
                    longest_results.append(results[i+1])
                    break

    print("LMSS: {}".format(longest_results))
    f = open("C:/Users/N0009/Documents/VisualStudioCode/nicholas/AlgBio/MSS/results.txt","a")
    for elem in longest_results:
        f.write(str(elem))
        f.write("\t")
    f.write(str(max))
    f.write("\n")
    f.close()
    print("LMSS file writing complete")
    print(longest_results)

def convert_to_list(string):
  print("string is {}".format(string))
  li = re.split(r'[\n\t\f\v\r ]+', string[1:(len(string) - 1)])
  for elem in li:
    if elem == '':
      li.remove(elem)
  print("list: ", li)
  for i in range(len(li)):
    li[i] = int(li[i])
  print (li)
  return li

def split(word):
    return [char for char in word]

def chr_convert_to_list(string):
  print("string is {}".format(string))
  li = split(string)
  for elem in li:
    if elem == '':
      li.remove(elem)
  for i in range(len(li)):
    if(li[i] == 'A'):
        li[i] = 5
    else:
        li[i] = -2
  return li
  
def chr_SMSS_clever_a_n(a,n):
    print ("FINDING THE SHORTEST MAXIMAL SCORING SUBSEQUENCE")
    results = []
    max = 0
    l = 1
    r = 0
    rmax = 0
    rstart = 1
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax > max):
            max = rmax
            l = rstart
            r = i
    print("{}, {}, {}".format(l,r,max))

    rmax = 0 
    rstart = 1
    min_length = 100
    shortest_results = []
    for i in range (0,n):
        if (rmax > 0):
            rmax = rmax + a[i]
        else:
            rmax = a[i]
            rstart = i 
        if (rmax == max):
            results.append(rstart)
            results.append(i)

            if((i - rstart + 1) < min_length):
                min_length = i - rstart + 1

    if (len(results) != 0):
        for i in range(0,len(results)):
            if(i % 2 == 0):
                length = results[i+1] - results[i] + 1
                if(length == min_length):
                    shortest_results.append(results[i])
                    shortest_results.append(results[i+1])

    print("SMSS: {}".format(shortest_results))


f = open("chr1.txt","r")
chr_list = []
for line in f:
    chr_list = chr_list + chr_convert_to_list(f.readline())
print(chr_list)
print(len(chr_list))
SMSS_clever(chr_list)
#rand_arr = random.randint(-5,3, size=(500))

#print("Test Array:",rand_arr)
print("")
#MSS_naive(rand_arr)
print("")
#all_MSS(rand_arr)
print("")
#SMSS_clever(rand_arr)
print("")
#print(dyn_MSS(rand_arr))
print("")
#dc_MSS(rand_arr)
print("")
#all_MSS_file(rand_arr)
print("")
#aLMSS_file(rand_arr)
print("")
#LMSS_file(rand_arr)
print("")
#print(mod_MSS_naive(rand_arr,len(rand_arr)))
print("")
#linear_MSS(rand_arr,len(rand_arr))
print("")
#dc_MSS_count(rand_arr,0,len(rand_arr)-1)
#print("calculations: ", calculations)