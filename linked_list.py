'''
# 20250905
# https://leetcode.cn/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# 383. 赎金信
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

    示例 1：

    输入：ransomNote = "a", magazine = "b"
    输出：false
    示例 2：

    输入：ransomNote = "aa", magazine = "ab"
    输出：false
    示例 3：

    输入：ransomNote = "aa", magazine = "aab"
    输出：true
'''

def judgeRansomeNoteIsComposedByMagazine(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    magazineDict = {}
    for char in magazine:
        if char in magazineDict:
            magazineDict[char] += 1
        else:
            magazineDict[char] = 1
    for char in ransomNote:
        if char not in magazineDict:
            return False
        else:
            magazineDict[char] -= 1
            if magazineDict[char] < 0:
                return False
    return True

if __name__ == "__main__":
    ransomNote = "aac"
    magazine = "aab"
    print(judgeRansomeNoteIsComposedByMagazine(ransomNote, magazine))
