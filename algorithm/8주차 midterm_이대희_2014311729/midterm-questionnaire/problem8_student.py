def main():
    # Get three integers N, K and M
    n, k, m = [int(v) for v in input().split(' ')]
    # N integers, each between 1 and K, the indices of videos the students start watching
    start_index = [int(v) for v in input().split(' ')]
    # K integers, each between 1 and K, the index of the first similar video for each video
    similar_video_index = [int(v) for v in input().split(' ')]

    # Write down your code here
    result =[0]*n
    
    for j in range(n):
        i = start_index[j]-1
        for l in range(m-1):
            result[j] = similar_video_index[i]
            i = result[j]
    for k in range(n):
        print(result[k], end= ' ')
main()
