count = 0

with open("2025-02-05_9num/9.txt", "r") as file:
    for _ in range(16000):
        line = file.readline()
        line = list(map(int, line.split()))  # from tables to list
        
        # first condition
        if (sum(line) - max(line)) >= max(line):
            
            # second condition
            for num in line:
                if line.count(num) > 1:
                    continue
            
        count += 1
        print(line)


print(count)
