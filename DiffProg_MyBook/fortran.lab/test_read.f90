program hello
    implicit none
    ! This is a comment line.
    integer :: amount
    complex :: frequency
    integer :: age
    print *, 'Please enter your age: '
    read(*,*) age
    print *, 'Your age is: ', age
    amount = 10
    frequency = (1.0, -0.5)
    print *, 'The value of amount (integer) is ', amount
    print *, 'The value of frequency (complex) is', frequency
    print *, 'Hello, World!'
end program hello