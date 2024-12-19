import json

class Groups:
    groups = {}
    elts_to_group = {}
    
    def __init__(self, l):
        self.groups = l
        self.update()
        
    def update(self):
        self.elts_to_group = {}
        for identifier, elts in self.groups.items():
            for elt in elts:
                self.elts_to_group[elt] = identifier
    
    def get_group(self, elt, default=None):
        if elt not in self.elts_to_group:
            return default
        return self.elts_to_group[elt]
    
    def get_elts(self, group, default=None):
        if group not in self.groups:
            return default
        return self.groups[group]
    
    def get_all_elts(self):
        return self.elts_to_group.keys()
     
    def get_groups_name(self):
        return self.groups.keys()

    def get_dict_groups_to_elts(self):
        return self.groups
    
    def get_dict_elts_to_groups(self):
        return self.elts_to_group
    

country_acronyms = Groups({

	"Afghanistan": [
		"Afghanistan",
		"afghanistan",
		"AF",
		"AFG",
		"4",
		"ISO 3166 2:AF",
	],

	"Åland Islands": [
		"Åland Islands",
		"aland islands",
		"AX",
		"ALA",
		"248",
		"ISO 3166 2:AX",
	],

	"Albania": [
		"Albania",
		"albania",
		"AL",
		"ALB",
		"8",
		"ISO 3166 2:AL",
	],

	"Algeria": [
		"Algeria",
		"algeria",
		"DZ",
		"DZA",
		"12",
		"ISO 3166 2:DZ",
        "algerie", 
	],

	"American Samoa": [
		"American Samoa",
		"american samoa",
		"AS",
		"ASM",
		"16",
		"ISO 3166 2:AS",
	],

	"Andorra": [
		"Andorra",
		"andorra",
		"AD",
		"AND",
		"20",
		"ISO 3166 2:AD",
	],

	"Angola": [
		"Angola",
		"angola",
		"AO",
		"AGO",
		"24",
		"ISO 3166 2:AO",
	],

	"Anguilla": [
		"Anguilla",
		"anguilla",
		"AI",
		"AIA",
		"660",
		"ISO 3166 2:AI",
	],

	"Antigua and Barbuda": [
		"Antigua and Barbuda",
		"antigua and barbuda",
		"AG",
		"ATG",
		"28",
		"ISO 3166 2:AG",
	],

	"Argentina": [
		"Argentina",
		"argentina",
		"AR",
		"ARG",
		"32",
		"ISO 3166 2:AR",
        "argentina espanol",
		"buenos aires",
		"arroyito"
	],

	"Armenia": [
		"Armenia",
		"armenia",
		"AM",
		"ARM",
		"51",
		"ISO 3166 2:AM",
        "armenia pyсский", 
	],

	"Aruba": [
		"Aruba",
		"aruba",
		"AW",
		"ABW",
		"533",
		"ISO 3166 2:AW",
        "aruba espanol"
	],

	"Australia": [
		"Australia",
		"australia",
		"AU",
		"AUS",
		"36",
		"ISO 3166 2:AU",
        "australia english", 
	],

	"Austria": [
		"Austria",
		"austria",
		"AT",
		"AUT",
		"40",
		"ISO 3166 2:AT",
        "osterreich",
		"autriche",
		"rakousko",
		"austria deutsch"
	],

	"Azerbaijan": [
		"Azerbaijan",
		"azerbaijan",
		"AZ",
		"AZE",
		"31",
		"ISO 3166 2:AZ",
        "azerbaijan русский"
	],

	"Bahamas": [
		"Bahamas",
		"bahamas",
		"BS",
		"BHS",
		"44",
		"ISO 3166 2:BS",
        "the bahamas"
	],

	"Bahrain": [
		"Bahrain",
		"bahrain",
		"BH",
		"BHR",
		"48",
		"ISO 3166 2:BH",
	],

	"Bangladesh": [
		"Bangladesh",
		"bangladesh",
		"BD",
		"BGD",
		"50",
		"ISO 3166 2:BD",
	],

	"Barbados": [
		"Barbados",
		"barbados",
		"BB",
		"BRB",
		"52",
		"ISO 3166 2:BB",
	],

	"Belarus": [
		"Belarus",
		"belarus",
		"BY",
		"BLR",
		"112",
		"ISO 3166 2:BY",
        "belarus pyсский"
	],

	"Belgium": [
		"Belgium",
		"belgium",
		"BE",
		"BEL",
		"56",
		"ISO 3166 2:BE",
        "belgique",
		"belgien",
		"belgie",
		"belgica",
		"belgium nederlands",
		"belgium francais"
	],

	"Belize": [
		"Belize",
		"belize",
		"BZ",
		"BLZ",
		"84",
		"ISO 3166 2:BZ",
	],

	"Benin": [
		"Benin",
		"benin",
		"BJ",
		"BEN",
		"204",
		"ISO 3166 2:BJ",
	],

	"Bermuda": [
		"Bermuda",
		"bermuda",
		"BM",
		"BMU",
		"60",
		"ISO 3166 2:BM",
	],

	"Bhutan": [
		"Bhutan",
		"bhutan",
		"BT",
		"BTN",
		"64",
		"ISO 3166 2:BT",
	],

	"Bolivia": [
		"Bolivia, Plurinational State of",
		"bolivia, plurinational state of",
		"BO",
		"BOL",
		"68",
		"ISO 3166 2:BO",
        "bolivia",
		"bolivia espanol",
		"la paz",
		"cochabamba",
		"el alto",
		"santa cruz de la sierra",
		"quillacollo"
	],

	"Bonaire and Sint Eustatius and Saba": [
		"Bonaire, Sint Eustatius and Saba",
		"bonaire, sint eustatius and saba",
		"BQ",
		"BES",
		"535",
		"ISO 3166 2:BQ",
	],

	"Bosnia and Herzegovina": [
		"Bosnia and Herzegovina",
		"bosnia and herzegovina",
		"BA",
		"BIH",
		"70",
		"ISO 3166 2:BA",
		"bosnia i hercegovina bosnian",
	],

	"Botswana": [
		"Botswana",
		"botswana",
		"BW",
		"BWA",
		"72",
		"ISO 3166 2:BW",
        "botswana english",
	],

	"Bouvet Island": [
		"Bouvet Island",
		"bouvet island",
		"BV",
		"BVT",
		"74",
		"ISO 3166 2:BV",
	],

	"Brazil": [
		"Brazil",
		"brazil",
		"BR",
		"BRA",
		"76",
		"ISO 3166 2:BR",
        "brasil",
		"brazil portugues", 
	],

	"British Indian Ocean Territory": [
		"British Indian Ocean Territory",
		"british indian ocean territory",
		"IO",
		"IOT",
		"86",
		"ISO 3166 2:IO",
	],

	"Brunei Darussalam": [
		"Brunei Darussalam",
		"brunei darussalam",
		"BN",
		"BRN",
		"96",
		"ISO 3166 2:BN",
        "brunei", 
	],

	"Bulgaria": [
		"Bulgaria",
		"bulgaria",
		"BG",
		"BGR",
		"100",
		"ISO 3166 2:BG",
        "bulgarie",
		"bulgaria български"
	],

	"Burkina Faso": [
		"Burkina Faso",
		"burkina faso",
		"BF",
		"BFA",
		"854",
		"ISO 3166 2:BF",
	],

	"Burundi": [
		"Burundi",
		"burundi",
		"BI",
		"BDI",
		"108",
		"ISO 3166 2:BI",
	],

	"Cabo Verde": [
		"Cabo Verde",
		"cabo verde",
		"CV",
		"CPV",
		"132",
		"ISO 3166 2:CV",
        "cape verde", 
	],

	"Cambodia": [
		"Cambodia",
		"cambodia",
		"KH",
		"KHM",
		"116",
		"ISO 3166 2:KH",
        "cambodia ភាសាខ្មែរ",
		"cambodia english"
	],

	"Cameroon": [
		"Cameroon",
		"cameroon",
		"CM",
		"CMR",
		"120",
		"ISO 3166 2:CM",
	],

	"Canada": [
		"Canada",
		"canada",
		"CA",
		"CAN",
		"124",
		"ISO 3166 2:CA",
        "quebec",
		"canada francais",
		"canada english",
		"5018 rue harwood",
		"kanada"
	],

	"Cayman Islands": [
		"Cayman Islands",
		"cayman islands",
		"KY",
		"CYM",
		"136",
		"ISO 3166 2:KY",
	],

	"Central African Republic": [
		"Central African Republic",
		"central african republic",
		"CF",
		"CAF",
		"140",
		"ISO 3166 2:CF",
	],

	"Chad": [
		"Chad",
		"chad",
		"TD",
		"TCD",
		"148",
		"ISO 3166 2:TD",
	],

	"Chile": [
		"Chile",
		"chile",
		"CL",
		"CHL",
		"152",
		"ISO 3166 2:CL",
        "chile espanol",
	],

	"China": [
		"China",
		"china",
		"CN",
		"CHN",
		"156",
		"ISO 3166 2:CN",
        "chine",
		"china 中文", 
	],

	"Christmas Island": [
		"Christmas Island",
		"christmas island",
		"CX",
		"CXR",
		"162",
		"ISO 3166 2:CX",
	],

	"Cocos (Keeling) Islands": [
		"Cocos (Keeling) Islands",
		"cocos (keeling) islands",
		"CC",
		"CCK",
		"166",
		"ISO 3166 2:CC",
	],

	"Colombia": [
		"Colombia",
		"colombia",
		"CO",
		"COL",
		"170",
		"ISO 3166 2:CO",
        "colombia espanol"
	],

	"Comoros": [
		"Comoros",
		"comoros",
		"KM",
		"COM",
		"174",
		"ISO 3166 2:KM",
	],

	"Congo": [
		"Congo",
		"congo",
		"CG",
		"COG",
		"178",
		"ISO 3166 2:CG",
	],

	"Democratic Republic of the Congo": [
		"Congo, Democratic Republic of the",
		"congo, democratic republic of the",
		"CD",
		"COD",
		"180",
		"ISO 3166 2:CD",
        "democratic republic of the congo",
		"republic of the congo", 
	],

	"Cook Islands": [
		"Cook Islands",
		"cook islands",
		"CK",
		"COK",
		"184",
		"ISO 3166 2:CK",
	],

	"Costa Rica": [
		"Costa Rica",
		"costa rica",
		"CR",
		"CRI",
		"188",
		"ISO 3166 2:CR",
        "costa rica espanol",
	],

	"Côte d'Ivoire": [
		"Côte d'Ivoire",
		"cote d'ivoire",
		"CI",
		"CIV",
		"384",
		"ISO 3166 2:CI",
        "cote d ivoire", 
	],

	"Croatia": [
		"Croatia",
		"croatia",
		"HR",
		"HRV",
		"191",
		"ISO 3166 2:HR",
        "croatia hrvatski", 
	],

	"Cuba": [
		"Cuba",
		"cuba",
		"CU",
		"CUB",
		"192",
		"ISO 3166 2:CU",
	],

	"Curaçao": [
		"Curaçao",
		"curacao",
		"CW",
		"CUW",
		"531",
		"ISO 3166 2:CW",
	],

	"Cyprus": [
		"Cyprus",
		"cyprus",
		"CY",
		"CYP",
		"196",
		"ISO 3166 2:CY",
        "cyprus ελληνικά",
	],

	"Czechia": [
		"Czechia",
		"czechia",
		"CZ",
		"CZE",
		"203",
		"ISO 3166 2:CZ",
        "czech republic",
		"česka republika",
		"république tchèque",
		"česko",
		"czech republic čeština"
	],

	"Denmark": [
		"Denmark",
		"denmark",
		"DK",
		"DNK",
		"208",
		"ISO 3166 2:DK",
        "danemark",
		"denmark dansk"
	],

	"Djibouti": [
		"Djibouti",
		"djibouti",
		"DJ",
		"DJI",
		"262",
		"ISO 3166 2:DJ",
	],

	"Dominica": [
		"Dominica",
		"dominica",
		"DM",
		"DMA",
		"212",
		"ISO 3166 2:DM",
	],

	"Dominican Republic": [
		"Dominican Republic",
		"dominican republic",
		"DO",
		"DOM",
		"214",
		"ISO 3166 2:DO",
        "republica dominicana espanol", 
	],

	"Ecuador": [
		"Ecuador",
		"ecuador",
		"EC",
		"ECU",
		"218",
		"ISO 3166 2:EC",
	],

	"Egypt": [
		"Egypt",
		"egypt",
		"EG",
		"EGY",
		"818",
		"ISO 3166 2:EG",
	],

	"El Salvador": [
		"El Salvador",
		"el salvador",
		"SV",
		"SLV",
		"222",
		"ISO 3166 2:SV",
        "el salvador espanol",
	],

	"Equatorial Guinea": [
		"Equatorial Guinea",
		"equatorial guinea",
		"GQ",
		"GNQ",
		"226",
		"ISO 3166 2:GQ",
		"ecuador espanol",
	],

	"Eritrea": [
		"Eritrea",
		"eritrea",
		"ER",
		"ERI",
		"232",
		"ISO 3166 2:ER",
	],

	"Estonia": [
		"Estonia",
		"estonia",
		"EE",
		"EST",
		"233",
		"ISO 3166 2:EE",
        "estonia",
		"estonia eesti",
	],

	"Eswatini": [
		"Eswatini",
		"eswatini",
		"SZ",
		"SWZ",
		"748",
		"ISO 3166 2:SZ",
        "swaziland english",
	],

	"Ethiopia": [
		"Ethiopia",
		"ethiopia",
		"ET",
		"ETH",
		"231",
		"ISO 3166 2:ET",
	],

	"Falkland Islands (Malvinas)": [
		"Falkland Islands (Malvinas)",
		"falkland islands (malvinas)",
		"FK",
		"FLK",
		"238",
		"ISO 3166 2:FK",
	],

	"Faroe Islands": [
		"Faroe Islands",
		"faroe islands",
		"FO",
		"FRO",
		"234",
		"ISO 3166 2:FO",
	],

	"Fiji": [
		"Fiji",
		"fiji",
		"FJ",
		"FJI",
		"242",
		"ISO 3166 2:FJ",
	],

	"Finland": [
		"Finland",
		"finland",
		"FI",
		"FIN",
		"246",
		"ISO 3166 2:FI",
        "suomi",
		"finland suomi",
	],

	"France": [
		"France",
		"france",
		"FR",
		"FRA",
		"250",
		"ISO 3166 2:FR",
        "bretagne",
		"normandie",
		"isere",
		"vandee",
		"francia",
		"saint philibert",
		"provence",
		"frankreich",
		"alsace",
		"angle",
		"frankrijk",
		"corsica",
		"francia espana",
		"france francais",
		"franca",
		"franciaorszag",
		"brittany",
		"normandy",
		"lait origine france",
		"porc origine france",
		"pays de la loire",
		"finistere",
		"vendee",
		"morbihan",
		"rhone alpes",
		"ille et vilaine",
		"nord pas de calais",
		"savoie",
		"cotes d armor",
		"sarthe",
		"loire atlantique",
		"calvados",
		"pas de calais",
		"loiret",
		"basse normandie",
		"29260 ploudaniel",
		"centre val de loire",
		"naturalim za quartier bel air 39330 port lesney france",
		"drome",
	],

	"French Guiana": [
		"French Guiana",
		"french guiana",
		"GF",
		"GUF",
		"254",
		"ISO 3166 2:GF",
	],

	"French Polynesia": [
		"French Polynesia",
		"french polynesia",
		"PF",
		"PYF",
		"258",
		"ISO 3166 2:PF",
	],

	"French Southern Territories": [
		"French Southern Territories",
		"french southern territories",
		"TF",
		"ATF",
		"260",
		"ISO 3166 2:TF",
	],

	"Gabon": [
		"Gabon",
		"gabon",
		"GA",
		"GAB",
		"266",
		"ISO 3166 2:GA",
	],

	"Gambia": [
		"Gambia",
		"gambia",
		"GM",
		"GMB",
		"270",
		"ISO 3166 2:GM",
	],

	"Georgia": [
		"Georgia",
		"georgia",
		"GE",
		"GEO",
		"268",
		"ISO 3166 2:GE",
        "georgia ქართული",
	],

	"Germany": [
		"Germany",
		"germany",
		"DE",
		"DEU",
		"276",
		"ISO 3166 2:DE",
        "deutschland",
		"allemagne",
		"alemania",
		"germania",
		"tyskland",
		"schleswig holstein",
		"německo",
		"германия",
		"germany deutsch"
	],

	"Ghana": [
		"Ghana",
		"ghana",
		"GH",
		"GHA",
		"288",
		"ISO 3166 2:GH",
        "ghana english"
	],

	"Gibraltar": [
		"Gibraltar",
		"gibraltar",
		"GI",
		"GIB",
		"292",
		"ISO 3166 2:GI",
	],

	"Greece": [
		"Greece",
		"greece",
		"GR",
		"GRC",
		"300",
		"ISO 3166 2:GR",
        "grece",
		"ελλάδα",
		"grèce",
		"greece ελληνικά"
	],

	"Greenland": [
		"Greenland",
		"greenland",
		"GL",
		"GRL",
		"304",
		"ISO 3166 2:GL",
        "griechenland", 
	],

	"Grenada": [
		"Grenada",
		"grenada",
		"GD",
		"GRD",
		"308",
		"ISO 3166 2:GD",
	],

	"Guadeloupe": [
		"Guadeloupe",
		"guadeloupe",
		"GP",
		"GLP",
		"312",
		"ISO 3166 2:GP",
	],

	"Guam": [
		"Guam",
		"guam",
		"GU",
		"GUM",
		"316",
		"ISO 3166 2:GU",
	],

	"Guatemala": [
		"Guatemala",
		"guatemala",
		"GT",
		"GTM",
		"320",
		"ISO 3166 2:GT",
        "guatemala espanol",
	],

	"Guernsey": [
		"Guernsey",
		"guernsey",
		"GG",
		"GGY",
		"831",
		"ISO 3166 2:GG",
	],

	"Guinea": [
		"Guinea",
		"guinea",
		"GN",
		"GIN",
		"324",
		"ISO 3166 2:GN",
	],

	"Guinea-Bissau": [
		"Guinea-Bissau",
		"guinea-bissau",
		"GW",
		"GNB",
		"624",
		"ISO 3166 2:GW",
        "Guinea Bissau",
		"guinea bissau"
	],

	"Guyana": [
		"Guyana",
		"guyana",
		"GY",
		"GUY",
		"328",
		"ISO 3166 2:GY",
        "guyane",
		"french guiana", 
	],

	"Haiti": [
		"Haiti",
		"haiti",
		"HT",
		"HTI",
		"332",
		"ISO 3166 2:HT",
	],

	"Heard Island and McDonald Islands": [
		"Heard Island and McDonald Islands",
		"heard island and mcdonald islands",
		"HM",
		"HMD",
		"334",
		"ISO 3166 2:HM",
	],

	"Holy See": [
		"Holy See",
		"holy see",
		"VA",
		"VAT",
		"336",
		"ISO 3166 2:VA",
	],

	"Honduras": [
		"Honduras",
		"honduras",
		"HN",
		"HND",
		"340",
		"ISO 3166 2:HN",
        "honduras espanol",
	],

	"Hong Kong": [
		"Hong Kong",
		"hong kong",
		"HK",
		"HKG",
		"344",
		"ISO 3166 2:HK",
        "hong kong 粵語", 
	],

	"Hungary": [
		"Hungary",
		"hungary",
		"HU",
		"HUN",
		"348",
		"ISO 3166 2:HU",
        "magyarorszag",
		"hungary magyar",
	],

	"Iceland": [
		"Iceland",
		"iceland",
		"IS",
		"ISL",
		"352",
		"ISO 3166 2:IS",
        "iceland islenska"
	],

	"India": [
		"India",
		"india",
		"IN",
		"IND",
		"356",
		"ISO 3166 2:IN",
        "indian subcontinent",
		"india english"
	],

	"Indonesia": [
		"Indonesia",
		"indonesia",
		"ID",
		"IDN",
		"360",
		"ISO 3166 2:ID",
        "indonesie",
		"indonesia bahasa indonesia",
		"indonésie"
	],

	"Iran": [
		"Iran, Islamic Republic of",
		"iran, islamic republic of",
		"IR",
		"IRN",
		"364",
		"ISO 3166 2:IR",
        "iran", 
	],

	"Iraq": [
		"Iraq",
		"iraq",
		"IQ",
		"IRQ",
		"368",
		"ISO 3166 2:IQ",
        "iraqi kurdistan",
		"irak"
	],

	"Ireland": [
		"Ireland",
		"ireland",
		"IE",
		"IRL",
		"372",
		"ISO 3166 2:IE",
        "irlande",
		"irland",
		"ireland english"
	],

	"Isle of Man": [
		"Isle of Man",
		"isle of man",
		"IM",
		"IMN",
		"833",
		"ISO 3166 2:IM",
	],

	"Israel": [
		"Israel",
		"israel",
		"IL",
		"ISR",
		"376",
		"ISO 3166 2:IL",
        "ישראל",
		"israel עברית"
	],

	"Italy": [
		"Italy",
		"italy",
		"IT",
		"ITA",
		"380",
		"ISO 3166 2:IT",
        "italie",
		"italia",
		"italien",
		"sardinia",
		"italy italiano"
	],

	"Jamaica": [
		"Jamaica",
		"jamaica",
		"JM",
		"JAM",
		"388",
		"ISO 3166 2:JM",
        "jamaica english"
	],

	"Japan": [
		"Japan",
		"japan",
		"JP",
		"JPN",
		"392",
		"ISO 3166 2:JP",
        "japan 日本語",
		"japon", 
	],

	"Jersey": [
		"Jersey",
		"jersey",
		"JE",
		"JEY",
		"832",
		"ISO 3166 2:JE",
	],

	"Jordan": [
		"Jordan",
		"jordan",
		"JO",
		"JOR",
		"400",
		"ISO 3166 2:JO",
	],

	"Kazakhstan": [
		"Kazakhstan",
		"kazakhstan",
		"KZ",
		"KAZ",
		"398",
		"ISO 3166 2:KZ",
        "kazakhstan pyсский"
	],

	"Kenya": [
		"Kenya",
		"kenya",
		"KE",
		"KEN",
		"404",
		"ISO 3166 2:KE",
	],

	"Kiribati": [
		"Kiribati",
		"kiribati",
		"KI",
		"KIR",
		"296",
		"ISO 3166 2:KI",
	],

	"South Korea": [
		"Korea, Democratic People's Republic of",
		"korea, democratic people's republic of",
		"KP",
		"PRK",
		"408",
		"ISO 3166 2:KP",
        "south korea", 
	],

	"North Korea": [
		"Korea, Republic of",
		"korea, republic of",
		"KR",
		"KOR",
		"410",
		"ISO 3166 2:KR",
        "north korea"
	],

	"Kuwait": [
		"Kuwait",
		"kuwait",
		"KW",
		"KWT",
		"414",
		"ISO 3166 2:KW",
	],

	"Kyrgyzstan": [
		"Kyrgyzstan",
		"kyrgyzstan",
		"KG",
		"KGZ",
		"417",
		"ISO 3166 2:KG",
        "kyrgyzstan русский", 
	],

	"Lao People's Democratic Republic": [
		"Lao People's Democratic Republic",
		"lao people's democratic republic",
		"LA",
		"LAO",
		"418",
		"ISO 3166 2:LA",
        "laos", 
	],

	"Latvia": [
		"Latvia",
		"latvia",
		"LV",
		"LVA",
		"428",
		"ISO 3166 2:LV",
        "latvia latviešu", 
	],

	"Lebanon": [
		"Lebanon",
		"lebanon",
		"LB",
		"LBN",
		"422",
		"ISO 3166 2:LB",
        "liban",
		"lebanon english"
	],

	"Lesotho": [
		"Lesotho",
		"lesotho",
		"LS",
		"LSO",
		"426",
		"ISO 3166 2:LS",
        "lesotho english"
	],

	"Liberia": [
		"Liberia",
		"liberia",
		"LR",
		"LBR",
		"430",
		"ISO 3166 2:LR",
	],

	"Libya": [
		"Libya",
		"libya",
		"LY",
		"LBY",
		"434",
		"ISO 3166 2:LY",
	],

	"Liechtenstein": [
		"Liechtenstein",
		"liechtenstein",
		"LI",
		"LIE",
		"438",
		"ISO 3166 2:LI",
	],

	"Lithuania": [
		"Lithuania",
		"lithuania",
		"LT",
		"LTU",
		"440",
		"ISO 3166 2:LT",
        "lithuania lietuvių"
	],

	"Luxembourg": [
		"Luxembourg",
		"luxembourg",
		"LU",
		"LUX",
		"442",
		"ISO 3166 2:LU",
	],

	"Macao": [
		"Macao",
		"macao",
		"MO",
		"MAC",
		"446",
		"ISO 3166 2:MO",
        "macau",
		"macau 中文", 
	],

	"Madagascar": [
		"Madagascar",
		"madagascar",
		"MG",
		"MDG",
		"450",
		"ISO 3166 2:MG",
	],

	"Malawi": [
		"Malawi",
		"malawi",
		"MW",
		"MWI",
		"454",
		"ISO 3166 2:MW",
	],

	"Malaysia": [
		"Malaysia",
		"malaysia",
		"MY",
		"MYS",
		"458",
		"ISO 3166 2:MY",
        "malaisie",
		"malaysia bahasa melayu",
		"malaysia english",
		"malaysia 中文",
		"johor" 
	],

	"Maldives": [
		"Maldives",
		"maldives",
		"MV",
		"MDV",
		"462",
		"ISO 3166 2:MV",
	],

	"Mali": [
		"Mali",
		"mali",
		"ML",
		"MLI",
		"466",
		"ISO 3166 2:ML",
	],

	"Malta": [
		"Malta",
		"malta",
		"MT",
		"MLT",
		"470",
		"ISO 3166 2:MT",
	],

	"Marshall Islands": [
		"Marshall Islands",
		"marshall islands",
		"MH",
		"MHL",
		"584",
		"ISO 3166 2:MH",
	],

	"Martinique": [
		"Martinique",
		"martinique",
		"MQ",
		"MTQ",
		"474",
		"ISO 3166 2:MQ",
	],

	"Mauritania": [
		"Mauritania",
		"mauritania",
		"MR",
		"MRT",
		"478",
		"ISO 3166 2:MR",
	],

	"Mauritius": [
		"Mauritius",
		"mauritius",
		"MU",
		"MUS",
		"480",
		"ISO 3166 2:MU",
	],

	"Mayotte": [
		"Mayotte",
		"mayotte",
		"YT",
		"MYT",
		"175",
		"ISO 3166 2:YT",
	],

	"Mexico": [
		"Mexico",
		"mexico",
		"MX",
		"MEX",
		"484",
		"ISO 3166 2:MX",
        "ciudad de mexico",
		"estado de mexico",
		"guanajuato",
		"jalisco",
		"cdmx",
		"durango",
		"mexique",
		"mexico espanol"
	],

	"Micronesia": [
		"Micronesia, Federated States of",
		"micronesia, federated states of",
		"FM",
		"FSM",
		"583",
		"ISO 3166 2:FM",
	],

	"Moldova": [
		"Moldova, Republic of",
		"moldova, republic of",
		"MD",
		"MDA",
		"498",
		"ISO 3166 2:MD",
        "moldova",
		"moldova roman", 
	],

	"Monaco": [
		"Monaco",
		"monaco",
		"MC",
		"MCO",
		"492",
		"ISO 3166 2:MC",
	],

	"Mongolia": [
		"Mongolia",
		"mongolia",
		"MN",
		"MNG",
		"496",
		"ISO 3166 2:MN",
        "mongolia монгол хэл"
	],

	"Montenegro": [
		"Montenegro",
		"montenegro",
		"ME",
		"MNE",
		"499",
		"ISO 3166 2:ME",
	],

	"Montserrat": [
		"Montserrat",
		"montserrat",
		"MS",
		"MSR",
		"500",
		"ISO 3166 2:MS",
	],

	"Morocco": [
		"Morocco",
		"morocco",
		"MA",
		"MAR",
		"504",
		"ISO 3166 2:MA",
        "maroc",
		"المغرب", 
	],

	"Mozambique": [
		"Mozambique",
		"mozambique",
		"MZ",
		"MOZ",
		"508",
		"ISO 3166 2:MZ",
	],

	"Myanmar": [
		"Myanmar",
		"myanmar",
		"MM",
		"MMR",
		"104",
		"ISO 3166 2:MM",
	],

	"Namibia": [
		"Namibia",
		"namibia",
		"nan",
		"NAM",
		"516",
		"ISO 3166 2:NA",
        "namibia english", 
	],

	"Nauru": [
		"Nauru",
		"nauru",
		"NR",
		"NRU",
		"520",
		"ISO 3166 2:NR",
	],

	"Nepal": [
		"Nepal",
		"nepal",
		"NP",
		"NPL",
		"524",
		"ISO 3166 2:NP",
	],

	"Netherlands": [
		"Netherlands, Kingdom of the",
		"netherlands, kingdom of the",
		"NL",
		"NLD",
		"528",
		"ISO 3166 2:NL",
        "pays bas",
		"netherlands",
		"niederlande",
		"nederland",
		"netherlands nederlands"
	],

	"New Caledonia": [
		"New Caledonia",
		"new caledonia",
		"NC",
		"NCL",
		"540",
		"ISO 3166 2:NC", 
	],

	"New Zealand": [
		"New Zealand",
		"new zealand",
		"NZ",
		"NZL",
		"554",
		"ISO 3166 2:NZ", 
        "new zealand english"
	],

	"Nicaragua": [
		"Nicaragua",
		"nicaragua",
		"NI",
		"NIC",
		"558",
		"ISO 3166 2:NI",
        "nicaragua espanol"
	],

	"Niger": [
		"Niger",
		"niger",
		"NE",
		"NER",
		"562",
		"ISO 3166 2:NE",
	],

	"Nigeria": [
		"Nigeria",
		"nigeria",
		"NG",
		"NGA",
		"566",
		"ISO 3166 2:NG",
	],

	"Niue": [
		"Niue",
		"niue",
		"NU",
		"NIU",
		"570",
		"ISO 3166 2:NU",
	],

	"Norfolk Island": [
		"Norfolk Island",
		"norfolk island",
		"NF",
		"NFK",
		"574",
		"ISO 3166 2:NF",
	],

	"North Macedonia": [
		"North Macedonia",
		"north macedonia",
		"MK",
		"MKD",
		"807",
		"ISO 3166 2:MK",
        "republic of macedonia",
		"north macedonia македонски јазик"
	],

	"Northern Mariana Islands": [
		"Northern Mariana Islands",
		"northern mariana islands",
		"MP",
		"MNP",
		"580",
		"ISO 3166 2:MP",
	],

	"Norway": [
		"Norway",
		"norway",
		"NO",
		"NOR",
		"578",
		"ISO 3166 2:NO",
        "norway norsk", 
	],

	"Oman": [
		"Oman",
		"oman",
		"OM",
		"OMN",
		"512",
		"ISO 3166 2:OM",
	],

	"Pakistan": [
		"Pakistan",
		"pakistan",
		"PK",
		"PAK",
		"586",
		"ISO 3166 2:PK",
	],

	"Palau": [
		"Palau",
		"palau",
		"PW",
		"PLW",
		"585",
		"ISO 3166 2:PW",
	],

	"Palestine": [
		"Palestine, State of",
		"palestine, state of",
		"PS",
		"PSE",
		"275",
		"ISO 3166 2:PS",
        "state of palestine",
		"palestinian territories", 
	],

	"Panama": [
		"Panama",
		"panama",
		"PA",
		"PAN",
		"591",
		"ISO 3166 2:PA",
        "panama espanol", 
	],

	"Papua New Guinea": [
		"Papua New Guinea",
		"papua new guinea",
		"PG",
		"PNG",
		"598",
		"ISO 3166 2:PG",
	],

	"Paraguay": [
		"Paraguay",
		"paraguay",
		"PY",
		"PRY",
		"600",
		"ISO 3166 2:PY",
        "paraguay espanol", 
	],

	"Peru": [
		"Peru",
		"peru",
		"PE",
		"PER",
		"604",
		"ISO 3166 2:PE",
        "lima",
		"peru espanol", 
	],

	"Philippines": [
		"Philippines",
		"philippines",
		"PH",
		"PHL",
		"608",
		"ISO 3166 2:PH",
        "philippines english", 
	],

	"Pitcairn": [
		"Pitcairn",
		"pitcairn",
		"PN",
		"PCN",
		"612",
		"ISO 3166 2:PN",
	],

	"Poland": [
		"Poland",
		"poland",
		"PL",
		"POL",
		"616",
		"ISO 3166 2:PL",
        "polska",
		"pologne",
		"polen",
		"poland polski"
	],

	"Portugal": [
		"Portugal",
		"portugal",
		"PT",
		"PRT",
		"620",
		"ISO 3166 2:PT",
        "portugal portugues", 
	],

	"Puerto Rico": [
		"Puerto Rico",
		"puerto rico",
		"PR",
		"PRI",
		"630",
		"ISO 3166 2:PR",
        "puerto rico espanol", 
	],

	"Qatar": [
		"Qatar",
		"qatar",
		"QA",
		"QAT",
		"634",
		"ISO 3166 2:QA",
	],

	"Réunion": [
		"Réunion",
		"reunion",
		"RE",
		"REU",
		"638",
		"ISO 3166 2:RE",
        "france la reunion",
		"la reunion", 
	],

	"Romania": [
		"Romania",
		"romania",
		"RO",
		"ROU",
		"642",
		"ISO 3166 2:RO",
        "romania romană", 
	],

	"Russian Federation": [
		"Russian Federation",
		"russian federation",
		"RU",
		"RUS",
		"643",
		"ISO 3166 2:RU",
        "russia",
		"russia русский",
		"абхазия",
		"soviet union"
	],

	"Rwanda": [
		"Rwanda",
		"rwanda",
		"RW",
		"RWA",
		"646",
		"ISO 3166 2:RW",
	],

	"Saint Barthélemy": [
		"Saint Barthélemy",
		"saint barthelemy",
		"BL",
		"BLM",
		"652",
		"ISO 3166 2:BL",
	],

	"Saint Helena and Ascension and Tristan da Cunha": [
		"Saint Helena, Ascension and Tristan da Cunha",
		"saint helena, ascension and tristan da cunha",
		"SH",
		"SHN",
		"654",
		"ISO 3166 2:SH",
	],

	"Saint Kitts and Nevis": [
		"Saint Kitts and Nevis",
		"saint kitts and nevis",
		"KN",
		"KNA",
		"659",
		"ISO 3166 2:KN",
	],

	"Saint Lucia": [
		"Saint Lucia",
		"saint lucia",
		"LC",
		"LCA",
		"662",
		"ISO 3166 2:LC",
	],

	"Saint Martin (French part)": [
		"Saint Martin (French part)",
		"saint martin (french part)",
		"MF",
		"MAF",
		"663",
		"ISO 3166 2:MF",
        "saint martin", 
	],

	"Saint Pierre and Miquelon": [
		"Saint Pierre and Miquelon",
		"saint pierre and miquelon",
		"PM",
		"SPM",
		"666",
		"ISO 3166 2:PM",
	],

	"Saint Vincent and the Grenadines": [
		"Saint Vincent and the Grenadines",
		"saint vincent and the grenadines",
		"VC",
		"VCT",
		"670",
		"ISO 3166 2:VC",
	],

	"Samoa": [
		"Samoa",
		"samoa",
		"WS",
		"WSM",
		"882",
		"ISO 3166 2:WS",
	],

	"San Marino": [
		"San Marino",
		"san marino",
		"SM",
		"SMR",
		"674",
		"ISO 3166 2:SM",
	],

	"Sao Tome and Principe": [
		"Sao Tome and Principe",
		"sao tome and principe",
		"ST",
		"STP",
		"678",
		"ISO 3166 2:ST",
	],

	"Saudi Arabia": [
		"Saudi Arabia",
		"saudi arabia",
		"SA",
		"SAU",
		"682",
		"ISO 3166 2:SA",
        "الدمام"
	],

	"Senegal": [
		"Senegal",
		"senegal",
		"SN",
		"SEN",
		"686",
		"ISO 3166 2:SN",
	],

	"Serbia": [
		"Serbia",
		"serbia",
		"RS",
		"SRB",
		"688",
		"ISO 3166 2:RS",
        "kosovo",
		"republika srpska",
		"serbia srpski",
	],

	"Seychelles": [
		"Seychelles",
		"seychelles",
		"SC",
		"SYC",
		"690",
		"ISO 3166 2:SC",
	],

	"Sierra Leone": [
		"Sierra Leone",
		"sierra leone",
		"SL",
		"SLE",
		"694",
		"ISO 3166 2:SL",
	],

	"Singapore": [
		"Singapore",
		"singapore",
		"SG",
		"SGP",
		"702",
		"ISO 3166 2:SG",
        "singapore english",
	],

	"Sint Maarten (Dutch part)": [
		"Sint Maarten (Dutch part)",
		"sint maarten (dutch part)",
		"SX",
		"SXM",
		"534",
		"ISO 3166 2:SX",
	],

	"Slovakia": [
		"Slovakia",
		"slovakia",
		"SK",
		"SVK",
		"703",
		"ISO 3166 2:SK",
        "slovak republic slovenčina", 
	],

	"Slovenia": [
		"Slovenia",
		"slovenia",
		"SI",
		"SVN",
		"705",
		"ISO 3166 2:SI",
        "slovenia slovene"
	],

	"Solomon Islands": [
		"Solomon Islands",
		"solomon islands",
		"SB",
		"SLB",
		"90",
		"ISO 3166 2:SB",
	],

	"Somalia": [
		"Somalia",
		"somalia",
		"SO",
		"SOM",
		"706",
		"ISO 3166 2:SO",
	],

	"South Africa": [
		"South Africa",
		"south africa",
		"ZA",
		"ZAF",
		"710",
		"ISO 3166 2:ZA",
        "south africa english"
	],

	"South Georgia and the South Sandwich Islands": [
		"South Georgia and the South Sandwich Islands",
		"south georgia and the south sandwich islands",
		"GS",
		"SGS",
		"239",
		"ISO 3166 2:GS",
	],

	"South Sudan": [
		"South Sudan",
		"south sudan",
		"SS",
		"SSD",
		"728",
		"ISO 3166 2:SS",
	],

	"Spain": [
		"Spain",
		"spain",
		"ES",
		"ESP",
		"724",
		"ISO 3166 2:ES",
        "espagne",
		"espana",
		"spanien",
		"cantabria",
		"santona",
		"spain espanol",
		"cordoba",
		"andalucia",
		"comunidad valenciana",
		"cataluna",
		"castilla y leon",
		"navarra",
		"castilla la mancha",
		"madrid comunidad autonoma",
		"valencia provincia",
		"murcia comunidad autonoma"
	],

	"Sri Lanka": [
		"Sri Lanka",
		"sri lanka",
		"LK",
		"LKA",
		"144",
		"ISO 3166 2:LK",
	],

	"Sudan": [
		"Sudan",
		"sudan",
		"SD",
		"SDN",
		"729",
		"ISO 3166 2:SD",
	],

	"Suriname": [
		"Suriname",
		"suriname",
		"SR",
		"SUR",
		"740",
		"ISO 3166 2:SR",
	],

	"Svalbard and Jan Mayen": [
		"Svalbard and Jan Mayen",
		"svalbard and jan mayen",
		"SJ",
		"SJM",
		"744",
		"ISO 3166 2:SJ",
	],

	"Sweden": [
		"Sweden",
		"sweden",
		"SE",
		"SWE",
		"752",
		"ISO 3166 2:SE",
        "sverige",
		"sweden svenska",
	],

	"Switzerland": [
		"Switzerland",
		"switzerland",
		"CH",
		"CHE",
		"756",
		"ISO 3166 2:CH",
        "suisse",
		"schweiz",
		"suiza",
		"švýcarsko",
		"switzerland francais",
		"switzerland deutsch"
	],

	"Syrian Arab Republic": [
		"Syrian Arab Republic",
		"syrian arab republic",
		"SY",
		"SYR",
		"760",
		"ISO 3166 2:SY",
        "syria", 
	],

	"Taiwan": [
		"Taiwan, Province of China",
		"taiwan, province of china",
		"TW",
		"TWN",
		"158",
		"ISO 3166 2:TW",
        "Taiwan",
		"taiwan",
		"taiwan 中文",
	],

	"Tajikistan": [
		"Tajikistan",
		"tajikistan",
		"TJ",
		"TJK",
		"762",
		"ISO 3166 2:TJ",
	],

	"Tanzania": [
		"Tanzania, United Republic of",
		"tanzania, united republic of",
		"TZ",
		"TZA",
		"834",
		"ISO 3166 2:TZ",
        "Tanzania","tanzania", 
	],

	"Thailand": [
		"Thailand",
		"thailand",
		"TH",
		"THA",
		"764",
		"ISO 3166 2:TH",
        "thailande",
		"thailand ไทย",
		"ประเทศไทย thai"
	],

	"Timor-Leste": [
		"Timor-Leste",
		"timor-leste",
		"TL",
		"TLS",
		"626",
		"ISO 3166 2:TL",
        "timor leste"
	],

	"Togo": [
		"Togo",
		"togo",
		"TG",
		"TGO",
		"768",
		"ISO 3166 2:TG",
	],

	"Tokelau": [
		"Tokelau",
		"tokelau",
		"TK",
		"TKL",
		"772",
		"ISO 3166 2:TK",
	],

	"Tonga": [
		"Tonga",
		"tonga",
		"TO",
		"TON",
		"776",
		"ISO 3166 2:TO",
	],

	"Trinidad and Tobago": [
		"Trinidad and Tobago",
		"trinidad and tobago",
		"TT",
		"TTO",
		"780",
		"ISO 3166 2:TT",
        "trinidad tobago english", 
	],

	"Tunisia": [
		"Tunisia",
		"tunisia",
		"TN",
		"TUN",
		"788",
		"ISO 3166 2:TN",
        "tunisie",
		"تونس"
	],

	"Türkiye": [
		"Türkiye",
		"turkiye",
		"TR",
		"TUR",
		"792",
		"ISO 3166 2:TR",
        "turquie",
		"turkey",
		"turkey turkce"
	],

	"Turkmenistan": [
		"Turkmenistan",
		"turkmenistan",
		"TM",
		"TKM",
		"795",
		"ISO 3166 2:TM",
	],

	"Turks and Caicos Islands": [
		"Turks and Caicos Islands",
		"turks and caicos islands",
		"TC",
		"TCA",
		"796",
		"ISO 3166 2:TC",
	],

	"Tuvalu": [
		"Tuvalu",
		"tuvalu",
		"TV",
		"TUV",
		"798",
		"ISO 3166 2:TV",
	],

	"Uganda": [
		"Uganda",
		"uganda",
		"UG",
		"UGA",
		"800",
		"ISO 3166 2:UG",
	],

	"Ukraine": [
		"Ukraine",
		"ukraine",
		"UA",
		"UKR",
		"804",
		"ISO 3166 2:UA",
        "україна",
		"ukraine yкраї́нська"
	],

	"United Arab Emirates": [
		"United Arab Emirates",
		"united arab emirates",
		"AE",
		"ARE",
		"784",
		"ISO 3166 2:AE",
		"emirats arabes unis",
		"émirats arabes unis", 
	],

	"United Kingdom of Great Britain and Northern Ireland": [
		"United Kingdom of Great Britain and Northern Ireland",
		"united kingdom of great britain and northern ireland",
		"GB",
		"GBR",
		"826",
		"ISO 3166 2:GB",
        "united kingdom",
		"royaume uni",
		"uk",
		"UK",
		"angleterre",
		"scotland",
		"england",
		"united kingdom english",
		"london",
		"ecosse",
	],

	"United States of America": [
		"United States of America",
		"united states of america",
		"US",
		"USA",
		"840",
		"ISO 3166 2:US",
        "united states",
		"usa",
		"estados unidos",
		"etats unis",
		"vereinigte staaten von amerika",
		"united states english",
		"united states espanol",
		"stany zjednoczone",
		"santa cruz"
	],

	"United States Minor Outlying Islands": [
		"United States Minor Outlying Islands",
		"united states minor outlying islands",
		"UM",
		"UMI",
		"581",
		"ISO 3166 2:UM",
	],

	"Uruguay": [
		"Uruguay",
		"uruguay",
		"UY",
		"URY",
		"858",
		"ISO 3166 2:UY", 
        "uruguay espanol"
	],

	"Uzbekistan": [
		"Uzbekistan",
		"uzbekistan",
		"UZ",
		"UZB",
		"860",
		"ISO 3166 2:UZ",
	],

	"Vanuatu": [
		"Vanuatu",
		"vanuatu",
		"VU",
		"VUT",
		"548",
		"ISO 3166 2:VU",
	],

	"Venezuela": [
		"Venezuela, Bolivarian Republic of",
		"venezuela, bolivarian republic of",
		"VE",
		"VEN",
		"862",
		"ISO 3166 2:VE",
        "Venezuela",
		"venezuela",
		"venezuela espanol"
	],

	"Viet Nam": [
		"Viet Nam",
		"viet nam",
		"VN",
		"VNM",
		"704",
		"ISO 3166 2:VN",
        "vietnam tiếng việt",
		"vietnam", 
	],

	"Virgin Islands (British)": [
		"Virgin Islands (British)",
		"virgin islands (british)",
		"VG",
		"VGB",
		"92",
		"ISO 3166 2:VG",
	],

	"Virgin Islands (U.S.)": [
		"Virgin Islands (U.S.)",
		"virgin islands (u.s.)",
		"VI",
		"VIR",
		"850",
		"ISO 3166 2:VI",
	],

	"Wallis and Futuna": [
		"Wallis and Futuna",
		"wallis and futuna",
		"WF",
		"WLF",
		"876",
		"ISO 3166 2:WF",
	],

	"Western Sahara": [
		"Western Sahara",
		"western sahara",
		"EH",
		"ESH",
		"732",
		"ISO 3166 2:EH",
	],

	"Yemen": [
		"Yemen",
		"yemen",
		"YE",
		"YEM",
		"887",
		"ISO 3166 2:YE",
	],

	"Zambia": [
		"Zambia",
		"zambia",
		"ZM",
		"ZMB",
		"894",
		"ISO 3166 2:ZM",
        "zambia english"
	],

	"Zimbabwe": [
		"Zimbabwe",
		"zimbabwe",
		"ZW",
		"ZWE",
		"716",
		"ISO 3166 2:ZW",
	],

})

