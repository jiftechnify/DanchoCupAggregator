'''
Created on 2015/05/18

@author: jiftech
'''
import csv

if __name__ == '__main__':
    # read ticket number-inviter name list
    with open("ticket.csv", newline="") as num_name_file:
        reader = csv.reader(num_name_file)
        num_name_dic = {}
        for row in reader:
            num_name_dic[int(row[0])] = row[1]

    # aggrigate
    with open("visitor.csv", newline="") as visitor_file:
        reader = csv.reader(visitor_file)
        sumup_dic = {}
        for row in reader:
            inviter = num_name_dic[int(row[0])]
            if inviter in sumup_dic:
                sumup_dic[inviter] += 1
            else:
                sumup_dic[inviter] = 1

    # write result
    with open("result.csv", "w", newline="") as result_file:
        writer = csv.writer(result_file)
        for i in sorted(sumup_dic.keys()):
            writer.writerow([i, sumup_dic[i]])