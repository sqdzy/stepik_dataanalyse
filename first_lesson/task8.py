workers = [['Ivan', 'Ivanov', 100000, 2], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]
for worker in workers:
    print(f"{worker[0]} {worker[1]} is {'junior' if worker[3] < 2 else ('middle' if 2 <= worker[3] <= 5 else 'senior')}")