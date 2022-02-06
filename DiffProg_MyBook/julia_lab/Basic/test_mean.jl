# gcc -Wall -shared -o myC.so mean.c
x = collect(Cint, 1:5)
println(x)
mylib = "/home/sjkim/wsl_data/github_clone/keraspp_2021/DiffProg_MyBook/julia_lab/Basic/myC.so"
aM = ccall((:vectorMean, mylib), Float64, (Ptr{Cint},Cint), x, 5)
println("Mean = ", aM)