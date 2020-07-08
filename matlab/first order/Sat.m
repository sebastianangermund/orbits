format long
clear all

%G=6.7*10^(-11);
%M=6*10^24;
%R0=3,84400000;
%K=G*M/(10^16);

R0=1;
K=1;

vox=0; %Kontrollera mot cirkul?r acceleration!!!
voy=1;
dt=0.01;

dvx = @(x,y) -K*(1/(x^2+y^2))*(x/(x^2+y^2)^(1/2))*dt;

dvy = @(x,y) -K*(1/(x^2+y^2))*(y/(x^2+y^2)^(1/2))*dt;

X=[R0];
Y=[0];
VX=[vox];
VY=[voy];

for i=1:629
    vx = vox + dvx(X(i),Y(i));
    vy = voy + dvy(X(i),Y(i));
    xny = X(i) + vx*dt;
    yny = Y(i) + vy*dt;
    X = [X xny];
    Y = [Y yny];
    vox = vx;
    voy = vy;
    VX = [VX vox];
    VY = [VY voy];
end

vfunc = @(u,v) (u.^2+v.^2).^(1/2);

VV = vfunc(VX,VY);
lll=length(VV);
plot(linspace(1,lll,lll),VV)
axis equal
figure
xx=0;
yy=0;
plot(xx,yy,'*')
hold on
plot(R0,0,'g*')
hold on
plot(X,Y)
%%
xlab = xlabel({'$m\cdot 10^8$'});
ylab = ylabel({'$m\cdot 10^8$'});
set(xlab,'Interpreter','latex');
set(xlab,'FontSize',18);
set(ylab,'Interpreter','latex');
set(ylab,'FontSize',18);
legend('Earth','Moon','Orbit')
%ylim([-1.2 1.2])
%xlim([-1.2 1.2])
%%
plot(0,0,'*')
ylim([-2 2])
xlim([-2 2])
hold on
for k=2:length(X)
    plot(X(k),Y(k),'c.');
    %ylim([-4 4])
    %xlim([-4 4])
    pause(0.001)
    %clf
end


%%
comet(X,Y,0.1)

    