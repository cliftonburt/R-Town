ggplot(data=<DATA>)+
  <GEOM_FUNCTION>(mapping=aes(<AESTHETIC MAPPINGS>))
  
#---
  
ggplot(data=penguins)+
  geom_point(mapping=aes(x=bill_length_mm,y=bill_depth_mm))
  
  