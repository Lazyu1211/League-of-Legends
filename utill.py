import pandas as pd
PATH = "/Users/junyuwu/League Of Legends NA/components/NAmatch.csv"
df = pd.read_csv(PATH)
df.drop(columns="Unnamed: 0", inplace=True)
df["side"] = df["side"].str.split(".", expand=True)[1]
df["role"] = df["role"].str.split(".", expand=True)[1]
df["kda"] = df["kda"].round(2)
df["result"] = df["result"].astype(str)
df["result"].replace({"True":1, "False":0}, inplace=True)

def get_winlist():
    win = df[df["result"]==1]["champion"].value_counts().to_frame()
    win.reset_index(inplace= True)
    win.rename(columns={"index":"champion", "champion":"win_num"}, inplace=True)
    lose = df[df["result"]==0]["champion"].value_counts().to_frame()
    lose.reset_index(inplace= True)
    lose.rename(columns={"index":"champion", "champion":"lose_num"}, inplace=True)
    merged_df = pd.merge(win, lose, on='champion', how='left')
    merged_df["total_game"] = merged_df["win_num"]+ merged_df["lose_num"]
    merged_df["winrate"] = (merged_df["win_num"]/merged_df["total_game"]).round(2)
    win10 = merged_df[merged_df["total_game"] > 60].sort_values(by="winrate", ascending=False)[:10]
    win_list = sorted(list(set(win10["champion"].tolist())))
    return win_list

def get_winrate():
    win = df[df["result"]==1]["champion"].value_counts().to_frame()
    win.reset_index(inplace= True)
    win.rename(columns={"index":"champion", "champion":"win_num"}, inplace=True)
    lose = df[df["result"]==0]["champion"].value_counts().to_frame()
    lose.reset_index(inplace= True)
    lose.rename(columns={"index":"champion", "champion":"lose_num"}, inplace=True)
    merged_df = pd.merge(win, lose, on='champion', how='left')
    merged_df["total_game"] = merged_df["win_num"]+ merged_df["lose_num"]
    merged_df["winrate"] = (merged_df["win_num"]/merged_df["total_game"]).round(2)
    win10 = merged_df[merged_df["total_game"] > 60].sort_values(by="winrate", ascending=False)[:10]
    return win10

def get_loselist():
    win = df[df["result"]==1]["champion"].value_counts().to_frame()
    win.reset_index(inplace= True)
    win.rename(columns={"index":"champion", "champion":"win_num"}, inplace=True)
    lose = df[df["result"]==0]["champion"].value_counts().to_frame()
    lose.reset_index(inplace= True)
    lose.rename(columns={"index":"champion", "champion":"lose_num"}, inplace=True)
    merged_df = pd.merge(win, lose, on='champion', how='left')
    merged_df["total_game"] = merged_df["win_num"]+ merged_df["lose_num"]
    merged_df["winrate"] = (merged_df["win_num"]/merged_df["total_game"]).round(2)
    lose10 = merged_df[merged_df["total_game"] > 60].sort_values(by="winrate", ascending=True)[:10]   
    lose_list = sorted(list(set(lose10["champion"].tolist())))
    return lose_list

def get_loserate():
    win = df[df["result"]==1]["champion"].value_counts().to_frame()
    win.reset_index(inplace= True)
    win.rename(columns={"index":"champion", "champion":"win_num"}, inplace=True)
    lose = df[df["result"]==0]["champion"].value_counts().to_frame()
    lose.reset_index(inplace= True)
    lose.rename(columns={"index":"champion", "champion":"lose_num"}, inplace=True)
    merged_df = pd.merge(win, lose, on='champion', how='left')
    merged_df["total_game"] = merged_df["win_num"]+ merged_df["lose_num"]
    merged_df["winrate"] = (merged_df["win_num"]/merged_df["total_game"]).round(2)
    lose10 = merged_df[merged_df["total_game"] > 60].sort_values(by="winrate", ascending=True)[:10]
    return lose10

def get_win_lose():
    win = df[df["result"]==1]["champion"].value_counts().to_frame()
    win.reset_index(inplace= True)
    win.rename(columns={"index":"champion", "champion":"win_num"}, inplace=True)
    lose = df[df["result"]==0]["champion"].value_counts().to_frame()
    lose.reset_index(inplace= True)
    lose.rename(columns={"index":"champion", "champion":"lose_num"}, inplace=True)
    merged_df = pd.merge(win, lose, on='champion', how='left')
    merged_df["total_game"] = merged_df["win_num"]+ merged_df["lose_num"]
    merged_df["winrate"] = (merged_df["win_num"]/merged_df["total_game"]).round(2)
    return merged_df

def get_dspell():
    dspell = df.groupby("result")["d_spell"].sum().to_frame()
    dspell.rename(index={0: "Lose",1:"Win"}, inplace=True)
    return dspell

def get_fspell():
    fspell = df.groupby("result")["f_spell"].sum().to_frame()
    fspell.rename(index={0: "Lose",1:"Win"}, inplace=True)
    return fspell

def get_red():
    redwinrate = df[df["side"]=="red"]["result"].value_counts()
    redwinrate.rename(index={0: "Lose",1:"Win"}, inplace=True)
    return redwinrate

def get_blue():
    bluewinrate = df[df["side"]=="blue"]["result"].value_counts()
    bluewinrate.rename(index={0: "Lose",1:"Win"}, inplace=True)
    return bluewinrate

def get_rolelist():
    bywinrole = df[df["result"]==1]["role"].value_counts().to_frame()
    bywinrole.reset_index(inplace=True)
    bywinrole.rename(columns={"index":"role_position","role":"win games"}, inplace= True)
    rolelist = sorted(list(set(bywinrole["role_position"].tolist())))
    return rolelist

