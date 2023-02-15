from models import save_to_json
import json 

book = [
{
'title':"Rok 1984",
'author':"George Orwell",
'release_year':"1949",
'genre':"Powieść dystopijna",
'description':'"Rok 1984" to opowieść o totalnym zniewoleniu człowieka przez władzę państwa totalitarnego, o przejęciu kontroli nad każdym aspektem życia jednostki, nawet jego uczuć i myśli.',
'readed': True,
'cover':'rok1984.jpg',
'score':"",
'reviev':""
},
{
'title':"Zabić drozda",
'author':"Charper Lee",
'release_year':"1960",
'genre':"Dramat",
'description':'"Zabic drozda" przedstawia życie w małym miasteczku na południu USA w okresie Wielkiego Kryzysu, w tym problem rasizmu',
'readed': True,
'cover':'zabic_drozda.jpg',
'score':"",
'reviev':""
},
{
'title':"Duma i upredzenie",
'author':"Jane Austen",
'release_year':"1813",
'genre':"Obyczajowa",
'description':'"Duma i uprzedzenie" opowiada o losach bohaterów ze środowiska angielskich wyższych sfer i pozwala zapoznać się z ich życiem na przełomie XVIII i XIX wieku.',
'readed': False,
'cover':'duma_i_uprzedzenie.jpg',
'score':"",
'reviev':""
}
]

save_to_json("books.json", book)