# Netlab
Tool for designing the BIRD topology and its configuration.

## Installation
1. BIRD dependencies installation (distro: debian:latest):
```
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install autoconf \
    build-essential \
    flex \
    bison \
    ncurses-dev \
    libreadline-dev
```

2. BIRD installation (from official repository):
```
sudo git clone https://gitlab.labs.nic.cz/labs/bird
cd bird/
sudo autoreconf
sudo ./configure
sudo make
```

3. NETLAB installation (from official repository):
```
sudo git clone https://gitlab.labs.nic.cz/labs/bird-tools
sudo cp bird/bird bird/birdc netlab/common/
```

4. NETLAB dependencies installation:
```
pip install -r requirements.txt
```

## Usage
Netlab standarne funguje ve dvou variantach.

### 1. Varianta start/stop
Tato varianta se spousti pres skript :/start:. Vlozenim parametru <test_case> k prepinaci "-c" spusti vybrany testovaci scenar ze slozky :cases:.
V tomto rezimu je mozne manualne pracovat s kazdym zarizenim individualne. BIRD spoustim u kazdeho zarizeni pomoci skriptu :m<number>/birdc: (dale pouzivam ovladani BIRDu, napoveda = "?"). Pro ukonceni aktualni bezici konfigurace spoustim skript :/stop:.

Spusteni scenare se zakladni konfiguraci pro protocol OSPF
```
./start -c cases/cf-ospf-base  
```
Zastavim bezici konfiguraci
```
./stop
```

### 2. Varianta runtest
Varianta, v ramci ktere dochazi ke spusteni integracnich testu (viz. (#Test suit)). Nutne spustit s prepinacem "-m". Jde o variantu se dvema rezimy.

#### 2.1 Rezim SAVE
Ulozi pro vybrany scenar (scenare) kernelovske routovaci tabulky do adresare :data: v zadanem testovacim scenari.

Spusteni scenare se zakladni konfiguraci pro protokol OSPF:
```
./runtest -m save cases/cf-ospf-base
```
Spusteni scenare se zakladni konfiguraci pro vsechny protokoly OSPF:
```
./runtest -m save cases/cf-ospf*
```
#### 2.2 Rezim CHECK
Porovnava primarne kernelovske routovaci tabulky s aktualniho spusteni s tabulkami z posledniho rezimu SAVE. V tomto rezimu se soucasne vytvori adresar :temp: v rootovskem adresari, kam se ukladaji tabulky z aktualniho spusteni pro pripadne rozdily. Pokud se oba zapisy v tabulkach shoduji, test projde a adresar :temp: se po skonceni odstrani. V opacne variante je mozne zkontrolovat pripadne rozdily.

Spusteni scenare se zakladni konfiguraci pro protokol OSPF:
```
./runtest -m check cases/cf-ospf-base
```
Spusteni scenare se zakladni konfiguraci pro vsechny protokoly OSPF:
```
./runtest -m check cases/cf-ospf*
```

## Folder content
Aktualni obsah adresare :netlab:
```
  /netlab
    ├─cases
    | ├─cf-<test_case_1>
    | ├─cf-<test_case_2>
    | ├─cf-<test_case_3>
    | ├─cf-...
    | ...
    ├─common
    | ├─common.start
    | ├─common.stop
    | └─NOTES
    ├─netlab_lib
    ├─runtest
    ├─start
    ├─stop
    └─tests
      ├─base.py
      ├─config.py
      ├─kernel.py
      └─test_doctests.py
```

## Test case
Jde o predem vytvorene konfiguracni soubory, ktere reprezentuji mozne situace v ramci protokolu. Seznam vsech testovacich scenaru se nachazi v adresari :cases:. Kazdy testovaci scenar obsahuje soubor :config:, ktery popisuje celkovou topologii zarizeni. Dale obsahuje konfiguracni soubory pro jednotliva zarizeni (:bird_m<number>.conf:). Adresar take obsahuje slozku :data:, kam se ukladaji routovaci kernelovske tabulky v rezimu SAVE (viz. [Usage](#rezim-save)).

### Varianty pro protokol OSPF
#### Topologie
```
      ┌─────┐
  M1 -|M3 M5| - M7
  |   |  O  |   |
  M2 -|M4 M6| - M8
      └─────┘
```
#### Popis
- cf-ospf
- cf-ospf-authentication
- cf-ospf-base
- cf-ospf-bfd
- cf-ospf-custom
- cf-ospf-default
- cf-ospf-nbma
- cf-ospf-net
- cf-ospf-priority
- cf-ospf-ptmp

### Varianty pro protokol BGP
#### Topologie
```
       ┌──────────────────────────┐       
       |      M12 ──── M13     AS1|       
       |      /           \       |       
       |     /             \      |       
       |    /               \     |       
       └── M11 ──────────── M14 ──┘       
          /                   \           
 ┌────── M44 ───┐        ┌──── M21 ──────┐ 
 |      /       |        |      \        | 
 |     /        |        |       \       | 
 |    /         |        |        \      | 
 |  M43         |        |        M22    | 
 |   |          |        |         |     | 
 |   |    AS4   |        | AS2     |     | 
 |  M42         |        |        M23    | 
 |     \        |        |        /      | 
 |      \       |        |       /       | 
 |       \      |        |      /        | 
 └────── M41 ───┘        └─── M24 ───────┘ 
           \                 /             
      ┌─── M34 ────────── M31 ───┐        
      |      \            /      |        
      |       \          /       |        
      |        \        /        |        
      |        M33 ── M32     AS3|        
      └──────────────────────────┘        
```

#### Popis
##### cf-bgp-base
- AS1: M44 --> M11 (ebgp4, ebgp6),
- AS1: M11, M13, M14 (ibgp4, ibgp6),
- AS1: M12 --> M13 (ospf4, ospf6),
- AS1: M13 --> M14 (ibgp4, ibgp6),
- AS1: M13 --> M21 (ebgp4, ebgp6),
- AS1: M14, M13, M11 (ibgp4, ibgp6),
...

##### cf-bgp-authentication
Configuration settings with parameter "password":
- M24-M31 --> Passwords are not matching on the eBGP4,
- M32-M33 --> Passwords are not matching on the iBGP4,
- M22-M21 --> Passwords are matching,
- M41-M42 --> Passwords are matching,

Configuration settings with parameter "ttl security":


## Test suit
Jde o balik se specifickymi testy, ktere overuji prubeh konkretniho testovaci scenare. Kazdy testovaci scenar ma zakladni testovaci balik (:cases/cf-<test_case>/test-<test_case>.py:). Jde o zakladni testy overujici stav routovaci tabulky. Dale obsahuje testy, ktere jsou pro jednotlive testovaci scenare individualni.
Testovaci balik :cases/cf-<test_case>/test-<test_case>.py: je pouze spoustecim souborem pro nastroj Pytest. Vlastni testovaci funkce se nachazi v souboru :/tests/kernel.py:. Pytest vzdy testuje vsechna definovana zarizeni.
