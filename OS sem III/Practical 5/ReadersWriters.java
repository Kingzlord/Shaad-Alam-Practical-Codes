
import java.util.Scanner;

class ReaderWriter {

    private int readers = 0;
    private Boolean writing = false;

    public synchronized void read(int id) {
        try {
            while (writing) {
                wait();
            }
            readers++;
            System.out.println("Reader" + id + "is reading.");
            Thread.sleep(1000);
            System.out.println("Reader" + id + "finished reading.");
            readers--;
            if (readers == 0) {
                notifyAll();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public synchronized void write(int id) {
        try {
            while (writing || readers > 0) {
                wait();
            }
            writing = true;
            System.out.println("Writer" + id + "is writing.");
            Thread.sleep(1000);
            System.out.println("Writer" + id + "finished writing.");
            writing = false;
            notifyAll();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class Reader extends Thread {

    ReaderWriter rw;
    int id;

    Reader(ReaderWriter rw, int id) {
        this.rw = rw;
        this.id = id;
    }

    public void run() {
        rw.read(id);
    }
}

class Writer extends Thread {

    ReaderWriter rw;
    int id;

    Writer(ReaderWriter rw, int id) {
        this.rw = rw;
        this.id = id;
    }

    public void run() {
        rw.write(id);
    }
}

public class ReadersWriters {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ReaderWriter rw = new ReaderWriter();
        System.out.print("Enter number of readers:");
        int r = sc.nextInt();
        System.out.print("Enter number of writers:");
        int w = sc.nextInt();
        for (int i = 1; i <= r; i++) {
            new Reader(rw, i).start();
        }
        for (int i = 1; i <= w; i++) {
            new Writer(rw, i).start();
        }
        sc.close();
    }
}
