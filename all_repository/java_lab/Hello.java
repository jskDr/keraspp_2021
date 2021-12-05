// package all_repository.java_lab;
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        
        Fact afact = new Fact();
        System.out.println(afact.Factorial(4));

        Puppy mypuppy = new Puppy("Greeny");
        mypuppy.setAge(3);
        int age = mypuppy.getAge();
        System.out.println("age = " + age);

        Algo myalgo = new Algo();
        System.out.println(myalgo.fact(3));
        myalgo.Print(10);
    }
}
