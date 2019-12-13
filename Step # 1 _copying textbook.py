# 31번 : 역상보서열 만들기
"""seq = "AGTTTATAG"
rev_seq = seq[::-1]
# print(rev_seq)

revcomp_seq = ""
for s in rev_seq:
    if s == "A":
        revcomp_seq += "T"
    elif s == "T":
        revcomp_seq += "A"
    elif s == "G":
        revcomp_seq += "C"
    elif s == "C":
        revcomp_seq += "G"
print(seq)
print(revcomp_seq)"""

# 32번 : 문자열에 특정 문자가 있는지 확인 (C, T 의 여부 확인)
"""seq = "AGTTTATAG"
print("C" in seq)
print("T" in seq)"""

# 33번 : 문자열에서 특정 문자의 indwx 번호 출력 (모든 TT)
"""seq = "AGTTTATAG"
motif = "TT"
for i in range(len(seq)):
    if seq[i:i+len(motif)] == motif:
        print(i)"""
# index를 쓰면 맨 앞에 하나만 출력됨 (즉 2 하나만 출력)

# 34번 : 문자열에서 특정 문자 개수 세기
"""seq = "AGTTTATAG"
A = seq.count("A")
T = seq.count("T")
G = seq.count("G")
C = seq.count("C")

print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)"""

# 또는
"""seq = "AGTTTATAG"
count_dic = {}

for s in seq:
    if s in count_dic:
        count_dic[s] += 1
    else:
        count_dic[s] = 1 # <- 모르겠음

for k, v in count_dic.items():
    print("%s: %s" % (k,v))"""


# 35번 : 문자열에서 특정 문자를 다른 문자로 교체 (T -> U)
seq = "AGTTTATAG"
"""print(seq.replace("T", "U"))"""

# 또는
"""import Bio
from Bio.Seq import Seq
seq = Seq("AGTTTATAG")
print(Seq.transcribe(seq))"""


# 36번 : 문자열에서 단어 개수 세기
"""s = "Welcome to the Bioinformatics World!"
arr = s.split()
print(arr)
print(len(arr))"""

# 37번 : 제곱근 구하기
"""import math
n = 144
print(math.sqrt(144))
# 또는
print(math.pow(144, 0.5))
# 또는
print(n**0.5)"""


# 38번 : 주어진 수의 절댓값 구하기 (10, -15)
"""print(abs(-15))
# 또는
def get_absolute(n):
    if n>= 0:
        return n
    else:
        return -n
print(get_absolute(-15))"""


# 39번 : 주어진 수의 로그값 구하기 (2)
"""import math
print(math.log10(2))"""

# 40번 : 자연로그 구하기 (2)
"""import math
print(math.log(2))"""

# 41번
"""import math
print(math.log(81, 3))"""

# 42번 : 반올림
#print(round(62.77779, 2))

# 43번
#print(round(78654, -3))

# 44번 : 난수 만들기
"""from random import randint

for i in range(6):
    print(randint(1,45))"""
# 또는
"""from random import randrange

for i in range(6):
    print(randrange(1, 45+1)) # a 이상 b 미만의 범위에서 랜덤 """

# 45번 로또번호 생성기
"""from random import randint

arr_lotto = []

for i in range(6):
    n = randint(1, 45)
    if n not in arr_lotto:
        arr_lotto.append(n)
for i in sorted(arr_lotto):
    print(i)"""


# 46번 : 문자열에서 숫자만 골라내기
"""damaged_seq = "11A2TG3TT000AT1A2G"
seq = ""

for s in damaged_seq:
    if s.isalpha():
        seq += s
print(seq)"""
# 또는
"""import re
damaged_seq = "11A2TG3TT000AT1A2G"
match = re.findall(r'[a-zA-Z]', damaged_seq)

if match:
    print(''.join(match))"""


# 47번 : 리스트 길이 구하기
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(len(a))
print(len(b))"""

# 48번 : 리스트 n번째 출력
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(a[1]) # a 의 1+1번째 출력
print(b[1])"""

# 49번 : 리스트 슬라이싱
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(a[1:4])
print(b[1:4])"""

# 50번 : 리스트 건너뛰며 슬라이싱
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(a[::2])
print(b[1::2])"""

# 51번
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(a[::-1])
print(b[::-2])"""

# 52번 : 오름차순
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(sorted(a))
b.sort()
print(b)"""

