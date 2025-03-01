# PASAD

This is the assignment repository of Group 5 for the course CS658. This repository contains the implementation of __PASAD__ (in Python) on the __SWaT__ and __TE__ Datasets. Process-Aware Stealthy Attack Detection (PASAD) is an advanced method used to detect cyber-physical attacks on industrial control systems (ICS). Unlike traditional security measures that focus on network traffic or software signatures, PASAD leverages the dynamics of physical processes themselves to identify anomalies indicative of a stealthy cyber attack. It is based on the paper [Truth Will Out: Departure-Based Process-Level Detection of Stealthy Attacks on Control Systems](https://dl.acm.org/doi/pdf/10.1145/3243734.3243781).

## Datasets

SWaT Dataset: [here](https://drive.google.com/drive/folders/1zn0DMCdSXA9b_CiaaoDzvkbwX5O4ikLn)

TE Dataset: [here](https://github.com/mikeliturbe/pasad/tree/master/data)

Create a directory named "Dataset" in the PASAD directory and organise it as -

Dataset

    - SWaT
        -- *Files
    - TE
        - 1-Scenario DA1
            -- *File
        - 2-Scenario DA2
            -- *File
        - 3-Scenario SA1
            -- *File
        - 4-Scenario SA2
            -- *File
        - 5-Scenario SA3
            -- *File

## Repository Structure

| Directory       | Description |
|-----------------|-------------|
| Implementation       | Contains the steps of PASAD in individual python files and notebooks containing the solution to the respective questions   |
| Results | Contains the images of various results  |

## How to run?

Enter the Implementation directory and download the required dependencies using ``` pip install -r requirements.txt ``` then run any notebook.

## Team

Himanshu Shekhar (220454)

Lokesh Yadav (220594)

Kamal Kant Tripathi (241110086)