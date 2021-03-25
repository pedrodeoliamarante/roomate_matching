import pandas as pd

profile_data = pd.read_csv('Answers/answers.csv', sep=',')

profiles_dict = {}

for index, row in profile_data.iterrows():
    ig_handle = str(row["what is your instagram handle? (@handle)"])
    snap_handle = str(row["what is your snapchat? (@handle)"])
    name = str(row["What is your name?"])
    city = str(row["Where are you from? (state-city)"])
    if str(row["Do you know what dorm you want to live in yet?"]) == "Undecided":
        dorm_preference = name + " is still undecided in relation to dorms."
    else:
        dorm_preference = name + " wants to go to " + str(row["Do you know what dorm you want to live in yet?"]) + "."
    profile_string = name + " is from " + city + ". His instagram handle is " + ig_handle + " and his snapchat is " + snap_handle + ". " + dorm_preference
    profiles_dict[ig_handle] = profile_string

print(profiles_dict)