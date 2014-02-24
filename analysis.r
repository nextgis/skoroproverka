# ---------------------------------------------------------------------------
# genproc_analysis.r
# Author: Maxim Dubinin (sim@gis-lab.info)
# Created: 18:17 11.01.2014
# About: Analysis script used to make simple stats on state checks database.
# Notes: For a description of stats, see github wiki page.
# Usage example: Run R, execute script
# ---------------------------------------------------------------------------

setwd("d:\\Programming\\Python\\genproc-plan\\!old\\")

fn = "testdata/genproc_checkplan2014_data_subset_pp.csv"
#cC = c("numeric","numeric","NULL","factor","NULL","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor","factor")

#cC = c("URL"="NULL","ADDRLOC_IP"="NULL","OSN_DATESTART"="Date")

cC = c("URL"="NULL","ADDRLOC_IP"="NULL")

d = read.csv(fn,encoding="UTF-8",colClasses=cC)

#TOTORG
totorg = length(unique(d$ID))

#TOTCHECK
totcheck = dim(d)[1] 

#MOSTCHECKED
mostcheckedd = table(d$OGRN)
mostchecked = mostcheckedd[mostcheckedd > 10]
checkedids = match(names(tt),d$OGRN)
checkednames = as.character(d[match(names(tt),d$OGRN),]$NAME)

mostchecked = data.frame(as.vector(mostchecked),names(tt),checkednames)
names(mostchecked)=c("count","ogrn","name")
order.cnt = order(mostchecked$count,decreasing=TRUE)
mostchecked = mostchecked[order.cnt,]

#MONTH
monthd = d$CHECK_MONTH_PROC
month = subset(monthd, monthd <= 12)
barplot(table(month))

#YEARREG
yeard = d$OSN_DATESTART_PROC
year = subset(yeard, yeard > 0)
barplot(table(year))


#GOAL
goald = d$GOAL_PROC
goal = subset(goald, goald != "")
par(mar=c(10,4,4,2))
barplot(table(goal),las=2)

#TYPE


#OGRNREG
ogrnregd = d$OGRN[nchar(d$OGRN) == 13]
ogrnreg = data.frame(table(as.numeric(sapply(ogrnregd,substring,4,5))))
names(ogrnreg) = c("reg","count")
write.csv(ogrnreg,"ogrn-regions.csv",row.names = F,col.names = T)
