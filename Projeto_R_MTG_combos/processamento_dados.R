
library(tidyverse)
library(readr)
library(pastecs)

MTG_JSON_Dream_Trawler <- 
  read_csv("D:/Projetos gyro4data/ML_MTG_combos/Dados/MTJ_JSON_Dream Trawler.csv")
spellbook_DB_combos <- 
  read_csv("D:/Projetos gyro4data/ML_MTG_combos/Dados/db_edh_spell.csv")
EDHREC_Number_of_Decks <- read_csv("D:/Projetos gyro4data/ML_MTG_combos/EDHREC Number of Decks.csv")

stk_spell<- stack(spellbook_DB_combos[2:11])
stk_spell <- na.omit(stk_spell)
lista_cartas_combo <- count(stk_spell, "values")
colnames(lista_cartas_combo) <- c("nomes_cartas", "n_combos")

teste <- left_join(lista_cartas_combo, MTG_JSON_Dream_Trawler, 
                   by = c("nomes_cartas" = "name"))

db_edh_spell <- left_join(EDHREC_Number_of_Decks, spellbook_DB_combos, 
                          by = c("ID_spellbook" = "ID"))

quantos_combos <- count(stk_spell, "values")
  
write.csv(lista_cartas_combo,
          "D:/Projetos gyro4data/ML_MTG_combos/Dados/lista_cartas_combo.csv", 
          row.names = FALSE)

i_ndice_Coralheim <- read_csv("D:/Projetos gyro4data/ML_MTG_combos/indice Coralheim.csv")

















