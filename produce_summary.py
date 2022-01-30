def produce_summary(day_number):
# for i in range(1,4):
    if day_number <4 and day_number >0:
        i = day_number
        print(f"Day {i}")
        the_file = open(f"um-deliveries-day-{i}.txt")
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            melon, count, amount = words
            print(f"Delivered {count} {melon}s for total of ${amount}")
        the_file.close()
    else:
        print("Please enter a day between 1 and 3")

produce_summary(2)



# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
