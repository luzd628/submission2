import sklearn
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load Model
try:
  with open('model.pkl','rb') as file:
    model = pickle.load(file)
except Exception as e:
  print("Erorr while load model")

# Function Predict
def predict(input_data):
  try:
    new_data = pd.DataFrame(input_data, index=[0])
    predict = model.predict(new_data)

    if predict[0] == 1:
        return "Lulus"
    else:
        return "Dropout"
  except Exception as e:
    st.erorr(f"Predict Erorr")

# ---------------------------------------Main Page-----------------------------------------------
# Head
st.title("Prediksi Status Siswa")
st.write("Masukkan data siswa untuk memprediksi status kelulusan.")


# Form Input
with st.form("data_form"):
  st.subheader("Data Pribadi")
  # status perkawinan
  marital_status_options = [1, 2, 3, 4, 5, 6]
  marital_status_labels= {
      1:"Lajang",2:"Menikah",3:"Duda/Janda",4:"Cerai",5:"Hidup Berasama tapi belum menikah",6:"Pisah Secara Hukum"
  }
  marital_status = st.selectbox(
      label="Pilih Status Perkawinan",
      options=marital_status_options,
      format_func=lambda x: marital_status_labels[x]
  )

  # Jenis Kelamin
  gender_options = [0,1]
  gender_labels = { 1:"Laki-laki", 0:"Perempuan"}
  gender = st.selectbox(
      label="Jenis Kelamin",
      options=gender_options,
      format_func=lambda x: gender_labels[x]
  )

  # Prodi/Jurusan
  course_labels ={
      33: "Teknologi Produksi Biofuel",
      171: "Desain Animasi dan Multimedia",
      8014: "Pelayanan Sosial (kelas malam)",
      9003: "Agronomi",
      9070: "Desain Komunikasi",
      9085: "Keperawatan Hewan",
      9119: "Teknik Informatika",
      9130: "Ekinkultur",
      9147: "Manajemen",
      9238: "Pelayanan Sosial",
      9254: "Pariwisata",
      9500: "Keperawatan",
      9556: "Higiene Mulut",
      9670: "Manajemen Periklanan dan Pemasaran",
      9773: "Jurnalistik dan Komunikasi",
      9853: "Pendidikan Dasar",
      9991: "Manajemen (kelas malam)"
  }
    
  course = st.selectbox(
    label="Program Studi",
    options=list(course_labels.keys()),
    format_func=lambda x: course_labels[x]
  )

  st.subheader("Data Pendaftaran")
  # Umur saat pendaftaran
  age_at_enrollment = st.number_input(
      label="Usia Saat Pendaftaran",
      max_value=100,
      step=1
  )

  col1, col2,  = st.columns(2)
  # Metode pendaftaran
  with col1:
      application_mode_labels = {
          1 : "Tahap 1 - Kontingen umum",
          2 : "Peraturan No. 612/93",
          5 : "Tahap 1 - Kontingen khusus (Pulau Azores)",
          7 : "Pemilik gelar pendidikan tinggi lainnya",
          10 : "Peraturan No. 854-B/99",
          15 : "Mahasiswa internasional (sarjana)",
          16 : "Tahap 1 - Kontingen khusus (Pulau Madeira)",
          17 : "Tahap 2 - Kontingen umum",
          18 : "Tahap 3 - Kontingen umum",
          26 : "Peraturan No. 533-A/99, butir b2) (Rencana berbeda)",
          27 : "Peraturan No. 533-A/99, butir b3) (Institusi lain)",
          39 : "Usia di atas 23 tahun",
          42 : "Transfer",
          43 : "Ganti program studi",
          44 : "Pemilik diploma spesialisasi teknologi",
          51 : "Ganti institusi/program studi",
          53 : "Pemilik diploma pendidikan jenjang pendek",
          57 : "Ganti institusi/program studi (Internasional)"
      }
   
      application_mode = st.selectbox(
          label="Metode Pendaftaran",
          options=list(application_mode_labels.keys()),
          format_func=lambda x: application_mode_labels[x]
      )
  # Urutan pendaftaran
  with col2:
      application_order = st.number_input(
          label="Urutan Pendaftaran",
          min_value=0,
          max_value=9,
          value=0,
          step=1
      )
    
  # Nilai Ujian Pendaftaran
  admission_grade = st.number_input(
      label="Nilai Ujian Pendaftaran Masuk",
      min_value=0.0,
      max_value=200.0,
      value=100.0,
      step=0.1
  )

  st.subheader("Data pendidikan Terakhir")
  col3, col4,  = st.columns(2)
  # Pendidikan Terakhir
  with col3:
      previous_qualification_labels = {
          1: "Pendidikan Menengah",
          2: "Pendidikan Tinggi - Sarjana",
          3: "Pendidikan Tinggi - Gelar",
          4: "Pendidikan Tinggi - Magister",
          5: "Pendidikan Tinggi - Doktor",
          6: "Pernah Mengikuti Pendidikan Tinggi",
          9: "Kelas 12 - Tidak Tamat",
          10: "Kelas 11 - Tidak Tamat",
          12: "Lain-lain - Kelas 11",
          14: "Kelas 10",
          15: "Kelas 10 - Tidak Tamat",
          19: "Pendidikan Dasar Siklus 3 (Kelas 9/10/11) atau setara",
          38: "Pendidikan Dasar Siklus 2 (Kelas 6/7/8) atau setara",
          39: "Kursus Spesialisasi Teknologi",
          40: "Pendidikan Tinggi - Gelar (Siklus 1)",
          42: "Kursus Teknik Tinggi Profesional",
          43: "Pendidikan Tinggi - Magister (Siklus 2)"
      }
      previous_qualification = st.selectbox(
          label="Pendidikan Terakhir",
          options=list(previous_qualification_labels.keys()),
          format_func=lambda x: previous_qualification_labels[x]
      )

  # Nilai Pendidikan Terakhir
  with col4:
      previous_qualification_grade = st.number_input(
          label="Nilai Pendidikan Terakhir",
          min_value=0.0,
          max_value=200.0,
          value=100.0,
          step=0.1
      )

  st.subheader("Data Pekerjaan orang tua")
  col5, col6,  = st.columns(2)
  # Pekerjaan Ibu
  with col5:
      mothers_occupation_labels = {
              0: "Siswa", 1: "Perwakilan Kekuasaan Legislatif dan Badan Eksekutif, Direktur, dan Manajer Eksekutif", 2: "Spesialis dalam Kegiatan Intelektual dan Ilmiah", 3: "Teknisi dan Profesi Tingkat Menengah", 4: "Staf Administrasi", 5: "Pekerja Layanan Pribadi, Keamanan dan Keselamatan, dan Penjual", 6: "Petani dan Pekerja Terampil di Bidang Pertanian, Perikanan, dan Kehutanan", 7: "Pekerja Terampil di Bidang Industri, Konstruksi, dan Kerajinan", 8: "Operator Instalasi dan Mesin serta Pekerja Perakitan", 9: "Pekerja Tidak Terampil", 10: "Profesi Angkatan Bersenjata", 90: "Situasi Lain", 99: "(kosong)", 122: "Profesional Kesehatan", 123: "Guru", 125: "Spesialis di Bidang Teknologi Informasi dan Komunikasi (TIK)", 131: "Teknisi dan Profesional Tingkat Menengah di Bidang Sains dan Teknik", 132: "Teknisi dan Profesional Tingkat Menengah di Bidang Kesehatan", 134: "Teknisi Tingkat Menengah dari Layanan Hukum, Sosial, Olahraga, Budaya, dan Sejenisnya", 141: "Pekerja Kantor, Sekretaris Umum, dan Operator Pengolah Data", 143: "Operator Data, Akuntansi, Statistik, Layanan Keuangan, dan Registrasi", 144: "Staf Pendukung Administrasi Lainnya", 151: "Pekerja Layanan Pribadi", 152: "Penjual", 153: "Pekerja Perawatan Pribadi dan Sejenisnya", 171: "Pekerja Konstruksi Terampil dan Sejenisnya, Kecuali Tukang Listrik", 173: "Pekerja Terampil di Bidang Percetakan, Pembuatan Instrumen Presisi, Perhiasan, Pengrajin, dan Sejenisnya", 175: "Pekerja di Bidang Pengolahan Makanan, Pengolahan Kayu, Pakaian, dan Industri serta Kerajinan Lainnya", 191: "Pekerja Kebersihan", 192: "Pekerja Tidak Terampil di Bidang Pertanian, Peternakan, Perikanan, dan Kehutanan", 193: "Pekerja Tidak Terampil di Bidang Industri Ekstraktif, Konstruksi, Manufaktur, dan Transportasi", 194: "Asisten Persiapan Makanan"
      }

      mothers_occupation = st.selectbox(
          label="Pekerjaan Ibu",
          options=list(mothers_occupation_labels.keys()),
          format_func=lambda x: mothers_occupation_labels[x]
      )

  # Pekerjaan Ayah
  with col6:
      fathers_occupation_labels = {
              0: "Siswa", 1: "Perwakilan Kekuasaan Legislatif dan Badan Eksekutif, Direktur, dan Manajer Eksekutif", 2: "Spesialis dalam Kegiatan Intelektual dan Ilmiah", 3: "Teknisi dan Profesi Tingkat Menengah", 4: "Staf Administrasi", 5: "Pekerja Layanan Pribadi, Keamanan dan Keselamatan, dan Penjual", 6: "Petani dan Pekerja Terampil di Bidang Pertanian, Perikanan, dan Kehutanan", 7: "Pekerja Terampil di Bidang Industri, Konstruksi, dan Kerajinan", 8: "Operator Instalasi dan Mesin serta Pekerja Perakitan", 9: "Pekerja Tidak Terampil", 10: "Profesi Angkatan Bersenjata", 90: "Situasi Lain", 99: "(kosong)", 122: "Profesional Kesehatan", 123: "Guru", 125: "Spesialis di Bidang Teknologi Informasi dan Komunikasi (TIK)", 131: "Teknisi dan Profesional Tingkat Menengah di Bidang Sains dan Teknik", 132: "Teknisi dan Profesional Tingkat Menengah di Bidang Kesehatan", 134: "Teknisi Tingkat Menengah dari Layanan Hukum, Sosial, Olahraga, Budaya, dan Sejenisnya", 141: "Pekerja Kantor, Sekretaris Umum, dan Operator Pengolah Data", 143: "Operator Data, Akuntansi, Statistik, Layanan Keuangan, dan Registrasi", 144: "Staf Pendukung Administrasi Lainnya", 151: "Pekerja Layanan Pribadi", 152: "Penjual", 153: "Pekerja Perawatan Pribadi dan Sejenisnya", 171: "Pekerja Konstruksi Terampil dan Sejenisnya, Kecuali Tukang Listrik", 173: "Pekerja Terampil di Bidang Percetakan, Pembuatan Instrumen Presisi, Perhiasan, Pengrajin, dan Sejenisnya", 175: "Pekerja di Bidang Pengolahan Makanan, Pengolahan Kayu, Pakaian, dan Industri serta Kerajinan Lainnya", 191: "Pekerja Kebersihan", 192: "Pekerja Tidak Terampil di Bidang Pertanian, Peternakan, Perikanan, dan Kehutanan", 193: "Pekerja Tidak Terampil di Bidang Industri Ekstraktif, Konstruksi, Manufaktur, dan Transportasi", 194: "Asisten Persiapan Makanan"
      }
     
      fathers_occupationst = st.selectbox(
          label="Pekerjaan Ayah",
          options=list(fathers_occupation_labels.keys()),
          format_func=lambda x: fathers_occupation_labels[x]
      )

  st.subheader("Data tentang mahasiswa")
  # Waktu kehadiran
  daytime_attendance_labels = {1:"Siang",0:"Malam"}
  
  daytime_attendance = st.selectbox(
      label="Waktu Kehadiran",
      options=list(daytime_attendance_labels.keys()),
      format_func=lambda x: daytime_attendance_labels[x]
  )

  # Perantauan
  displaced = st.selectbox(
      label="Apakah Siswa merupakan Perantau",
      options={
          1:"Ya",
          2:"Tidak"
      },
      index=0
  )

  # Pemegang Beasiswa
  scholarship_holder = st.selectbox(
      label="Apakah Penerima Beasiswa",
      options={
          1:"Ya",
          0:"Tidak"
      },
      index=0
  )

  st.subheader("Data administrasi")
  col7, col8,  = st.columns(2)
  # Pembayaran terlambat
  with col7:
      tuition_fees_up_to_date = st.selectbox(
          label = "Apakah Biaya Kuliah bayar tepat waktu",
          options={
              1:"Ya",
              0:"Tidak"
          },
          index=0
      )

  # Hutang
  with col8:
      debtor = st.selectbox(
          label="Apakah Siswa Memiliki Hutang?",
          options={1: "Ya", 0: "Tidak"},
          index=0
      )


  st.subheader("Data nilai")
  col9, col10,  = st.columns(2)
  # Nlai matkul pada semester 1
  with col9:
      curricular_units_1st_sem_grade = st.number_input(
            label="Nilai Mata Kuliah Semester 1",
            min_value=0.0,
            max_value=20.0,
            value=10.0,
            step=0.1
      )

  # Nlai matkul pada semester 2
  with col10:
      curricular_units_2nd_sem_grade = st.number_input(
          label="Nilai Mata Kuliah Semester 2",
          min_value=0.0,
          max_value=20.0,
          value=10.0,
          step=0.1
      )

  st.subheader("Data kondisi ekonomi secara umum")
  # Tingkat Pengangguran
  unemployment_rate = st.number_input(
      label="Tingkat Pengangguran"
  )

  # Tingkat Inflasi
  inflation_rate = st.number_input(
      label="Tingkat Inflasi",
      min_value=0.0,
      value=2.0,
      step=0.1
  )

  # Indeks GDP
  gdp = st.number_input(
      label="Indeks GDP",
      min_value=0.0,
  )

  st.subheader("Data SKS")
  # Sks yang credited
  total_curricular_credited = st.number_input(
      label = "Total SKS Credited",
      min_value=0,
      value=0,
      step=1
  )

  col11, col12,  = st.columns(2)
  # Sks yg didaftarkan
  with col11:
      total_curricular_enrolled = st.number_input(
          label = "Total SKS didaftarkan",
          min_value=0,
          value=0,
          step=1
      )

  # Sks yang lulus
  with col12:
      total_curricular_approved = st.number_input(
          label = "Total SKS yang diterima/lulus",
          min_value=0,
          value=0,
          step=1
      )

  col13, col14,  = st.columns(2)
  # total sks evaluasi
  with col13:
      total_curricular_evaluations = st.number_input(
          label = "Total SKS yang di Evaluasi",
          min_value=0,
          value=0,
          step=1
      )
  
  # total sks tanpa evaluasi
  with col14:
      total_curricular_without_evaluation = st.number_input(
          label = "Total SKS tanpa evaluasi",
          min_value=0,
          value=0,
          step=1
      )

  submitted = st.form_submit_button("Prediksi")

