#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
# vim:et
# ---------------------------------------------------------------------------
# genproc-plan-processor-lxml.py
# Author: Maxim Dubinin (sim@gis-lab.info)
# About: Process html grabbed from http://plan.genproc.gov.ru/plan2014 to csv.
# Created: 20:32 31.12.2013
# Usage example: python genproc-plan-processor.py
# ---------------------------------------------------------------------------

from lxml import etree
import sys
import os
import ucsv as csv
import datetime
import time
import glob

def parse_org(id):
    id_data = open(id)
    id = id.replace(".html","")
    parser = etree.HTMLParser()
    tree = etree.parse(id_data,parser)
    maintables = tree.xpath("//table[@class='plan_filter']")
    subid = 0
    for maintable in maintables:
        subid = subid + 1
        if str(maintable) == 'None':
            name = addrloc_jur = addrloc_ip = addr_act = addr_obj = ogrn = inn = goal = osn_datestart = osn_dateend = osn_datestart2 = osn_other = check_month = check_days = check_hours = check_form = check_org = "EMPTY"
            f_errors.write(id + "," + link + ", id is empty" + "\n")
        else:
            tds = maintable.xpath(".//td")
            
            if len(tds) < 32:
                name = addrloc_jur = addrloc_ip = addr_act = addr_obj = ogrn = inn = goal = osn_datestart = osn_dateend = osn_datestart2 = osn_other = check_month = check_days = check_hours = check_form = check_org = "ERROR"
                f_errors.write(id + "," + link + ", incorrect data" + "\n")
            else:
                name = tds[1].text
                if name == None: name = ""
                addrloc_jur = tds[3].text
                if addrloc_jur == None: addrloc_jur = ""
                addrloc_ip = tds[5].text
                if addrloc_ip == None: addrloc_ip = ""
                addr_act = tds[7].text
                if addr_act == None: addr_act = ""
                addr_obj = tds[9].text
                if addr_obj == None: addr_obj = ""
                ogrn = tds[11].text
                if ogrn == None: ogrn = ""
                inn = tds[13].text
                if inn == None: inn = ""
                goal = tds[15].text
                if goal == None: goal = ""
                osn_datestart = tds[17].text
                if osn_datestart == None: osn_datestart = ""
                osn_dateend = tds[19].text
                if osn_dateend == None: osn_dateend = ""
                osn_datestart2 = tds[21].text
                if osn_datestart2 == None: osn_datestart2 = ""
                osn_other = tds[23].text
                if osn_other == None: osn_other = ""
                check_month = tds[25].text
                if check_month == None: check_month = ""
                check_days = tds[27].text
                if check_days == None: check_days = ""
                check_hours = tds[29].text
                if check_hours == None: check_hours = ""
                check_form = tds[31].text
                if check_form == None: check_form = ""
                check_org = tds[33].text
                if check_org == None: check_org = ""
                
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
