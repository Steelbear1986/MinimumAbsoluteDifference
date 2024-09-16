class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        s=max(arr)
        Dlina=len(arr)
        ans=[]
        j=0
        if len(arr)==2: return [arr]
        for i in range(1,Dlina):
            if arr[i]-arr[j]<s:
                ans=[[arr[j],arr[i]]]
                s=arr[i]-arr[j]
            elif  arr[i]-arr[j]==s:
                ans.append([arr[j],arr[i]])
            i+=1
            j+=1
        return ans