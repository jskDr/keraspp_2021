// package all_repository.java_lab;
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        // run();
        Firstrepeater first_repeater = new Firstrepeater();
        first_repeater.run();
    }

    public static void run() {
        Fact afact = new Fact();
        System.out.println(afact.Factorial(4));

        Puppy mypuppy = new Puppy("Greeny");
        mypuppy.setAge(3);
        int age = mypuppy.getAge();
        System.out.println("age = " + age);

        FactAlgo myalgo = new FactAlgo();
        System.out.println(myalgo.fact(3));
        myalgo.Print(10);

        sort_test();
    }

    public static void sort_test() {
        Qsort myQsort = new Qsort();
        myQsort.qsort_test();
        myQsort.binsearch_test();
    }
}