subregion_country = Groups({
	
	"Western Europe" : [
        "Austria",
		"Belgium",
		"France",
		"Germany",
		"Liechtenstein",
		"Luxembourg",
		"Monaco",
		"Switzerland"
    ], 
    
	"Africa" : [
        "Congo",
		"Saint Helena and Ascension and Tristan da Cunha",   
		"Tanzania"
    ], 
    
	"Central Asia" : [
        "Kazakhstan",
		"Kyrgyzstan",
		"Tajikistan",
		"Turkmenistan",
		"Uzbekistan"
    ], 
    
	"Northern Europe" : [
        "Åland Islands",
		"Denmark",
		"Estonia",
		"Faroe Islands",
		"Finland",
		"Guernsey",
		"Iceland",
		"Ireland",
		"Isle of Man",
		"Jersey",
		"Latvia",
		"Lithuania",
		"Norway",
		"Svalbard and Jan Mayen",
		"Sweden",
		"United Kingdom of Great Britain and Northern Ireland"
    ], 
    
	"Americas" : [
        "Bolivia",
		"Bonaire and Sint Eustatius and Saba",
		"Venezuela"
    ], 
    
	"Sub-Saharan Africa" : [
        "Angola",
		"Benin",
		"Botswana",
		"British Indian Ocean Territory",
		"Burkina Faso",
		"Burundi",
		"Cabo Verde",
		"Cameroon",
		"Central African Republic",
		"Chad",
		"Comoros",
		"Congo",
        "Democratic Republic of the Congo",
		"Côte d'Ivoire",
		"Djibouti",
		"Equatorial Guinea",
		"Eritrea",
		"Eswatini",
		"Ethiopia",
		"French Southern Territories",
		"Gabon",
		"Gambia",
		"Ghana",
		"Guinea",
		"Guinea-Bissau",
		"Kenya",
		"Lesotho",
		"Liberia",
		"Madagascar",
		"Malawi",
		"Mali",
		"Mauritania",
		"Mauritius",
		"Mayotte",
		"Mozambique",
		"Namibia",
		"Niger",
		"Nigeria",
		"Réunion",
		"Rwanda",
		"Sao Tome and Principe",
		"Senegal",
		"Seychelles",
		"Sierra Leone",
		"Somalia",
		"South Africa",
		"South Sudan",
		"Togo",
		"Uganda",
		"Zambia",
		"Zimbabwe"
    ], 
    
	"Northern Africa" : [
        "Algeria",
		"Egypt",
		"Libya",
		"Morocco",
		"Sudan",
		"Tunisia",
		"Western Sahara"
    ], 
    
	"Polynesia" : [
        "American Samoa",
		"Cook Islands",
		"French Polynesia",
		"Niue",
		"Pitcairn",
		"Samoa",
		"Tokelau",
		"Tonga",
		"Tuvalu",
		"Wallis and Futuna"
    ], 
    
	"Melanesia" : [
        "Fiji",
		"New Caledonia",
		"Papua New Guinea",
		"Solomon Islands",
		"Vanuatu"
    ], 
    
	"Australia and New Zealand" : [
        "Australia",
		"Christmas Island",
		"Cocos (Keeling) Islands",
		"Heard Island and McDonald Islands",
		"New Zealand",
		"Norfolk Island"
    ], 
    
	"Oceania" : [
        "Micronesia"
    
	], 
    
	"Eastern Asia" : [
        "China",
		"Hong Kong",
		"Japan",
		"Macao",
		"Mongolia"
    ], 
    
	"Western Asia" : [
        "Armenia",
		"Azerbaijan",
		"Bahrain",
		"Cyprus",
		"Georgia",
		"Iraq",
		"Israel",
		"Jordan",
		"Kuwait",
		"Lebanon",
		"Oman",
		"Qatar",
		"Saudi Arabia",
		"Syrian Arab Republic",
		"Türkiye",
		"United Arab Emirates",
		"Yemen"
    ], 
    
	"Southern Asia" : [
        "Afghanistan",
		"Bangladesh",
		"Bhutan",
		"India",
		"Maldives",
		"Nepal",
		"Pakistan",
		"Sri Lanka"
    ], 
    
	"Asia" : [
        "Iran",
		"North Korea",
		"South Korea",
		"Palestine"
    ], 
    
	"Latin America and the Caribbean" : [
        "Anguilla",
		"Antigua and Barbuda",
		"Argentina",
		"Aruba",
		"Bahamas",
		"Barbados",
		"Belize",
		"Bouvet Island",
		"Brazil",
		"Cayman Islands",
		"Chile",
		"Colombia",
		"Costa Rica",
		"Cuba",
		"Curaçao",
		"Dominica",
		"Dominican Republic",
		"Ecuador",
		"El Salvador",
		"Falkland Islands (Malvinas)",
		"French Guiana",
		"Grenada",
		"Guadeloupe",
		"Guatemala",
		"Guyana",
		"Haiti",
		"Honduras",
		"Jamaica",
		"Martinique",
		"Mexico",
		"Montserrat",
		"Nicaragua",
		"Panama",
		"Paraguay",
		"Peru",
		"Puerto Rico",
		"Saint Barthélemy",
		"Saint Kitts and Nevis",
		"Saint Lucia",
		"Saint Martin (French part)",
		"Saint Vincent and the Grenadines",
		"Sint Maarten (Dutch part)",
		"South Georgia and the South Sandwich Islands",
		"Suriname",
		"Trinidad and Tobago",
		"Turks and Caicos Islands",
		"Uruguay",
		"Virgin Islands (British)",
		"Virgin Islands (U.S.)"
    ], 
    
	"South-eastern Asia" : [
        "Brunei Darussalam",
		"Cambodia",
		"Indonesia",
		"Lao People's Democratic Republic",
		"Malaysia",
		"Myanmar",
		"Philippines",
		"Singapore",
		"Thailand",
		"Timor-Leste",
		"Viet Nam",
        "singapore english", 
        "Taiwan",
    ], 
    
	"Northern America" : [
        "Bermuda",
		"Canada",
		"Greenland",
		"Saint Pierre and Miquelon",
		"United States of America",
		"kanada", 
	], 
    
	"Southern Europe" : [
        "Albania",
		"Andorra",
		"Bosnia and Herzegovina",
		"Croatia",
		"Gibraltar",
		"Greece",
		"Holy See",
		"Italy",
		"Malta",
		"Montenegro",
		"North Macedonia",
		"Portugal",
		"San Marino",
		"Serbia",
		"Slovenia",
		"Spain"
    
	], 
    
	"Micronesia" : [
        "Guam",
		"Kiribati",
		"Marshall Islands",
		"Nauru",
		"Northern Mariana Islands",
		"Palau",
		"United States Minor Outlying Islands"
    ], 
    
	"Eastern Europe" : [
        "Belarus",
		"Bulgaria",
		"Czechia",
		"Hungary",
		"Poland",
		"Romania",
		"Russian Federation",
		"Slovakia",
		"Ukraine"
    ], 
    
	"Europe" : [
        "Moldova",
		"Netherlands"
    ]

})

