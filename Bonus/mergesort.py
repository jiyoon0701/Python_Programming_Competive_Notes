'''
입력
10
2 5 3 4 8 7 -1 9 10 2

출력
-1 2 2 3 4 5 7 8 9 10

'''
def merge_sort(arr, N):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, N)

if __name__ == "__main__":
  N = int(input())
  arr = list(map(int, input().split()))
  merge_sort(arr,N)
  
  for i in range(len(arr)):
    print(arr[i], end = " ")
    