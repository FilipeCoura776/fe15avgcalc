import banco

def calc_avg(cur,char,clas,is_base,job,lv):
    avg_stats=[
        char["bhp"],
        char["batk"],
        char["bskl"],
        char["bspd"],
        char["blck"],
        char["bdef"],
        char["bres"]
    ]

    stats_keys_base = ["bhp", "batk", "bskl", "bspd", "blck", "bdef", "bres"]
    stats_keys_growth = ["ghp", "gatk", "gskl", "gspd", "glck", "gdef", "gres"]

    if is_base:
        tree = [clas]
    else:
        tree = banco.get_promos(cur,char,clas,job)

    for i in tree:
        if char["base_class_id"] == i["id"]:
            if is_base:
                lv_ups = lv - char["base_lv"]
            else:
                lv_ups = i["promo_req"] - char["base_lv"]
        else:
            if job == i["name"]:
                lv_ups = lv-1
            else:
                lv_ups = i["promo_req"] - 1

        if char["base_class_id"] != i["id"]:
            for j, key in enumerate(stats_keys_base):
                if avg_stats[j] < i[key]:
                    avg_stats[j] = float(i[key])

        for j in range(7):
            growth_total = char[stats_keys_growth[j]] + i[stats_keys_growth[j]]
            avg_stats[j] += (growth_total/100.0) * lv_ups

    avg_stats = aplicar_caps(avg_stats, char)

    return avg_stats + [char["name"], clas["name"],lv]

'''
    if is_base:
        lv_ups = lv - char["base_lv"]

        avg_stats = [
            char["bhp"] + (char["ghp"]+clas["ghp"])/100*lv_ups,
            char["batk"] + (char["gatk"]+clas["gatk"])/100*lv_ups,
            char["bskl"] + (char["gskl"]+clas["gskl"])/100*lv_ups,
            char["bspd"] + (char["gspd"]+clas["gspd"])/100*lv_ups,
            char["blck"] + (char["glck"]+clas["glck"])/100*lv_ups,
            char["bdef"] + (char["gdef"]+clas["gdef"])/100*lv_ups,
            char["bres"] + (char["gres"]+clas["gres"])/100*lv_ups,
            char["name"],
            clas["name"],
            lv
        ]
    else:
        tree = banco.get_promos(cur,char, clas, job)

        for i in tree:
            lv_ups = (
                lv - 1 if job == i["name"] 
                else i["promo_req"] - 1 if char["base_class_id"] != i["id"] 
                else i["promo_req"] - char["base_lv"]
            )

            for j in range(7):
                k = i[4:11] #hp base a res base
                if avg_stats[j] < k[j]:
                    avg_stats[j] = float(k[j])

            avg_stats = [
                        avg_stats[0] + (char["ghp"]+i["ghp"])/100*lv_ups,
                        avg_stats[1] + (char["gatk"]+i["gatk"])/100*lv_ups,
                        avg_stats[2] + (char["gskl"]+i["gskl"])/100*lv_ups,
                        avg_stats[3] + (char["gspd"]+i["gspd"])/100*lv_ups,
                        avg_stats[4] + (char["glck"]+i["glck"])/100*lv_ups,
                        avg_stats[5] + (char["gdef"]+i["gdef"])/100*lv_ups,
                        avg_stats[6] + (char["gres"]+i["gres"])/100*lv_ups
            ]

    avg_stats.append(char["name"])
    avg_stats.append(clas["name"])
    avg_stats.append(lv)
            
    return avg_stats
'''

def aplicar_caps(stats_calculados, char):
    stats_limitados = list(stats_calculados)
    stats_keys_cap = ["chp", "catk", "cskl", "cspd", "clck", "cdef", "cres"]

    for idx, key in enumerate(stats_keys_cap):
        cap_val = char[key]
        if cap_val is not None and stats_limitados[idx] > cap_val:
            stats_limitados[idx] = float(cap_val)

    return stats_limitados
