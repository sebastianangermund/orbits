function ry = ryFunc(y2,y1,Dx,Dy,K)

Rsq = Dx^2+Dy^2;
R = (Rsq)^(1/2);

sinV = Dy/R;

ry = 2*y2 - y1 - (K/Rsq)*sinV ; 

end