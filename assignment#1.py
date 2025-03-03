
def main():
    with open('jobs.txt', 'r') as file:
        num_jobs = int(file.readline())
        jobs = []
        for _ in range(num_jobs):
            weight, length = map(int, file.readline().split())

            # Append the weight and length as the key to sort by
            jobs.append((weight, length))


    # Sort the jobs by the (difference descending, weight descending)
    sorted_jobs = sorted(jobs, key=lambda x: (-(x[0] - x[1]), -x[0]))

    current_time = 0
    total_weighted_completion_time = 0

    for weight, length in sorted_jobs:
        current_time += length
        total_weighted_completion_time += weight * current_time

    print(total_weighted_completion_time)

if __name__ == '__main__':
    main()

# Output: 69119377652 correct!

# Time complexity: O(nlogn) where n is the number of jobs
# Space complexity: O(n) where n is the number of jobs
# This algorithm works by sorting the jobs by the difference of weight and length in descending order, and then by weight in descending order.
# It then iterates through the sorted jobs, calculating the weighted completion time for each job and adding it to the total weighted completion time.
# Finally, it prints the total weighted completion time.
# The algorithm has a time complexity of O(nlogn) due to the sorting step, and a space complexity of O(n) due to the storage of the sorted jobs.
# The algorithm correctly calculates the total weighted completion time for the given jobs



