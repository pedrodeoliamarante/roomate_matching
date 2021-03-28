# work in progress
# import pandas as pd
#
# # import answers
# profile_data = pd.read_csv('Answers/answers.csv', sep=',')
#
# # creating the dictionary that will contain all profiles
# profiles_dict = {}
#
# # iterating though every row and storing their columns in variables to create the profile string
# for index, row in profile_data.iterrows():
#     # creating info variables
#     ig_handle = row["what is your instagram handle? (@handle)"]
#     snap_handle = row["what is your snapchat? (@handle)"]
#     name = row["What is your name?"]
#     city = row["Where are you from? (state-city)"]
#     # dorm_preference variable can be either a dorm or not decided
#     if row["Do you know what dorm you want to live in yet?"] == "Undecided":
#         dorm_preference = name + " is still undecided in relation to dorms."
#     else:
#         dorm_preference = name + " wants to go to " + row["Do you know what dorm you want to live in yet?"] + "."
#     # pronouns must be divided into subject and object pronoun
#     pronouns_list = row["What are your pronouns? (subject/object)"].rsplit("/")
#     subject_pronoun = pronouns_list[0]
#     object_pronoun = pronouns_list[1]
#     room_temp = row["What is your ideal room temperature? (example : 75F)"]
#
#
#
#
#
#
#
#     # profile string
#     profile_string = name + " is from " + city + ". His instagram handle is " + ig_handle + " and his snapchat is " + snap_handle + ". " + dorm_preference
#     # creating the key value pairs, using ig handle as key because it is unique
#     profiles_dict[ig_handle] = profile_string
#
# print(profiles_dict)
