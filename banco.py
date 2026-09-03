import sqlite3

#--------------------------------------------------------------------------------------------------
def conectar():
    con = sqlite3.connect('calcfe.db')
    con.row_factory = sqlite3.Row
    return con, con.cursor()

#--------------------------------------------------------------------------------------------------
def get_char(cur, name):
    cur.execute(f"""
        SELECT c.id, name, base_class_id, base_lv,
        cb.hp bhp, cb.atk batk, cb.skl bskl, cb.spd bspd, cb.lck blck, cb.def bdef, cb.res bres, 
        cg.hp ghp, cg.atk gatk, cg.skl gskl, cg.spd gspd, cg.lck glck, cg.def gdef, cg.res gres,
        cc.hp chp, cc.atk catk, cc.skl cskl, cc.spd cspd, cc.lck clck, cc.def cdef, cc.res cres 
        FROM characters c 
        JOIN char_bases cb ON c.id = cb.id 
        JOIN char_growths cg ON c.id = cg.id
        LEFT JOIN char_caps cc on c.id = cc.id
        WHERE c.name=?
    """,(name,))

    char = cur.fetchone()

    print(char[:])

    return char

#--------------------------------------------------------------------------------------------------
def get_class(cur, char, job):
    job = 'Priestess (Celica)' if char["name"] == 'Celica' and job == 'Priestess' else job

    cur.execute(f"""SELECT c.id, name, promo_req, prev_id,
    cb.hp bhp, cb.atk batk, cb.skl bskl, cb.spd bspd, cb.lck blck, cb.def bdef, cb.res bres, 
    cg.hp ghp, cg.atk gatk, cg.skl gskl, cg.spd gspd, cg.lck glck, cg.def gdef, cg.res gres 
    FROM classes c 
    JOIN class_bases cb ON c.id = cb.id 
    JOIN class_growths cg ON c.id = cg.id 
    WHERE c.name = ?""",(job,))

    clas = cur.fetchone()
    print(clas[:])

    is_base = True if char["base_class_id"] == clas["id"] else False

    return clas, is_base

#--------------------------------------------------------------------------------------------------
def get_promos(cur,char,clas,job):
    tree = [clas]

    while True:
        clas = get_class_by_id(cur, clas["prev_id"])
        tree.insert(0, clas)
    
        if(clas["prev_id"] == 0 or clas["id"] == char["base_class_id"]):
            break

    return tree

#---------------------------------------------------------------------------------------------------
def get_class_by_id(cur,id):
    cur.execute(f"""SELECT c.id, name, promo_req, prev_id,
        cb.hp bhp, cb.atk batk, cb.skl bskl, cb.spd bspd, cb.lck blck, cb.def bdef, cb.res bres, 
        cg.hp ghp, cg.atk gatk, cg.skl gskl, cg.spd gspd, cg.lck glck, cg.def gdef, cg.res gres 
        FROM classes c 
        JOIN class_bases cb ON c.id = cb.id 
        JOIN class_growths cg ON c.id = cg.id
        WHERE c.id = ?""",(id,))

    return cur.fetchone()

#---------------------------------------------------------------------------------------------------
def get_classes_for_char(cur,char_name):
    query = """
    WITH RECURSIVE PromotionTree AS (
        SELECT cl.id, cl.name, cl.prev_id
        FROM classes cl
        JOIN characters ch ON ch.base_class_id = cl.id
        WHERE ch.name = ?

        UNION ALL

        SELECT cl.id, cl.name, cl.prev_id
        FROM classes cl
        JOIN PromotionTree pt ON cl.prev_id = pt.id
        JOIN characters ch ON ch.name = ?
        WHERE (cl.required_gender IS NULL OR cl.required_gender = ch.gender)
    )
    SELECT DISTINCT id, name FROM PromotionTree;
    """

    cur.execute(query, (char_name, char_name))
    return cur.fetchall()