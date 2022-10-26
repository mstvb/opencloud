# OPENAPI

### STATELOADER

###### FUNKTIONEN

---

> addState(state) *Fügt einen State zum Loader hinzu*
####
> setState(stateName: str | optional: auto_start: bool) *Setzt einen State als Ziel*
####
> startState() *Startet den aktuell ausgewählten State*
####
> stopState() *Stoppt den ausgewählten State*
####
> isExisted(stateName) *Gibt True aus wenn der State existiert ansonsten False*
####
> isActive(stateName) *Gibt True aus wenn der State aktiv ist ansonsten False*

---


### STATETEMPLATE

###### VORAUSSETZUNGEN

---

> start() *Startet den State*
####
> stop() *Stoppt den State*
####
> getStateName() *Gibt den stateName aus*

---