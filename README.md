# Netlab
Nastroj pro nastavovani topologii BIRDu a testovani konfiguraci.

## test case
  Individualni nastaveni topologie pro ruzne protokoly.
  pr. cf-bgp, cf-ospf, cf-rip

## test suits
  Sada testu, ktera overuje funkcionalitu test cases.
  pr. kernel.py (basic testy), test-<test_case>.py (specificke testy pro jednotlive cases)
  
### test-cf-ospf-base.py
    def test_wait():
      ...
       
    def test_krt_tables():
      ...
      
    def test_<specific_test_name>():
      ...

### test-cf-bgp-base
Topology:
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

