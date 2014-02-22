# ---------------------------------------------------------------------------
# genproc_analysis.r
# Author: Maxim Dubinin (sim@gis-lab.info)
# Created: 18:17 11.01.2014
# About: 
# Notes: 
# Usage example: Run R, execute script
# ---------------------------------------------------------------------------

setwd("d:\\Programming\\Python\\genproc-plan\\!old\\")
fn = "genproc_checkplan2014_data.csv"
#cC = c("numeric","numeric","NULL","factor","NULL","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor")
cC = c("URL"="NULL","ADDRLOC_IP"="NULL","OSN_DATESTART"="Date")
d = read.csv(fn,encoding="UTF-8",colClasses=cC)