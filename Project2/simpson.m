function result = simpson(f,a,b,n)
result=0;

dx=(b-a)/n;
step=dx;
result=result+f(a)+f(b);
%^first and last indicies
for i=1:n-1
    c = a+ i*dx;
    r=rem(i,2);
    if isequal(r,0)
        result=result+4*f(c);
    else
        result=result+2*f(c);
    end
    %result=result+f(c);
end
d=dx/3;
result=d*result;

end
