
############################################     DETERMINING # OF LOOPS        ##################################################  
fill_arr = 125       # TEST VALUE
samp_arr_raw = []      # TEST VALUE
for fa in range(fill_arr):      # TEST VALUE
    samp_arr_raw.append(fa)      # TEST VALUE

print("Sample Array Raw is: ", samp_arr_raw)

samp_len_25 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_50 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_75 = 0                                                 # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_100 = 0                                                # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len_125 = 0                                                # if this is 0 & loop does not get updated by if statement, loop will not execute.
samp_len = len(samp_arr_raw)
print("Sample Length is: ", samp_len)

if samp_len <= 25:                                                                      # if the array length is less than 25
    print("Sample array length is less than 25 samples.")
    samp_len_25 = samp_len                                                              # Set the numeric sample length to variable samp_len_25 to use for the loop
    print("samp_len_25 is: ", samp_len_25, ". Therefore 0 outer loops.")
elif samp_len > 25 and samp_len <= 50:                                                  # if the array length is between 26 and 50, prob most common
    print("Sample array length is between 26 and 50 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = samp_len - 25                                                         # second inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50, ". Therefore 1 outer loop.")
elif samp_len > 50 and samp_len <= 75:                                                  # if the array length is between 51 and 75
    print("Sample array length is between 51 and 75 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = samp_len - 50                                                         # third inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ". Therefore 2 outer loops.")
elif samp_len > 75 and samp_len <= 100:                                                 # this is for scalability. If the array length is between 76 and 100
    print("Sample array length is between 76 and 100 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = 25                                                                    # third inner loop
    samp_len_100 = samp_len - 75                                                        # fourth inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ", samp_len_100 is: ", samp_len_100)
    print("Therefore 3 outer loops.")
elif samp_len > 101 and samp_len <= 125:                                                # this is for scalability. If the array length is between 101 and 125
    print("Sample array length is between 101 and 125 samples.")
    samp_len_25 = 25                                                                    # first inner loop
    samp_len_50 = 25                                                                    # second inner loop
    samp_len_75 = 25                                                                    # third inner loop
    samp_len_100 = 25                                                                   # fourth inner loop
    samp_len_125 = samp_len - 100                                                       # fifth inner loop
    print("samp_len_25 is: ", samp_len_25, ", samp_len_50 is: ", samp_len_50)
    print("samp_len_75 is: ", samp_len_75, ", samp_len_100 is: ", samp_len_100)
    print("samp_len_125 is: ", samp_len_125, ", Therefore 4 outer loops.")
else:
    print("Too many samples, software not configured for this.")

index_015 = 0                                                   # count is for the sample index, naming each sample based on the array. Initiate only once and don't reset.
index_040 = 0                                                   # count is for the sample index, naming each sample based on the array. Initiate only once and don't reset.
for len25_015 in range(samp_len_25):                                                      # will loop from 0 to samp_len_25
    print("Testing the 015 for loop of len25.", len25_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    index_015 +=1
for len25_040 in range(samp_len_25):                                                      # will loop from 0 to samp_len_25
    print("Testing the 040 for loop of len25.", len25_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    index_040 +=1


for len50_015 in range(samp_len_50):                                                      # will loop from 0 to samp_len_50
    print("Testing the 015 for loop of len50.", len50_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    index_015 +=1
for len50_040 in range(samp_len_50):                                                      # will loop from 0 to samp_len_50
    print("Testing the 040 for loop of len50.", len50_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    index_040 +=1


for len75_015 in range(samp_len_75):                                                      # will loop from 0 to samp_len_75
    print("Testing the 015 for loop of len75.", len75_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    index_015 +=1
for len75_040 in range(samp_len_75):                                                      # will loop from 0 to samp_len_75
    print("Testing the 040 for loop of len75.", len75_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    index_040 +=1


for len100_015 in range(samp_len_100):                                                    # will loop from 0 to samp_len_100
    print("Testing the 015 for loop of len100.", len100_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    index_015 +=1
for len100_040 in range(samp_len_100):                                                    # will loop from 0 to samp_len_100
    print("Testing the 040 for loop of len100.", len100_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    index_040 +=1


for len125_015 in range(samp_len_125):                                                    # will loop from 0 to samp_len_125
    print("Testing the 015 for loop of len125.", len125_015)
    print("Index 015 test: ", samp_arr_raw[index_015])
    index_015 +=1
for len125_040 in range(samp_len_125):                                                    # will loop from 0 to samp_len_125
    print("Testing the 040 for loop of len125.", len125_040)
    print("Index 040 test: ", samp_arr_raw[index_040])
    index_040 +=1
