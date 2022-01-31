load Q4.2_1rad.mat            % load experimental data
%load Q4.2_50rad.mat
%load Q4.2_100rad.mat

 
dt=.004;                 % sample time
 
% plot the experimentally obtained speed on the left axis
yyaxis left
plot(t, speed), hold on
ylabel('Rotational speed (rad/s)')
 
% Adjust the following limit so that the sine wave takes up the % entire plot for the first frequency, then keep the limits fixed % for the other two plots
%ylim([70 220])
ylim([-50 200])             %Used for w=50,100 rad/s
 
% plot the experimentally obtained input voltage on the right %axis
yyaxis right
plot(t, V)
ylabel('Input voltage (V)')
 
% Adjust the following limit so that the sine wave takes up the % entire plot for the first frequency, then keep the limits fixed % for the other two plots
ylim([2 4])
 
% (*) PARAMETERS FOR PREDICTED RESPONSE 
K = 59;                      % steady state gain
tau = 0.042;                % time constant
yshift = -27.31;                % motor driver deadband shift
Vamp = 1;                   % voltage amplitude for sine wave
Voff = 2.5;                   % voltage offset
w=1;                        % sine wave frequency

 
% plot the predicted response on the output axis
yyaxis left 

% mag and phase from predicted frequency response (pre-lab)
s = tf('s');
 
% (***) MODIFY THIS LINE TO ACCOUNT FOR SAMPLING DELAY
G=tf(K,[tau 1],'OutputDelay',dt)
%G= K/(tau*s+1);            % system transfer function
[mag,phase] = bode(G,w);


% (**) MODIFY THIS LINE TO ACCOUNT FOR OFFSETS
plot(t, mag*Vamp*sin(w*t+phase/180*pi)+K*Voff, '--');
legend('experiment','prediction')
title(['William Lee w= ',num2str(w), 'rad/s'])
  
% only view the last 3 periods of the data
T3=3*2*pi/w;  % time for 3 periods (from pre-lab)
xlim([ t(end)-T3 t(end)])

