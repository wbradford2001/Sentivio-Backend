import json
loc = [
    {
        "location_name": "Afghanistan",
        "country_iso_code": "AF",
        "flag": "AF.svg"
    },
    {
        "location_name": "Albania",
        "country_iso_code": "AL",
        "flag": "AL.svg"
    },
    {
        "location_name": "Antarctica",
        "country_iso_code": "AQ",
        "flag": "AQ.svg"
    },
    {
        "location_name": "Algeria",
        "country_iso_code": "DZ",
        "flag": "DZ.svg"
    },
    {
        "location_name": "American Samoa",
        "country_iso_code": "AS",
        "flag": "AS.svg"
    },
    {
        "location_name": "Andorra",
        "country_iso_code": "AD",
        "flag": "AD.svg"
    },
    {
        "location_name": "Angola",
        "country_iso_code": "AO",
        "flag": "AO.svg"
    },
    {
        "location_name": "Antigua and Barbuda",
        "country_iso_code": "AG",
        "flag": "AG.svg"
    },
    {
        "location_name": "Azerbaijan",
        "country_iso_code": "AZ",
        "flag": "AZ.svg"
    },
    {
        "location_name": "Argentina",
        "country_iso_code": "AR",
        "flag": "AR.svg"
    },
    {
        "location_name": "Australia",
        "country_iso_code": "AU",
        "flag": "AU.svg"
    },
    {
        "location_name": "Austria",
        "country_iso_code": "AT",
        "flag": "AT.svg"
    },
    {
        "location_name": "The Bahamas",
        "country_iso_code": "BS",
        "flag": "BS.svg"
    },
    {
        "location_name": "Bahrain",
        "country_iso_code": "BH",
        "flag": "BH.svg"
    },
    {
        "location_name": "Bangladesh",
        "country_iso_code": "BD",
        "flag": "BD.svg"
    },
    {
        "location_name": "Armenia",
        "country_iso_code": "AM",
        "flag": "AM.svg"
    },
    {
        "location_name": "Barbados",
        "country_iso_code": "BB",
        "flag": "BB.svg"
    },
    {
        "location_name": "Belgium",
        "country_iso_code": "BE",
        "flag": "BE.svg"
    },
    {
        "location_name": "Bhutan",
        "country_iso_code": "BT",
        "flag": "BT.svg"
    },
    {
        "location_name": "Bolivia",
        "country_iso_code": "BO",
        "flag": "BO.svg"
    },
    {
        "location_name": "Bosnia and Herzegovina",
        "country_iso_code": "BA",
        "flag": "BA.svg"
    },
    {
        "location_name": "Botswana",
        "country_iso_code": "BW",
        "flag": "BW.svg"
    },
    {
        "location_name": "Brazil",
        "country_iso_code": "BR",
        "flag": "BR.svg"
    },
    {
        "location_name": "Belize",
        "country_iso_code": "BZ",
        "flag": "BZ.svg"
    },
    {
        "location_name": "Solomon Islands",
        "country_iso_code": "SB",
        "flag": "SB.svg"
    },
    {
        "location_name": "Brunei",
        "country_iso_code": "BN",
        "flag": "BN.svg"
    },
    {
        "location_name": "Bulgaria",
        "country_iso_code": "BG",
        "flag": "BG.svg"
    },
    {
        "location_name": "Myanmar (Burma)",
        "country_iso_code": "MM",
        "flag": "MM.svg"
    },
    {
        "location_name": "Burundi",
        "country_iso_code": "BI",
        "flag": "BI.svg"
    },
    {
        "location_name": "Cambodia",
        "country_iso_code": "KH",
        "flag": "KH.svg"
    },
    {
        "location_name": "Cameroon",
        "country_iso_code": "CM",
        "flag": "CM.svg"
    },
    {
        "location_name": "Canada",
        "country_iso_code": "CA",
        "flag": "CA.svg"
    },
    {
        "location_name": "Cabo Verde",
        "country_iso_code": "CV",
        "flag": "CV.svg"
    },
    {
        "location_name": "Central African Republic",
        "country_iso_code": "CF",
        "flag": "CF.svg"
    },
    {
        "location_name": "Sri Lanka",
        "country_iso_code": "LK",
        "flag": "LK.svg"
    },
    {
        "location_name": "Chad",
        "country_iso_code": "TD",
        "flag": "TD.svg"
    },
    {
        "location_name": "Chile",
        "country_iso_code": "CL",
        "flag": "CL.svg"
    },
    {
        "location_name": "China",
        "country_iso_code": "CN",
        "flag": "CN.svg"
    },
    {
        "location_name": "Christmas Island",
        "country_iso_code": "CX",
        "flag": "CX.svg"
    },
    {
        "location_name": "Cocos (Keeling) Islands",
        "country_iso_code": "CC",
        "flag": "CC.svg"
    },
    {
        "location_name": "Colombia",
        "country_iso_code": "CO",
        "flag": "CO.svg"
    },
    {
        "location_name": "Comoros",
        "country_iso_code": "KM",
        "flag": "KM.svg"
    },
    {
        "location_name": "Republic of the Congo",
        "country_iso_code": "CG",
        "flag": "CG.svg"
    },
    {
        "location_name": "Democratic Republic of the Congo",
        "country_iso_code": "CD",
        "flag": "CD.svg"
    },
    {
        "location_name": "Cook Islands",
        "country_iso_code": "CK",
        "flag": "CK.svg"
    },
    {
        "location_name": "Costa Rica",
        "country_iso_code": "CR",
        "flag": "CR.svg"
    },
    {
        "location_name": "Croatia",
        "country_iso_code": "HR",
        "flag": "HR.svg"
    },
    {
        "location_name": "Cyprus",
        "country_iso_code": "CY",
        "flag": "CY.svg"
    },
    {
        "location_name": "Czechia",
        "country_iso_code": "CZ",
        "flag": "CZ.svg"
    },
    {
        "location_name": "Benin",
        "country_iso_code": "BJ",
        "flag": "BJ.svg"
    },
    {
        "location_name": "Denmark",
        "country_iso_code": "DK",
        "flag": "DK.svg"
    },
    {
        "location_name": "Dominica",
        "country_iso_code": "DM",
        "flag": "DM.svg"
    },
    {
        "location_name": "Dominican Republic",
        "country_iso_code": "DO",
        "flag": "DO.svg"
    },
    {
        "location_name": "Ecuador",
        "country_iso_code": "EC",
        "flag": "EC.svg"
    },
    {
        "location_name": "El Salvador",
        "country_iso_code": "SV",
        "flag": "SV.svg"
    },
    {
        "location_name": "Equatorial Guinea",
        "country_iso_code": "GQ",
        "flag": "GQ.svg"
    },
    {
        "location_name": "Ethiopia",
        "country_iso_code": "ET",
        "flag": "ET.svg"
    },
    {
        "location_name": "Eritrea",
        "country_iso_code": "ER",
        "flag": "ER.svg"
    },
    {
        "location_name": "Estonia",
        "country_iso_code": "EE",
        "flag": "EE.svg"
    },
    {
        "location_name": "South Georgia and the South Sandwich Islands",
        "country_iso_code": "GS",
        "flag": "GS.svg"
    },
    {
        "location_name": "Fiji",
        "country_iso_code": "FJ",
        "flag": "FJ.svg"
    },
    {
        "location_name": "Finland",
        "country_iso_code": "FI",
        "flag": "FI.svg"
    },
    {
        "location_name": "France",
        "country_iso_code": "FR",
        "flag": "FR.svg"
    },
    {
        "location_name": "French Polynesia",
        "country_iso_code": "PF",
        "flag": "PF.svg"
    },
    {
        "location_name": "French Southern and Antarctic Lands",
        "country_iso_code": "TF",
        "flag": "TF.svg"
    },
    {
        "location_name": "Djibouti",
        "country_iso_code": "DJ",
        "flag": "DJ.svg"
    },
    {
        "location_name": "Gabon",
        "country_iso_code": "GA",
        "flag": "GA.svg"
    },
    {
        "location_name": "Georgia",
        "country_iso_code": "GE",
        "flag": "GE.svg"
    },
    {
        "location_name": "The Gambia",
        "country_iso_code": "GM",
        "flag": "GM.svg"
    },
    {
        "location_name": "Germany",
        "country_iso_code": "DE",
        "flag": "DE.svg"
    },
    {
        "location_name": "Ghana",
        "country_iso_code": "GH",
        "flag": "GH.svg"
    },
    {
        "location_name": "Kiribati",
        "country_iso_code": "KI",
        "flag": "KI.svg"
    },
    {
        "location_name": "Greece",
        "country_iso_code": "GR",
        "flag": "GR.svg"
    },
    {
        "location_name": "Grenada",
        "country_iso_code": "GD",
        "flag": "GD.svg"
    },
    {
        "location_name": "Guam",
        "country_iso_code": "GU",
        "flag": "GU.svg"
    },
    {
        "location_name": "Guatemala",
        "country_iso_code": "GT",
        "flag": "GT.svg"
    },
    {
        "location_name": "Guinea",
        "country_iso_code": "GN",
        "flag": "GN.svg"
    },
    {
        "location_name": "Guyana",
        "country_iso_code": "GY",
        "flag": "GY.svg"
    },
    {
        "location_name": "Haiti",
        "country_iso_code": "HT",
        "flag": "HT.svg"
    },
    {
        "location_name": "Heard Island and McDonald Islands",
        "country_iso_code": "HM",
        "flag": "HM.svg"
    },
    {
        "location_name": "Vatican City",
        "country_iso_code": "VA",
        "flag": "VA.svg"
    },
    {
        "location_name": "Honduras",
        "country_iso_code": "HN",
        "flag": "HN.svg"
    },
    {
        "location_name": "Hungary",
        "country_iso_code": "HU",
        "flag": "HU.svg"
    },
    {
        "location_name": "Iceland",
        "country_iso_code": "IS",
        "flag": "IS.svg"
    },
    {
        "location_name": "India",
        "country_iso_code": "IN",
        "flag": "IN.svg"
    },
    {
        "location_name": "Indonesia",
        "country_iso_code": "ID",
        "flag": "ID.svg"
    },
    {
        "location_name": "Iraq",
        "country_iso_code": "IQ",
        "flag": "IQ.svg"
    },
    {
        "location_name": "Ireland",
        "country_iso_code": "IE",
        "flag": "IE.svg"
    },
    {
        "location_name": "Israel",
        "country_iso_code": "IL",
        "flag": "IL.svg"
    },
    {
        "location_name": "Italy",
        "country_iso_code": "IT",
        "flag": "IT.svg"
    },
    {
        "location_name": "Cote d'Ivoire",
        "country_iso_code": "CI",
        "flag": "CI.svg"
    },
    {
        "location_name": "Jamaica",
        "country_iso_code": "JM",
        "flag": "JM.svg"
    },
    {
        "location_name": "Japan",
        "country_iso_code": "JP",
        "flag": "JP.svg"
    },
    {
        "location_name": "Kazakhstan",
        "country_iso_code": "KZ",
        "flag": "KZ.svg"
    },
    {
        "location_name": "Jordan",
        "country_iso_code": "JO",
        "flag": "JO.svg"
    },
    {
        "location_name": "Kenya",
        "country_iso_code": "KE",
        "flag": "KE.svg"
    },
    {
        "location_name": "South Korea",
        "country_iso_code": "KR",
        "flag": "KR.svg"
    },
    {
        "location_name": "Kuwait",
        "country_iso_code": "KW",
        "flag": "KW.svg"
    },
    {
        "location_name": "Kyrgyzstan",
        "country_iso_code": "KG",
        "flag": "KG.svg"
    },
    {
        "location_name": "Laos",
        "country_iso_code": "LA",
        "flag": "LA.svg"
    },
    {
        "location_name": "Lebanon",
        "country_iso_code": "LB",
        "flag": "LB.svg"
    },
    {
        "location_name": "Lesotho",
        "country_iso_code": "LS",
        "flag": "LS.svg"
    },
    {
        "location_name": "Latvia",
        "country_iso_code": "LV",
        "flag": "LV.svg"
    },
    {
        "location_name": "Liberia",
        "country_iso_code": "LR",
        "flag": "LR.svg"
    },
    {
        "location_name": "Libya",
        "country_iso_code": "LY",
        "flag": "LY.svg"
    },
    {
        "location_name": "Liechtenstein",
        "country_iso_code": "LI",
        "flag": "LI.svg"
    },
    {
        "location_name": "Lithuania",
        "country_iso_code": "LT",
        "flag": "LT.svg"
    },
    {
        "location_name": "Luxembourg",
        "country_iso_code": "LU",
        "flag": "LU.svg"
    },
    {
        "location_name": "Madagascar",
        "country_iso_code": "MG",
        "flag": "MG.svg"
    },
    {
        "location_name": "Malawi",
        "country_iso_code": "MW",
        "flag": "MW.svg"
    },
    {
        "location_name": "Malaysia",
        "country_iso_code": "MY",
        "flag": "MY.svg"
    },
    {
        "location_name": "Maldives",
        "country_iso_code": "MV",
        "flag": "MV.svg"
    },
    {
        "location_name": "Mali",
        "country_iso_code": "ML",
        "flag": "ML.svg"
    },
    {
        "location_name": "Malta",
        "country_iso_code": "MT",
        "flag": "MT.svg"
    },
    {
        "location_name": "Mauritania",
        "country_iso_code": "MR",
        "flag": "MR.svg"
    },
    {
        "location_name": "Mauritius",
        "country_iso_code": "MU",
        "flag": "MU.svg"
    },
    {
        "location_name": "Mexico",
        "country_iso_code": "MX",
        "flag": "MX.svg"
    },
    {
        "location_name": "Monaco",
        "country_iso_code": "MC",
        "flag": "MC.svg"
    },
    {
        "location_name": "Mongolia",
        "country_iso_code": "MN",
        "flag": "MN.svg"
    },
    {
        "location_name": "Moldova",
        "country_iso_code": "MD",
        "flag": "MD.svg"
    },
    {
        "location_name": "Montenegro",
        "country_iso_code": "ME",
        "flag": "ME.svg"
    },
    {
        "location_name": "Morocco",
        "country_iso_code": "MA",
        "flag": "MA.svg"
    },
    {
        "location_name": "Mozambique",
        "country_iso_code": "MZ",
        "flag": "MZ.svg"
    },
    {
        "location_name": "Oman",
        "country_iso_code": "OM",
        "flag": "OM.svg"
    },
    {
        "location_name": "Namibia",
        "country_iso_code": "NA",
        "flag": "NA.svg"
    },
    {
        "location_name": "Nauru",
        "country_iso_code": "NR",
        "flag": "NR.svg"
    },
    {
        "location_name": "Nepal",
        "country_iso_code": "NP",
        "flag": "NP.svg"
    },
    {
        "location_name": "Netherlands",
        "country_iso_code": "NL",
        "flag": "NL.svg"
    },
    {
        "location_name": "Curacao",
        "country_iso_code": "CW",
        "flag": "CW.svg"
    },
    {
        "location_name": "Sint Maarten",
        "country_iso_code": "SX",
        "flag": "SX.svg"
    },
    {
        "location_name": "Caribbean Netherlands",
        "country_iso_code": "BQ",
        "flag": "BQ.svg"
    },
    {
        "location_name": "New Caledonia",
        "country_iso_code": "NC",
        "flag": "NC.svg"
    },
    {
        "location_name": "Vanuatu",
        "country_iso_code": "VU",
        "flag": "VU.svg"
    },
    {
        "location_name": "New Zealand",
        "country_iso_code": "NZ",
        "flag": "NZ.svg"
    },
    {
        "location_name": "Nicaragua",
        "country_iso_code": "NI",
        "flag": "NI.svg"
    },
    {
        "location_name": "Niger",
        "country_iso_code": "NE",
        "flag": "NE.svg"
    },
    {
        "location_name": "Nigeria",
        "country_iso_code": "NG",
        "flag": "NG.svg"
    },
    {
        "location_name": "Niue",
        "country_iso_code": "NU",
        "flag": "NU.svg"
    },
    {
        "location_name": "Norfolk Island",
        "country_iso_code": "NF",
        "flag": "NF.svg"
    },
    {
        "location_name": "Norway",
        "country_iso_code": "NO",
        "flag": "NO.svg"
    },
    {
        "location_name": "Northern Mariana Islands",
        "country_iso_code": "MP",
        "flag": "MP.svg"
    },
    {
        "location_name": "United States Minor Outlying Islands",
        "country_iso_code": "UM",
        "flag": "UM.svg"
    },
    {
        "location_name": "Micronesia",
        "country_iso_code": "FM",
        "flag": "FM.svg"
    },
    {
        "location_name": "Marshall Islands",
        "country_iso_code": "MH",
        "flag": "MH.svg"
    },
    {
        "location_name": "Palau",
        "country_iso_code": "PW",
        "flag": "PW.svg"
    },
    {
        "location_name": "Pakistan",
        "country_iso_code": "PK",
        "flag": "PK.svg"
    },
    {
        "location_name": "Panama",
        "country_iso_code": "PA",
        "flag": "PA.svg"
    },
    {
        "location_name": "Papua New Guinea",
        "country_iso_code": "PG",
        "flag": "PG.svg"
    },
    {
        "location_name": "Paraguay",
        "country_iso_code": "PY",
        "flag": "PY.svg"
    },
    {
        "location_name": "Peru",
        "country_iso_code": "PE",
        "flag": "PE.svg"
    },
    {
        "location_name": "Philippines",
        "country_iso_code": "PH",
        "flag": "PH.svg"
    },
    {
        "location_name": "Pitcairn Islands",
        "country_iso_code": "PN",
        "flag": "PN.svg"
    },
    {
        "location_name": "Poland",
        "country_iso_code": "PL",
        "flag": "PL.svg"
    },
    {
        "location_name": "Portugal",
        "country_iso_code": "PT",
        "flag": "PT.svg"
    },
    {
        "location_name": "Guinea-Bissau",
        "country_iso_code": "GW",
        "flag": "GW.svg"
    },
    {
        "location_name": "Timor-Leste",
        "country_iso_code": "TL",
        "flag": "TL.svg"
    },
    {
        "location_name": "Qatar",
        "country_iso_code": "QA",
        "flag": "QA.svg"
    },
    {
        "location_name": "Romania",
        "country_iso_code": "RO",
        "flag": "RO.svg"
    },
    {
        "location_name": "Rwanda",
        "country_iso_code": "RW",
        "flag": "RW.svg"
    },
    {
        "location_name": "Saint Helena, Ascension and Tristan da Cunha",
        "country_iso_code": "SH",
        "flag": "SH.svg"
    },
    {
        "location_name": "Saint Kitts and Nevis",
        "country_iso_code": "KN",
        "flag": "KN.svg"
    },
    {
        "location_name": "Saint Lucia",
        "country_iso_code": "LC",
        "flag": "LC.svg"
    },
    {
        "location_name": "Saint Pierre and Miquelon",
        "country_iso_code": "PM",
        "flag": "PM.svg"
    },
    {
        "location_name": "Saint Vincent and the Grenadines",
        "country_iso_code": "VC",
        "flag": "VC.svg"
    },
    {
        "location_name": "San Marino",
        "country_iso_code": "SM",
        "flag": "SM.svg"
    },
    {
        "location_name": "Sao Tome and Principe",
        "country_iso_code": "ST",
        "flag": "ST.svg"
    },
    {
        "location_name": "Saudi Arabia",
        "country_iso_code": "SA",
        "flag": "SA.svg"
    },
    {
        "location_name": "Senegal",
        "country_iso_code": "SN",
        "flag": "SN.svg"
    },
    {
        "location_name": "Serbia",
        "country_iso_code": "RS",
        "flag": "RS.svg"
    },
    {
        "location_name": "Seychelles",
        "country_iso_code": "SC",
        "flag": "SC.svg"
    },
    {
        "location_name": "Sierra Leone",
        "country_iso_code": "SL",
        "flag": "SL.svg"
    },
    {
        "location_name": "Singapore",
        "country_iso_code": "SG",
        "flag": "SG.svg"
    },
    {
        "location_name": "Slovakia",
        "country_iso_code": "SK",
        "flag": "SK.svg"
    },
    {
        "location_name": "Vietnam",
        "country_iso_code": "VN",
        "flag": "VN.svg"
    },
    {
        "location_name": "Slovenia",
        "country_iso_code": "SI",
        "flag": "SI.svg"
    },
    {
        "location_name": "Somalia",
        "country_iso_code": "SO",
        "flag": "SO.svg"
    },
    {
        "location_name": "South Africa",
        "country_iso_code": "ZA",
        "flag": "ZA.svg"
    },
    {
        "location_name": "Zimbabwe",
        "country_iso_code": "ZW",
        "flag": "ZW.svg"
    },
    {
        "location_name": "Spain",
        "country_iso_code": "ES",
        "flag": "ES.svg"
    },
    {
        "location_name": "Suriname",
        "country_iso_code": "SR",
        "flag": "SR.svg"
    },
    {
        "location_name": "Eswatini",
        "country_iso_code": "SZ",
        "flag": "SZ.svg"
    },
    {
        "location_name": "Sweden",
        "country_iso_code": "SE",
        "flag": "SE.svg"
    },
    {
        "location_name": "Switzerland",
        "country_iso_code": "CH",
        "flag": "CH.svg"
    },
    {
        "location_name": "Tajikistan",
        "country_iso_code": "TJ",
        "flag": "TJ.svg"
    },
    {
        "location_name": "Thailand",
        "country_iso_code": "TH",
        "flag": "TH.svg"
    },
    {
        "location_name": "Togo",
        "country_iso_code": "TG",
        "flag": "TG.svg"
    },
    {
        "location_name": "Tokelau",
        "country_iso_code": "TK",
        "flag": "TK.svg"
    },
    {
        "location_name": "Tonga",
        "country_iso_code": "TO",
        "flag": "TO.svg"
    },
    {
        "location_name": "Trinidad and Tobago",
        "country_iso_code": "TT",
        "flag": "TT.svg"
    },
    {
        "location_name": "United Arab Emirates",
        "country_iso_code": "AE",
        "flag": "AE.svg"
    },
    {
        "location_name": "Tunisia",
        "country_iso_code": "TN",
        "flag": "TN.svg"
    },
    {
        "location_name": "Turkiye",
        "country_iso_code": "TR",
        "flag": "TR.svg"
    },
    {
        "location_name": "Turkmenistan",
        "country_iso_code": "TM",
        "flag": "TM.svg"
    },
    {
        "location_name": "Tuvalu",
        "country_iso_code": "TV",
        "flag": "TV.svg"
    },
    {
        "location_name": "Uganda",
        "country_iso_code": "UG",
        "flag": "UG.svg"
    },
    {
        "location_name": "Ukraine",
        "country_iso_code": "UA",
        "flag": "UA.svg"
    },
    {
        "location_name": "North Macedonia",
        "country_iso_code": "MK",
        "flag": "MK.svg"
    },
    {
        "location_name": "Egypt",
        "country_iso_code": "EG",
        "flag": "EG.svg"
    },
    {
        "location_name": "United Kingdom",
        "country_iso_code": "GB",
        "flag": "GB.svg"
    },
    {
        "location_name": "Guernsey",
        "country_iso_code": "GG",
        "flag": "GG.svg"
    },
    {
        "location_name": "Jersey",
        "country_iso_code": "JE",
        "flag": "JE.svg"
    },
    {
        "location_name": "Isle of Man",
        "country_iso_code": "IM",
        "flag": "IM.svg"
    },
    {
        "location_name": "Tanzania",
        "country_iso_code": "TZ",
        "flag": "TZ.svg"
    },
    {
        "location_name": "United States",
        "country_iso_code": "US",
        "flag": "US.svg"
    },
    {
        "location_name": "Burkina Faso",
        "country_iso_code": "BF",
        "flag": "BF.svg"
    },
    {
        "location_name": "Uruguay",
        "country_iso_code": "UY",
        "flag": "UY.svg"
    },
    {
        "location_name": "Uzbekistan",
        "country_iso_code": "UZ",
        "flag": "UZ.svg"
    },
    {
        "location_name": "Venezuela",
        "country_iso_code": "VE",
        "flag": "VE.svg"
    },
    {
        "location_name": "Wallis and Futuna",
        "country_iso_code": "WF",
        "flag": "WF.svg"
    },
    {
        "location_name": "Samoa",
        "country_iso_code": "WS",
        "flag": "WS.svg"
    },
    {
        "location_name": "Yemen",
        "country_iso_code": "YE",
        "flag": "YE.svg"
    },
    {
        "location_name": "Zambia",
        "country_iso_code": "ZM",
        "flag": "ZM.svg"
    }
]
loc = sorted(loc, key=lambda x: x["location_name"])
print(json.dumps(loc))
i=0
for location in loc:
    if location["location_name"] == "United States":
        print(i)
    i += 1