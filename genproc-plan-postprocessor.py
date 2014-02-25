#!/bin/env python
# -*- coding: utf-8 -*-

#import ucsv as csv
import csv

def process_month(month):
    months = [u"ЯНВАРЬ",u"ФЕВРАЛЬ",u"МАРТ",u"АПРЕЛЬ",u"МАЙ",u"ИЮНЬ",u"ИЮЛЬ",u"АВГУСТ",u"СЕНТЯБРЬ",u"ОКТЯБРЬ",u"НОЯБРЬ",u"ДЕКАБРЬ"]
    try:
        res = months.index(month.decode("utf-8").upper()) + 1
    except:
        res = 999
    
    return res

def process_form(ogrn):
    if len(ogrn) == 13:
        res = "юрлицо"
    elif len(ogrn) == 15:
        res = "физлицо"
    else:
        res = "др"

    return res

def process_region(ogrn):
    if len(ogrn) == 13:
        res = ogrn[3:5]
    else:
        res = 999

    return res

def process_datestart(datestart):
    if len(datestart) == 10:
        res = datestart[6:10]
    else:
        res = 0
    
    return res

def process_goal(goal):
    goals = [u"ЭПИД",u"ПОЖАР",u"ПРОМЫШЛ",u"ЭКОЛОГ",u"ДОРОЖ",u"УСТАВ",u"ВЕТЕРИН",u"ЗЕМЕЛ",u"ПРИРОДООХР",u"ТРУД",u"ЭНЕРГ",u"ОРУЖ",u"АЛКОГ",u"ОКРУЖАЮЩ",u"ТРАНСПОРТ",u"ОБРАЗОВА",u"АТОМН",u"ФАРМАЦ",u"ФИТОСАН",u"РАСТЕН"]
    goals.append(u"ЛИЦЕНЗ")
    goals_codes = [u"эпидемиологический",u"пожарный",u"промышленный",u"экологический",u"дорожный",u"уставной",u"ветеринарный",u"земельный",u"природоохранный",u"трудовой",u"энергетический",u"оружейный",u"алкогольный",u"экологический",u"транспортный",u"образовательный",u"атомный",u"фармацевтический",u"фитосанитарный",u"фитосанитарный"]
    goals_codes.append(u"лицензионный")
    
    i = 0
    res = ""
    while res == "" and i < len(goals):
        if goals[i] in goal.decode("utf-8").upper():
            res = goals_codes[i]
        else:
            res = ""
            i = i + 1
    
    return res.encode("utf-8")

def process_type(type):
    types = [u"ЗАКРЫТОЕ",u"С ОГРАНИЧЕННОЙ",u"ДОШКОЛЬНОЕ ОБРАЗОВАТЕЛЬНОЕ",u"ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ ЗДРАВООХРАНЕНИЯ",u"ОТКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО",u"ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ",u"МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ОБЩЕОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ",u"МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ",u"НЕКОММЕРЧЕСКОЕ ПАРТНЕРСТВО",u"МУНИЦИПАЛЬНОЕ КАЗЕННОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ",u"ГОСУДАРСТВЕННОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ",u"ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ",u"БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ ЗДРАВООХРАНЕНИЯ",u"КРЕСТЬЯН",u"МУНИЦИПАЛЬНОЕ ДОШКОЛЬНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ",u"МУНИЦИПАЛЬНОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ КУЛЬТУРЫ"]
    types_codes = [u"ЗАО",u"ООО",u"МБДОУ",u"ГБУЗ",u"ОАО",u"ГБОУ",u"МБОУ",u"МБОУ",u"МОУ",u"НП",u"МКОУ",u"ГКУ",u"ГБУ",u"БУЗ",u"КФХ",u"МДОУ",u"МБУК"]
    
    i = 0
    res = ""
    while res == "" and i < len(types):
        if types[i] in type.decode("utf-8").upper().replace("  "," "):
            res = types_codes[i]
        else:
            res = ""
            i = i + 1
    
    return res.encode("utf-8")

if __name__ == '__main__':
    #set input file - data
    fn_in = "testdata/genproc_checkplan2014_data_subset.csv"
    f_in = open(fn_in,'rb')
    csvreader = csv.DictReader(f_in)
    field_names = csvreader.fieldnames
    field_names.append('CHECK_MONTH_PROC')
    field_names.append('OSN_DATESTART_PROC')
    field_names.append('OGRN_REGION')
    field_names.append('OGRN_FORM')
    field_names.append('GOAL_PROC')
    field_names.append('TYPE_PROC')

    fields_str = ",".join(field_names)

    #set output file - postprocessed data
    fn_out = "testdata/genproc_checkplan2014_data_subset_pp.csv"
    ftemp = open(fn_out,"wb")
    ftemp.write(fields_str + "\n")
    ftemp.close()

    f_out = open(fn_out,"a")
    csvwriter = csv.DictWriter(f_out, fieldnames=field_names)

    for row in csvreader:

        idid = row['ID']
        subid = row['SUBID']
        link = row['URL']
        name = row['NAME']
        type_proc = process_type(name)
        addrloc_jur = row['ADDRLOC_JUR']
        addrloc_ip = row['ADDRLOC_IP']
        addr_act = row['ADDR_ACT']
        addr_obj = row['ADDR_OBJ']
        ogrn = row['OGRN']
        ogrn_region = process_region(ogrn)
        ogrn_form = process_form(ogrn)
        inn = row['INN']
        goal = row['GOAL']
        goal_proc = process_goal(goal)
        osn_datestart = row['OSN_DATESTART']
        osn_datestart_proc = process_datestart(osn_datestart)
        osn_dateend = row['OSN_DATEEND']
        osn_datestart2 = row['OSN_DATESTART2']
        osn_other = row['OSN_OTHER']
        check_month = row['CHECK_MONTH']
        check_month_proc = process_month(check_month)
        check_days = row['CHECK_DAYS']
        check_hours = row['CHECK_HOURS']
        check_form = row['CHECK_FORM']
        check_org = row['CHECK_ORG']

        csvwriter.writerow(dict(ID=idid,
                                SUBID=subid,
                                URL=link,
                                NAME=name,
                                TYPE_PROC=type_proc,
                                ADDRLOC_JUR=addrloc_jur,
                                ADDRLOC_IP=addrloc_ip,
                                ADDR_ACT=addr_act,
                                ADDR_OBJ=addr_obj,
                                OGRN=ogrn,
                                OGRN_REGION=ogrn_region,
                                OGRN_FORM=ogrn_form,
                                INN=inn,
                                GOAL=goal,
                                GOAL_PROC=goal_proc,
                                OSN_DATESTART=osn_datestart,
                                OSN_DATESTART_PROC=osn_datestart_proc,
                                OSN_DATEEND=osn_dateend,
                                OSN_DATESTART2=osn_datestart2,
                                OSN_OTHER=osn_other,
                                CHECK_MONTH=check_month,
                                CHECK_MONTH_PROC=check_month_proc,
                                CHECK_DAYS=check_days,
                                CHECK_HOURS=check_hours,
                                CHECK_FORM=check_form,
                                CHECK_ORG=check_org))
        
    f_in.close()
    f_out.close()