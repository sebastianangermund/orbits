function ry = ryFunc(y2,y1,Dx1,Dy1,Dx2,Dy2,K1,K2)

Rsq1 = Dx1^2+Dy1^2;
Rsq2 = Dx2^2+Dy2^2;

R1 = (Rsq1)^(1/2);
R2 = (Rsq2)^(1/2);

sinV1 = Dy1/R1;
sinV2 = Dy2/R2;

ry = 2*y2 - y1 - (K1/Rsq1)*sinV1 - (K2/Rsq2)*sinV2 ; 

end