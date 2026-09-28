
class SharedResource {
//Synchronized method

    synchronized void printNumbers(String threadName) {
        for (int i = 1; i <= 5; i++) {
            System.out.println(threadName + ": " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}

class MyThread extends Thread {

    SharedResource resource;

    MyThread(SharedResource resource, String name) {
        this.resource = resource;
        setName(name);
    }

    public void run() {
        resource.printNumbers(getName());
    }
}

public class SynchronizationDemo {

    public static void main(String[] args) {
        SharedResource resource = new SharedResource();
        MyThread t1 = new MyThread(resource, "Thread-1");
        MyThread t2 = new MyThread(resource, "Thread-2");
        t1.start();
        t2.start();
    }
}
