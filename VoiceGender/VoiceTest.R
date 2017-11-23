library(caTools)
library(warbleR)
library(randomForest)
library(tuneR)
library(seewave)


test <- readWave("male1.wav")
b <- fir(test)
