# Netlab
Tool for defining the BIRD topology and its configuration.
<<<<<<< HEAD

## Content
  1. Installation
  2. Usage
  3. Folder content
  4. test cases
    4.1 Introduction
    4.2 Usage
    4.4 cf-<test_case_1>
    4.5 cf-<test_case_2>
    4.6 cf-<test_case_3>
  5. test suits
    5.1 Introduction
    5.2 Usage
    5.3 tests/kernel.py
    5.4 test-<test_suit_1>
    5.5 test-<test_suit_2>
    5.6 test-<test_suit_3>
=======
## Content
```
/netlab
 ├─Installation
 ├─Usage
 ├─test cases
 | ├─Introduction
 | ├─Usage
 | ├─cf-<test_case_1>
 | ├─cf-<test_case_2>
 | └─cf-<test_case_3>
 |
 ├─test suits
 | ├─Introduction
 | ├─Usage
 | ├─tests/kernel.py
 | ├─test-<test_suit_1>
 | ├─test-<test_suit_2>
 | ├─test-<test_suit_3>
 |
```
>>>>>>> d9637221424e739ebc88b05d1924f8c9577f584b

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

## Folder content
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

## test case
  Individual topology settings for different protocols.
  examples: cf-bgp, cf-ospf, cf-rip

## test suits
  Set of tests that verifies the functionality of test cases.
  examples: kernel.py (basic test-case), test-<test_case>.py


### tests/kernel.py
File contains basic tests. These tests contains basic integration tests to verify if there are correct krt tables returning from the netlab.
#### test_wait
Wait until time is up. Variable "LIMIT" specify the time value (default LIMIT = 60).
#### test_
### test-cf-ospf-base.py
#### Topology:
```
      ┌─────┐
  M1 -|M3 M5| - M7
  |   |  O  |   |
  M2 -|M4 M6| - M8
      └─────┘
```
    def test_wait():
      ...
       
    def test_krt_tables():
      ...
      
    def test_<specific_test_name>():
      ...

#### Settings:
  - in progress

### test-cf-bgp-base
#### Topology:
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
#### Settings:
  - AS1: M44 --> M11 (ebgp4, ebgp6),
  - AS1: M11, M13, M14 (ibgp4, ibgp6),
  - AS1: M12 --> M13 (ospf4, ospf6),
  - AS1: M13 --> M14 (ibgp4, ibgp6),
  - AS1: M13 --> M21 (ebgp4, ebgp6),
  - AS1: M14, M13, M11 (ibgp4, ibgp6),
  ...

### test-cf-bgp-auth
#### Topology:
Same as case: test-cf-bgp-base

#### Settings:
Configuration settings with parameter "password":
  - M24-M31 --> Passwords are not matching on the eBGP4,
  - M32-M33 --> Passwords are not matching on the iBGP4,
  - M22-M21 --> Passwords are matching,
  - M41-M42 --> Passwords are matching,

Configuration settings with parameter "ttl security":
  - in progress
