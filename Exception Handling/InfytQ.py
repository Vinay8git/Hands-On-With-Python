# def find_average(mark_list):
#     try:
#         total = 0
#         for i in range(0, len(mark_list)):
#             total += mark_list[i]
#         marks_avg = total / len(mark_list)
#         return marks_avg
#     except Exception as err:
#         print(err)
#
#
# m_list = []
# print("Average marks:", find_average(m_list))
# # except Exception as err:
# #     print(err)

# def human_tower(no_of_people):
#     if(no_of_people==1):
#         return 1*(50)
#     else:
#         return no_of_people*(50)+human_tower(no_of_people-2)
# print("Total weight of human tower: ",human_tower(5))

def find_ten_substring(num_str):
    try:
        l = len(num_str)
        lt = list()
        for i in range(1, l - 1):
            for j in range(l - i + 1):
                wd = ""
                sum = 0
                for k in range(j, j + i):
                    wd = wd + num_str[k]
                    sum += int(num_str[k])
                if len(lt) == 10:
                    return lt
                if sum == 10:
                    lt.append(wd)

        return lt
    except Exception as err:
        print(err)


num_str = 0
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
# except Exception as err:
#     print(err)
