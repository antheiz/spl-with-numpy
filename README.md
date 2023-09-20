# Dokumentasi Metode Eliminasi Gauss-Jordan

## Deskripsi
Kode ini merupakan implementasi dari metode eliminasi Gauss-Jordan untuk menyelesaikan sistem persamaan linear (SPL). Metode ini mengubah matriks koefisien menjadi bentuk eselon tereduksi, sehingga kita dapat dengan mudah menemukan solusi dari sistem persamaan tersebut.

## Fungsi `gauss_jordan(A, B)`
Fungsi ini menerima dua argumen, yaitu matriks koefisien `A` dan vektor hasil `B`. Fungsi ini akan mengembalikan solusi dari SPL.

### Algoritma:
1. **Eliminasi Gauss**: Proses ini bertujuan untuk mengubah matriks menjadi bentuk eselon atas.
    - Untuk setiap baris `k` dari matriks:
        - Untuk setiap baris `i` di bawah baris `k`:
            - Hitung faktor `lam` sebagai rasio elemen baris `i` kolom `k` dengan elemen diagonal baris `k`.
            - Kurangi baris `i` dengan `lam` kali baris `k`.
            - Kurangi elemen vektor hasil `B[i]` dengan `lam` kali `B[k]`.
2. **Substitusi Mundur**: Setelah matriks berada dalam bentuk eselon atas, kita dapat menemukan solusi dengan substitusi mundur.
    - Untuk setiap baris `m` dari bawah ke atas:
        - Hitung solusi `x[m]` dengan mengurangkan dot product dari baris matriks dengan solusi yang sudah ditemukan, dibagi dengan elemen diagonal.

## Contoh Penggunaan
Kode ini menyelesaikan empat sistem persamaan linear sebagai contoh. Setiap SPL dicetak ke layar bersama dengan matriks yang telah diubah dan solusi yang ditemukan.
