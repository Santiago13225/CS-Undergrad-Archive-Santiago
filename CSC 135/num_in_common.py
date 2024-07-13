num_pop = -72

l1 = [3, 7, 3, -1, 2, 3, 7, 2, 15, 15]
l2 = [-5, 15, 2, -1, 7, 15, 36]

def num_in_common(list1,list2):
    if len(list1) == 0 or len(list2) == 0:
        return 0
    else:
        #u_nums1 = {}
        a = []
        u_nums1 = set(a)
        
        #u_nums2 = {}
        b = []
        u_nums2 = set(b)
        
        #numbers1 = []
        #unique_nums = set(numbers1)
        for nums1 in list1:
            u_nums1.add(nums1)
            
        common = 0
        for nums2 in list2:
            u_nums2.add(nums2)
        
        for c_nums in u_nums2:
            if c_nums in u_nums1:
                common = common + 1

    return common
   
    #return count
return_value = num_in_common(l1,l2)

print('Number of common numbers: {}'.format(return_value))