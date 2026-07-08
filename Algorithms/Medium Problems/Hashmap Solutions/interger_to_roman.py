class Solution:
    def intToRoman(self, num: int) -> str:
        translation_table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = ""

        for i in range(len(translation_table)):
            while num >= translation_table[i][0]:
                res += translation_table[i][1]
                num -= translation_table[i][0]

        return res
            
# July 8, 2026
# Documentary: You put the translation table for easy look up, then subtract it starting from the biggest number.
# Time Complexity: O(k + m)
# Space Complexity: O(1) or O(n) if res variable is accounted

# So could actually say its hashmap but same thing
class Solution:
    def intToRoman(self, num: int) -> str:
        translation_table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        res = ""

        for n, rom in translation_table.items():
            while num >= n:
                num -= n
                res += rom

        return res
