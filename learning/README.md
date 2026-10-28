# Learning Quantum Transport Precision

The physical question is how a finite coherent conductor can transmit a steady stream of particles with small long-time count fluctuations. A chain has two distinct resources: its number of orbitals and the strength of its coupling to the source and drain. Understanding the project means following both resources through the same transmission function.

The selected educational anchor is **Supriyo Datta, *Electronic Transport in Mesoscopic Systems* (Cambridge University Press, 1995)**, [book DOI](https://doi.org/10.1017/CBO9780511805776). The [Datta bridge](DATTA_BRIDGE.md) identifies the relevant verified chapters and translates their transport framework into the conventions used here. The full book is not needed to identify the local definitions, assumptions, and proof steps: those are stated in the linked repository accounts. Access to the book itself depends on the publisher or a library.

## Start with one orbital

Consider one orbital at zero energy, with equal physical contact rates $`\Gamma`$ to a completely filled source and an empty drain. An incoming particle with energy $`E`$ is transmitted with probability

```math
T(E)=\frac{\Gamma^2}{E^2+\Gamma^2}.
```

The resonance is perfectly transmitting at its center, yet the current samples the entire energy axis. Away from the center, transmission is partial and contributes partition noise. Integrating this profile gives mean particle current $`J=\Gamma/2`$, count-variance rate $`D=\Gamma/4`$, and Fano factor $`F=D/J=1/2`$. The [worked derivation](DATTA_BRIDGE.md#one-orbital) fixes the factors of two before moving to a longer chain.

A longer coherent chain can make its transmission closer to a broad, nearly ideal passband. The research asks how quickly the remaining noise can fall with the number of sites, whether the chosen profile has an exact physical realization, and how its current changes when the contact rates are held fixed.

## Two phases, one connected account

The [milestone map](MILESTONES.md) contains exactly 30 project-defined understanding targets. Each record states its central question, target, earlier dependencies, role in the argument, conceptual connection, and source pointers.

| Phase | Milestones | What becomes connected |
|---|---|---|
| Background and preliminaries | [M01](MILESTONES.md#m01)–[M14](MILESTONES.md#m14) | Particle counting, the serial Hamiltonian, reservoirs, transmission and noise, polynomial bounds, and physical synthesis |
| Narrative and innovation | [M15](MILESTONES.md#m15)–[M30](MILESTONES.md#m30) | The universal size converse, the inherited attaining filter, its exact site count, and the contact-limited throughput law |

The closing milestone in each phase assembles the preceding local ideas. Dependencies are explicit so a reader can revisit the prerequisite that explains a difficult step.

## Follow a reading goal

| Goal | Entry point | Next connection |
|---|---|---|
| Understand the physical setting and units | [Datta bridge](DATTA_BRIDGE.md) | [Model and observables](../science/model.md) |
| Follow the whole conceptual argument | [30 milestones](MILESTONES.md) | [Scientific reading map](../science/README.md) |
| Read the proofs directly | [Scientific reading map](../science/README.md) | The topic pages linked there |
| Understand what comes from earlier work | [Related work](../references/RELATED_WORK.md) | [Bibliography](../references/references.bib) |
| Inspect finite realizations and counting checks | [Verification guide](../verification/README.md) | The recorded data and reproducible calculations |

Datta supplies the educational anchor. The primary papers cited in the scientific account supply attribution, comparisons, and particular mathematical ingredients. The [bridge](DATTA_BRIDGE.md) identifies where the project needs additional material beyond the book's transport framework.

Return to the [repository overview](../README.md).
