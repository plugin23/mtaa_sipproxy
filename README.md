# mtaa_sipproxy
## Spustenie programu

Program sa dá spustiť v termináli, konkrétne súbor sipproxy.py - python sipproxy.py <IP adresa>.
Môže sa spustiť bez argumentov, v takom prípade na základe mena zariadenia cez knižnicu socket
zistí program aj IP adresu, kde spustí SIP proxy. Avšak táto funkcia môže v niektorých prípadoch
získavať nesprávnu IP adresu, preto je možnosť spustiť program aj s jedným argumentom a to
s manuálne zadanou správnou IP adresou zariadenia.