import pandas as pd
from datetime import datetime
# import answers
profile_data = pd.read_csv('Answers/answers.csv', sep=',')


def get_matching_score(row_a, row_b):
    score = 0
    # location
    if row_a["Where are you from? (state-city)"] == row_b["Where are you from? (state-city)"]:
        score += 10
    # dorm
    if row_a["Do you know what dorm you want to live in yet?"] != "Undecided" and row_b["Do you know what dorm you want to live in yet?"] != "Undecided":
        if row_a["Do you know what dorm you want to live in yet?"] == row_b["Do you know what dorm you want to live i   n yet?"]:
            score += 40
        else:
            score -= 20
    # room temperature
    temperature_difference = abs(int(row_a["What is your ideal room temperature? (example : 75F)"][:-1]) - int(row_b["What is your ideal room temperature? (example : 75F)"][:-1]))
    if temperature_difference <= 3:
        score += 20
    elif temperature_difference <= 5:
        score += 10
    elif temperature_difference <= 10:
        score -= 15
    # sports
    if row_a["If so, what sport?"] == row_b["If so, what sport?"] and row_a["Do you want to be roommates with someone who plays the same sport?"] == "Yes" and row_b["Do you want to be roommates with someone who plays the same sport?"] == "Yes":
        score += 50
    # rushing
    if row_a["Do you intend on rushing?"] == row_b["Do you intend on rushing?"]:
        score += 10
    else:
        score -= 10
    # major
    if row_a["What's your intended major?"] == row_b["What's your intended major?"]:
        score += 20
    # cleanliness
    if row_a["How messy/clean do you intend on keeping the room?"] == "Very clean" and row_b["How messy/clean do you intend on keeping the room?"] == "Very clean" or "Clean":
        score += 10
    elif row_a["How messy/clean do you intend on keeping the room?"] == "Clean" and row_b["How messy/clean do you intend on keeping the room?"] == "Very clean" or "Clean" or "Enough to get by":
        score += 10
    elif row_a["How messy/clean do you intend on keeping the room?"] == "Enough to get by" and row_b["How messy/clean do you intend on keeping the room?"] == "Clean" or "Enough to get by" or "Messy":
        score += 10
    elif row_a["How messy/clean do you intend on keeping the room?"] == "Messy" and row_b["How messy/clean do you intend on keeping the room?"] == "Enough to get by" or "Messy":
        score += 10
    else:
        score -= 20
    # drinking
    if row_a["Do you drink socially?"] == "Yes" and row_b["Do you feel comfortable with having a roommate who drinks?"] == "No":
        score -= 40
    if row_b["Do you drink socially?"] == "Yes" and row_a["Do you feel comfortable with having a roommate who drinks?"] == "No":
        score -= 40
    # vaping
    if row_a["Do you vape?"] == "Yes" and row_b["Do you feel comfortable with having a roommate who vapes?"] == "No":
        score -= 40
    if row_b["Do you vape?"] == "Yes" and row_a["Do you feel comfortable with having a roommate who vapes?"] == "No":
        score -= 40
    # smoking
    if row_a["Do you smoke?"] == "Yes" and row_b["Do you feel comfortable with having a roommate who smokes?"] == "No":
        score -= 40
    if row_b["Do you smoke?"] == "Yes" and row_a["Do you feel comfortable with having a roommate who smokes?"] == "No":
        score -= 40
    # smoking weed
    if row_a["Do you smoke weed?"] == "Yes" and row_b["Do you feel comfortable with having a roommate who smokes weed?"] == "No":
        score -= 40
    if row_b["Do you smoke weed?"] == "Yes" and row_a["Do you feel comfortable with having a roommate who smokes weed?"] == "No":
        score -= 40
    if row_a["Do you smoke weed?"] == "Yes" and row_b["Do you smoke weed?"] == "Yes":
        score += 24
    # party
    if row_a["Do you party?"] == "Yes" and row_b["Do you party?"] == "Yes" or "Occasionally":
        score += 15
    if row_a["Do you party?"] == "Occasionally" and row_b["Do you party?"] == "Yes" or "Occasionally" or "No":
        score += 15
    if row_a["Do you party?"] == "No" and row_b["Do you party?"] == "Occasionally" or "No":
        score += 15
    # in or out
    if row_a["Do you prefer going out or staying in?"] == row_b["Do you prefer going out or staying in?"]:
        score += 20
    else:
        score -= 5
    # clubs
    a_clubs = list(row_a["What clubs interest you? Please list than as club1, club2, club3, ... alphabetically"].split(", "))
    b_clubs = list(row_b["What clubs interest you? Please list than as club1, club2, club3, ... alphabetically"].split(", "))
    for i in range(len(a_clubs)):
        if a_clubs[i] == b_clubs[i]:
            score += 15
    # politics
    if row_a["Do you mind matching with someone who shares your political views?"] == "Yes" or row_b["Do you mind matching with someone who shares your political views?"] == "Yes":
        if row_a["What best describes you politically"] != "Rather not say" or row_b["What best describes you politically"] != "Rather not say":
            if row_a["What best describes you politically"] != row_b["What best describes you politically"]:
                score -= 40
    if row_a["What best describes you politically"] == row_b["What best describes you politically"]:
        score += 20
    # time prep
    FMT = '%H:%M'
    # wake up time
    wake_up_time_row_a = row_a["What time do you typically get up in the morning?"]
    wake_up_time_row_b = row_b["What time do you typically get up in the morning?"]
    if wake_up_time_row_a > wake_up_time_row_b:
        wake_up_dif = abs(int((datetime.strptime(wake_up_time_row_a, FMT) - datetime.strptime(wake_up_time_row_b, FMT)).seconds / 3600))
    else:
        wake_up_dif = abs(int((datetime.strptime(wake_up_time_row_b, FMT) - datetime.strptime(wake_up_time_row_a, FMT)).seconds / 3600))
    if wake_up_dif <= 2:
        score += 15
    elif wake_up_dif <= 4:
        score += 5
    elif wake_up_dif <= 6:
        score -= 10
    else:
        score -= 20
    # sleep time
    sleep_time_row_a = row_a["What time do you typically go to bed?"]
    sleep_time_row_b = row_b["What time do you typically go to bed?"]
    if sleep_time_row_a > sleep_time_row_b:
        sleep_time_dif = abs(int((datetime.strptime(sleep_time_row_a, FMT) - datetime.strptime(sleep_time_row_b, FMT)).seconds / 3600))
    else:
        sleep_time_dif = abs(int((datetime.strptime(sleep_time_row_b, FMT) - datetime.strptime(sleep_time_row_a, FMT)).seconds / 3600))
    if sleep_time_dif <= 2:
        score += 30
    elif sleep_time_dif <= 4:
        score += 10
    elif sleep_time_dif <= 6:
        score -= 20
    else:
        score -= 40
    # sound
    if row_a["How quiet/loud do you want your room to be?"] == "Complete silence" and row_b["How quiet/loud do you want your room to be?"] == "Complete silence" or "Quiet":
        score += 10
    elif row_a["How quiet/loud do you want your room to be?"] == "Quiet" and row_b["How quiet/loud do you want your room to be?"] == "Complete silence" or "Quiet" or "Medium term":
        score += 10
    elif row_a["How quiet/loud do you want your room to be?"] == "Medium term" and row_b["How quiet/loud do you want your room to be?"] == "Quiet" or "Medium term" or "Noisy":
        score += 10
    elif row_a["How quiet/loud do you want your room to be?"] == "Noisy" and row_b["How quiet/loud do you want your room to be?"] == "Medium term" or "Noisy" or "Loud":
        score += 10
    elif row_a["How quiet/loud do you want your room to be?"] == "Loud" and row_b["How quiet/loud do you want your room to be?"] == "Noisy" or "Loud":
        score += 10
    else:
        score -= 20
    # guests
    if row_a["Do you intend on having people over in your room a lot?"] == "Yes" and row_b["Do you mind if there are constantly other people in your room?"] == "Yes":
        score += 20
    if row_a["Do you intend on having people over in your room a lot?"] == "Yes" and row_b["Do you mind if there are constantly other people in your room?"] == "No":
        score -= 30
    if row_b["Do you intend on having people over in your room a lot?"] == "Yes" and row_a["Do you mind if there are constantly other people in your room?"] == "Yes":
        score += 20
    if row_b["Do you intend on having people over in your room a lot?"] == "Yes" and row_a["Do you mind if there are constantly other people in your room?"] == "No":
        score -= 30

    return score
