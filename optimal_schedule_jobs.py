
def optionally_schedule_jobs():
    """
    Greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length).
    :return: positive int -> sum of weighted completion times of the resulting schedule
    """
    with open('jobs.txt', 'r') as file:
        nums_of_jobs = int(file.readline())
        jobs = []
        for i in range(nums_of_jobs):
            weight, length = map(int, file.readline().split())
            jobs.append((weight, length))


    # Decreasing ratio of Weight & Length
    jobs.sort(key=lambda x: x[0] / x[1], reverse=True)

    current_time = 0
    sum_of_completion_times = 0

    for weight, length in jobs:
        current_time += length
        sum_of_completion_times += weight * current_time

    print(f"Sum of completion times: {sum_of_completion_times}")

if __name__ == '__main__':
    optionally_schedule_jobs()


