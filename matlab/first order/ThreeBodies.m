format long
clear all

%instabilt system (planet-m?ne-satellit)

m1=2000;
m2=50;
m3=0;
G=1;

K1=m1*G;
K2=m2*G;
K3=m3*G;

dt=0.002;

dv = @(d,dx,K) -K*(1/d)*(dx/(d^(1/2)))*dt;

X1=[0];
Y1=[0];
X2=[6];
Y2=[0];
X3=[6.26];%6.25
Y3=[0];

V1X=0;
V1Y=0;
V2X=0;
V2Y=17;
V3X=0;
V3Y=0;

%%

%instabilt system tre kroppar lite olika massa

format short
clear all

m1=100;
m2=100;
m3=100;
G=1;

K1=m1*G;
K2=m2*G;
K3=m3*G;

dt=0.001;

dv = @(d,dx,K) -K*(1/d)*(dx/(d^(1/2)))*dt;

X1=[0];
Y1=[0];
X2=[1];
Y2=[0];
X3=[1/2];
Y3=[sin((2*pi)/3)];

V1X=10*(1/2);
V1Y=10*(-sin((2*pi)/3));
V2X=10*(1/2);
V2Y=10*(sin((2*pi)/3));
V3X=-10*(1/4+(sin((2*pi)/3)^2))^(1/2);
V3Y=0;
%%

%jord måne störande planet

format short
clear all

m1=5.97e24;
m2=7.34e22;
m3=6e25;
m3=0;
G=6.67e-11;

K1=m1*G;
K2=m2*G;
K3=m3*G;

dt=400;
T=(30*24*60*60)/400;

dv = @(d,dx,K) -K*(1/d)*(dx/(d^(1/2)))*dt;

X1=[-4.4088e6];
Y1=[0];
X2=[363e6-(4.4088e6)];
Y2=[0];
X3=[400e6];
Y3=[400e6];

V1X=0;
V1Y=-13.52;
V2X=0;
V2Y=1100;
V3X=-200;
V3Y=0;


%%

%jord måne raket

format short
clear all

m1=5.97e24;
m2=7.34e22;
m3=0;
G=6.67e-11;

K1=m1*G;
K2=m2*G;
K3=m3*G;

dt=4;
T=(50*60*60)/2;
dv = @(d,dx,K) -K*(1/d)*(dx/(d^(1/2)))*dt;

R=6.571e6;
a=R/(2^(1/2));

X1=[0];
Y1=[0];
X2=[363e6];
Y2=[0];
X3=[-a];
Y3=[-a];

V1X=0;
V1Y=0;
V2X=0;
V2Y=1100;
V3X=11e3/(2^(1/2));
V3Y=-11e3/(2^(1/2));
Vvx=[];
Vvy=[];

 %%

