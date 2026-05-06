fort_names = [
    "Raigad Fort",
    "Rajgad Fort",
    "Pratapgad Fort",
    "Ahmednagar Fort",
    "Lohagad Fort",
    "Shivneri Fort",
    "Sindhudurg Fort",
    "Murud-Janjira Fort",
    "Vijaydurg Fort",
    "Sinhagad Fort",
    "Daulatabad Fort",
    "Panhala Fort"
]

class_prompts = {
    "Raigad Fort": [
        "Raigad Fort steep hilltop Sahyadri Maharashtra stone fortification",
        "Raigad Fort Maha Darwaja grand entrance gate stone steps",
        "Raigad Fort ropeway cable car hilltop aerial view",
        "Raigad Fort Shivaji Maharaj coronation throne Jagdishwar temple ruins",
        "Raigad Fort panoramic view valley Sahyadri mountain plateau",
        "Raigad Fort massive stone walls hilltop isolated mountain Maharashtra",
        "Raigad capital Maratha empire stone ruins hilltop fort",
        "Raigad Fort market ruins Hirkani bastion stone walls"
    ],

    "Rajgad Fort": [
        "Rajgad Fort large flat plateau mountain top Maharashtra wide",
        "Rajgad Fort three machis Padmavati Suvela Sanjeevani plateau",
        "Rajgad Fort Padmavati temple on plateau hilltop",
        "Rajgad Fort massive sprawling hill fort Sahyadri",
        "Rajgad Fort Pali Darwaja entrance stone steps narrow path",
        "Rajgad Fort wide mountain plateau dense forest surroundings Pune district",
        "Rajgad Fort Balekilla citadel highest point hill fort",
        "Rajgad Fort steep rocky climb trekking Maharashtra"
    ],

    "Pratapgad Fort": [
        "Pratapgad Fort dense forest mountain hill fort Mahabaleshwar",
        "Pratapgad Fort Afzal Khan tomb near fort base forest",
        "Pratapgad Fort Bhavani Devi temple inside fort",
        "Pratapgad Fort cannon overlooking valley dense green forest",
        "Pratapgad Fort lower fort upper fort two-level structure",
        "Pratapgad Fort Maratha fort green hills Satara district",
        "Pratapgad Fort stone battlements overlooking thick forest valley",
        "Pratapgad Fort historic battle site green mountain Maharashtra"
    ],

    "Ahmednagar Fort": [
        "Ahmednagar Fort large circular ground level fort flat terrain",
        "Ahmednagar Fort circular bastion round towers walls flat land",
        "Ahmednagar Fort moat surrounding walls ground fort city",
        "Ahmednagar Fort twelve bastions circular stone fort",
        "Ahmednagar Fort Mughal prison British era fort flat ground",
        "Ahmednagar Fort wide open courtyard circular boundary walls",
        "Ahmednagar Fort low lying fort surrounded by moat city Maharashtra",
        "Ahmednagar Fort Chand Bibi palace inside fort grounds"
    ],

    "Lohagad Fort": [
        "Lohagad Fort zigzag narrow path four gates Vinchukata scorpion tail",
        "Lohagad Fort Vinchukata narrow rocky ridge path aerial view",
        "Lohagad Fort four successive gates Ganesh Narayan Hanuman Maha Darwaja",
        "Lohagad Fort hilltop Sahyadri Pune district stone walls",
        "Lohagad Fort narrow spine path connecting fort hill Maharashtra",
        "Lohagad Fort steep hill trekking destination Malavli",
        "Lohagad Fort stone steps winding path narrow ridge",
        "Lohagad Fort hilltop view Pawna lake below Maharashtra"
    ],

    "Shivneri Fort": [
        "Shivneri Fort triangular hill fort Junnar Maharashtra",
        "Shivneri Fort seven successive gates steep climb",
        "Shivneri Fort birthplace Shivaji Maharaj birth chamber inside",
        "Shivneri Fort Shivai Devi temple hilltop Junnar",
        "Shivneri Fort water tanks cisterns carved rock hilltop",
        "Shivneri Fort steep rocky hill triangular shape Pune district",
        "Shivneri Fort Kokna Darwaja entrance gate stone fort",
        "Shivneri Fort hilltop isolated rocky hill surrounded by valley"
    ],

    "Sindhudurg Fort": [
        "Sindhudurg Fort island sea fort Arabian Sea Malvan",
        "Sindhudurg Fort palm trees inside walls island fort",
        "Sindhudurg Fort surrounded by sea blue water island Maharashtra",
        "Sindhudurg Fort stone walls ocean water Malvan coast",
        "Sindhudurg Fort boat access island fort Konkan coast",
        "Sindhudurg Fort Shivaji Maharaj handprint footprint temple inside",
        "Sindhudurg Fort coral stone construction sea fort",
        "Sindhudurg Fort aerial view island surrounded by Arabian Sea"
    ],

    "Murud-Janjira Fort": [
        "Murud Janjira Fort circular island surrounded by sea tall towers",
        "Murud Janjira Fort tall round bastions island sea fort",
        "Murud Janjira Fort boat ride access island fort Murud",
        "Murud Janjira Fort massive walls rising from sea unconquered fort",
        "Murud Janjira Fort circular plan multiple round towers ocean",
        "Murud Janjira Fort Siddi sultanate island fort Konkan",
        "Murud Janjira Fort large cannons on sea walls",
        "Murud Janjira Fort dark stone walls tall towers surrounded water"
    ],

    "Vijaydurg Fort": [
        "Vijaydurg Fort coastal fort where river meets sea Devgad",
        "Vijaydurg Fort triple walls layered fortification sea fort",
        "Vijaydurg Fort Vaghotan river estuary sea meeting point fort",
        "Vijaydurg Fort Maratha navy base western coast Maharashtra",
        "Vijaydurg Fort three concentric walls sea fort Sindhudurg district",
        "Vijaydurg Fort stone fort at river mouth sea Konkan",
        "Vijaydurg Fort aerial view land connecting sea fort peninsula",
        "Vijaydurg Fort attached to land narrow strip coastal fort"
    ],

    "Sinhagad Fort": [
        "Sinhagad Fort hilltop fort near Pune Maharashtra plateau",
        "Sinhagad Fort steep cliff face rocky hilltop Pune",
        "Sinhagad Fort Kondana hill fort Pune valley view",
        "Sinhagad Fort Tanaji Malusare battle site historic fort",
        "Sinhagad Fort wide plateau top green hills Pune district",
        "Sinhagad Fort aerial view flat hilltop surrounded by valleys",
        "Sinhagad Fort stone walls plateau top popular trekking Pune",
        "Sinhagad Fort panoramic view Khadakwasla lake below Pune"
    ],

    "Daulatabad Fort": [
        "Daulatabad Fort spiral conical hill fort Aurangabad Maharashtra",
        "Daulatabad Fort perfectly conical rocky hill fort India",
        "Daulatabad Fort Deogiri hill fort cone shaped Aurangabad",
        "Daulatabad Fort steep conical rock isolated hill Maharashtra",
        "Daulatabad Fort ancient hilltop fort cone shape surrounded moat",
        "Daulatabad Fort Chand Minar tower near fort Aurangabad",
        "Daulatabad Fort vertical rocky cliff conical hill medieval fort",
        "Daulatabad Fort aerial view cone shaped hill fort Deccan"
    ],

    "Panhala Fort": [
        "Panhala Fort large hilltop fort Kolhapur Maharashtra plateau",
        "Panhala Fort wide plateau fort Sahyadri hills Kolhapur",
        "Panhala Fort Teen Darwaja three gates entrance fort",
        "Panhala Fort Andha Darwaja blind gate historic fort Kolhapur",
        "Panhala Fort large sprawling fort plateau western Maharashtra",
        "Panhala Fort Shivaji escape route Vishalgad fort Kolhapur",
        "Panhala Fort stone buildings granary inside fort Kolhapur",
        "Panhala Fort hilltop fort panoramic view Kolhapur district"
    ]
}