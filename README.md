# travelyours-ml-model

- Link Deploy ML = https://travelyours-ml-model-4zcm2uhcpq-as.a.run.app

This repository content 2 machine learning models.
1. Image Classification
2. System Recommendation

## Update Flask API 

- Method : POST 
- URL : /

### Mengembalikan Nilai JSON
```json
{
  "name": "borobudur", 
  "uid": "647a94e9066891e6d6b9fcad"
}
```
### Lalu Redirect ke Link https://travelyours-api-4zcm2uhcpq-as.a.run.app/destination/{uid} 

```json
{
  "_id": "647caa51e853d9aaccbf0fbd",
  "name": "Candai Prambanan",
  "description": "Candi Prambanan adalah sebuah kompleks candi Hindu terkenal yang terletak di Yogyakarta, Indonesia. Dibangun pada abad ke-9 Masehi oleh kerajaan Mataram Kuno, candi ini merupakan salah satu warisan budaya yang paling mengagumkan di Indonesia. Dengan arsitektur yang megah dan detail ukiran yang indah, Candi Prambanan menjadi contoh keajaiban arsitektur Hindu klasik. Kompleks candi ini terdiri dari tiga candi utama yang didedikasikan untuk Trimurti Hindu, yaitu Shiva, Vishnu, dan Brahma, serta candi-candi kecil yang mengelilinginya. Keindahan dan keagungan Candi Prambanan membuatnya menjadi salah satu destinasi wisata paling populer di Indonesia, menarik minat pengunjung dari berbagai belahan dunia.",
  "location": "Yogyakarta",
  "price": 35000,
  "facilities": [
    "Area Wisata",
    "Restoran",
    "Toko Souvenir",
    "Toilet",
    "Panggung Pertunjukan"
  ],
  "__v": 0
}
```