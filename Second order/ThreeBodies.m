%
% SIMULATE ORBITS OF A THREE BODY SYSTEM (SPECIFICALLY AN
% EARTH-MOON-SATELLITE SYSTEM) USING NEWTONS LAW OF GRAVITY.
%
% O(h^2)
%
% agge
%

% ------------------------- SCALING CONSTANTS ---------------------------
clear all

%Time step [seconds]
h = 2;
% N*timestep = simulation length in seconds
N = 300000;

%Earth mass [kg]
M1=5.97e24;
%Moon mass [kg]
M2=7.34e22;
%Satellite mass [kg]
M3=0;

%Gravitational constant [SI units]
G=6.67e-11;

%Calculation constants 
K1 = h^2*G*M1;
K2 = h^2*G*M2;
K3 = h^2*G*M3;

%Earth radius [m]
R=6.571e6;
%Moon radius [m]
Rmoon = 3.737e6;

%Coordinate constant
a=R/(2^(1/2));

%Earth escape velocity [m/s]
escV = 11e3;
%Satellite initial absolute velocity (scale the escape velocity)
v = 1.0*escV;

%Has the satellite crashed?
crashBinary = 0;


%%

% ------------------------ PARTICLE INITIAL VALUES -----------------------

% ---------------------------------------------- Particle 1

% ------- x-coordinate position and velocity X1

V1X1 = 0;

X11 = 0;
X12 = X11 + h*V1X1;

X1r = zeros(1,N);
X1r(1) = X11;
X1r(2) = X12;

% ------- y-coordinate position and velocity Y1

V1Y1 = 0;

Y11 = 0;
Y12 = Y11 + h*V1Y1;

Y1r = zeros(1,N);
Y1r(1) = Y11;
Y1r(2) = Y12;

% ---------------------------------------------- Particle 2

% ------- x-coordinate position and velocity X2

V1X2 = 0;

X21 = 363e6;
X22 = X21 + h*V1X2;

X2r = zeros(1,N);
X2r(1) = X21;
X2r(2) = X22;

% ------- y-coordinate position and velocity Y2

V1Y2 = 1100;

Y21 = 0;
Y22 = Y21 + h*V1Y2;

Y2r = zeros(1,N);
Y2r(1)=Y21;
Y2r(2)=Y22;

% ----------------------------------------------- Particle 3

% ------- x-coordinate position and velocity X3

V1X3 = 0.99*v/(2^(1/2));

X31 = -a;
X32 = X31 + h*V1X3;

X3r = zeros(1,N);
X3r(1) = X31;
X3r(2) = X32;

% ------- y-coordinate position and velocity Y3

V1Y3 = -0.99*v/(2^(1/2));

Y31 = -a;
Y32 = Y31 + h*V1Y3;

Y3r = zeros(1,N);
Y3r(1)=Y31;
Y3r(2)=Y32;

% ------------------------ UPDATE POSITION --------------------------------


for i = 3:N  
    
    % Slow the satellites velocity relative to the earth with some factor
    % at time t=t(i) 
    %if i == 85100
    %    ddx = X3r(i-1)-X3r(i-2);
    %    ddy = Y3r(i-1)-Y3r(i-2);
    %    X3r(i-1) = X3r(i-2) + ddx/(1.5);
    %    Y3r(i-1) = Y3r(i-2) + ddy/(1.5);
    %end
    
    %Speed up again
    %if i == 125000
    %    ddx = X3r(i-1)-X3r(i-2);
    %    ddy = Y3r(i-1)-Y3r(i-2);
    %    X3r(i-1) = X3r(i-2) + ddx*8;
    %    Y3r(i-1) = Y3r(i-2) + ddy*8;
    %end
    
    % Calculate change in position
    Dx12 = X1r(i-1)-X2r(i-1);
    Dy12 = Y1r(i-1)-Y2r(i-1);
    %Rsq12 = Dx12^2+Dy12^2;
    %R12 = (Rsq12)^(1/2);
    %
    Dx13 = X1r(i-1)-X3r(i-1);
    Dy13 = Y1r(i-1)-Y3r(i-1);
    %Rsq13 = Dx13^2+Dy13^2;
    %R13 = (Rsq13)^(1/2);
    %
    Dx23 = X2r(i-1)-X3r(i-1);
    Dy23 = Y2r(i-1)-Y3r(i-1);
    %Rsq23 = Dx23^2+Dy23^2;
    %R23 = (Rsq23)^(1/2);
    %
    % Update (X1,Y1)
    X1r(i) = rxFunc(X1r(i-1),X1r(i-2),Dx12,Dy12,Dx13,Dy13,K2,K3);
    Y1r(i) = ryFunc(Y1r(i-1),Y1r(i-2),Dx12,Dy12,Dx13,Dy13,K2,K3);
    % Update (X2,Y2)
    X2r(i) = rxFunc(X2r(i-1),X2r(i-2),-Dx12,-Dy12,Dx23,Dy23,K1,K3);
    Y2r(i) = ryFunc(Y2r(i-1),Y2r(i-2),-Dx12,-Dy12,Dx23,Dy23,K1,K3);
    % Update (X3,Y3)
    X3r(i) = rxFunc(X3r(i-1),X3r(i-2),-Dx13,-Dy13,-Dx23,-Dy23,K1,K2);
    Y3r(i) = ryFunc(Y3r(i-1),Y3r(i-2),-Dx13,-Dy13,-Dx23,-Dy23,K1,K2);
    
    crash = ((X2r(i)-X3r(i))^2+(Y2r(i)-Y3r(i))^2)^(1/2);
    endIndex = i;
    
    if crash<Rmoon
        crashBinary = 1;
        break
    end
end


%% ------------------------ SIMULATION PLOT ------------------------------

ylim([-1-2*X2r(1) 1.2*X2r(1)])          % choose suitable values for axes
xlim([-1.2*X2r(1) 1.2*X2r(1)])
hold on
for k=1:300:endIndex                    % plot e.g every 20:th if slow
    a=plot(X1r(k),Y1r(k),'b*');
    b=plot(X2r(k),Y2r(k),'g*');
    c=plot(X3r(k),Y3r(k),'r.');
    ylim([-1.2*X2r(1) 1.2*X2r(1)])      % choose suitable values for axes
    xlim([-1.2*X2r(1) 1.2*X2r(1)])
    pause(0.001)
    set(a,'Visible','off')
    set(b,'Visible','off')
    set(c,'Visible','off')
end

%% ------------------------ REGUALR PLOT ---------------------------------

plot(X1r(1),Y1r(1),'*')
%axis equal
hold on
plot(X2r(1),Y2r(1),'g*')
plot(X1r(1:i),Y1r(1:i))
plot(X2r(1:i),Y2r(1:i))
plot(X3r(1:i),Y3r(1:i))
if crashBinary == 1
    plot(X3r(i),Y3r(i),'r*')
end








