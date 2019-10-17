library(tidyverse)
library(vroom)

#load data
my_data = vroom::vroom("https://raw.githubusercontent.com/BarbaraDiazE/CABANA_CHEMOINFORMATICS/master/Day_3/UnsupervisedLearning_Clustering/K_Means/Data_cluster.csv")

#make feature set for quant features
features = c('HBA', 
            'HBD', 
            'RB', 
            'LogP', 
            'TPSA', 
            'MW', 
            'Heavy Atom', 
            'Ring Count', 
            'Fraction CSP3')

#make a hierarchical clustering object for heatmap reordering

my_clust_order <- 
my_data[features] %>% 
  cor() %>% 
  as.data.frame()  %>% 
  rownames_to_column(var = "feature_1") %>% 
  dist() %>% 
  hclust() 

my_clust_order <- my_clust_order$order

#reorder features
features <- features[my_clust_order]

#make heatmap
my_data[features] %>% 
  cor() %>% #calculate pearson cor
  as.data.frame()  %>% 
  rownames_to_column(var = "feature_1") %>% 
  tidyr::pivot_longer(cols = -feature_1, #pivot to long format
                      names_to = "feature_2", 
                      values_to = "value") %>% #consider features as factors, for plotting
  mutate(feature_1 = as_factor(feature_1),
         feature_2 = as_factor(feature_2)) %>% 
  ggplot(aes(x = feature_1, 
             y = feature_2, 
             fill = value)) +
  geom_tile() + #heatmap style
  scale_fill_distiller(palette = "Spectral") #define pallete

#kmeans clustering
my_clusters <- 
my_data[features] %>% 
  kmeans(centers = 3)

#plot, colored by cluster
my_data[features] %>% 
  mutate(cluster = my_clusters$cluster) %>% 
  ggplot(aes(x = TPSA, 
             y = MW,
             color = as_factor(cluster))) +
  geom_point()
  

