
%plot(V(160:end),w(160:end))
%hold on
%xlabel('voltage (volts)')
%ylabel('angular velocity (w)')
%title('Angular vel. vs. volts for a DC motor')


%plot(t,speed)
%hold on
%xlabel('time (Sec)')
%ylabel('speed (rad/s)')
%title('Frequency Response for 1 rad/s with no offset')

w=1;
yyaxis left
plot(t,speed)
ylim([40 230])
ylabel('Rotational speed (rad/s)')
yyaxis right
plot(t,V)

ylim([0 5])
ylabel('Input voltage (V)')
title(['William Lee Voltage and rotational speed for ',num2str(w), 'rad/s'])
T3=3*2*pi/w
xlim([t(end)-T3 t(end)])
