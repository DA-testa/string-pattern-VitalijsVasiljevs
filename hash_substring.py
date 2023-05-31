# Vitalijs Vasiljevs 3. grupa , 221RDB265 
import re # importeju so biblioteku , lai atbrivoties no liekiem simboliem.
hashMap = {} # biblioteka, kur glabasies simboli
def read_input(): # Si funkcija dot izveleties lietotajam, vai tas grib ievadit manuali datus, vai izmantot gatavus datus no faila.
    mode = input()  
    if ((re.sub("[\r\n]", "", mode) == "I")) : # seit lietotajs manuali rakstit datus. P.s. ar re.sub() palidzibu atbrivojos no liekiem simboliem. 
        return (input().rstrip(), input().rstrip())  # P.s. ar rstrip() atbrivojos no liekam atstarpem sakuma un teksta beigas.            
    elif (re.sub("[\r\n]", "", mode) == "F") : # seit lietotajs izmantos gatavo failu ar datiem.
        file_name = "tests/06" 
        with open(file_name, 'r') as f: # kopeju informaciju no faila.
            lines = f.readlines()
        return(re.sub("[\n]", "", lines[0]), lines[1])   
    pass

def print_occurrences(output): # izvadu ieguto beiga rezultatu, ja tas eksiste.
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text): # saja funkcija es izmantoju Rabin–Karp’s algoritmu. Lai efektivi atrast
    list = [] # veidoju masivu kur glabasies atbilde.
    i = 0
    if len(pattern) > len(text): # parbaudu vai sablons nav lielaks par pasu tekstu, gadijuma ja ta ir taisniba, tad kods beidz savu darbibu.
        return ""
    for char in text: # Saja funkcija es ievietoju katru simbolu no teksta vardnica un dotu tam specialu indeksu.
        if char.isdigit(): # Seit es parbaudu ar isdigit(), vai esosais simbols ir cipars. Tas ir domats, lai vardnica nebutu kludu.
            hashMap[char] = int(char) # ievietoju vardnica jauno simbolu
        if not char in hashMap: # Seit parbaudu vai esosais simbols atrodas jau vardnica, ja neatrodas ievietoju to vardnica.
            hashMap[char] = 10+i
            i = i + 1
    start_index = 0 
    end_index = len(pattern) 
    pattern_value = get_value(pattern) # izsaucu funkciju, kura dabus sablona heshu, kurs talak tiks salidzinats ar teksta atseviskam dalam heshu.
    if pattern_value == "": # gadijuma ja metode get_value() tika konstatets, ka sablona kads no simboliem neeksite vardnica, apstadina kodu un nosuta tuksu kopu.
        return []
    substring_value = get_value(text[start_index:end_index]) # atkal izsauc funkciju, bet tagad lai dabut teksta dalas heshu, lai velak salidzinat to ar sablona heshu
    for i in range(len(text)-len(pattern)+1): # Seit darbojas Rabin–Karp’s algoritms. 
        if pattern_value == substring_value: # gadijuma ja sablona hesh sakrit ar teksta apskatamas dalas heshu, tad pievieno masiva list(kurs glaba rezultatu) sakumindeksu, kura tika atrasta sakariba starp abiem heshiem.
            list.append(start_index) # pievieno rezultatu
        if end_index == len(text): # parbauda vai robeza netika parsniegta.
            return list
        start_char_value = hashMap[text[start_index]] * 10**(len(pattern)-1) # aprekina heshu pirma teskta dalas simbola.
        end_index = end_index + 1 
        start_index = start_index + 1
        substring_value = (substring_value - start_char_value) * 10 + hashMap[text[end_index-1]] # aprekina jauno teksta dalas heshu, lai velak salidzinat to ar sablona heshu.
    return list 

def get_value(pattern): # Si metode parveido tekstu par specialu skaitli, kurs izmantosies salidzinajumam.
    value = 0
    len_of_pattern = len(pattern) - 1
    i = 0
    for char in pattern: 
        if not char in hashMap: # parbaudu vai visi sablona simboli eksiste vardnica, ja kaut viens nav, tad kods beidz savu darbibu, jo teksta nebus tada sablona.
            return ""
        value = value + hashMap[char] * 10**(len_of_pattern-i) # seit es izmanotoju algoritmu kurs palidz izveidot heshu(specialu skaitli)
        i = i + 1
    return value
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
