%V=3.25;                  % an example voltage 
%T3=0.1844; w=100; 	% an example frequency of 16 rad/sec needs 1.18 seconds for 3 cycles
%dt=.005;t=0:dt:T3;   	% create a time vector so we can plot sin(wt)
%plot(t, V*sin(w*t))  	% Verify input magnitude and period

%K=64;                  % steady state gain (rad/sec)/volt 
%tau=0.04; 		% time constant (sec)
%Gvspd=tf(K,[tau 1]);   	% transfer function from V to spd (volts to speed)
%bode(Gvspd,1:100)   	% type “help bode” at the command line for units


%t=0:.05:18.84;
%w=1; Vamp=3.25;
%Mg=63.9489; Ag=-2.2906;
%Vin=Vamp*sin(w*t);

%t=0:.005:0.378;
%w=50; Vamp=3.25;
%Mg=28.6217; Ag=-63.4349;

t=0:.0005:0.1884;
w=100; Vamp=3.25;
Mg=15.5223; Ag=-75.9638;

speed=Mg*Vamp*sin(w*t+Ag/180*pi);
plot(t,speed);
hold on
xlabel('time sec')
ylabel('speed in rad/sec')
title('speed output for w=100 rad/s')

%yyaxis left
%plot(t,Mg*sin(w*t+Ag/180*pi))
%ylim([-100 100])             % Refine these limits as needed, then 
                             % use this same limit for all 3 graphs
%ylabel('Rotational speed')
%yyaxis right
%plot(t,3.25*sin(w*t))
%ylim([-3.5 3.5])             % Refine these limits at needed, then
				        % use this same limit for all 3 graphs
%ylabel('Voltage input')
%title('Voltage and rotational speed for 1 rad/s')
%xlabel('time sec')

%legend( 'Rotational speed', 'Voltage input');
