<div align="center">
  
<img width="50%" height="50%" src=https://github.com/SerhiiRI/svmacm/blob/master/scm.jpg>
  
</div>

## Simple Containers Manager
 Program pozwalający na sterowania docker contenerami za pomocą webowego interfejsu, lub zewnętrznymi żądaniami, używając JSON notacje.
 Program stworzony w ramach pracy inżynierskiej. Celem projektu jest oprogramowania aplikacji z wlasnym wbuduwanym API, dla póżniejszej synchrnonizacji z np android aplikacji.
 
 Aplikacja napisana na flasku i jest implementowana jako linux serwis. Aplikacja dziala na porcie `8777` 
 
 #### Wymagania:
 - Docker
 - Python 3+
 
 #### Instalacja
 Instalacja aplikacji odbywa sie za pomocą poleceń 
 ```Shell
 make config
 sudo make install
 ```
 Usuwania aplikacji 
 ```shell
 sudo make remove
 ```
 Odpalenia servera bez instalacji
 ```bash
 sudo make run-local
 ```
 #### Stworzyli:
 - SerhiiRI
 - MarcinO400
 
