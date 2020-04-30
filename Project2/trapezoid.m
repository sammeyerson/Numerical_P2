function result = trapezoid(f,a,b,n)
result=0;

dx=(b-a)/n;
for i=0:n-1
    c = a+ i*dx;
    d=a+(i+1)*dx;
    midpoint=(c+d)/2;
    result=result+f(midpoint);
end
result=dx*result;


end

