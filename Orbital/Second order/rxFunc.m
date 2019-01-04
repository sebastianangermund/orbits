function rx = rxFunc(x2,x1,Dx,Dy,K)

Rsq = Dx^2+Dy^2;
R = (Rsq)^(1/2);

cosV = Dx/R;

rx = 2*x2 - x1 - (K/Rsq)*cosV ; 

end