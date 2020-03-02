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