region_country = Groups({
    "Africa" : [
        "Algeria",
		"Angola",
		"Benin",
		"Botswana",
		"British Indian Ocean Territory",
		"Burkina Faso",
		"Burundi",
		"Cabo Verde",
		"Cameroon",
		"Central African Republic",
		"Chad",
		"Comoros",
		"Congo",
        "Democratic Republic of the Congo",
		"Côte d'Ivoire",
		"Djibouti",
		"Egypt",
		"Equatorial Guinea",
		"Eritrea",
		"Eswatini",
		"Ethiopia",
		"French Southern Territories",
		"Gabon",
		"Gambia",
		"Ghana",
		"Guinea",
		"Guinea-Bissau",
		"Kenya",
		"Lesotho",
		"Liberia",
		"Libya",
		"Madagascar",
		"Malawi",
		"Mali",
		"Mauritania",
		"Mauritius",
		"Mayotte",
		"Morocco",
		"Mozambique",
		"Namibia",
		"Niger",
		"Nigeria",
		"Réunion",
		"Rwanda",
        "Saint Helena and Ascension and Tristan da Cunha",
		"Sao Tome and Principe",
		"Senegal",
		"Seychelles",
		"Sierra Leone",
		"Somalia",
		"South Africa",
		"South Sudan",
		"Sudan",
		"Togo",
		"Tanzania",
		"Tunisia",
		"Uganda",
		"Western Sahara",
		"Zambia",
		"Zimbabwe", 
    ], 
    
	"Americas" : [
        "Anguilla",
		"Antigua and Barbuda",
		"Argentina",
		"Aruba",
		"Bahamas",
		"Barbados",
		"Belize",
		"Bermuda",
        "Bolivia",
        "Bonaire and Sint Eustatius and Saba",
		"Bouvet Island",
		"Brazil",
		"Canada",
		"Cayman Islands",
		"Chile",
		"Colombia",
		"Costa Rica",
		"Cuba",
		"Curaçao",
		"Dominica",
		"Dominican Republic",
		"Ecuador",
		"El Salvador",
		"Falkland Islands (Malvinas)",
		"French Guiana",
		"Greenland",
		"Grenada",
		"Guadeloupe",
		"Guatemala",
		"Guyana",
		"Haiti",
		"Honduras",
		"Jamaica",
		"Martinique",
		"Mexico",
		"Montserrat",
		"Nicaragua",
		"Panama",
		"Paraguay",
		"Peru",
		"Puerto Rico",
		"Saint Barthélemy",
		"Saint Kitts and Nevis",
		"Saint Lucia",
		"Saint Martin (French part)",
		"Saint Pierre and Miquelon",
		"Saint Vincent and the Grenadines",
		"Sint Maarten (Dutch part)",
		"South Georgia and the South Sandwich Islands",
		"Suriname",
		"Trinidad and Tobago",
		"Turks and Caicos Islands",
		"United States of America",
		"Uruguay",
		"Venezuela",
		"Virgin Islands (British)",
		"Virgin Islands (U.S.)"
    ], 
    
	"Oceania" : [
        "American Samoa",
		"Australia",
		"Christmas Island",
		"Cocos (Keeling) Islands",
		"Cook Islands",
		"Fiji",
		"French Polynesia",
		"Guam",
		"Heard Island and McDonald Islands",
		"Kiribati",
		"Marshall Islands",
        "Micronesia",
		"Nauru",
		"New Caledonia",
		"New Zealand",
		"Niue",
		"Norfolk Island",
		"Northern Mariana Islands",
		"Palau",
		"Papua New Guinea",
		"Pitcairn",
		"Samoa",
		"Solomon Islands",
		"Tokelau",
		"Tonga",
		"Tuvalu",
		"United States Minor Outlying Islands",
		"Vanuatu",
		"Wallis and Futuna"
    ], 
    
	"Asia" : [
        "Afghanistan",
		"Armenia",
		"Azerbaijan",
		"Bahrain",
		"Bangladesh",
		"Bhutan",
		"Brunei Darussalam",
		"Cambodia",
		"China",
		"Cyprus",
		"Georgia",
		"Hong Kong",
		"India",
		"Indonesia",
        "Iran",
		"Iraq",
		"Israel",
		"Japan",
		"Jordan",
		"Kazakhstan",
		"Kuwait",
		"Kyrgyzstan",
		"Lao People's Democratic Republic",
		"Lebanon",
		"Macao",
		"Malaysia",
		"Maldives",
		"Mongolia",
		"Myanmar",
		"Nepal",
        "North Korea",
		"Oman",
		"Pakistan",
        "Palestine",
		"Philippines",
		"Qatar",
		"Saudi Arabia",
		"Singapore",
        "South Korea",
		"Sri Lanka",
		"Syrian Arab Republic",
		"Tajikistan",
		"Thailand",
        "Taiwan",
		"Timor-Leste",
		"Türkiye",
		"Turkmenistan",
		"United Arab Emirates",
		"Uzbekistan",
		"Viet Nam",
		"Yemen",
    ], 
    
	"Europe" : [
        "Åland Islands",
		"Albania",
		"Andorra",
		"Austria",
		"Belarus",
		"Belgium",
		"Bosnia and Herzegovina",
		"Bulgaria",
		"Croatia",
		"Czechia",
		"Denmark",
		"Estonia",
		"Faroe Islands",
		"Finland",
		"France",
		"Germany",
		"Gibraltar",
		"Greece",
		"Guernsey",
		"Holy See",
		"Hungary",
		"Iceland",
		"Ireland",
		"Isle of Man",
		"Italy",
		"Jersey",
		"Latvia",
		"Liechtenstein",
		"Lithuania",
		"Luxembourg",
		"Malta",
        "Moldova",
		"Monaco",
		"Montenegro",
		"Netherlands",
		"North Macedonia",
		"Norway",
		"Poland",
		"Portugal",
		"Romania",
		"Russian Federation",
		"San Marino",
		"Serbia",
		"Slovakia",
		"Slovenia",
		"Spain",
		"Svalbard and Jan Mayen",
		"Sweden",
		"Switzerland",
		"Ukraine",
		"United Kingdom of Great Britain and Northern Ireland",
    ]
})


