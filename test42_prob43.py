# 1~n整数中1的出现次数

# 解法一
# 缺点是: 时间复杂度是nlogn
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        num = 0
        for i in range(1, n + 1):
            while i:
                if i % 10 == 1:
                    num += 1
                i = i // 10

        return num


# s = Solution1()
# print(s.NumberOf1Between1AndN_Solution(30000))


# O(logn)的解法
class Solution2:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        count = 0
        i = 1

        while n // i != 0:
            # 当前位数字
            current = (n // i) % 10
            # 高位数字
            high = n // (i * 10)
            # 低位数字
            low = n - (n // i) * i

            if current == 0:
                count += high * i
            elif current == 1:
                count += high * i + low + 1
            else:
                count += (high + 1) * i
            i *= 10

        return count


# 主要思路：设定整数点（如1、10、100等等）作为位置点i（对应n的各位、十位、百位等等），分别对每个数位上有多少包含1的点进行分析
# 根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
# 当i表示百位，且百位对应的数>=2,如n=31456,i=100，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31），每一次都包含100个连续的点，即共有(a%10+1)*100个点的百位为1
# 当i表示百位，且百位对应的数为1，如n=31156,i=100，则a=311,b=56，此时百位对应的就是1，则共有a%10(最高两位0-30)次是包含100个连续点，当最高两位为31（即a=311），本次只对应局部点00~56，共b+1次，所有点加起来共有（a%10*100）+(b+1)，这些点百位对应为1
# 当i表示百位，且百位对应的数为0,如n=31056,i=100，则a=310,b=56，此时百位为1的次数有a/10=31（最高两位0~30）
# 综合以上三种情况，当百位对应0或>=2时，有(a+8)/10次包含所有100个点，还有当百位为1(a%10==1)，需要增加局部点b+1

# 之所以补8，是因为当百位为0，则a/10==(a+8)/10，当百位>=2，补8会产生进位位，效果等同于(a/10+1)

# 这一解法和解法二的思想是一样的,只是将两种情况合并了, 并且将第三种情况的判断语句写成了一行
class Solution3:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        count, m = 0, 1
        while m <= n:
            count += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return count

# s = Solution3()
# print(s.NumberOf1Between1AndN_Solution(18))
