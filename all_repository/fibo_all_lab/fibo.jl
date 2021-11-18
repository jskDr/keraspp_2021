function fibo(n::Int)
    if n < 2
        n;
    else
        fibo(n-1) + fibo(n-2)
    end
end

println(fibo(45))
