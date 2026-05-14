+++
title = "Biologie synthétique"
description = "La biologie synthétique est un domaine interdisciplinaire qui combine les principes de la biologie, de la génétique et de l'ingénierie pour concevoir et construire des systèmes biologiques artificiels, des circuits génétiques et des organismes dotés de nouvelles fonctions ou caractéristiques. Cela implique la modification ou la création délibérée de matériel génétique et l'ingénierie de composants biologiques pour programmer des cellules vivantes afin qu'elles effectuent des tâches spécifiques ou présentent des traits souhaités. La biologie synthétique vise à comprendre et à réorganiser les systèmes biologiques."
template = "wiki-page.html"
toc = true

[extra]
category = "Science & Technology"
editorial_pass = "2026-05"
entry_type = "discipline"
claim_type = "direct"
alternative_names = ["Engineering biology", "Constructive biology", "Designed biology", "SynBio"]

[extra.infobox]
type = "Engineering discipline applied to living systems"
parent_field = "Life engineering"
sister_fields = "Genetic engineering; synthetic genomics; xenobiology"
distinguishing_feature = "Engineering-discipline practice (standardisation, modularity, abstraction, design–build–test cycles) applied to biological systems"
foundational_milestones = "Repressilator (Elowitz and Leibler, 2000); genetic toggle switch (Gardner, Cantor, and Collins, 2000); first synthesis of a viral genome (Wimmer, 2002); BioBricks standard and Registry of Standard Biological Parts (Knight, 2003); iGEM (2004); semi-synthetic artemisinin (Keasling and colleagues, 2005 onward); JCVI-syn1.0 (2010)"
key_techniques = "Genetic circuit design; metabolic pathway engineering; protein engineering (rational design and directed evolution); cell-free reaction systems; CRISPR-based circuit construction"
current_status = "Active scientific discipline; commercial deployment in pharmaceuticals, food, materials, and industrial chemicals; multi-billion-dollar industry sector"
framework_significance = "The discipline whose engineering-discipline vocabulary and methods most directly match the operational description of the Elohim's work in the Raëlian source material"
+++

**Synthetic biology** is the engineering-discipline branch of contemporary [life engineering](../life-engineering/). It applies engineering methods — standardisation, modularity, abstraction, characterisation, and design–build–test cycles — to the construction of biological systems with predetermined properties. The field is distinguished from older [genetic engineering](../genetic-engineering/), which it overlaps and extends, by its programmatic commitment to genuine engineering-discipline practice rather than the case-by-case empirical approach that characterised most pre-2000 biological-modification work; and from [synthetic genomics](../synthetic-genomics/), which it overlaps and includes, by its concern with sub-systems and components in addition to complete genomes.

The field's central ambition is articulated in a small set of foundational documents from the early 2000s: that biology should become an engineering discipline in the same sense that mechanical engineering, electrical engineering, and software engineering are engineering disciplines — with standardised parts, predictable composition rules, formal design methodologies, and design–build–test cycles that scale across many laboratories and many projects. This ambition has been partially realised. Biological systems remain less predictable than electronic systems; the parts catalogue is smaller; the composition rules are less well understood. But the trajectory has been forward across two decades, and the field has produced an impressive cumulative set of achievements across genetic-circuit engineering, metabolic engineering, protein engineering, cell-free reaction systems, mammalian and human cell engineering, and synthetic developmental biology.

The discipline formalised in the early 2000s with the publication, in *Nature* in January 2000, of the first two designed-from-scratch synthetic genetic circuits — Elowitz and Leibler's *repressilator*, a three-gene oscillator, and Gardner, Cantor, and Collins's *toggle switch*, a bistable two-gene system. The two papers are commonly identified as the inaugural publications of the contemporary field. The establishment of the BioBricks parts standard in 2003, the first International Conference on Synthetic Biology at MIT in 2004, and the founding of the iGEM (International Genetically Engineered Machine) competition the same year established the field's institutional infrastructure.

The reading on which the framework's interest in synthetic biology depends is not contested. The scientific reality of the field — its techniques, its achievements, its commercial and clinical deployments — is established and documented across a substantial scientific literature. What is contested is the framework's interpretation of the field's emergence and methods: the claim that the engineering-discipline vocabulary and methods of contemporary synthetic biology are the present-day local instance of the operational vocabulary in which the Raëlian source material describes the Elohim's work. The corpus presents the field accurately as it currently stands, registers the framework's reading of its significance, and treats the broader interpretive question with the discipline applied throughout the wiki. The convergence argument is developed at full length in the [life engineering](../life-engineering/) entry; the present entry treats it more briefly, since the broader argument applies and the synthetic-biology-specific aspects are what require dedicated treatment here.

## Definition and scope

The boundaries of synthetic biology as a unified concept are contested within the field itself and the term is used with somewhat different scopes by different authors. A brief survey of the principal usages clarifies what the entry means by the term.

### The engineering-discipline definition

The most common contemporary definition treats synthetic biology as the discipline that applies engineering-discipline principles — modularity, standardisation, abstraction, predictable composition, design–build–test cycles — to the construction of biological systems. On this definition, the field is distinguished from earlier genetic engineering not by what it modifies (both fields modify biological systems) but by *how* it modifies it: through formal design methodologies rather than empirical trial-and-error. The definition is the one articulated in the foundational documents of the early 2000s, including Tom Knight's BioBricks proposal, Drew Endy's "Foundations for Engineering Biology" essay (*Nature*, 2005), and Andrianantoandro and colleagues' "Synthetic Biology: New Engineering Rules for an Emerging Discipline" (*Molecular Systems Biology*, 2006).

### The constructive-biology definition

A broader definition treats synthetic biology as any approach to biology that proceeds by *construction* rather than only by analysis — the engineering-discipline epistemology applied to the biological sciences. On this definition, synthetic biology is partly an engineering discipline (when it aims at producing useful systems) and partly a basic-science discipline (when it aims at understanding biological systems by constructing them). The two aims often run together: a designed-from-scratch oscillator simultaneously tests the design principles by which oscillation is achievable and produces a useful oscillator. This definition captures the broader scientific significance of the field, which extends well beyond commercial applications to the foundational question of what living systems are and how they work.