# 53번 : 내림차순
"""a = [3, 5, 2, 1, 4]
b = [8, 10 ,7, 6, 9]
print(sorted(a, reverse=True))
b.sort(reverse=True)
print(b)"""


# 54번 : 리스트 요소 추가
"""a = ["leu", "Met", "Thr"]
a.append("Lys")
# 또는
a += ["Lys"]
print(a)"""

# 55번 : 리스트 특정위치에 요소 추가
"""a = ["leu", "Met", "Thr"]
a.insert(2, "Lys")
print(a)"""

# 56번 : 리스트 항목 제거
"""a = ["leu", "Met", "Thr"]
a.remove("Met")
# 또는
idx = a.index.("Met")
a.pop(idx)
print(a)"""

# 57번 : 리스트 특정 요소 갯수 세기
"""a = ["Leu", "Met", "Thr", "Thr", "Met", "Met"]
print(a.count("Met"))"""

# 58번 : 리스트 내부의 최댔값 구하기
"""a = [3, 5, 2, 1, 4]
print(max(a))
# 또는
max_val = a[0] # 리스트 맨 앞 값이 최속값이라 가정 (a[0]는 그냥 리스트 첫 번째 값)

for i in range(1, len(a)):
    if max_val < a[i]:
        max_val = a[i]"""

# 59번 : 리스트 내부의 최솟값 구하기
"""a = [3, 5, 2, 1, 4]
print(min(a))
# 또는
min_val = a[0]

for i in range(1, len(a)):
    if a[i] < min_val:
        min_val = a[i]

print(min_val)"""

"""참고
def minimum(list):
  current_min = list[0]  # Start by assuming the first number is smallest
  for num in list:       # Loop through each number in the list
    if num < current_min:
      current_min = num  # Update current_min if current number is less
  return current_min

print minimum([1,2,3,-1])"""

# 60번 : 리스트 내부의 모든 요소 합 구하기
"""a = [3, 5, 2, 1, 4]
sum_val = sum(a)
print(sum_val)
#또는
sum_val = 0
for i in a:
    sum_val += i
print(sum_val)"""

# 61번 : 리스트 내부 요소 평균 구하기
"""a = [3, 5, 2, 1, 4]
print(sum(a)/len(a))"""

# 62번 : 문자열의 특정 구분자를 기준으로 리스트 만들기
"""s = "a;b;c;d;e"
arr = s.split(";")
print(arr)"""

# 63번 : 리스트를 특정 구분자 기준으로 문자열 만들기
"""arr = ['a', 'b', 'c', 'd', 'e']
s = "특정_구분자_입니다".join(arr)
print(s)"""

# 64번 : 리스트 섞기
"""a = [1, 2, 3, 4, 5]
from random import shuffle
shuffle(a)
print(a)"""

# 65번 : 사전 길이 출력
"""d = d = {"Leu": 'L', "Met": 'M', "Ser": 'S'}
print(len(d))"""

# 66번 : 사전 만들기
"""d = {"Leu": 'L', "Met": 'M', "Ser": 'S'}
print(d)
#또는
d = {}
key_list = ["Leu", "Met", "Ser"]
value_list = ["L", "M", "S"]

for i in range(len(key_list)):
    d[key_list[i]] = value_list[i] # dictionary[key] = value
print(d)
"""

# 67번 : 사전의 특정 요소 지우기
"""d = {"Leu": 'L', "Met": 'M', "Ser": 'S'}
del d["Met"]
print(d)"""

# 68번 : 사전에 키값이 있는지 확인
"""d = {"Leu": 'L', "Met": 'M', "Ser": 'S'}
print("Met" in d)
print("Arg" in d)"""

# 69번 : 사전을 이용해 아미노산 서열 종류 개수 찾기
"""seq = "MLSSSMPPGGLACHADDDII"
d = {}
for s in seq:
    if s in d:
        d[s] += 1
    else :
        d[s] = 1
print(d)"""

# 70번 : 사전 키 출력
"""d = {'M' : 2, 'L' : 2, 'S' : 3, 'P' : 2, 'G' : 2, 'A' : 2, 'C' : 1, 'H' : 1, 'D' : 3, 'I' : 2}
for k in d.keys():
    print(k)"""

# 71번 : 사전 값 출력
"""d = {'M' : 2, 'L' : 2, 'S' : 3, 'P' : 2, 'G' : 2, 'A' : 2, 'C' : 1, 'H' : 1, 'D' : 3, 'I' : 2}
for v in d.values():
    print(v)"""

