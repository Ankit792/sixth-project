clc;
clear all;
close all;
a = input('Enter Message: ');
b = input('Enter Divisor: ');
c = length(b)
len = zeros(1,c-1)
d = [a,len]
[quo,rem] = gfdeconv(fliplr(d),fliplr(b))
if length(rem)<length(b)-1
 rem = [zeros(1,c-1-length(rem)),rem]
end
t = [a,rem]
[quo2,rem2] = gfdeconv(fliplr(t),fliplr(b))
display('Remainder is: ')
display(rem2)
if rem2==0
 display('Error not detected')
else
 display('Error detected')
end
