#Podesti

def materialaUzskaite(tips, izmers1, izmers2, skaits):
    #materialuAprekins() nodods datus

    # tips - "FINIERIS", "LISTE", "LENKIS"
    #"FINIERSIS" - izmers1, izmers2 - garums platums, skaits
    #"LISTE" - izmers1(garums), skaits
    #"LENKIS" - skaits

    pass





def materialuAprekins(platums, garums, augstums, skaits):
    #mainigie raksturo podestu

    #Podestam augsa un apaksa
    materialaUzskaite("FINIERIS", platums, garums, 2*skaits)

    #Podesta priekseja mala un aizmugureja mala
    materialaUzskaite("FINIERIS", garums, augstums, 2*skaits)

    #Podesta sanu malas
    materialaUzskaite("FINIERIS", platums, augstums, 2*skaits)



    #Listes

    #Augseja finiera plaksne - 4 listes
    #apakseja finiera plaksne - 4 listes
    #sanu malas - 4 listes

    materialaUzskaite("LISTE", garums, 0, 4*skaits)    

    materialaUzskaite("LISTE", platums, 0, 4*skaits)

    materialaUzskaite("LISTE", augstums, 0, 4*skaits)



    #Lenki

    materialaUzskaite("LENKIS", 0, 0, 8*skaits)

