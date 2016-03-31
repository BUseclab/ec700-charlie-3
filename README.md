# Analyzing VM-aware Malware on Bare-Metal

Repo for the EC700 group Charlie-3 currently made up of:
- Drew kierke@bu.edu
- Leen leenshe@bu.edu
- Blake btribou@bu.edu

## Malware Epoch

_Initial Project Description:_ Malware authors will sometimes utilize anti-virtual machine techniques to avoid attempts for recognition and analysis.  The malware attempts to detect whether it is being executed within a VM and adjust it's behaviour accordingly to avoid detection and analysis.  Our proposed project, based on the BareCloud project, will utilize Cuckoo sandbox recording malware behaviour on a VM, an emulator, and a physical bare-metal machine.  Our inital, perhaps naive, analysis will attempt to identify malware samples that make five or more API calls in the bare-metal dynamic analysis environment that were not made in the virtualized environments.  This goal involves some manual analysis of the information that cuckoo logs after setting up automated dynamic analysis environments for bare-metal, the virtual machine, and the emulator.  Evaluation will come from the effective analysis of as many samples as possible after setting up the three environments, providing an analysis of the difficulties associated and time constraints needed to impose this system effectively, as well as the naive and manual analysis of what the samples with varying behaviour are doing.


### Goals:

__Main:__ Description of the main goal is above, though at first we will limit our goal to one virtualized analysis system and the bare metal analysis system (i.e., skip the emulator here).  For the initial bare-metal system we will be using customized hardware and for the initial VM we will be utilizing cuckoo on VirtualBox.

__Stretch 1:__ Expand our comparative analysis by adding in a 2nd virtualization mechanism and an emulated system to assess further differences.  For this system we will utilize qemu and kvm to get cuckoo running. 

__Stretch 2:__ Provide a more fine-grained analysis scheme derived from our work in the main goal, identify and justify the changes to our detection threshold.  There will be some innate differences in behaviour that are benign due to the differences between the virtualized and bare-metal environments - we will attempt to identify and weed these differences out.

### Ideal Timeline:

[Discussion/Research Inital Setup] (First Weekend: 3/30 - Monday 4/3)

#### Week #1 (4/5 - 4/12)
- [ ] Obtain physical machine and connect it through one of the approved ports in the fourth floor labs, look into physical modifications necessary to automate restoration of machine state and external storage of sample analysis
- [ ] Setup webserver that will serve the malware samples to the machines via some queueing mechanism
- [ ] Familiarize ourselves with cuckoo framework
- [ ] Set up the VM and configure it for automated dynamic analysis
- [ ] Log initial difficulties and issues in detail to redefine tasks in the coming week

#### Week #2 (4/12-4/19)
- [ ] Identify issues from first sprint and communicate to professors/blog posts any initial difficulties to work them out as quickly as possible
- [ ] Collect malware samples with help from the professor or perhaps other groups/research contacts
- [ ] Hopefully start running the machines, debug initial issues, finish any 
- [ ] Set up the Emulated environment and configure it for automated dynamic analysis
- [ ] Compile some naive results and prepare midterm report

#### Week #3 (4/19-4/26)
- [ ] Stretch #1 - Manual analysis of the initial results (classification via API calls), evaluate the efficacy of this method and look into differences in behaviour to try and systematically adjust the detection/classification of VM-aware malware and it's behaviour
- [ ] Stretch #2 - Based on judgements that can be made on our work at this point we should be able to provide a projected timeline for how many samples our framwork can look at within the remaining time, attempt to scale our results to include as many samples as possible (hopefully come up with a more concrete projection by the time of the midterm)

#### Project Wrap Up (4/26-4/27 Last Day)
- [ ] Prepare white paper and final project results/presentation

### Projected Initial Distribution of Labor

Drew:
* I will initially be focusing on the set-up of the physical machine and the automation of the bare-metal dynamic analysis environment

Leen:
* Leen may focus on the setup of the webserver to queue up samples, depending on how this process goes and timeline she may work together with Blake on the setup of the emulator and VM

Blake:
* Focus on the setup of the VM and emulator and configuring them to mirror the physical environment as closely as possible.

### Sources/Papers Referenced:

BareCloud (main paper referenced and one presented for Monday discussion):

	https://www.cs.ucsb.edu/~vigna/publications/2014_USENIX_BareCloud.pdf
	
BareBox - [ ] same authors earlier work, utilize the differences between this and the new work to hopefully avoid potential pitfalls:

	https://www.cs.ucsb.edu/~chris/research/doc/acsac11_barebox.pdf
	
Effective Detection of Split Personalities in Malware:

	https://www.cs.ucsb.edu/~chris/research/doc/ndss10_splitmal.pdf
