import time
from sortedcontainers import SortedDict


number_of_accounts=10000

normal_dict={}
sorted_dict=SortedDict()


# Dictionary insert benchmark
start_time=time.perf_counter()

for account_id in range(number_of_accounts):

    normal_dict[account_id]=account_id

dict_insert_time=time.perf_counter()-start_time


# SortedDict insert benchmark
start_time=time.perf_counter()

for account_id in range(number_of_accounts):

    sorted_dict[account_id]=account_id

sorted_dict_insert_time=time.perf_counter()-start_time


print("Dictionary insert time:",dict_insert_time)
print("SortedDict insert time:",sorted_dict_insert_time)


# Dictionary search benchmark
start_time=time.perf_counter()

for account_id in range(number_of_accounts):

    account_id in normal_dict

dict_search_time=time.perf_counter()-start_time


# SortedDict search benchmark
start_time=time.perf_counter()

for account_id in range(number_of_accounts):

    account_id in sorted_dict

sorted_dict_search_time=time.perf_counter()-start_time


print("Dictionary search time:",dict_search_time)
print("SortedDict search time:",sorted_dict_search_time)


# Dictionary range query benchmark
start_time=time.perf_counter()

normal_range=[]

for account_id in normal_dict:

    if 4000<=account_id<=6000:
        normal_range.append(account_id)

dict_range_time=time.perf_counter()-start_time


# SortedDict range query benchmark
start_time=time.perf_counter()

sorted_range=list(
    sorted_dict.irange(
        minimum=4000,
        maximum=6000
    )
)

sorted_dict_range_time=time.perf_counter()-start_time


print("Dictionary range query time:",dict_range_time)
print("SortedDict range query time:",sorted_dict_range_time)

print("Number of results:",len(sorted_range))
