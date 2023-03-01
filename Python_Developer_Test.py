import random

# we define five variables each of which represent a list of all dress colours for the week
monday = ['GREEN','YELLOW','GREEN','BROWN','BLUE','PINK','BLUE','YELLOW','ORANGE','CREAM','ORANGE','RED','BLUE',
          'WHITE','BLUE','BLUE','BLUE','GREEN']

tuesday = ['ARSH','BROWN','GREEN','BROWN','BLUE','BLUE','BLUE','PINK','PINK','ORANGE','ORANGE','RED','WHITE','BLUE',
           'WHITE','WHITE','BLUE','BLUE','BLUE']

wednesday = ['GREEN','YELLOW','GREEN','BROWN','BLUE','PINK','RED','YELLOW','ORANGE','RED','ORANGE','RED','BLUE','BLUE',
             'WHITE','BLUE','BLUE','WHITE','WHITE']

thursday = ['BLUE','BLUE','GREEN','WHITE','BLUE','BROWN','PINK','YELLOW','ORANGE','CREAM','ORANGE','RED','WHITE',
            'BLUE','WHITE','BLUE','BLUE','BLUE','GREEN']

friday = ['GREEN','WHITE','GREEN','BROWN','BLUE','BLUE','BLACK','WHITE','ORANGE','RED','RED','RED','WHITE','BLUE',
          'WHITE','BLUE','BLUE','BLUE','WHITE']

# we concatenate all the dress colors into a single list
all_dress_colors = monday + tuesday + wednesday + thursday + friday
print(all_dress_colors)

# analyzing the data
# count the occurrences of each color using a dictionary
dress_color_data = {}
for color in all_dress_colors:
    if color not in dress_color_data:
        dress_color_data[color] = 1
    else:
        dress_color_data[color] += 1
print(dress_color_data)


# QUESTION 1

# calculate the mean color of dress
max_count = 0
for color, count in dress_color_data.items():
    if count > max_count:
        max_count = count
        mean_color = color
print(f"The mean color of dress is : {mean_color}")



# QUESTION 2

# To check for the color mostly worn for the week, we use our dress_color_data
most_worn_color_count = 0
for color, count in dress_color_data.items():
    if count > most_worn_color_count:
        most_worn_color_count = count
        most_worn_color = color

print(f"The color mostly worn throughout the week is {most_worn_color}")


# QUESTION 3

# To find the median color, we have to sort all our colors first
sorted_dress_colors = sorted(all_dress_colors)

# find the median colors
n = len(sorted_dress_colors)

# check if the no of sorted colors is even, if it is, we then take the average of the two middle colors
if n % 2 == 0:
    median_index_1 = n // 2 - 1
    median_index_2 = n // 2
    median_color_1 = sorted_dress_colors[median_index_1]
    median_color_2 = sorted_dress_colors[median_index_2]
    median_colors = [median_color_1, median_color_2]
    if median_colors[0] == median_colors[1]:
        print(f"The median color is {median_colors[0]}")
    else:
        print(f"The median colors are {median_colors}")
else:
    # if the no of sorted colors is odd, we take the middle color
    median_index = n // 2
    median_color = sorted_dress_colors[median_index]
    print(f"The median color is {median_color}")


#  QUESTION 4

# To get the variance of the colors, we need to know its formula and also calculate the mathematical mean of the 
# shirt colors
mean_color = sum(dress_color_data.values()) / len(dress_color_data)

# calculate the variance
variance = sum((x - mean_color)**2 for x in dress_color_data.values()) / (len(dress_color_data))-1
print(f"The variance of the colors is {variance}")


# QUESTION 5

# To calculate the probability that the color chosen at random is red
# count the no of times red appears in the list of colors

red_count = all_dress_colors.count('RED')
probability_red = red_count / len(all_dress_colors)
print(f"The probability that a randomly chosen color is red is : {probability_red}")


# QUESTION 7
def recursive_search(numbers_list, target_number):
    if not numbers_list:
        return False
    elif numbers_list[0] == target_number:
        return True
    return recursive_search(numbers_list[1:], target_number)


# QUESTION 8

# Generate a random 4 digit number consisting of 0s and 1s
binary_num = ''
for i in range(4):
    binary_num += str(random.randint(0,1))

# convert binary number to base 10
decimal_num = int(binary_num,2)
print(f"The binary number is : {binary_num}")
print(f"The base 10 equivalent is : {decimal_num}")


# QUESTION 9

# A program to sum the first 50 fibonacci sequence

# Define the first two fibonacci numbers
a,b = 0,1

# initialize a total variable
total = 0

for i in range(50):
    total += a
    a,b = b, a+b

print(f"The sum of the first 50 fibonacci numbers is : {total}")
