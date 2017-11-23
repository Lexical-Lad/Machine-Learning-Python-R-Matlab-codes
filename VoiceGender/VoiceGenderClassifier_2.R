library(caTools)
library(randomForest)
library(warbleR)
library(seewave)
library(tuneR)

#~~~~~~~~~~~~~~~~~~~~~Training the model on the 'voice.csv.' dataset~~~~~~~~~~~~~~~~~~~~~#

dataset <- read.csv("voice2.csv")
dataset<- dataset[,2:29]

split <- sample.split(dataset$label, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

model <- randomForest(label~., dataset, importance = TRUE)

train_prediction <- predict(model, training_set)
test_prediction <- predict(model, test_set)

test_labels <- table(test_set$label, test_prediction)
table(test_set$label, test_prediction)




#~~~~~~~~~~~~~~Extracting features from sample audio file~~~~~~~~~~~~~~~~~~~~~~~#

data <- data.frame()

# Get list of files in the folder.
list <- list.files(".", '\\.wav')

# Adding file list to data.frame for processing.
for (fileName in list) {
  row <- data.frame(fileName, 0, 0, 20)
  data <- rbind(data, row)
}

# Setting column names.
names(data) <- c('sound.files', 'selec', 'start', 'end')


features <- specan(data)

features <- features[,4:30]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Final Prediciton~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

prediction <- predict(model, features)

output<- data.frame("Audio File" = list, "Prediction/Label" = prediction)
View(output)



