function fibo(n::Int)
    if n < 2
        return n;
    end
    fibo(n-1) + fibo(n-2);
end

println(fibo(45))
