clear all

% ------------------------ Scaling constants

N = 5000;
M1 = 1000;
M2 = 10;
M3 = 10;

G = 1;

h = 0.01;

K1 = h^2*G*M1;
K2 = h^2*G*M2;
K2 = h^2*G*M3;

% ------------------------ Particle initial values

% ------- X1

V1X1 = 0;

X11 = 0;
X12 = X11 + h*V1X1;

X1r = zeros(1,N);
X1r(1) = X11;
X1r(2) = X12;

% ------- Y1

V1Y1 = 0;

Y11 = 0;
Y12 = Y11 + h*V1Y1;

Y1r = zeros(1,N);
Y1r(1) = Y11;
Y1r(2) = Y12;

% ------- X2

V1X2 = 0;

X21 = 40;
X22 = X21 + h*V1X2;

X2r = zeros(1,N);
X2r(1) = X21;
X2r(2) = X22;

% ------- Y2

V1Y2 = 4;

Y21 = 0;
Y22 = Y21 + h*V1Y2;

Y2r = zeros(1,N);
Y2r(1)=Y21;
Y2r(2)=Y22;

% ------------------------ Update position


for i = 3:N  
    
    Dx = X1r(i-1)-X2r(i-1);
    Dy = Y1r(i-1)-Y2r(i-1);
    
    % Update (X1,Y1)
    X1r(i) = rxFunc(X1r(i-1),X1r(i-2),Dx,Dy,K2);
    Y1r(i) = ryFunc(Y1r(i-1),Y1r(i-2),Dx,Dy,K2);
    % Update (X2,Y2)
    X2r(i) = rxFunc(X2r(i-1),X2r(i-2),-Dx,-Dy,K1);
    Y2r(i) = ryFunc(Y2r(i-1),Y2r(i-2),-Dx,-Dy,K1);
end

%%
plot(X1r(1),Y1r(1),'*')
hold on
plot(X2r(1),Y2r(1),'g*')
plot(X1r,Y1r)
plot(X2r,Y2r)

