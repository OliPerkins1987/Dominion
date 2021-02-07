

library(tidyverse)
library(ggplot2)
library(viridisLite)

setwd('C:/Users/Oli/Documents/PhD/Training/Dominion')

dat <- read.csv('Modelruns.csv')
colnames(dat)[1] <- 'Turn'
dat <- pivot_longer(dat, cols = colnames(dat)[2:7],
                    values_to = 'Mean_Purchasing_Power', names_to = 'key')


ggplot(dat, aes(x = Turn, y = Mean_Purchasing_Power, colour = key)) +
  geom_line(size = 1.5) + theme_classic() + scale_colour_viridis_d()
