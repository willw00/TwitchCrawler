data <- read.csv("Twitch_snapshot.csv")

for (i in 8:length(data[1,])) {
  data[,i] <- as.integer(data[,i])
}

data$time <- 3600 * 24 * data$Day + 3600 * data$Hour + 60 * data$Minute + data$Second