# 72번 : 사전-키 값 모두 출력
"""d = {'M' : 2, 'L' : 2, 'S' : 3, 'P' : 2, 'G' : 2, 'A' : 2, 'C' : 1, 'H' : 1, 'D' : 3, 'I' : 2}
for k, v in d.items():
    print(k, v)"""

# 73번 : 사전값을 기준으로 정렬
"""d = {'M' : 2, 'L' : 2, 'S' : 3, 'P' : 2, 'G' : 2, 'A' : 2, 'C' : 1, 'H' : 1, 'D' : 3, 'I' : 2}
d_sorted = sorted(d.items(), key=lambda v:v[1])
for k, v in d_sorted:
    print(k, v)"""

# 74번 : 세트 만들기
"""arr1 = ["Ala", "Phe", "Phe", "Cys", "Ala", "Gly"]
arr2 = ["Phe", "Gly", "Gly", "Val", "Val", "Phe"]
s1 = set(arr1)
s2 = set(arr2)
print(s1)
print(s2)"""

# 75번 : 세트 합집합 구하기
"""s1 = {'Phe', 'Gly', 'Cys', 'Ala'}
s2 = {'Val', 'Phe', 'Gly'}
print(s1.union(s2))"""

# 76번 : 세트 교집합 구하기
"""s1 = {'Phe', 'Gly', 'Ala', 'Cys'}
s2 = {'Val', 'Phe', 'Gly'}
print(s1.intersection(s2))"""

# 77번 : 세트 여집합 구하기
"""s1 = {'Phe', 'Gly', 'Ala', 'Cys'}
s2 = {'Val', 'Phe', 'Gly'}
print(s1-s2)"""

# 78번 : 튜플 만들기
"""essential_aminoacids = ["Val", "Leu", "Ile", "Met", "Thr", "Lys", "Phe", "Trp"]
t = tuple(essential_aminoacids)
print(t)
# 또는
eaa = ("Val", "Leu", "Ile", "Met", "Thr", "Lys", "Phe", "Trp")
print(eaa)
# 주의
t1 = ("Val")
print(t1) # Val
t2 = ("Val", )
print(t2) # ("Val", )"""

# 79번 : 튜플의 특성
"""t = ('Val', 'Leu', 'Ile', 'Met', 'Thr', 'Lys', 'Phe', 'Trp')
print(t[1:4])
print(t.index("Lys"))"""

# 80번 : 객체 만들기
"""class MyClass:
    pass
obj = MyClass()
print(type(obj))""" # <class '__main__.MyClass'>

# 81 : 객체의 속성
"""class MyClass:
    base = ["A", "T", "G", "C"]
    bass = ["hit", "the", "bass"]
obj = MyClass()
print(obj.base)
print(obj.bass)"""

# 82 : 객체의 매서드
"""class MyClass:
    def get_length(self, seq):
        return len(seq)

obj = MyClass()
seq = "ACGTACGT"
print(obj.get_length(seq))"""

# 83번 : 객체의 생성자(__int__)
"""class MyClass:
    def __init__(self):
        print("object created!")
        self.seq = ""
    def get_length(self):
        return len(self.seq)

obj = MyClass()
obj.seq = "ACGTACGT"
print(obj.get_length())"""

# 84번 : 객체의 소멸자(__del__)
"""class MyClass:
    def __init__(self):
        print("object created!")
        self.seq = ""
    def __del__(self):
        print("object deleted!")
    def get_length(self):
        return len(self.seq)
obj = MyClass()
del obj"""

# 85번 : 객체의 덧셈(__add__)
"""class MyClass:
    def __init__(self):
        self.seq = ""
    def __add__(self, other):
        return self.seq + other.seq
obj1 = MyClass()
obj2 = MyClass()
obj1.seq = "AAA"
obj2.seq = "TTT"

print(obj1 + obj2)"""

# 86번 : 객체의 비교 (__gt__) -> 왜 안대애애애애애애
"""class MyClass:
    def __init__(self):
        self.seq = ""
    def __gt__(self, other):
        if len(self.seq) > len(other.seq):
            return("%s is longer than %s." %(self.seq, other.seq)
        elif len(self.seq) < len(other.seq):
            return("%s is not longer than %s." %(self.seq, other.seq))
        else:
            return("The lenght is same.")
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()
obj1.seq = "AAA"
obj2.seq = "TTT"
obj3.seq = "GGG"
obj4.seq = "CC"

print(obj1 > obj2)
print(obj2 > obj3)
print(obj4 > obj3)"""

