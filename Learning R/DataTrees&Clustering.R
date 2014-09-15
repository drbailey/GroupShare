mydata <- read.table("C:\\Users\\dbai00o\\Desktop\\Analytics\\SQLAExport.txt", header=TRUE,sep="\t")
mydata$card <- NULL
fit <- princomp(mydata, cor=TRUE)
summary(fit) # print variance accounted for 
loadings(fit) # pc loadings 
plot(fit,type="lines") # scree plot 
fit$scores # the principal components
biplot(fit)


mydata$card <- NULL
mydata$rx <- NULL
mydata$coffee <- NULL
require(tree)
treefit = tree(log(sales) ~ trxn+bakery+dairy+deli+floral+frozen+HHB+grocery+meat+prepac_meat+produce+seafood+tab+lifetime+last_seen,data=mydata)
plot(treefit)
text(treefit,cex=0.75)
sales.deciles = quantile(mydata$sales,0:10/10)
cut.sales = cut(mydata$sales,sales.deciles,include.lowest=TRUE)
plot(mydata$grocery,mydata$seafood,col=grey(10:2/11)[cut.sales],pch=20,xlab="grocery",ylab="seafood")
partition.tree(treefit,ordvars=c("grocery","seafood"),add=TRUE)
summary(treefit)treefit = tree(log(sales) ~ trxn+bakery+dairy+deli+floral+frozen+HHB+grocery+meat+prepac_meat+produce+seafood+tab+lifetime+last_seen,data=mydata,)

D <- read.table("C:\\Users\\dbai00o\\Desktop\\Analytics\\SQLAExport.txt", header=TRUE,sep="\t")
k = kmeans(D,10)
pairs(~trxn+log(sales)+bakery+dairy+deli+floral+frozen+HHB+grocery+meat+prepac_meat+produce+seafood+tab+lifetime+last_seen,data=D,main="Clustering in Plot Matrix", col=k$cluster) 




