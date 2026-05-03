class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""

        if strs == []:
            return "None"

        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        if s == "None":
            return []

        return s.split("π")

#     def encode(self, strs: List[str]) -> str:
#         """
#         Encodes a string array into a single string

#         Args:
#             strs: list[str]

#         Returns:
#             encoded_string: str = The encoded string

#         Complexity:
#             Time: O(n)
#             Space: O(n)

#         """
        
#         encoded_string = ""
        
#         for string in strs:
#             encoded_string += str(len(string)) + "#" + string

#         return encoded_string

#     def decode(self, s: str) -> List[str]:
#         """
#         Decodes an encoded string into an array of strings

#         Args:
#             s: str = The encoded string

#         Returns:
#             original_strings: list[str] = The decoded version of a string

#         Complexity:
#             Time: O(n) 
#             Space: O(n)
#         """

#         # 3#cat4#ball
#         # L
#         # R

#         left = 0

#         original_strings = []

#         for right in range(len(s)):
#             if isinstance(int(s[right]), int):
#                 offset = int(s[right]) + 1  # The +1 is for the pound symbol
            
#             encoded_section = ""

#             while left <= right:
#                 encoded_section += s[left]
#                 left += 1 

#             right += 1

#             original_string = encoded_section[2:]

#             original_strings.append(original_string)

#         return original_strings