region_subregion = Groups({
    "Africa" : [
		"Africa",
    	"Sub-Saharan Africa",
         "Northern Africa",
	], 
    
	"Americas" : [
		"Americas",
        "Latin America and the Caribbean",
        "Northern America",
	], 
    
	"Oceania" : [
		"Polynesia",
        "Melanesia",
        "Australia and New Zealand",
        "Oceania",
        "Micronesia",
	], 
    
	"Asia" : [
		"Central Asia",
        "Eastern Asia",
        "Western Asia",
        "Southern Asia",
        "Asia",
        "South-eastern Asia",
	], 
    
	"Europe" : [
		"Western Europe",
        "Northern Europe",
        "Southern Europe",
        "Eastern Europe",
        "Europe",
	]
})


def __main__():

	with open("../data/regions_to_countries_table.json",
		"w") as json_file:
		json.dump(region_country.get_dict_groups_to_elts(), json_file, indent=4)
    
	with open("../data/countries_to_regions_table.json",
		"w") as json_file:
		json.dump(region_country.get_dict_elts_to_groups(), json_file, indent=4)

	with open("../data/subregions_to_countries_table.json",
		"w") as json_file:
		json.dump(subregion_country.get_dict_groups_to_elts(), json_file, indent=4)
    
	with open("../data/countries_to_subregions_table.json",
		"w") as json_file:
		json.dump(subregion_country.get_dict_elts_to_groups(), json_file, indent=4)
          
	with open("../data/regions_to_subregions_table.json",
		"w") as json_file:
		json.dump(region_subregion.get_dict_groups_to_elts(), json_file, indent=4)
    
	with open("../data/subregions_to_regions_table.json",
		"w") as json_file:
		json.dump(region_subregion.get_dict_elts_to_groups(), json_file, indent=4)

	return

if __name__ == "__main__":
    __main__()