T=[(V1X^2+V1Y^2)^(1/2);(V2X^2+V2Y^2)^(1/2);(V3X^2+V3Y^2)^(1/2)];
for i=1:50000
    dx1=X1(i)-X2(i);
    dy1=Y1(i)-Y2(i);
    dx2=X1(i)-X3(i);
    dy2=Y1(i)-Y3(i);
    d1=dx1^2+dy1^2;
    d2=dx2^2+dy2^2;
    vx1 = V1X + dv(d1,dx1,K2) + dv(d2,dx2,K3);
    vy1 = V1Y + dv(d1,dy1,K2) + dv(d2,dy2,K3);
    xny = X1(i) + vx1*dt;
    yny = Y1(i) + vy1*dt;
    X1 = [X1 xny];
    Y1 = [Y1 yny];
    V1X = vx1;
    V1Y = vy1;
    %%%%
    dx1=X2(i)-X1(i);
    dy1=Y2(i)-Y1(i);
    dx2=X2(i)-X3(i);
    dy2=Y2(i)-Y3(i);
    d1=dx1^2+dy1^2;
    d2=dx2^2+dy2^2;
    vx1 = V2X + dv(d1,dx1,K1) + dv(d2,dx2,K3);
    vy1 = V2Y + dv(d1,dy1,K1) + dv(d2,dy2,K3);
    xny = X2(i) + vx1*dt;
    yny = Y2(i) + vy1*dt;
    X2 = [X2 xny];
    Y2 = [Y2 yny];
    V2X = vx1;
    V2Y = vy1;
    %%%%
    dx1=X3(i)-X1(i);
    dy1=Y3(i)-Y1(i);
    dx2=X3(i)-X2(i);
    dy2=Y3(i)-Y2(i);
    d1=dx1^2+dy1^2;
    d2=dx2^2+dy2^2;
    vx1 = V3X + dv(d1,dx1,K1) + dv(d2,dx2,K2);
    vy1 = V3Y + dv(d1,dy1,K1) + dv(d2,dy2,K2);
    xny = X3(i) + vx1*dt;
    yny = Y3(i) + vy1*dt;
    X3 = [X3 xny];
    Y3 = [Y3 yny];
    V3X = vx1;
    V3Y = vy1;
    %%%% energi
    T=[T [(V1X^2+V1Y^2)^(1/2);(V2X^2+V2Y^2)^(1/2);(V3X^2+V3Y^2)^(1/2)]];
    
    
    %Vvx=[Vvx V3X];
    %Vvy=[Vvy V3Y];
end

%%
Vabs=(Vvx.^2+Vvy.^2).^(1/2);
time=1:1:T;
plot(time,Vvx,'b');
hold on
plot(time,Vvy,'r');
plot(time,Vabs,'g');

%%
figure
plot(X1(1),Y1(1),'*')
hold on
plot(X2(1),Y2(1),'g*')
hold on
plot(X3(1),Y3(1),'c*')
hold on
plot(X1,Y1)
hold on
plot(X2,Y2)
hold on
plot(X3,Y3)
hold on
%pos = [-6.371e6 -6.371e6 2*6.371e6 2*6.371e6];
%rectangle('Position',pos,'Curvature',[1 1])
axis equal
figure
plot(1:1:length(X1),T(1,:))
%%
%enkel rörelseplot

ylim([-10 10])
xlim([-10 10])
hold on
for k=1:3:length(X1)
    a=plot(X1(k),Y1(k),'r.');
    b=plot(X2(k),Y2(k),'b.');
    c=plot(X3(k),Y3(k),'g.');
    ylim([-10 10])
    xlim([-10 10])
    pause(0.001)
    set(a,'Visible','off')
    set(b,'Visible','off')
    set(c,'Visible','off')
end

%%
%jord måne störande planet rörelseplot

ylim([-6.1e8 6.1e8])
xlim([-6.1e8 6.1e8])
hold on
for k=1:100:length(X1)
    pos = [X1(k)-6.371e6 Y1(k)-6.371e6 2*6.371e6 2*6.371e6];
    a=plot(X1(k),Y1(k),'r.');
    b=plot(X2(k),Y2(k),'b.');
    c=plot(X3(k),Y3(k),'g.');
    d=rectangle('Position',pos,'Curvature',[1 1]);
    ylim([-6e8 6e8])
    xlim([-6e8 6e8])
    pause(0.03)
    set(a,'Visible','off')
    set(b,'Visible','off')
    set(c,'Visible','off')
    set(d,'Visible','off')
end


%%

VV1end=(V1X^2+V1Y^2)^(1/2)
VV2end=(V2X^2+V2Y^2)^(1/2)
VV3end=(V3X^2+V3Y^2)^(1/2)

ett=10*(1/2);
tva=10*(-sin((2*pi)/3));
VV1beg=(ett^2+tva^2)^(1/2)
tre=10*(1/2);
fyr=10*(sin((2*pi)/3));
VV2beg=(tre^2+fyr^2)^(1/2)
fem=-10*(1/4+(sin((2*pi)/3)^2))^(1/2);
sex=0;
VV3beg=(fem^2+sex^2)^(1/2)


