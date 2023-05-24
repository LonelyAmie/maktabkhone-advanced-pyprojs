import csv
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    
    with open(input_file_name) as f_in : 
        with open(output_file_name , 'w') as f_out :
            csv_w = csv.writer(f_out)
            csv_r = csv.reader(f_in)
            for line in csv_r : # iterates over each line of input file and calculates avg of each person
                    name = line[0]
                    results = list()
                    results.append (name)
                    for i in range(1,len(line)) :
                        line[i] = int(line[i])
                    avg = float(mean(line[1:]))
                    results.append(avg)
                    csv_w.writerow(results)
    
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f_in : 
        with open(output_file_name , 'w') as f_out :
            csv_w = csv.writer(f_out)
            csv_r = csv.reader(f_in) 
            my_list = []
            for line in csv_r : # iterates over each line of input file and calculates avg of each person
                    name = line[0]
                    for i in range(1,len(line)) :
                        line[i] = int(line[i])
                    avg = float(mean(line[1:]))
                    my_list.append((avg,name))
            # my_list.sort(key = lambda t : (-t[0],t[1]))
            my_list.sort()
            ########################################################
            for element in my_list: 
                new_element = (element[1] , element[0])
                csv_w.writerow(new_element)
                
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f_in : 
        with open(output_file_name , 'w') as f_out :
            csv_w = csv.writer(f_out)
            csv_r = csv.reader(f_in) 
            my_list = []
            for line in csv_r : # iterates over each line of input file and calculates avg of each person
                    name = line[0]
                    for i in range(1,len(line)) :
                        line[i] = int(line[i])
                    avg = float(mean(line[1:]))
                    my_list.append((avg,name))
            my_list.sort(key = lambda t : (-t[0],t[1]))
            ########################################################
            counter = 0
            for element in my_list: 
                new_element = (element[1] , element[0])
                csv_w.writerow(new_element)
                counter += 1
                if counter == 3 :
                    break

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f_in : 
        with open(output_file_name , 'w') as f_out :
            csv_w = csv.writer(f_out)
            csv_r = csv.reader(f_in) 
            my_list = []
            for line in csv_r : # iterates over each line of input file and calculates avg of each person
                    name = line[0]
                    for i in range(1,len(line)) :
                        line[i] = int(line[i])
                    avg = float(mean(line[1:]))
                    my_list.append((avg,name))
            # my_list.sort(key = lambda t : (-t[0],t[1]))
            my_list.sort()
            ########################################################
            counter = 0
            while counter != 3 :
                x = (my_list[counter][0],)
                csv_w.writerow(x)
                counter += 1

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f_in : 
        with open(output_file_name , 'w') as f_out :
            csv_w = csv.writer(f_out)
            csv_r = csv.reader(f_in) 
            avgs = []
            for line in csv_r : # iterates over each line of input file and calculates avg of each person
                    for i in range(1,len(line)) :
                        line[i] = int(line[i])
                    avgs.append(float(mean(line[1:])))
                    
            final_avg = (mean(avgs),)
            csv_w.writerow(final_avg)
            
    