function force(x, y, z)
    r2 = x^2 + y^2 + z^2
    n = sqrt(r2)
    return [x/(n*r2), y/(n*r2), z/(n*r2)]
end

function force_sum(pts)
    s = zeros(3)
    @time for i in 1:size(pts, 1) # ~0.3 seconds
        s += force(pts[i,:]...)
    end
    return s
end