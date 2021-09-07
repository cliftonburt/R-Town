ggplot(data=<DATA>)+
  <GEOM_FUNCTION>(mapping=aes(<AESTHETIC MAPPINGS>))
  
#---
  
ggplot(data=penguins)+
  geom_point(mapping=aes(x=bill_length_mm,y=bill_depth_mm))
  
  
ggplot(data=activity, aes(x=TotalSteps, y=Calories)) + 
    geom_point() + geom_smooth() + labs(title="Total Steps vs. Calories")
	
penguins %>%
 select( -species, -sex, -year)

penguins %>%
 rename(island_new=island)

clean_names(penguins)

penguins %>% arrange (-bill_length_mm)

penguins2 <- penguins %>% arrange (-bill_length_mm)
View(penguins2)

penguins %>% group_by(island) %>% drop_na() %>% summarize(mean_bill_length_mm = mean(bill_length_mm))

penguins %>% group_by(island) %>% drop_na() %>% summarize(mean_bill_length_mm = max(bill_length_mm))

penguins %>% group_by(species, island) %>% drop_na() %>% summarize(max_bl = max_bill_length_mm), mean_bl = mean(bill_lenth_mm))



