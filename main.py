# advent of code day one
# Joshua Whynot
# 12/12/23


def main():
    file = open("input.txt", "r")
    data = file.readlines()
    file.close()
    total_sum = 0
    num_string_arr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = 0
    for line in data:
        # change str nums to digits
        temp_str = ''
        temp_dict = {}
        for i in range(len(num_string_arr)):
            if num_string_arr[i] in line:
                #get starting index of substring
                start_index = find_substring(line, num_string_arr[i], temp_dict)
                #add to temp_dict
                temp_dict[start_index] = i + 1
                
                
        #get digits and add them and index to temp dict
        for i in range(len(line)):
            if line[i].isdigit():
                temp_dict[i] = int(line[i])

        #sort dict by key
        temp_dict = dict(sorted(temp_dict.items()))
        #get first and last element of dict
        first = str(list(temp_dict.values())[0])
        last = str(list(temp_dict.values())[-1])
        #join two digits together
        temp_str = first + last
        print(temp_str)
        #add to total sum
        total_sum = total_sum + num

    #output
    print(total_sum)

                

        
        
#function to find substring and return starting index 
def find_substring(string, substring, dictionary):
    for i in range(len(string)):
        if string[i] == substring[0]:
            #check key from dict to see if index is already present in dictionary, skip this so we dont stop searching at something we already found
            if i in dictionary:
                continue
            if string[i:i+len(substring)] == substring:
                return i
    return -1
                
if __name__ == "__main__":
    main()