### The artificial-life definition

A still broader definition, more common in some European and academic-philosophical contexts, treats synthetic biology as the discipline whose aim is the construction of *artificial life* — biological systems that have no antecedent in the natural world. On this definition, synthetic biology is the contemporary realisation of the artificial-life ambition that goes back at least to the early-twentieth-century work of Stéphane Leduc on synthetic biology *avant la lettre* (Leduc himself coined the term *la biologie synthétique* in 1912). This definition emphasises the discontinuity between synthetic biology and earlier biotechnology — the move from working with existing life to constructing new life — and is the definition most closely connected to the Wheel of Heaven framework's reading.

### The usage adopted in this entry

The entry adopts the engineering-discipline definition as primary, since it is the dominant usage in the contemporary scientific literature, with the constructive-biology and artificial-life definitions recognised as relevant complementary perspectives. The framework's interest extends across all three definitions; the discussion below treats each as relevant.

## Historical development

The history of synthetic biology has both a pre-history extending back to the early twentieth century and a properly modern phase beginning around 2000. The two phases are treated separately because they differ substantially in their scientific content, their institutional infrastructure, and their intellectual ambitions.

### Pre-history: from Leduc to the cybernetic tradition

The term *la biologie synthétique* was coined by the French biologist **Stéphane Leduc** in 1912, in his book *La biologie synthétique*. Leduc proposed that biology, like organic chemistry, would eventually become a synthetic as well as an analytic discipline — that biological systems would be constructed in the laboratory rather than only studied in nature. Leduc's own experimental work involved the construction of biomimetic systems through inorganic chemistry (osmotic growths, chemical gardens) that he interpreted as models for the simplest forms of biological organisation. His scientific programme did not directly produce contemporary synthetic biology, but his terminology and ambitions anticipated the modern field by nearly a century.

The mid-twentieth-century cybernetic tradition contributed the conceptual vocabulary on which contemporary synthetic biology depends. Norbert Wiener's *Cybernetics* (1948), the foundational work of the cybernetic tradition, treated biological systems as information-processing systems amenable to engineering-discipline analysis. The cybernetic vocabulary of feedback loops, control circuits, regulatory networks, and signal processing became the standard vocabulary for thinking about gene-regulatory networks once those networks began to be characterised in the 1960s. The *operon model* of François Jacob and Jacques Monod (1961), describing the regulation of bacterial gene expression as a circuit with promoters, repressors, and feedback, is the foundational example of the cybernetic vocabulary applied to molecular biology.

