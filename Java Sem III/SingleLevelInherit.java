
class Vehicle {

    public Vehicle() {
        System.out.println("This is a vehicle");
    }
}

class Car extends Vehicle {

    public Car() {
        System.out.println("This vehicle is a Car ");
    }

}

public class SingleLevelInherit {

    public static void main(String[] args) {
        Car obj = new Car();

    }
}
