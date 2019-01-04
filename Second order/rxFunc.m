function rx = rxFunc(x2,x1,Dx1,Dy1,Dx2,Dy2,K1,K2)

Rsq1 = Dx1^2+Dy1^2;
Rsq2 = Dx2^2+Dy2^2;

R1 = (Rsq1)^(1/2);
R2 = (Rsq2)^(1/2);

cosV1 = Dx1/R1;
cosV2 = Dx2/R2;

rx = 2*x2 - x1 - (K1/Rsq1)*cosV1 - (K2/Rsq2)*cosV2 ; 

end