#---------------------------------Prediction---------------------------------------
  if submitted:
    input_data = {
         'Marital_status': [marital_status],
            'Application_mode': [application_mode],
            'Application_order': [application_order],
            'Course': [course],
            'Daytime_evening_attendance': [daytime_attendance],
            'Previous_qualification': [previous_qualification],
            'Previous_qualification_grade': [previous_qualification_grade],
            'Mothers_occupation': [mothers_occupation],
            'Fathers_occupation': [fathers_occupation],
            'Admission_grade': [admission_grade],
            'Displaced': [displaced],
            'Debtor': [debtor],
            'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
            'Gender': [gender],
            'Scholarship_holder': [scholarship_holder],
            'Age_at_enrollment': [age_at_enrollment],
            'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
            'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
            'Unemployment_rate': [unemployment_rate],
            'Inflation_rate': [inflation_rate],
            'GDP': [gdp],
            'Total_Curricular_Credited': [total_curricular_credited],
            'Total_Curricular_Enrolled': [total_curricular_enrolled],
            'Total_Curricular_Approved': [total_curricular_approved],
            'Total_Curricular_Evaluations': [total_curricular_evaluations],
            'Total_Curricular_Without_Evaluation': [total_curricular_without_evaluation]
    }

    prediction = predict(input_data)
    if prediction:
      st.subheader(f"Hasil Prediksi:{prediction}")
