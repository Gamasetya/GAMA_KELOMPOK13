public class PercobaanFunction {
    static void penjumlahan(int a, int b) {
        int c = a + b;
        System.out.println("Hasil penjumlahan: " + c);
    }
    static void pengurangan() {
        int c = 67 - 69;
        System.out.println("Hasil pengurangan: " + c);
    }
    static int pembagian(int a, int b) {
        int c = a / b;
        return c;
    }
    static int perkalian() {
        int c = 67 * 69;
        return c;
    }
    public static void main(String[] args) {
        penjumlahan(67,69);
        pengurangan();
        System.out.println("Hasil perkalian: " + perkalian());
        int d = pembagian(60,6);
        System.out.println("Hasil pembagian: " + d);
        System.out.println();
        System.out.println("-----------------");

        PercobaanMethod objek = new PercobaanMethod();

        objek.sapa();

        System.out.println(objek.perkenalan("Gama","Magetan","Ngerakit Gundam"));

        objek.umur(20);

    }
}
