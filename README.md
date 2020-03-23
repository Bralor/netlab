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
Netlab works by default in two variants.

### 1. Start/stop option
This variant is running through script :start:. Inserting the <test_case> parameter to the "-c" switch runs the selected test case from the :cases: folder.
In this mode it is possible to work with each device individually. Running BIRD for each device with the script :/m<number>/birdc: (for hint, write "?"). To end the current running configuration, run the script :stop:.

Running the scenario with the basic configuration for the OSPF protocol:
```
./start -c cases/cf-ospf-base  
```
Stopping the current running test case:
```
./stop
```

### 2. Runtest option
A variant in which the integration tests will run (see [test suit](#test-suit)). It is necessary to run with "-m" switch. This option has two modes.

#### 2.1 Save mode
Save the kernel routing tables for selected scenario to :data: folder in the specified test case's folder.

Running the scenario with the basic configuration for the OSPF protocol:
```
./runtest -m save cases/cf-ospf-base
```
Running all the scenarios starting with "cf-ospf":
```
./runtest -m save cases/cf-ospf*
```

#### 2.2 Check mode
It compares the primary kernel routing tables with the current run with the tables from the last SAVE mode. In this mode, the directory: temp: is created at the same time in the root directory where tables from the current run for any differences are stored. If both entries in the tables match, the test passes and the: temp: directory is removed at the end. In the opposite variant, it is possible to check for any differences.

Running the scenario with the basic configuration for the OSPF protocol:
```
./runtest -m check cases/cf-ospf-base
```
Running all the scenarios starting with "cf-ospf":
```
./runtest -m check cases/cf-ospf*
```

## Folder content
Current directory content :netlab:
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
These are predefined configuration files that represent possible situations within the protocol. A list of all test scenarios can be found in the directory: cases :. Each test scenario contains a file: config:, which describes the overall device topology. It also contains configuration files for each device (: bird_m <number> .conf :). The directory also contains a folder: data: where the routing kernel tables are stored in SAVE mode (see [Usage](#21-save-mode)).

### Variants for the OSPF protocol
#### Topology
```
      ┌─────┐
  M1 -|M3 M5| - M7
  |   |  O  |   |
  M2 -|M4 M6| - M8
      └─────┘
```
#### Description
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

### Variants for the BGP protocol
#### Topology
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

#### Description
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
It is a package with specific tests that verify the specific testing case. Each test case has a basic test package (:cases/cf-<test_case>/test-<test_case>.py:). These are basic tests verifying the routing table content. It also contains tests that are individual to each test case.
The test package :cases/cf-<test_case>/test-<test_case>.py: is only a starting file for the tool Pytest. The test function itself is in the file :/tests/kernel.py:. The patch always tests all defined devices.
