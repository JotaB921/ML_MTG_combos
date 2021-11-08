
library(tidyverse)
library(readr)
Magic_complete_database <- read_delim("~/Downloads/Magic complete database.csv", 
                                      delim = ";", escape_double = FALSE, trim_ws = TRUE)

library(rjson)
mtg_json_file <- "/home/jaylton/Área de Trabalho/Temporários/AllPrintings.json"

mtg_json_data <- fromJSON(paste(readLines(mtg_json_file), collapse=""))

library(jsonlite)

data_raw <- enframe(unlist(mtg_json_data))

#teste do git hub
x <- data.frame()
