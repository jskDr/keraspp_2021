def fibo(n)
    if n < 2
        n
    else
        fibo(n-1) + fibo(n-2)
    end
end

puts fibo 45
