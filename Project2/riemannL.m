function result = riemannL(f, a, b, n)


result =0;
dx=(b-a)/n;
for i=0:n-1
    c = a+ i*dx;
    result=result+f(c);
end
result=dx*result;


end

