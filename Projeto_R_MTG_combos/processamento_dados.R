
library(tidyverse)
library(readr)
library(pastecs)

MTG_JSON_Dream_Trawler <- 
  read_csv("D:/Projetos gyro4data/ML_MTG_combos/Dados/MTJ_JSON_Dream Trawler.csv")
spellbook_DB_combos <- 
  read_csv("D:/Projetos gyro4data/ML_MTG_combos/Dados/Commander Spellbook Database - combos.csv")

stk_spell<- stack(spellbook_DB_combos[2:11])
stk_spell <- na.omit(stk_spell)
lista_cartas_combo <- unique(stk_spell)
lista_cartas_combo <- data.frame(lista_cartas_combo[,-2])
colnames(lista_cartas_combo) <- c("nomes_cartas")

teste <- left_join(lista_cartas_combo, MTG_JSON_Dream_Trawler, 
                   by = c("nomes_cartas" = "completeName"))

sum(is.na(teste$name))

new_DF <- teste

new_DF[is.na(new_DF)] = 0

lista_cartas_faltando <- subset(new_DF, name == 0)
lista_cartas_faltando <- data.frame(lista_cartas_faltando$nomes_cartas)

write.csv(lista_cartas_faltando,
          "D:/Projetos gyro4data/ML_MTG_combos/Dados/lista_cartas_faltando.csv", 
          row.names = FALSE)

