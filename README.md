# stellaris-austrian-namelist

A small namelist-mod I am trying to compile collecting names used in Austria for use in the game [Stellaris](https://store.steampowered.com/app/281990/Stellaris/).
This repositoriy contains two subdirectories:

* mod

   This directory contains the mod structure as it is required by Stellaris to work. It will probably be uploaded to the Steam Workshop as soon it is at least mostly finished. 

* supporting

   Scripts I wrote using Python for data-collecting purposes. They are not needed for the mod to work, but collecting that amount of data by hand would not be really fun. For now these scripts will be outputting the data in extra files, but given time and interest I'll probably condense them in a script that generates the austrian_namelist.txt completely.

## Datasources

* https://namenskarten.lima-city.at/
* http://www.statistik.at/verzeichnis/reglisten/ortsliste.csv
* https://www.statistik.at/web_de/statistiken/menschen_und_gesellschaft/bevoelkerung/geborene/vornamen/index.html
* http://www.a-winkler.at/presse/13_solid%202017_top%20150%20bauunternehmen_platz%20135.pdf (Not used in a script, used for constructors)
* https://de.wikipedia.org/wiki/Liste_der_Schiffe_der_k.u.k._Kriegsmarine (Not used in a script, used for generic shipnames)
* https://de.wikipedia.org/wiki/Liste_%C3%B6sterreichischer_Erfinder_und_Entdecker (Not ussed in a script, used for science shipnames)