def build_list_Stack_Operations(target, n):
        result = []
        curr = n

        for i in target:
            result.extend(["Push", "Pop"]*(i - curr))
            result.append("Push")
            curr = i + 1
            
        return result
    
print(build_list_Stack_Operations([1, 2, 3], 3))
