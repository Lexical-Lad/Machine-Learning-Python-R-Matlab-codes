library(warbleR)
library(tuneR)
library(seewave)

#~~~~~~~~~~~~~~~~~~~~~~~~~Generating the male voice data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
setwd("./male")

list <- list.files(".", "\\.wav")

dataset <- data.frame()

for( f in list)
{
  row <- data.frame(f, 0,0,20)
  dataset <- rbind(dataset, row)
}

names(dataset) <- c('sound.files', 'selec', 'start', 'end')


features <- specan(dataset)
features[,'label'] <- 'male'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Generating the female voice data~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
setwd("..");
setwd("./female");

list <- list.files(".", "\\.wav")

dataset <- data.frame()

for( f in list)
{
  row <- data.frame(f, 0,0,20)
  dataset <- rbind(dataset, row)
}

names(dataset) <- c('sound.files', 'selec', 'start', 'end')


f <- specan(dataset)
f[,'label'] <- 'female'

features <- rbind(features, f)

setwd("..")

features <- features[,4:31]
write.csv(features,"voice2.csv")
