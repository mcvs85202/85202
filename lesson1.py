def binary_search(data, left, right, target):
    if left > right:                                       
        return -1    
    middle = int((right-left) / 2 + left)                    
    if data[middle] > target:                               
        return binary_search(data, left, middle-1, target)
    elif data[middle] < target:                            
        return binary_search(data, middle+1, right, target)
    else:                                                   
        return middle
data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]         
data_count = len(data)
target = 16
found_index = binary_search(data, 0, data_count-1, target)  
    print('無法找到搜尋目標', target)
else:
    print('發現搜尋目標', target, ', 位於陣列中第', found_index, '個位置')