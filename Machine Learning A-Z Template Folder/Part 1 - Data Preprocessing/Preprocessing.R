dataset = read.csv("Data.csv")

#no need to split the data.frame into feature matrix and dependent variable vector, unlike python


#compensating for the missing data, if any
dataset$Age = ifelse( is.na(dataset$Age), ave( dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$Salary = ifelse( is.na(dataset$Salary), ave( dataset$Salary, FUN= function(x) mean(x, na.rm = TRUE)), dataset$Salary)


#replacing the textual data with numerical factors 
dataset$Country = factor( dataset$Country, levels = c("France","Germany","Spain"), labels = c(1,2,3))
dataset$Purchased = factor( dataset$Purchased , levels = c("Yes","No"), labels = c(1,0))

#splitting the data into training and test sets
library(caTools)
#set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#applying feature scaling(excluding the categorical(non-numeric) features
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])

