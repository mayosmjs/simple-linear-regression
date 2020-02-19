library(tidyverse)

x <- c(17,13,12,15,16,14,16,16,18,19)
y <- c(94,73,59,80,93,85,66,79,77,91)

df <- cbind.data.frame(x,y)
df <- df %>%mutate(xsq = x^2,ysq = y^2 ,xy = x*y)

#Build a scatter plot of our values
scatter.smooth(x=df$x, y=df$y, main="Attitude ~ Score")  # scatterplot

# build linear regression model on full data
# remember y preceeds x since y is dependent of x
linearMod <- lm(y ~ x, data=df)  


# capture model summary as an object
modelSummary <- summary(linearMod)  

# model coefficients
modelCoeffs <- modelSummary$coefficients  

# get beta estimate for X
beta.estimate <- modelCoeffs["x", "Estimate"]

# get std.error for X  
std.error <- modelCoeffs["x", "Std. Error"]  


#######################PREDICTION TIME #########################

#test data to predict

t_pred = data.frame(x = c(15,13))

predict(linearMod,t_pred)



###################### TRAINING SET  TEST SET##################

# Create Training and Test data -
set.seed(100)  # setting seed to reproduce results of random sampling
trainingRowIndex <- sample(1:nrow(df), 0.6*nrow(df))  # row indices for training data 0.8 is better
trainingData <- df[trainingRowIndex, ]  # model training data
testData  <- df[-trainingRowIndex, ]   # test data

#OR USE 
# split = sample.split(df$y,SplitRatio = 2/3)
# training_set = subset(df,split == TRUE)
# test_set = subset(df,split == FALSE)



# BUILD THE MODEL ON TRAINING DATA 
lmMod <- lm(y ~ x, data=trainingData)  # build the model
distPred <- predict(lmMod, testData,interval = "confidence")   # predict y


# MODEL SUMMARY
summary (lmMod) 

# PREDICTION ACCURACY
actuals_preds <- data.frame(cbind(actuals=testData$dist, predicteds=distPred))  # make actuals_predicteds dataframe.
correlation_accuracy <- cor(actuals_preds)  # 90%
head(actuals_preds)


library(moderndive) #linear packages
library(gapminder)
library(skimr)

get_regression_table(lmMod)
get_regression_summaries(lmMod)










