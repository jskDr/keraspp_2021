abstract type DrawObj end
struct Point <: DrawObj
    x::Int32
    y::Int32
end

struct Vec2D <: DrawObj
    x::Int32
    y::Int32
end 

function test1() 
    p1 = Point(1, 2)
    println(p1)
end

sum(p1::Point, p2::Point) = Point(p1.x + p2.x, p1.y + p2.y)
Base.:+(p1::Point, p2::Point) = Point(p1.x + p2.x, p1.y + p2.y)
Base.:+(p1::DrawObj, p2::DrawObj) = Point(p1.x + p2.x, p1.y + p2.y)

function test2()
    p1 = Point(1,2)
    p2 = Point(3,4)
    #println(sum(p1,p2))
    println(p1+p2)

    v1 = Vec2D(5,6)
    println(v1)
    println(v1+p1)
end

function test3()
    t = ccall(:clock, Int32, ())
    println(t)

    foo = 10
    @ccall printf("%s = %d\n"::Cstring; "foo"::Cstring, foo::Cint)::Cint
end

# main part
test1()
println("--------------------")
test2()
println("--------------------")
test3()


