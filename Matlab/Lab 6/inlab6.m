K=61;
tau=0.042;


s=tf('s');
G=K/(tau*s^2+s)

[y,t]=step(G);

plot(time,reference_speed,'r','LineWidth',2);
hold on
plot(time,actual_speed,'b');
hold on
plot(t,y,'g');
xlabel('time (seconds)')
ylabel('speed (radians/sec)')
title('Kpmax with voltage offset')
legend('reference speed','actual speed', 'theoretical speed')