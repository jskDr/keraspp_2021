public class Puppy {
    int puppyAge; 
    String puppyName;
    public Puppy() {
        System.out.println("I am a new Puppy.");
    }
    public Puppy(String name) {
        puppyName = name;
        System.out.println("My name  is " + puppyName);
    }
    public void setAge(int age) {
        puppyAge = age;
    }
    public int getAge() {
        return puppyAge;
    }
}