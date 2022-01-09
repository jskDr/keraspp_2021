using Zygote

f(x) = sin(cos(x))
ir = Zygote.@code_ir f(1.0)
display(ir)