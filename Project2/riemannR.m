function result = riemannR(f, a, b, n)


result =0;
dx=(b-a)/n;
for i=1:n
    c = a+ i*dx;
    result=result+f(c);
end
result=dx*result;


end