def get_winrole():
    bywinrole = df[df["result"]==1]["role"].value_counts().to_frame()
    bywinrole.reset_index(inplace=True)
    bywinrole.rename(columns={"index":"role_position","role":"win games"}, inplace= True)
    return bywinrole

def get_loserole():
    byloserole = df[df["result"]==0]["role"].value_counts().to_frame()
    byloserole.reset_index(inplace=True)
    byloserole.rename(columns={"index":"role_position","role":"lose games"}, inplace= True)
    return byloserole

def get_assists():
    byass = df.groupby("result")["assists"].mean().round(2).to_frame()
    byass = byass.reset_index().rename_axis(None, axis=1)
    byass = byass.rename(columns={"result": "game_result", "assists":"average_assists"})
    byass.iloc[0,0] = "Lose"
    byass.iloc[1,0] = "Win"
    return byass

def get_kda():
    bykda = df.groupby("result")["kda"].mean().round(2).to_frame()
    bykda = bykda.reset_index().rename_axis(None, axis=1)
    bykda = bykda.rename(columns={"result": "game_result", "kda":"average_kda"})
    bykda.iloc[0,0] = "Lose"
    bykda.iloc[1,0] = "Win"
    return bykda

def get_kills():
    bykills = df.groupby("result")["kills"].mean().round(2).to_frame()
    bykills = bykills.reset_index().rename_axis(None, axis=1)
    bykills = bykills.rename(columns={"result": "game_result", "kills":"average_kills"})
    bykills.iloc[0,0] = "Lose"
    bykills.iloc[1,0] = "Win"
    return bykills

def get_death():
    bydeath = df.groupby("result")["deaths"].mean().round(2).to_frame()
    bydeath = bydeath.reset_index().rename_axis(None, axis=1)
    bydeath = bydeath.rename(columns={"result": "game_result", "deaths":"average_death"})
    bydeath.iloc[0,0] = "Lose"
    bydeath.iloc[1,0] = "Win"
    return bydeath

def get_level():
    bylevel = df.groupby("result")["level"].mean().round().to_frame()
    bylevel = bylevel.reset_index().rename_axis(None, axis=1)
    bylevel = bylevel.rename(columns={"result": "game_result", "level":"average_level"})
    bylevel.iloc[0,0] = "Lose"
    bylevel.iloc[1,0] = "Win"
    return bylevel

def get_timecc():
    bytime_cc = df.groupby("result")["time_cc"].mean().round(2).to_frame()
    bytime_cc = bytime_cc.reset_index().rename_axis(None, axis=1)
    bytime_cc = bytime_cc.rename(columns={"result": "game_result", "time_cc":"average_time_cc"})
    bytime_cc.iloc[0,0] = "Lose"
    bytime_cc.iloc[1,0] = "Win"
    return bytime_cc

def get_damage_total():
    bydamage_total = df.groupby("result")["damage_total"].mean().round(2).to_frame()
    bydamage_total = bydamage_total.reset_index().rename_axis(None, axis=1)
    bydamage_total = bydamage_total.rename(columns={"result": "game_result", "damage_total":"average_damage_total"})
    bydamage_total.iloc[0,0] = "Lose"
    bydamage_total.iloc[1,0] = "Win"
    return bydamage_total

def get_damage_taken():
    bydamage_taken = df.groupby("result")["damage_taken"].mean().round(2).to_frame()
    bydamage_taken = bydamage_taken.reset_index().rename_axis(None, axis=1)
    bydamage_taken = bydamage_taken.rename(columns={"result": "game_result", "damage_taken":"average_damage_taken"})
    bydamage_taken.iloc[0,0] = "Lose"
    bydamage_taken.iloc[1,0] = "Win"
    return bydamage_taken

def get_gold_earned():
    bygold_earned = df.groupby("result")["gold_earned"].mean().round(2).to_frame()
    bygold_earned = bygold_earned.reset_index().rename_axis(None, axis=1)
    bygold_earned = bygold_earned.rename(columns={"result": "game_result", "gold_earned":"average_gold_earned"})
    bygold_earned.iloc[0,0] = "Lose"
    bygold_earned.iloc[1,0] = "Win"
    return bygold_earned

def get_total_minions_killed():
    bytotal_minions_killed = df.groupby("result")["total_minions_killed"].mean().round(2).to_frame()
    bytotal_minions_killed = bytotal_minions_killed.reset_index().rename_axis(None, axis=1)
    bytotal_minions_killed = bytotal_minions_killed.rename(columns={"result": "game_result", "total_minions_killed":"average_total_minions_killed"})
    bytotal_minions_killed.iloc[0,0] = "Lose"
    bytotal_minions_killed.iloc[1,0] = "Win"
    return bytotal_minions_killed

def get_turret_kills():
    byturret_kills = df.groupby("result")["turret_kills"].mean().round(2).to_frame()
    byturret_kills = byturret_kills.reset_index().rename_axis(None, axis=1)
    byturret_kills = byturret_kills.rename(columns={"result": "game_result", "turret_kills":"average_turret_kills"})
    byturret_kills.iloc[0,0] = "Lose"
    byturret_kills.iloc[1,0] = "Win"
    return byturret_kills

def get_vision_score():
    byvision_score = df.groupby("result")["vision_score"].mean().round(2).to_frame()
    byvision_score = byvision_score.reset_index().rename_axis(None, axis=1)
    byvision_score = byvision_score.rename(columns={"result": "game_result", "vision_score":"average_vision_score"})
    byvision_score.iloc[0,0] = "Lose"
    byvision_score.iloc[1,0] = "Win"
    return byvision_score