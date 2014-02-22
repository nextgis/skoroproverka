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

if __name__ == '__main__':
    #set input file - data
    fn_in = "genproc_checkplan2014_data_subset.csv"
    f_in = open(fn_in,'rb')
    csvreader = csv.DictReader(f_in)
    field_names = csvreader.fieldnames
    field_names.append('CHECK_MONTH_PROC')
    field_names.append('OSN_DATESTART_PROC')
    field_names.append('OGRN_REGION')

    fields_str = ",".join(field_names)

    #set output file - postprocessed data
    fn_out = "genproc_checkplan2014_data_subset_pp.csv"
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
        addrloc_jur = row['ADDRLOC_JUR']
        addrloc_ip = row['ADDRLOC_IP']
        addr_act = row['ADDR_ACT']
        addr_obj = row['ADDR_OBJ']
        ogrn = row['OGRN']
        ogrn_region = process_region(row['OGRN'])
        inn = row['INN']
        goal = row['GOAL']
        osn_datestart = row['OSN_DATESTART']
        osn_datestart_proc = process_datestart(row['OSN_DATESTART'])
        osn_dateend = row['OSN_DATEEND']
        osn_datestart2 = row['OSN_DATESTART2']
        osn_other = row['OSN_OTHER']
        check_month = row['CHECK_MONTH']
        check_month_proc = process_month(row['CHECK_MONTH'])
        check_days = row['CHECK_DAYS']
        check_hours = row['CHECK_HOURS']
        check_form = row['CHECK_FORM']
        check_org = row['CHECK_ORG']

        csvwriter.writerow(dict(ID=idid,
                                SUBID=subid,
                                URL=link,
                                NAME=name,
                                ADDRLOC_JUR=addrloc_jur,
                                ADDRLOC_IP=addrloc_ip,
                                ADDR_ACT=addr_act,
                                ADDR_OBJ=addr_obj,
                                OGRN=ogrn,
                                OGRN_REGION=ogrn_region,
                                INN=inn,
                                GOAL=goal,
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