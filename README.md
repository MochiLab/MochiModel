# MochiModel
[![DOI](https://zenodo.org/badge/86887744.svg)](https://zenodo.org/badge/latestdoi/86887744)


This python script generates a hierarchical MDSplus model tree which interfaces with the Mochi LabJet MochiControl LabVIEW software.
MochiControl stores all experiment settings such as capacitor bank voltages and discharge times together with all data acquired through National Instruments PXI-6133 and NI-5752 digitizer cards, Tektronix TDS-2024B oscilloscopes, and a Princeton Instruments PI-MAX 3 fast framing camera to the MochiModel tree.
Also, MochiControl can load experiment settings from any previous shot by accessing the desired MDSplus tree.

## Requirements
### Software Dependencies
* Python 2.7
* MDSplus python library

### Hardware Setup
This code is designed for this specific hardware.
* PXI-1042Q chassis with
    * PXI-MXI-4 (communication with PC)
    * PXI-6653 (synchronization card)
    * 2x PXI-6602 (Timing cards with 8 channels each)
    * 3x PXI-6133 (Digitizers each 8 channel 2.5 MS/s 14 bit)
* PXIe-1082 chassis with
    * PXIe-8375 (communication with PC)
    * 3x PXIe-7962R with NI-5752 (Digitizers each 32 channel 50MS/s 12 bit)
    * PXIe-6672 (synchronization card)
* Tektronix 2024B oscilloscope
* 1 PI-MAX3 Princeton Instruments Camera

## Run
python Master.py

## Reference
* Alexander Card. (In preparation). A new measurement of electron densities in the MOCHI LabJet experiment using an unequal path length, heterodyne interferometer (Master's thesis). University of Washington

## Contact
Alexander Card card@uw.edu
