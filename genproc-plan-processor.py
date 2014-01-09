#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
# vim:et
# ---------------------------------------------------------------------------
# genproc-plan-processor.py
# Author: Maxim Dubinin (sim@gis-lab.info)
# About: Process html grabbed from http://plan.genproc.gov.ru/plan2014 to csv.
# Created: 20:32 31.12.2013
# Usage example: python genproc-plan-processor.py
# ---------------------------------------------------------------------------

from bs4 import BeautifulSoup
import sys
import os
import ucsv as csv
import datetime
import time
import glob

def parse_org(id):
    id_data = open(id)
    id = id.replace(".html","")
    soup = BeautifulSoup(''.join(id_data.read()))
    maintables = soup.findAll("table", { "class" : "plan_filter" })
    subid = 0
    for maintable in maintables:
        subid = subid + 1
        if str(maintable) == 'None':
            name = addrloc_jur = addrloc_ip = addr_act = addr_obj = ogrn = inn = goal = osn_datestart = osn_dateend = osn_datestart2 = osn_other = check_month = check_days = check_hours = check_form = check_org = "EMPTY"
            f_errors.write(id + "," + link + ", id is empty" + "\n")
        else:
            tds = maintable.findAll("td")
            
            if len(tds) < 32:
                name = addrloc_jur = addrloc_ip = addr_act = addr_obj = ogrn = inn = goal = osn_datestart = osn_dateend = osn_datestart2 = osn_other = check_month = check_days = check_hours = check_form = check_org = "ERROR"
                f_errors.write(id + "," + link + ", incorrect data" + "\n")
            else:
                name = list(tds[1].strings)[0]
                addrloc_jur = list(tds[3].strings)[0]
                addrloc_ip = list(tds[5].strings)[0]
                addr_act = list(tds[7].strings)[0]
                if list(tds[9].strings) != []:
                    addr_obj = list(tds[9].strings)[0]
                else:
                    addr_obj = ""
                ogrn = list(tds[11].strings)[0]
                inn = list(tds[13].strings)[0]
                goal = list(tds[15].strings)[0]
                osn_datestart = list(tds[17].strings)[0]
                if list(tds[19].strings) != []:
                    osn_dateend = list(tds[19].strings)[0]
                else:
                    osn_dateend = ""
                if list(tds[21].strings) != []:
                    osn_datestart2 = list(tds[21].strings)[0]
                else:
                    osn_dateend = ""
                osn_other = list(tds[23].strings)[0]
                if list(tds[25].strings) != []:
                    check_month = list(tds[25].strings)[0]
                else:
                    check_month = ""
                check_days = list(tds[27].strings)[0]
                check_hours = list(tds[29].strings)[0]
                check_form = list(tds[31].strings)[0]
                check_org = list(tds[33].strings)[0]
                
        #write to results file
        csvwriter.writerow(dict(ID=id,
                                SUBID=subid,
                                URL=link,
                                NAME=name,
                                ADDRLOC_JUR=addrloc_jur.strip(),
                                ADDRLOC_IP=addrloc_ip.strip(),
                                ADDR_ACT=addr_act.strip(),
                                ADDR_OBJ=addr_obj.strip(),
                                OGRN=ogrn.strip(),
                                INN=inn.strip(),
                                GOAL=goal.strip(),
                                OSN_DATESTART=osn_datestart.strip(),
                                OSN_DATEEND=osn_dateend.strip(),
                                OSN_DATESTART2=osn_datestart2.strip(),
                                OSN_OTHER=osn_other.strip(),
                                CHECK_MONTH=check_month.strip(),
                                CHECK_DAYS=check_days.strip(),
                                CHECK_HOURS=check_hours.strip(),
                                CHECK_FORM=check_form.strip(),
                                CHECK_ORG=check_org.strip()))

if __name__ == '__main__':
    os.chdir("data")
    f_errors = open("../errors.csv","wb")
       
    fieldnames_data = ("ID","SUBID","URL","NAME","ADDRLOC_JUR","ADDRLOC_IP","ADDR_ACT","ADDR_OBJ","OGRN","INN","GOAL","OSN_DATESTART","OSN_DATEEND","OSN_DATESTART2","OSN_OTHER","CHECK_MONTH","CHECK_DAYS","CHECK_HOURS","CHECK_FORM","CHECK_ORG")
    f_data = open("../all_data.csv","wb")
    csvwriter = csv.DictWriter(f_data, fieldnames=fieldnames_data)
    
    
    for id in glob.glob("*.html"):
        link = "http://plan.genproc.gov.ru/plan2014/detail.php?ID=" + id.replace(".html","")
        print("Processing id " + id)
        parse_org(id)
        
    f_data.close()
    f_errors.close()
