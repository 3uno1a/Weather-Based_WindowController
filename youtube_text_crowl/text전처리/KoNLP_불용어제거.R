# KoNLP 패키지 설치
# install.packages("KoNLP")
# install.packages("multilinguer")
library(multilinguer)
# java 설치
# install_jdk()

# KoNLP 패키지 종속 패키지 설치
install.packages(c('stringr', 'hash', 'tau', 'Sejong', 'RSQLite', 'devtools'), type = "binary")

# KoNLP 설치 확인
library(KoNLP)
# Checking user defined dictionary!

# 사전사용(사전설치)
useSejongDic()

setwd("~/Desktop/Window23/youtube/youtube_text_crowl/text전처리")

data0<- readLines('./textdata/joyful_music.txt')

data0

head(unlist(data0), 30)

data3 <- unlist(data0)
data3

data3 <- gsub("<a>","", data3)
data3 <- gsub("서울시", "", data3)
data3 <- gsub("서울", "", data3)
data3 <- gsub("요청", "", data3)
data3 <- gsub("제안", "", data3)
data3 <- gsub(" ", "", data3)
data3 <- gsub("-","", data3)
data3

write(unlist(data3), "joyful_3.txt")

data4 <- read.table("joyful_3.txt")
data4
