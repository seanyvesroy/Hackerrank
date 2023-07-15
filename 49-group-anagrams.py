class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        check = {}
        count = 0

        for word in strs:
            srt = sorted(word)
            if str(srt) not in check:
                check[str(srt)] = count
                output.append([word])
                count += 1
            elif str(srt) in check:
                output[check[str(srt)]].append(word)
        
        return output
