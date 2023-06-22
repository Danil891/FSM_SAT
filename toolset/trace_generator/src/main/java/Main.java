
import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {

        // Считываем аргументы в виде названий файлов в последовательности: a, b, m
        try {
            if (args.length == 0)
                throw new Exception("No parameters given");
            else if (!args[0].toUpperCase().equals("CSV") && !args[0].toUpperCase().equals("DAT"))
                throw new Exception("File format not specified");
            else if ((args.length > 4 && args[0].toUpperCase().equals("CSV")) || (args.length > 2 && args[0].toUpperCase().equals("DAT")))
                throw new Exception("Too many files to read");
            else if (args.length < 4 && args[0].toUpperCase().equals("CSV") || args.length < 2)
                throw new Exception("Not enough files to read");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(0);
        }

        File folder = new File("output_trace");
        if (!folder.exists()) {
            folder.mkdir();
        }

        List<Double> a = new ArrayList<>();
        List<Double> b = new ArrayList<>();
        List<Double> m = new ArrayList<>();

        //Работа с CSV файлом
        if (args[0].toUpperCase().equals("CSV")) {
            String[] names = new String[args.length];
            for (int i = 0; i < args.length - 1; i++) {
                names[i] = args[i+1];
                if (!names[i].toUpperCase().endsWith(".CSV"))
                    names[i] += ".CSV";
            }
            Double[] min = new Double[3];
            Double[] max = new Double[3];
            for (int i = 0; i < 3; i++) {
                min[i] = Double.MAX_VALUE;
                max[i] = Double.MIN_VALUE;
            }
            String row;
            // Заполняем списки a, b, m значениями на каждый считанный момент времени
            for (int i = 0; i < 3; i++) {
                BufferedReader csvReader = new BufferedReader(new FileReader("input\\" + names[i]));
                while ((row = csvReader.readLine()) != null) {
                    String[] data = row.split(",");
                    if (!data[0].equals("[s]")) {
                        Double right = Double.parseDouble(data[1]);
                        switch (i) {
                            case 0:
                                a.add(right);
                                break;
                            case 1:
                                b.add(right);
                                break;
                            default:
                                m.add(right);
                                break;
                        }
                        if (right > max[i])
                            max[i] = right;
                        if (right < min[i])
                            min[i] = right;
                    }
                }
                csvReader.close();
            }
            generate_comparison(a, b, m, false);
            // Преобразуем аналоговые значения в цифровые
            for (int i = 0; i < a.size(); i++) {
                if (a.get(i) <= ((max[0] + min[0]) / 2))
                    a.set(i, 0.0);
                else
                    a.set(i, 1.0);
                if (b.get(i) <= ((max[1] + min[1]) / 2))
                    b.set(i, 0.0);
                else
                    b.set(i, 1.0);
                if (m.get(i) <= ((max[2] + min[2]) / 2))
                    m.set(i, 0.0);
                else
                    m.set(i, 1.0);

            }
            generate_comparison(a, b, m, true);

        } else {
            //Работа с DAT файлом
            String name = args[1];
            if (!name.toUpperCase().endsWith(".DAT"))
                name += ".DAT";
            BufferedReader doReader = new BufferedReader(new FileReader("input\\" + name));
            String row;
            while ((row = doReader.readLine()) != null) {
                String[] data = row.split(" ");
                a.add(Double.parseDouble(data[1].substring(data[1].length() - 1)));
                b.add(Double.parseDouble(data[2].substring(data[2].length() - 1)));
                m.add(Double.parseDouble(data[3].substring(data[3].length() - 1)));
            }
            doReader.close();
            generate_comparison(a, b, m, true);
            File ana = new File("output_trace\\analog_waveform.txt");
            if (ana.exists()) {
                ana.delete();
            }
        }

        //Divide _-_-_---____---_
        // Находим среди a, b, m минимальный период смены сигнала
        int least = Integer.MAX_VALUE;
        int[] cnt = {0, 0, 0};
        boolean[] start = {false, false, false};
        for (int i = 1; i < a.size(); i++) { //Найти минимальный период смены сигнала среди a, b, m
            if (!a.get(i).equals(a.get(i - 1))) {
                if (!start[0])
                    start[0] = true;
                else {
                    if (cnt[0] < least) {
                        least = cnt[0];
                    }else
                        cnt[0] = 0;
                }
            }
            if (!b.get(i).equals(b.get(i - 1))) {
                if (!start[1])
                    start[1] = true;
                else {
                    if (cnt[1] < least) {
                        least = cnt[1];
                    }
                    cnt[1] = 0;
                }
            }
            if (!m.get(i).equals(m.get(i - 1))) {
                if (!start[2])
                    start[2] = true;
                else {
                    if (cnt[2] < least) {
                        least = cnt[2];
                    }
                    cnt[0] = 0;
                }
            }
            cnt[0]++;
            cnt[1]++;
            cnt[2]++;
        }
        start[0] = false;
        int div_cnt = 1; // Задаёт шаг записи значений a, b, m

        FileWriter nFile = new FileWriter("output_trace\\formed_trace.txt");
        nFile.write(a.get(0).intValue() + String.valueOf(b.get(0).intValue()) + " " + m.get(0).intValue() + "\n");
        for (int i = 1; i < a.size(); i++) {
            if (!start[0]) {
                if (!m.get(i).equals(m.get(i - 1)) || !b.get(i).equals(b.get(i - 1)) || !a.get(i).equals(a.get(i - 1)))
                    start[0] = true;
            } else {
                if (div_cnt >= (least / 2)) {
                    div_cnt = 1;
                    start[0] = false;
                    nFile.write(a.get(i).intValue() + String.valueOf(b.get(i).intValue()) + " " + m.get(i).intValue() + "\n");
                } else
                    div_cnt++;
            }
        }
        nFile.close();
        System.out.println("Finished successfully");
    }

    static void generate_comparison(List<Double> a, List<Double> b, List<Double> m, boolean digital) throws IOException {
        String name;
        if (digital) {
            name = "digital_waveform";
        } else {
            name = "analog_waveform";
        }
        FileWriter quick = new FileWriter("output_trace\\" + name + ".txt");
        for (int i = 0; i < a.size(); i++) {
            if (digital)
                quick.write(a.get(i).intValue() + " " + b.get(i).intValue() + " " + m.get(i).intValue() + "\n");
            else
                quick.write(a.get(i) + " " + b.get(i) + " " + m.get(i) + "\n");
        }
        quick.close();
    }
}
