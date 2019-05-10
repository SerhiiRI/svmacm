<div align="center">
  
<img width="75%" src=https://github.com/SerhiiRI/svmacm/blob/master/scm.png>
  
</div>

## Simple Containers Manager
 Program pozwalający na sterowania docker contenerami za pomocą webowego interfejsu, lub zewnętrznymi żądaniami, używając JSON notacje.
 Program stworzony w ramach pracy inżynierskiej(nie mojej he-he). Celem projektu jest oprogramowania aplikacji z wlasnym wbuduwanym API, dla póżniejszej synchrnonizacji z np android aplikacji.
 
 Aplikacja napisana na flasku i jest implementowana jako linux serwis. Aplikacja dziala na porcie `8777` 
 
 #### Wymagania:
 - Docker
 - Python 3+ with [docker API](https://pypi.org/project/docker/) and [flask](https://pypi.org/project/Flask/) library
 - GNU/make 
 
 #### Instalacja
 Instalacja aplikacji odbywa sie za pomocą poleceń 
 ```bash
 make install
 ```
 Usuwania aplikacji 
 ```bash
 make remove
 ```
 Odpalenia servera bez instalacji
 ```bash
 make runloc
 ```
 Dla otrzymania dodatkowej informacji:
 ```bash
 make help
 ```