# 87번 : 재귀 알고리즘
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))"""

# 88번 : 동적계획법
"""arr = [0, 1]
def fibo(n):
    for i in range(n-1):
        arr.append(arr[-2] + arr[-1])
    return arr

print(fibo(10))"""

# 89번 : kmer 만들기
"""def mer(n, arr1, arr2):
    if n == 1:
        return arr2
    else:
        tmp = []
        for i in arr1:
            for j in arr2:
                tmp.append(i+j)
        arr2 = tmp
        n -= 1
        return mer(n, arr1, arr2)

arr1 = ["A", "C", "G", "T"]
arr2 = ["A", "C", "G", "T"]
print(mer(3, arr1, arr2))"""

# 90번 : palindrome 찾기
"""def palindrome_checker(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
        else:
            return True

s1 = "ACACA"
s2 = "ATTCA"
print(palindrome_checker(s1))
print(palindrome_checker(s2)) # 오류
"""
# 또는
"""def palindrome_checker(s):
    if s == s[::-1]:
        return True
    else:
        return False
s1 = "ACACA"
s2 = "ATTCA"
print(palindrome_checker(s1))
print(palindrome_checker(s2))"""

# 91 : FASTA 파일에서 염기 개수 세기

"""A, C, G, T = 0, 0, 0, 0
with open("Influenzavirus A (AduckShanghai12000) hemagglutinin gene, complete cds.fasta", "r") as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:

            A += line.count("A")
            C += line.count("C")
            G += line.count("G")
            T += line.count("T")
            
print("A", A)
print("C", C)
print("G", G)
print("T", T)"""

# 92번 : FASTA 에서 레코드 개수 세기
"""count = 0
with open("Pachira aquatica sample.fasta", "r") as fr:
    for line in fr:
        if line.startswith(">"):
            count += 1

print(count)"""

# 93번 : VCF에서 header ~ data 분리
"""header = ""
data = ""
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            header += line
        else:
            data += line
print(header)
print("")
print(data)"""

# 94번 : VCF파일에서 샘플 개수 세기
"""with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#CHROM"):
            print(len(line.split()) -9) # 8개의 필수 열 + 1개의 format"""

# 95 번 : VCF 파일에서 Filter 열 PASS만 골라내기기
"""cnt = 0
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            if l[6] == "PASS":
                cnt += 1
print(cnt)"""

# 96번 : VCF 파일에서 변이 개수 세기
"""variants = 0
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            variants += 1
print(variants)"""

# 97번 : VCF 파일에서 SNPm InDel 개수 세기
"""SNP = 0
Insertion = 0
Delition = 0
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            ref = l[3]
            alt = l[4]

            if len(ref) == len(alt):
                SNP += 1
            elif len(ref) > len(alt):
                Deletion += 1
            elif len(ref) < len(alt):
                Insertion += 1
print("SNP:", SNP)
print("Insertion:", Insertion)
print("Delition:", Delition)"""

# 98번 : VCF 파일에서 dsSNP에서 발견된 변이 개수 구하기
"""rs = 0
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            rsID = l[2]
            if rsID != ".":
                rs += 1
print(rs)"""

# 99번 : VCF 파일에서 Ts/Tv 비율 구하기
"""ts = 0 # A <-> G, c <-> T
tv = 0
with open("VCFsample.vcf", "r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split()
            ref = l[3]
            alt = l[4]
            if len(ref) == len(alt):
                if ref =="A":
                    if alt == "G":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "C":
                    if alt == "T":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "G":
                    if alt == "A":
                        ts += 1
                    else:
                        tv += 1
                elif ref == "T":
                    if alt == "C":
                        ts +=1
                    else:
                        tv += 1
print("trasnition:", ts)
print("transversion", tv)
print("ts/tv:", ts/tv) # 0.5"""
# ts/tv ratio
    # Randome sequence error: 0.5
    # Genome-wide: ~2.0-2.1
    # Exome: ~2.5-2.8
    # Coding: ~3.0-3.3

# 100번 : BED 파일이 담고 있는 전체 영역 구하기
"""length = 0
with open("sample.bed", "r") as fr:
    for line in fr:
        l = line.strip().split()
        start = int(l[1])
        end = int(l[2])
        lenght += end - start
print(length)"""