The cybernetic tradition also produced the broader theoretical literature on self-organisation, autopoiesis (Humberto Maturana and Francisco Varela's term for the self-producing organisation of living systems), and the systems-theoretic understanding of life that subsequently became one of the intellectual foundations of synthetic biology.

### The molecular-biology foundation

The molecular-biology revolution of the mid-twentieth century provided the substrate on which synthetic biology operates. The full historical arc is treated in the [life engineering](../life-engineering/) entry; the principal foundational discoveries for synthetic biology specifically were the Watson–Crick structure of DNA (1953), the genetic-code work of the early 1960s (Nirenberg, Khorana, Holley), the operon model (Jacob and Monod, 1961), the discovery of restriction enzymes (Arber, Smith, Nathans, late 1960s), the Boyer–Cohen recombinant DNA work (1973), Sanger and Maxam–Gilbert sequencing (1977), and the development of PCR (Mullis, 1985). By the late 1990s, the toolkit for the construction of designed genetic circuits — sequencing, synthesis, cloning, transformation, characterisation — was sufficiently developed that the field's foundational experiments became possible.

### 2000: the foundational publications

The contemporary field of synthetic biology dates from January 2000, when two papers were published in *Nature* in the same issue that together established the engineering-discipline approach to biological-circuit construction.

**Michael Elowitz and Stanislas Leibler** at Princeton published *A Synthetic Oscillatory Network of Transcriptional Regulators* — the **repressilator**. The repressilator is a three-gene oscillatory circuit in which each gene's product (a transcriptional repressor) inhibits the next gene in the cycle: gene A's product represses gene B, gene B's product represses gene C, gene C's product represses gene A. The result is a feedback loop with an inherent oscillatory behaviour, since no stable equilibrium exists. The Elowitz–Leibler experiment built the circuit in *Escherichia coli* using existing repressor proteins (LacI, TetR, and lambda CI), coupled it to a green fluorescent protein reporter, and demonstrated that the cells produced regular oscillations in fluorescence with periods of approximately 150 minutes. The work established that biological oscillators could be designed from first principles, predicted theoretically, and built and tested experimentally — the engineering-discipline workflow applied to a biological system.

**Timothy Gardner, Charles Cantor, and James Collins** at Boston University published *Construction of a Genetic Toggle Switch in Escherichia coli* in the same issue. The toggle switch is a two-gene bistable circuit in which each gene's product represses the other gene's expression: in steady state, exactly one of the two genes is active, and the system can be flipped between its two stable states by transient external signals. The work demonstrated that biological memory elements could be designed and constructed, paralleling the role of flip-flops in electronic computing.

The two papers together established the field's engineering-discipline foundation. Both demonstrated designed circuits with predictable behaviour. Both used quantitative mathematical models to predict the circuits' behaviour before constructing them. Both validated the predictions experimentally. The methodology — design from first principles, predict mathematically, build, test — was, from the start, the methodology of an engineering discipline rather than the methodology of traditional biological research.

### 2002: the first synthetic virus

**Eckard Wimmer and colleagues** at SUNY Stony Brook published, in 2002, the chemical synthesis of a functional poliovirus from mail-ordered DNA fragments. The work assembled the complete poliovirus genome (approximately 7.5 kilobases) from chemically synthesised oligonucleotides obtained from commercial DNA-synthesis vendors, transcribed the synthetic DNA to RNA, and demonstrated that the resulting RNA generated infectious viral particles when introduced into mammalian cell culture. The first synthesis of a complete viral genome from chemical components was a foundational demonstration that the techniques of synthetic biology could be applied at the scale of a complete pathogen — with the immediate biosecurity implications that subsequently informed the regulatory development of the field.

### 2003–2004: institutional formalisation

The years 2003 and 2004 mark the field's institutional formalisation.

**Tom Knight** at MIT proposed the **BioBricks** standard in 2003 — a system of standardised genetic parts designed for predictable composition. The proposal followed the engineering-discipline logic explicitly: just as electronic engineering depends on standardised components with characterised properties that can be combined according to known rules, biological engineering would depend on standardised genetic parts (promoters, ribosome binding sites, coding sequences, terminators) with characterised properties and standardised interfaces. The **Registry of Standard Biological Parts** was established the same year at MIT to catalogue the standardised parts, characterise their behaviour, and distribute them to researchers.

The **first International Conference on Synthetic Biology (SB1.0)** was held at MIT in 2004, bringing together the founding researchers of the contemporary field. The conference established the institutional gathering point for the discipline and inaugurated the biennial conference series that has continued to the present.

The **iGEM (International Genetically Engineered Machine) competition** was established the same year, initially as an MIT-internal summer course and then quickly expanding to an international undergraduate competition in which student teams design, build, and test synthetic-biological systems using parts from the Registry. The iGEM competition has since trained a generation of synthetic biologists and produced a substantial fraction of the parts in the Registry's catalogue.

### 2005–2010: metabolic engineering and the first synthetic genome

The mid-2000s saw the field's first major commercial demonstrations and the foundational work on synthetic genomes.

**Jay Keasling and colleagues** at UC Berkeley published, beginning in 2003 and consolidating through subsequent papers, the engineering of yeast (*Saccharomyces cerevisiae*) to produce artemisinic acid — a precursor of the antimalarial drug artemisinin. The work involved the introduction of a multi-gene biosynthetic pathway from *Artemisia annua* (the plant that naturally produces artemisinin) into yeast, with substantial optimisation of the host metabolism to support the engineered pathway. The work was commercialised through Amyris over the subsequent decade and demonstrated that synthetic biology could produce industrially relevant quantities of complex molecules previously sourced from rare or difficult plants. The artemisinin programme is commonly identified as the field's flagship demonstration of metabolic engineering at industrial scale.

**Daniel Gibson and colleagues** at the J. Craig Venter Institute published, in 2008, the synthesis and assembly of the complete *Mycoplasma genitalium* genome from chemically synthesised oligonucleotides — the largest synthetic genome assembled to date and the precursor to the JCVI-syn1.0 work. The Mycoplasma genitalium genome (approximately 583 kilobases) was assembled hierarchically: short oligonucleotides were combined into intermediate fragments through PCR and overlap extension, the intermediate fragments were combined into larger assemblies through recombination in yeast, and the complete genome was reconstructed as a single circular DNA molecule. The work established the technical foundation for the synthesis of complete bacterial genomes.

**JCVI-syn1.0** (2010) followed: the first organism with an entirely synthetic genome, a *Mycoplasma mycoides* strain whose 1.08-megabase genome was chemically synthesised, assembled in yeast, transplanted into a *Mycoplasma capricolum* recipient cell, and propagated as a free-living bacterium. The detailed treatment lives in the [synthetic genomics](../synthetic-genomics/) entry; the relevance to synthetic biology is that the work demonstrated, at genome scale, the engineering-discipline approach the field had previously demonstrated at circuit scale.

### 2012–present: CRISPR, cell engineering, and the maturation phase

The 2010s saw synthetic biology mature into an industrial discipline with substantial commercial deployment.

The **2012 publication of CRISPR–Cas9** (Jinek, Chylinski, Fonfara, Hauer, Doudna, and Charpentier) transformed the editing side of the field. The full historical treatment is in the [life engineering](../life-engineering/) entry; the specific relevance to synthetic biology is that CRISPR provided the precision-editing capability that the engineering-discipline ambitions of the field had previously lacked. Designed circuits could now be inserted at predictable positions in host genomes; specific genes could be silenced, activated, or modified without the empirical chassis-construction work that earlier methods had required.

**CAR-T cell engineering** — the engineering of patient T-cells to recognise tumour antigens — emerged as a major clinical application of synthetic biology across the 2010s, with the first FDA approvals (Kymriah, Yescarta) coming in 2017. CAR-T cells are designed using synthetic-biology methods: a chimaeric antigen receptor combining elements of an antibody (the antigen-recognition domain), a transmembrane domain, and an intracellular signalling domain is constructed from designed sequence and introduced into patient T-cells using engineered viral vectors. The engineering-discipline approach — predictable behaviour from designed components — has been validated by the clinical efficacy of the resulting cells.

**Engineered cell-based therapies more broadly** — including additional engineered T-cell platforms, engineered stem cells, and engineered microbial therapies for the gut microbiome — have continued to develop across the past decade. Several engineered-cell therapies are in clinical trial for solid tumours, autoimmune diseases, and other indications.

**Synthetic developmental biology** has emerged as a distinct sub-field across the 2010s and 2020s. The **Xenobot** work of Michael Levin and colleagues at Tufts (2020 onward) demonstrated that multicellular organisms can be assembled from designed combinations of frog (*Xenopus laevis*) cells with computationally designed body plans, producing functional behaviour (locomotion, self-replication, simple problem-solving) from cells originally specified for completely different developmental roles. The Xenobot work is not the engineering of multicellular organisms from designed DNA — the cells themselves are wild-type, only their spatial arrangement is designed — but it demonstrates the engineering of multicellular form, which is one of the major open problems of synthetic biology.

**The Synthetic Yeast 2.0 (Sc2.0) consortium**, working since the early 2010s on the synthesis of a complete redesigned genome for *Saccharomyces cerevisiae*, has reported progress on individual chromosome syntheses across the past decade with the integration of all sixteen synthetic chromosomes into a single yeast strain approaching completion. The work, treated more fully in the [synthetic genomics](../synthetic-genomics/) entry, is the eukaryotic-scale realisation of the synthetic-biology programme.

**AI-driven protein design** — particularly the work of David Baker on RFdiffusion and related methods, and the AlphaFold protein-structure-prediction work of Demis Hassabis and John Jumper at DeepMind — has transformed the protein-engineering side of synthetic biology across the past five years. The 2024 Nobel Prize in Chemistry recognised these contributions. The implications for synthetic biology are direct: with reliable methods for predicting protein structure from sequence and for designing new sequences with specified structural and functional properties, the parts catalogue of synthetic biology can be extended substantially beyond the empirically characterised parts that have constituted it to date.

## Intellectual foundations

The intellectual foundations of synthetic biology are drawn from several scientific and engineering traditions that converged in the late twentieth and early twenty-first centuries. Each contributed a specific component of the discipline's contemporary character.

### Molecular biology

Molecular biology provided the technical substrate. The molecular-biological understanding of DNA structure and function, of gene-regulatory mechanisms, of protein structure and function, and of the relationships among DNA, RNA, and proteins is the substrate on which synthetic-biological design operates. Without the cumulative work of molecular biology across the second half of the twentieth century, no contemporary synthetic-biological design would be possible.

### Engineering disciplines (electrical, mechanical, software)

The mature engineering disciplines provided the methodological vocabulary. The conceptual moves of synthetic biology — abstraction, modularity, standardisation, hierarchical composition, design–build–test cycles, characterisation of components, predictable composition — are not native to biology but are imported wholesale from the engineering disciplines that had developed them across the nineteenth and twentieth centuries. The explicit ambition of synthetic biology has been to introduce these engineering-discipline practices into biological design, where they had not previously been standard.

The analogy to electrical engineering and computer engineering has been particularly explicit. The BioBricks standard, the iGEM competition, the Registry of Standard Biological Parts, and the broader institutional infrastructure of the field were modelled on the standards and practices of electronic engineering. Drew Endy's articulation in *Foundations for Engineering Biology* (*Nature*, 2005) makes this explicit: synthetic biology aims to do for biological systems what electrical engineering does for electronic systems.

### Systems biology

The systems-biology tradition of the 1990s and 2000s provided the empirical and computational foundation. Systems biology — the study of biological systems at the network level, measuring all components simultaneously and modelling their interactions — produced the characterisation of gene-regulatory networks, metabolic networks, and signalling networks that synthetic-biological design depends on. The two fields developed in parallel and remain closely coupled: synthetic biology often serves as a test-bed for systems-biological understanding (a circuit that behaves as predicted validates the model on which it was designed), and systems biology often provides the characterisation data on which new designs are based.

### Cybernetics and information theory

The cybernetic tradition contributed the conceptual vocabulary for treating biological systems as information-processing systems. Wiener's cybernetics, Shannon's information theory, and the broader systems-theoretic tradition of the mid-twentieth century established the vocabulary of feedback, control, signal, noise, channel, code, and information flow that contemporary synthetic biology uses to describe biological circuits and systems.

### Origins-of-life research

The origins-of-life research tradition contributed the philosophical foundation for the constructive approach to biology. If the question of how life arose can in principle be answered by demonstrating the construction of life from non-living components, then the constructive methodology — building biological systems rather than only studying them — has direct scientific significance beyond its engineering applications. The origins-of-life tradition is the intellectual ancestor of the *artificial-life* definition of synthetic biology and remains a significant motivation for some of the field's most ambitious research programmes (the minimal-cell work, the xenobiology work, the prebiotic-chemistry-to-living-systems programmes).

## Principal research programmes

Contemporary synthetic biology comprises several distinct research programmes, each with its own methods, achievements, and limitations. The principal programmes are treated in turn below.

### Genetic circuit engineering

Genetic circuit engineering — the design and construction of gene-regulatory networks with specified behavioural properties — is the foundational research programme of the modern field. The repressilator and toggle switch of 2000 established the methodology; subsequent work has produced an expanding catalogue of designed circuits.

The catalogue of designed circuits now includes:

- **Oscillators** — Circuits with regular periodic behaviour, used both for timing applications and for understanding the principles of biological oscillation. The repressilator and its descendants, plus a growing set of alternative oscillator designs based on different topologies and components.
- **Switches** — Bistable or multistable circuits with discrete states, used for memory applications and for understanding biological decision-making. The Gardner toggle switch and its descendants, including multi-state switches and switches integrated with sensors and effectors.
- **Logic gates** — Circuits implementing Boolean logic operations (AND, OR, NOT, NAND, XOR), used for integrating multiple input signals into specified output decisions. A substantial catalogue of biological logic gates is now available, with implementations in bacterial and mammalian cells.
- **Counters** — Circuits that count discrete events (cell divisions, signal pulses), maintaining a stable record of past events.
- **Feedback controllers** — Circuits implementing engineering-style feedback control for the maintenance of specific cellular variables at set-point values, with relevance to therapeutic applications where physiological variables must be controlled.
- **Edge detectors and spatial-pattern generators** — Circuits that respond to spatial patterns of input signals, used for studying tissue-level organisation and for engineering specific spatial patterns of cellular activity.

The state of the field as a practical engineering discipline is improving but still substantially less reliable than electronic-circuit engineering. Designed circuits commonly behave somewhat differently in practice than their theoretical models predict, due to context-dependence (the same part behaves differently in different host cells or in different genetic backgrounds), resource competition (the host cell's metabolic and translational resources are shared among the engineered circuit and the cell's native processes), and stochastic noise (gene expression is intrinsically noisy at the single-cell level). The cumulative work of the field across the past two decades has been substantially concerned with characterising and managing these effects to improve the predictability of designed circuits.

### Metabolic engineering

Metabolic engineering — the design and optimisation of multi-gene biosynthetic pathways in microbial hosts for the production of specific molecules — has been the most commercially significant programme of contemporary synthetic biology. The flagship demonstration is Keasling's artemisinin pathway; the cumulative output of the field across the past two decades has produced microbial production routes for an expanding list of valuable molecules.

The metabolic-engineering programme typically proceeds through several stages: identification of the target molecule and its natural biosynthetic pathway (where one exists); cloning of the relevant pathway genes into a microbial host (typically *E. coli* or *S. cerevisiae*); optimisation of the host's native metabolism to support the engineered pathway (often involving the deletion of competing pathways and the up-regulation of precursor synthesis); fine-tuning of the engineered pathway's expression levels and enzyme activities through directed evolution and rational design; and scale-up to industrially relevant production volumes.

Significant commercial deployments include the artemisinin pathway (Amyris), microbial production of opioids (alkaloids), of cannabinoids, of vanillin, of saffron-derived compounds (crocins, picrocrocin, safranal), of various flavour and fragrance compounds, and of an expanding list of food ingredients and industrial chemicals. The *precision-fermentation* industry — engineered microbes producing dairy and egg proteins for the alternative-protein market — has grown rapidly across the past decade.

### Protein engineering

Protein engineering — the design and modification of proteins for specific functions — is the discipline that produces the functional components of synthetic-biological circuits and systems. The two principal approaches are rational design and directed evolution, with hybrid approaches combining the two having become increasingly common.

**Rational design** uses computational modelling of protein structure and function to predict the consequences of specific sequence changes, with the goal of producing proteins with specified properties through informed sequence modification rather than empirical screening. The approach requires detailed structural information about the target protein and substantial computational infrastructure. The pre-2020 state of rational design was successful for limited classes of protein engineering — primarily stability engineering and modest functional modification — but limited for more ambitious tasks like de novo function design.

The transformation of the field in the past five years has come from AI-driven methods. **AlphaFold** (Jumper and colleagues at DeepMind, 2020–2021) achieved accurate prediction of protein three-dimensional structure from amino-acid sequence at a level previously considered essentially impossible; the AlphaFold database now contains predicted structures for essentially every characterised protein. **RFdiffusion** (David Baker and colleagues at the University of Washington, 2023) uses related diffusion-model approaches to generate new protein sequences with specified structural and functional properties — the de novo design of proteins from scratch, now feasible at a level that pre-AI rational design had not approached. The 2024 Nobel Prize in Chemistry recognised these contributions.

**Directed evolution** uses the principles of natural selection at the molecular level: large populations of variant proteins are generated through random mutagenesis or recombination of the target gene, the resulting variants are screened or selected for the desired function, the best-performing variants are used as the starting population for the next round of mutation and selection, and the process is iterated until variants with the desired function are obtained. The method is powerful because it requires no detailed structural or mechanistic understanding of the target protein; it requires only a way to screen or select for the desired function. Frances Arnold shared the 2018 Nobel Prize in Chemistry for the development of directed evolution methods for enzymes.

Directed evolution has been particularly successful for engineering enzymes with novel catalytic activities — including catalytic activities that natural enzymes do not perform. The expanding catalogue of designer enzymes from directed-evolution campaigns has supported the metabolic-engineering programme by providing optimised enzymes for engineered biosynthetic pathways.

### Cell-free synthetic biology

Cell-free synthetic biology — the reconstitution of biological function in cell-free extracts — is a research programme that has expanded rapidly across the past decade. Cell-free systems prepare the molecular machinery of biological function (ribosomes, polymerases, regulatory proteins, energy-regeneration systems) from cellular extracts and reconstitute biological function in solution rather than within living cells. The approach offers several advantages for synthetic-biological design: simpler systems with fewer confounding effects, faster experimental turnover (no waiting for cell growth), the ability to operate with components that would be toxic to living cells, and the ability to combine components from very different species without compatibility issues.

Significant work in cell-free synthetic biology includes the rapid prototyping of designed circuits, the production of pharmaceuticals in cell-free systems for personalised or on-demand manufacturing, the characterisation of biological-circuit behaviour in controlled molecular contexts, and the construction of minimal cell-like systems that approach the lower bound of what living systems require.

### Mammalian and human cell engineering

The application of synthetic-biology methods to mammalian cells, and specifically to human cells, has emerged as a major research programme across the past decade. The principal applications:

- **Engineered T-cell therapies** (CAR-T cells and successor platforms) for cancer and increasingly for autoimmune and other diseases.
- **Engineered stem-cell therapies** for regenerative medicine, with directed differentiation of stem cells into specific cell types under engineered control.
- **Synthetic gene circuits in mammalian cells** for the controlled production of therapeutic proteins, for the detection of disease states, and for the conditional activation of therapeutic responses.
- **Engineered organoids** — three-dimensional multicellular structures that recapitulate aspects of organ structure and function, used as models for disease and as platforms for drug screening.

The mammalian-cell-engineering programme is technically more challenging than bacterial-cell engineering because mammalian cells are more complex (with regulatory networks, signalling pathways, and metabolic processes considerably more elaborate than those of bacteria), less predictable (with greater cell-to-cell variability and more sensitivity to environmental conditions), and slower (with population-doubling times measured in days rather than minutes). The cumulative work of the field has nonetheless produced a substantial set of demonstrated capabilities, with clinical translation now established for the engineered-T-cell platforms.

### Synthetic developmental biology

Synthetic developmental biology — the application of synthetic-biology methods to the question of how organised multicellular structures emerge from cell-cell interactions — is the field's most recent major sub-discipline. The fundamental problem the field addresses is the transition from designed single cells to designed multicellular organisms, which is one of the major remaining frontiers of synthetic biology.

Significant work includes:

- **Synthetic morphogenesis** — Designed cell–cell signalling and adhesion that produces organised tissue-like patterns from initially homogeneous cell populations. The work has demonstrated that simple designed interactions among cells can produce a substantial range of self-organising spatial patterns.
- **The Xenobot programme** (Levin and colleagues at Tufts, 2020 onward) — Multicellular organisms assembled from frog (*Xenopus laevis*) embryonic cells in computationally designed configurations, producing functional behaviour from cells that, in a normal frog, would have developed into skin and heart tissue. The Xenobots have demonstrated locomotion, simple problem-solving, and a form of kinematic self-replication.
- **Engineered organoid development** — Directed differentiation of stem cells into multi-cell-type organoid structures with controlled three-dimensional organisation, used for disease modelling and drug screening.

The field is in its early stages but represents the leading edge of the synthetic-biology programme's progress toward the multicellular regime. Whether the methods developed in synthetic developmental biology will eventually scale to the design of complete multicellular organisms from designed DNA — the regime in which the source material's account of the Elohim's work places their capabilities — is an open question.

## Applications

The applications of synthetic biology span medicine, agriculture, industry, and foundational research. The list below is partial and intended to convey the field's current operational scope rather than to be exhaustive; many applications overlap with those of genetic engineering more broadly, and the distinction between synthetic-biology applications and conventional genetic-engineering applications is often a matter of emphasis rather than of fundamental difference.

**Medicine.** Engineered cell therapies (CAR-T cells, engineered stem cells, engineered microbial therapies for the gut microbiome) are an established or emerging treatment modality for several disease classes. mRNA vaccines and therapeutics, developed using synthetic-biology methods across the past two decades, were deployed at planetary scale during the COVID-19 pandemic. Microbial production of pharmaceuticals — including artemisinin, opioids, and a growing list of complex molecules — has reorganised parts of the pharmaceutical supply chain. Engineered diagnostic devices and sensors are an active area of development.

**Agriculture and food.** Precision-fermentation production of dairy and egg proteins by engineered yeasts and other microbes has produced a growing alternative-protein industry. Engineered crops with designed metabolic pathways, beyond the simpler transgenic crops of earlier genetic engineering, are at various development stages. Engineered nitrogen-fixing crops — long discussed as a goal of synthetic biology — remain a research target with substantial agricultural and environmental implications.

**Industrial chemistry.** Engineered microbes produce an expanding range of industrial chemicals, biofuels, bioplastics, and materials. The replacement of petrochemical processes by fermentation-based processes using engineered microbes is a major commercial and environmental trajectory; the cost-competitiveness depends on the specific molecule but has been demonstrated for an increasing number of products.

**Environmental applications.** Engineered organisms for bioremediation — the breakdown of specific pollutants, the sequestration of heavy metals, the degradation of plastic waste — are at varying stages of development and deployment. Engineered microbes for carbon capture and conversion are an active research area.

**Foundational research.** Beyond commercial applications, synthetic biology has produced foundational research contributions across cell biology, developmental biology, evolutionary biology, and the broader study of how living systems work. The constructive methodology — building systems rather than only observing them — has revealed organisational principles of biological systems that pre-constructive methods had not surfaced.

## Limits and open questions

The field's limits and unresolved questions are worth registering, both for accuracy and because they bound any broader interpretation of the field's achievements.

- **Predictability.** Designed biological circuits remain substantially less predictable than designed electronic circuits. A given designed circuit, transferred from one host strain to another or from one laboratory to another, commonly exhibits behaviour different from what the original characterisation predicted. The cumulative work of the field has reduced but not eliminated this unpredictability.
- **Scale.** Most contemporary synthetic-biological design operates at the scale of small numbers of genes (typically less than ten) integrated into existing host organisms. The scaling of designed circuits to the level of hundreds or thousands of genes — the scale at which whole-organism design would become possible — has not been achieved.
- **Multicellular design.** The transition from designed single cells to designed multicellular organisms remains a major open problem. The Xenobot programme and the synthetic-developmental-biology field more broadly are early steps but remain far from the design of complete multicellular organisms from designed DNA.
- **The function of essential genes.** Even in the minimal synthetic cell (JCVI-syn3.0), approximately 30 percent of essential genes have functions that remain uncharacterised. A free-living organism whose every component is fully understood — the engineering-discipline standard — does not yet exist.
- **Resource competition and context-dependence.** Designed circuits interact unpredictably with their host cells' native metabolism, regulatory networks, and resource allocation. The development of *orthogonal* systems — designed circuits whose components do not interact with the host's native systems — is a major research direction but has not been fully achieved.
- **Biosafety and dual use.** The same techniques that permit the engineering of beneficial systems permit the engineering of dangerous ones. The 2002 poliovirus synthesis, the broader literature on potential dual-use research, and the policy debates around regulation, oversight, and the publication of dual-use research are an active and unresolved area of policy concern.
- **The philosophical status of designed life.** Whether designed biological systems are the same kind of thing as evolved biological systems, whether the engineering-discipline approach to biology will eventually erase the natural-evolved/designed distinction, and what the broader implications of the field are for the human relationship to the natural world are questions debated across the philosophy of biology, the ethics of technology, and the broader humanistic literature.

## In the Wheel of Heaven framework

The framework's interest in synthetic biology is treated at full length in the [life engineering](../life-engineering/) entry, where the broader convergence argument between contemporary terrestrial life-engineering capability and the source material's account of the Elohim's work is developed. The treatment below addresses what is specific to synthetic biology — the engineering-discipline character of the field, the parts-and-circuits paradigm, and the operational vocabulary the field has developed — and the ways in which these features specifically illuminate the framework's reading of the source material.

### The engineering-discipline epistemology

The framework's reading attends specifically to the *engineering-discipline epistemology* that distinguishes synthetic biology from earlier biological work. Where earlier genetic engineering was empirical — modify the genome, see what happens, optimise through trial and error — synthetic biology is constructive in a stronger sense: design from first principles, predict mathematically, build, test against prediction. This is the epistemology of an engineering discipline rather than of a natural-science discipline.

The source material's account of the Elohim's work uses the operational vocabulary of an engineering discipline. The Elohim are described as conducting their work in laboratories, with designs developed before construction, with results tested against design specifications, with optimisation through iterative refinement. This is the vocabulary that synthetic biology has, in the past two decades, developed for terrestrial biological design. The match between the source material's operational vocabulary and synthetic biology's engineering-discipline vocabulary is, on the framework's reading, evidence that the source material is describing the kind of work synthetic biology has now developed the capability to perform — at small scale, with the trajectory pointing toward larger scales.

### The parts-and-circuits paradigm

The framework reads the *parts-and-circuits paradigm* of synthetic biology as the contemporary terrestrial recovery of the conceptual approach the source material attributes to the Elohim. The Raëlian source material describes the Elohim's biological design as proceeding from components — molecular-level designs of specific genes, specific proteins, specific regulatory mechanisms — to integrated systems. The parts-and-circuits paradigm of synthetic biology proceeds in the same way: from standardised genetic parts (promoters, ribosome binding sites, coding sequences, terminators) through designed circuits (oscillators, switches, logic gates) to integrated metabolic and developmental systems.

The framework reads the convergence at the level of paradigm as significant. The source material did not describe the Elohim's work in vague terms (some kind of magical creation); it described the work in operational terms whose specific structure is the structure synthetic biology has now developed: components, circuits, integrated systems, designed for specified function, characterised against specified behaviour. The match between the source material's operational structure and synthetic biology's operational structure is one of the specific features the framework's reading attends to.

### The trajectory of the field

The framework reads the *trajectory* of synthetic biology — from designed circuits in 2000 through designed pathways in the mid-2000s through designed genomes in 2010 through designed multicellular systems in the early 2020s — as the developmental arc the source material's account predicts for any civilisation moving from pre-life-engineering to mature-life-engineering capability. The Elohim, on the source material's account, traversed this developmental arc themselves, from their initial laboratory cellular constructs to the species- and ecosystem-scale capability that produced the Earth project. The Elohim are not currently on the developmental arc but are at its mature endpoint; contemporary terrestrial synthetic biology is at the early end of the same arc. The framework treats the trajectory's direction as significant: not whether contemporary terrestrial capability matches the Elohim's capability (it does not), but whether it is moving toward such a capability and at what rate.

The structural implication is that synthetic biology is the field whose continued development the framework treats as the most direct empirical test of the source material's broader claims. If the field's trajectory continues forward — toward designed multicellular organisms, toward designed ecosystems, toward the species- and ecosystem-scale capability the source attributes to the Elohim — the framework reads this as continued vindication of the source material's account of where humanity is going. If the field's trajectory stalls — if designed multicellular life proves to be impossible, if the species-scale design barrier turns out to be insurmountable — the framework's reading would require substantial revision.

### Specific connections to source-material content

The Raëlian source material's account of the Elohim's early laboratory work — the period before the Earth project, when the Elohim's scientists were producing what the source calls primitive embryonic forms of life in laboratory conditions — corresponds, on the framework's reading, approximately to the contemporary state of synthetic biology. The minimal synthetic cell (JCVI-syn3.0, 2016) is a primitive, minimal cellular life-form constructed in laboratory conditions; the designed genetic circuits and metabolic pathways of synthetic biology are the kinds of constructs the source material would describe as the early outputs of an emerging life-engineering programme. The match between the source material's description of the Elohim's early state and the contemporary state of terrestrial synthetic biology is, on the framework's reading, the specific evidential signature the convergence argument depends on.

The treatment of the broader framework reading — the cosmic-chain account, the parallel-humanities account, the Earth-project account — lives in the dedicated entries on those topics. The synthetic-biology entry's contribution to the broader framework is the specific observation that the *methods* of contemporary synthetic biology match the *operational vocabulary* of the source material's account of biological design, and that this match is one of the structural features the framework's reading depends on.

## Comparative observations

The corpus's reading of synthetic biology sits within a broader landscape of how the field has been interpreted across different traditions of commentary. A brief survey clarifies the corpus's reading by contrast.

### The mainstream scientific reading

The mainstream scientific reading of synthetic biology treats the field as a contemporary engineering discipline with substantial scientific and commercial potential but without metaphysical or theological implications. The field is interpreted within the standard scientific worldview: living systems are products of evolution, the engineering of living systems is a contemporary human capability with practical implications, and the broader questions of meaning are not within the field's scope. This is the reading adopted by essentially all of the scientific literature on the field and is the framework against which any alternative reading must be measured.

The corpus's reading does not contest the mainstream scientific reading's accuracy at the level of empirical facts; the field is what the mainstream literature describes it as. What the corpus's reading contests is the interpretive frame within which those facts are placed. The corpus reads the contemporary emergence of synthetic biology as the present-day local instance of a capability the source material attributes to a non-terrestrial civilisation in deep antiquity; the mainstream scientific reading treats the contemporary emergence as the autonomous achievement of contemporary human science. The two readings are not necessarily contradictory at the level of empirical fact but are substantially different at the level of interpretive significance.

### The transhumanist and futurist readings

A substantial literature in the transhumanist and futurist traditions has interpreted synthetic biology, alongside artificial intelligence and other emerging technologies, as the early indication of a coming developmental phase in which human capability extends beyond current limits — into the engineering of biological systems, the modification of human biology itself, and eventually the construction of post-human forms of life. The transhumanist reading shares with the corpus's reading the interpretation of synthetic biology as more than a routine engineering discipline — as the beginning of something larger — but differs in the specific framework within which the development is placed.

### The bioconservative readings

Bioconservative readings — found across both religious and secular conservative traditions — have interpreted synthetic biology with concern about the human relationship to the natural world, the ethical status of designed life, and the broader implications of engineering biological systems. The bioconservative literature includes both religious arguments (synthetic biology as an inappropriate human appropriation of divine prerogatives) and secular arguments (synthetic biology as a transgression against the natural integrity of biological systems). The corpus's reading is partially aligned with the religious bioconservative reading — both treat the contemporary emergence of life-engineering capability as developmentally significant — but differs in the specific account of why and how. The religious bioconservative reading typically locates the divine creator in the supernatural realm; the corpus's reading locates the creator civilisation as a specific extraterrestrial biological civilisation. Where the bioconservative reading sometimes treats the contemporary emergence of life engineering as a transgression against the divine prerogative, the corpus's reading treats it as the development that brings humanity into the position the source material describes as the Elohim's own pre-Earth-project state — the developmental phase that precedes inheritance of the cosmic-chain pattern.

### The Sendy–Raëlian tradition

Within the specific Sendy–Raëlian interpretive tradition that the corpus reads as its principal scholarly antecedent, the framework's reading of synthetic biology is consistent with Sendy's broader reading and develops it forward. Sendy did not have the benefit of the subsequent fifty years of scientific development; his identification of the Elohim as biological engineers, working at the molecular level on the design and synthesis of organisms, was based on his philological-historiographic reading of the Hebrew Bible and on the comparative ancient-source literature. The subsequent development of synthetic biology vindicates Sendy's reading in the specific sense that the engineering-discipline biology he attributed to the Elohim has now been partially demonstrated by terrestrial human science. The framework reads this as the kind of vindication a philological reconstruction is positioned to receive from independent empirical development — a structural feature of the convergence argument the corpus develops.

## See also

- [Life engineering](../life-engineering/)
- [Genetic engineering](../genetic-engineering/)
- [Synthetic genomics](../synthetic-genomics/)
- [Xenobiology](../xenobiology/)
- [Genesis](../genesis/)
- [Elohim](../elohim/)
- [Tree of Life](../tree-of-life/)
- [Age of Aquarius](../timeline/age-of-aquarius/)
- [Apocalypse](../apocalypse/)
- [Cosmic Chain](../cosmic-chain/)
- [Jean Sendy](../jean-sendy/)
- [Raël](../rael/)
- [*Message from the Designers*](../library/message-from-the-designers/)

## References

Vorilhon, Claude (Raël). *The Book Which Tells the Truth* (1974) and *Extraterrestrials Took Me to Their Planet* (1976), collected as *Message from the Designers* (Raëlian Foundation, current English edition).

Sendy, Jean. *La Lune, clé de la Bible*. Julliard, 1968.

Sendy, Jean. *Ces dieux qui firent le ciel et la terre*. Robert Laffont, 1969. English: *Those Gods Who Made Heaven and Earth*. Berkley, 1972.

Ball, Philip. *How Life Works: A User's Guide to the New Biology*. Picador / University of Chicago Press, 2023.

Leduc, Stéphane. *La biologie synthétique*. A. Poinat, 1912.

Wiener, Norbert. *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press, 1948.

Jacob, François, and Jacques Monod. "Genetic Regulatory Mechanisms in the Synthesis of Proteins." *Journal of Molecular Biology* 3 (1961): 318–356. [The operon model.]

Elowitz, Michael B., and Stanislas Leibler. "A Synthetic Oscillatory Network of Transcriptional Regulators." *Nature* 403 (2000): 335–338. [The repressilator.]

Gardner, Timothy S., Charles R. Cantor, and James J. Collins. "Construction of a Genetic Toggle Switch in Escherichia coli." *Nature* 403 (2000): 339–342. [The toggle switch.]

Cello, Jeronimo, Aniko V. Paul, and Eckard Wimmer. "Chemical Synthesis of Poliovirus cDNA: Generation of Infectious Virus in the Absence of Natural Template." *Science* 297 (2002): 1016–1018.

Endy, Drew. "Foundations for Engineering Biology." *Nature* 438 (2005): 449–453.

Andrianantoandro, Ernesto, Subhayu Basu, David K. Karig, and Ron Weiss. "Synthetic Biology: New Engineering Rules for an Emerging Discipline." *Molecular Systems Biology* 2 (2006): 0028.

Ro, Dae-Kyun, et al. "Production of the Antimalarial Drug Precursor Artemisinic Acid in Engineered Yeast." *Nature* 440 (2006): 940–943. [Keasling group, artemisinin pathway.]

Gibson, Daniel G., et al. "Complete Chemical Synthesis, Assembly, and Cloning of a *Mycoplasma genitalium* Genome." *Science* 319 (2008): 1215–1220.

Gibson, Daniel G., et al. "Creation of a Bacterial Cell Controlled by a Chemically Synthesized Genome." *Science* 329 (2010): 52–56. [JCVI-syn1.0.]

Jinek, Martin, Krzysztof Chylinski, Ines Fonfara, Michael Hauer, Jennifer A. Doudna, and Emmanuelle Charpentier. "A Programmable Dual-RNA–Guided DNA Endonuclease in Adaptive Bacterial Immunity." *Science* 337 (2012): 816–821. [The CRISPR–Cas9 foundational paper.]

Hutchison, Clyde A., III, et al. "Design and Synthesis of a Minimal Bacterial Genome." *Science* 351 (2016): aad6253. [JCVI-syn3.0.]

Kriegman, Sam, Douglas Blackiston, Michael Levin, and Josh Bongard. "A Scalable Pipeline for Designing Reconfigurable Organisms." *Proceedings of the National Academy of Sciences* 117 (2020): 1853–1859. [The Xenobot work.]

Pelletier, James F., et al. "Genetic Requirements for Cell Division in a Genomically Minimal Cell." *Cell* 184 (2021): 2430–2440. [JCVI-syn3A.]

Jumper, John, et al. "Highly Accurate Protein Structure Prediction with AlphaFold." *Nature* 596 (2021): 583–589.

Watson, Joseph L., et al. "De Novo Design of Protein Structure and Function with RFdiffusion." *Nature* 620 (2023): 1089–1100.

Hanczyc, Martin M. "Engineering Life: A Review of Synthetic Biology." *Artificial Life* 26, no. 2 (2020): 260–273.

Cameron, D. Ewen, Caleb J. Bashor, and James J. Collins. "A Brief History of Synthetic Biology." *Nature Reviews Microbiology* 12 (2014): 381–390.

Royal Society. *Synthetic Biology: Scientific Discussion Meeting Report*. 2008.

National Academies of Sciences, Engineering, and Medicine. *Biodefense in the Age of Synthetic Biology*. National Academies Press, 2018.

J. Craig Venter Institute. "First Minimal Synthetic Bacterial Cell." <https://www.jcvi.org/research/first-minimal-synthetic-bacterial-cell>

National Human Genome Research Institute. "Synthetic Biology." <https://www.genome.gov/about-genomics/policy-issues/Synthetic-Biology>

iGEM Foundation. <https://igem.org>

Registry of Standard Biological Parts. <http://parts.igem.org>

"Synthetic biology." *Wikipedia*. <https://en.wikipedia.org/wiki/Synthetic_biology>

"BioBrick." *Wikipedia*. <https://en.wikipedia.org/wiki/BioBrick>

"iGEM." *Wikipedia*. <https://en.wikipedia.org/wiki/International_Genetically_Engineered_Machine>
