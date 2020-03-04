# Netlab
Tool for setting BIRD topology and configuration testing.

## test case
  Individual topology settings for different protocols.
  examples: cf-bgp, cf-ospf, cf-rip

## test suits
  Set of tests that verifies the functionality of test cases.
  examples: kernel.py (basic test-case), test-<test_case>.py
  
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
