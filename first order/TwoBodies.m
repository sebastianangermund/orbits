format long
clear all

m1=1;
m2=100;
G=1;

K1=m1*G;
K2=m2*G;

dt=0.002;

dv = @(d,dx,K) -K*(1/d)*(dx/(d^(1/2)))*dt;

X1=[4];
Y1=[0];
X2=[0];
Y2=[0];

V1X=0;
V1Y=3;
V2X=0;
V2Y=-0.1*(m1/m2)^(1/2)*3;

for i=1:10000
    dx1=X1(i)-X2(i);
    dy1=Y1(i)-Y2(i);
    d=dx1^2+dy1^2;
    vx1 = V1X + dv(d,dx1,K2);
    vy1 = V1Y + dv(d,dy1,K2);
    xny = X1(i) + vx1*dt;
    yny = Y1(i) + vy1*dt;
    X1 = [X1 xny];
    Y1 = [Y1 yny];
    V1X = vx1;
    V1Y = vy1;
    %%%%
    dx1=X2(i)-X1(i);
    dy1=Y2(i)-Y1(i);
    d=dx1^2+dy1^2;
    vx1 = V2X + dv(d,dx1,K1);
    vy1 = V2Y + dv(d,dy1,K1);
    xny = X2(i) + vx1*dt;
    yny = Y2(i) + vy1*dt;
    X2 = [X2 xny];
    Y2 = [Y2 yny];
    V2X = vx1;
    V2Y = vy1;
end

figure
plot(X1(1),Y1(1),'*')
hold on
plot(X2(1),Y2(1),'g*')
hold on
plot(X1,Y1)
hold on
plot(X2,Y2)

%%
ylim([-2 2])
xlim([-1 4])
hold on
for k=2:length(X1)
    plot(X1(k),Y1(k),'g.');
    plot(X2(k),Y2(k),'b.');
    %ylim([-4 4])
    %xlim([-4 4])
    pause(0.0001)
    %clf
end

%% 

clear all

N=1000;

Ms = 100;

G=1;

h=0.002;

rFunc = @(d2,d1,R,V) 2*d2 - d1 - ((h^2*G*Ms)/(R))*V ; % 

% X info

V1X=0;

X1 = 4;
X2 = X1 + h*V1X;

Xr = zeros(1,N);
Xr(1)=X1;
Xr(2)=X2;

% Y info

V1Y = 4;

Y1 = 0;
Y2 = Y1 + h*V1Y;

Yr = zeros(1,N);
Yr(1)=Y1;
Yr(2)=Y2;

% Update position

for i = 3:N
    %                                       Distance and x,y-components
    Rsq = Xr(i-1)^2+Yr(i-1)^2;
    R = (Rsq)^(1/2);
    cosV = Xr(i-1)/Rsq;
    sinV = Yr(i-1)/Rsq;
    %                                       Calculate new position
    Xr(i) = rFunc(Xr(i-1),Xr(i-2),R,cosV);
    Yr(i) = rFunc(Yr(i-1),Yr(i-2),R,sinV);
end

%%
plot(Xr,Yr)







