nums1= [4,1,2,3,4]
nums2 = [2,2]

out=[]
j =0
if len(nums1) > len(nums2):
    for i in range(len(nums2)):
        if nums2[i] in nums1:
            out.append(nums2[i])
            nums1.remove(nums2[i])
else:
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            out.append(nums1[i])
            nums2.remove(nums1[i])
print(out)
