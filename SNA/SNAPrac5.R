#1.	a network as a sociogram (or "network graph")
library(igraph)
ng=graph.formula(Andy++Garth,Garth-+Bill,Bill-
                    +Elena,Elena++Frank,Carol-+Andy,Carol-
                    +Elena,Carol++Dan,Carol++Bill,Dan++Andy,Dan++Bill)
plot(ng)
#2.	a network as a matrix
get.adjacency(ng)
#3.	a network as an edge list.
E(ng)
get.adjedgelist(ng,mode="in")

