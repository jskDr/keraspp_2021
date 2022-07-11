println("Hello, Julia!")

# sum from 1 to 10
sum = 0
for i in 1:10
    global sum += i
end
println(sum)
