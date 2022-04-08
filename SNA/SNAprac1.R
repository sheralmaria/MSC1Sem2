install.packages("igraph")
library(igraph)
g=graph.formula(A-B,B-C,C-D,D-E,E-F,G-H)
g
ecount(g)
vcount(g)
E(g)
V(g)
degree(g)
dg=graph.formula(A-+B,B+-C,C-+B,C++D)
dg
degree(g,mode="in")
V(g)$name[degree(g)==min(degree(g))]
get.adjlist(g)
get.adjacency(dg)











