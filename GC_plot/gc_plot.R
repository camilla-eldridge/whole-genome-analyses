#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

input_genome<-args[1]  # genome
step<-args[2]  # window

library("seqinr")   

S<-as.numeric(step)

genome <- read.fasta(file = input_genome)   # Read input file
genome_seq <- genome[[1]] # get genome characters  

starts <- seq(1, length(genome_seq)- S, by = S)
n <- length(starts)    # Find length of vector "starts"
chunkGCs <- numeric(n) # Make empty vector of the same length as "starts"

for (i in 1:n) {
  chunk <- genome_seq[starts[i]:(starts[i]+S)]
  chunkGC <- GC(chunk)
  #print(chunkGC)
  chunkGCs[i] <- chunkGC
}

# plot GC:

pdf("GC_plot.pdf") #open pdf

plot(starts,chunkGCs, type="l", xlab="Nucleotide start",ylab="GC content")

dev.off() # close pdf 

