# Netlab
Nastroj pro testovani Bird-u

## test cases
  Jde o nastaveni topologii, pro specificke protokoly. Definovane protokoly maji individualni atributy, jejiz soucinost se ma   testovat
  
  pr. test-case --> cf-ospf; cf-ospf-base; cf-ospf-default; cf-ospf-auth; ...
 
## test suits
  Jde o soubor testovacich souboru (.py), ktere maji testovat konkretni test case.
  
### kernel.py
  Jde o soubor testu, ktery ma na starost ulozit routovaci tabulku. Dale ji porovnat se soucasnym stavem, pripadne overit jejich stav.
  
### specific_<test_case>.py
  Sada testu, ktera testuje specificke cases.

  pr. test-cf-ospf-base
  def test_wait():  # general
    ...

  def test_krt_routes():  # also general
    ...

  def test_<specific-cases>():  # specific test only for this test case
    ...
