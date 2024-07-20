import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.1,        # Lower temperature reduces randomness
    "top_p": 1.0,              # Setting top_p to 1 disables nucleus sampling
    "top_k": 0,                # Setting top_k to 0 disables top-k sampling
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(history=[])
text = """Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 1
MODULE 1: CELL BASIC UNIT OF LIFE
BIOMOLECULES
Introduction: Biology is the study of all aspects of life. In many ways, the last 1000 years have
seen a meteoric rise in the study of biology as natural science. For a long time, biology was
thought to deal with only the classification of all known living organisms, animal behaviour, and
habitats. So, in short, biology is the detailed study of living organisms. This includes the genetic,
chemical, physical, ecological and evolutionary aspect of life.
Applications of Biology
Cell: A cell is the structural and fundamental unit of life. The study of cells from its basic
structure to the functions of every cell organelle is called Cell Biology. Robert Hooke was the first
Biologist who discovered cells. All organisms are made up of cells. They may be made up of a
single cell, or many cells. Mycoplasmas are the smallest known cells. Cells are the building
blocks of all living beings. They provide structure to the body and convert the nutrients taken
from the food into energy. Cells are complex and their components perform various functions in
an organism. They are of different shapes and sizes, pretty much like bricks of the buildings. Our
body is made up of cells of different shapes and sizes. From organism to organism, the count of
cells may vary. Humans have a greater number of cells compared to that of bacteria. Cells
comprise several cell organelles that perform specialized functions to carry out life processes.
Syllabus
1. Introduction. Structure and functions of a cell.
2. Stem cells and their application.
3. Biomolecules: Properties and functions of
I. Carbohydrates
II. Nucleic acids
III. Proteins
IV. Lipids
4. Importance of special biomolecules: Properties and functions of
I. Enzymes,
II. Vitamins and
III. Hormones
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 2
Structure of cell:
The cell structure comprises individual components with specific functions essential to carry out
life’s processes.
Cell Membrane:
The cell membrane supports and protects the cell. It controls the movement of substances in and
out of the cells. It separates the cell from the external environment. The cell membrane is the outer
covering of a cell within which all other organelles, such as the cytoplasm and nucleus, are
enclosed. It is also referred to as the plasma membrane. By structure, it is a porous membrane
(with pores) which permits the movement of selective substances in and out of the cell.
Cell Wall:
The cell wall is the most prominent part of the plant’s cell structure. It is made up of cellulose,
hemicellulose and pectin. It protects the plasma membrane and other cellular components. The
cell wall is also the outermost layer of plant cells. It is a rigid and stiff structure surrounding the
cell membrane. It provides shape and support to the cells and protects them from mechanical
shocks and injuries.
Cytoplasm:
The cytoplasm is a thick, clear, jelly-like substance present inside the cell membrane. Most of the
chemical reactions within a cell take place in this cytoplasm. The cell organelles such as
endoplasmic reticulum, vacuoles, mitochondria, ribosomes, are suspended in this cytoplasm.
Nucleus:
This is a spherical structured organelle found majorly at the centre of a cell surrounded by a
double-layered nuclear membrane separating it from the cytoplasm. The nucleus contains the
hereditary material of the cell, the DNA. It sends signals to the cells to grow, mature, divide and
die. The nucleus is surrounded by the nuclear envelope that separates the DNA from the rest of
the cell. The nucleus protects the DNA and is an integral component of a plant’s cell structure.
Cell Organelles:
Cells are composed of various cell organelles that perform certain specific functions to carry out
life’s processes. The different cell organelles, along with its principal functions, are as follows:
Nucleolus:
Nucleolus, spherical body within the nucleus of most eukaryotic cells, involved in the synthesis of
ribosomal RNA (rRNA) and the formation of ribosomes. The nucleolus contains the genes that
encode rRNA. Also, it is involved in controlling cellular activities and cellular reproduction.
Nuclear membrane:
Every nucleus is encircled and covered by a double-layered membrane, known as the nuclear
envelope or nuclear membrane. It separates the nucleoplasm (the fluid present in the nucleus),
from the cytoplasm.
Chromosomes:
Chromosomes are threadlike structures made of protein and a single molecule of DNA that serve
to carry the genomic information from cell to cell. In plants and animals (including humans),
chromosomes reside in the nucleus of cells. Chromosomes play a crucial role in determining the
sex of an individual. Each human cells contain 23 pairs of chromosomes.
Endoplasmic reticulum:
This is a continuous folded membranous organelle found in the cytoplasm made up of a thin
network of flattened interconnected compartments (sacs) that connects from the cytoplasm to the
cell nucleus. The endoplasmic reticulum is involved in the transportation of substances throughout
the cell. It plays a primary role in the metabolism of carbohydrates, synthesis of lipids, steroids
and proteins.
Golgi Bodies:
These are membrane-bound cell organelles found in the cytoplasm of a eukaryotic cell, next to the
endoplasmic reticulum and near the nucleus. Golgi bodies are supported together by cytoplasmic
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 3
microtubules and held by a protein matrix. Golgi bodies are called the cell’s post office as it is
involved in the transportation of materials within the cell.
Ribosomes:
These are small organelles majorly made up of 60% RNA cytoplasmic- granules and 40%
proteins. All living cells contain ribosomes, which may be freely circulating in the cytoplasm and
some are bound to the endoplasmic reticulum. It is the site for protein synthesis.
Mitochondria:
These are membrane-bound organelles located in the cytoplasm of all eukaryotic cells. The
number of mitochondria found in each cell varies widely depending on the function of the cell it
performs. The mitochondrion is called “the powerhouse of the cell.” It is called so because it
produces ATP the cell’s energy currency.
Lysosomes:
They are round subcellular organelle found in almost all eukaryotic cells. Lysosomes are very
acidic organelles containing the digestive enzymes and therefore each of the lysosomes is
surrounded by a membrane to protect it from the outer environment. Lysosomes protect the cell
by engulfing the foreign bodies entering the cell and help in cell renewal. Therefore, they are
known as the cell’s suicide bags.
Chloroplast:
A chloroplast is a type of organelle known as a plastid, predominantly found in plant cells and
algae. It is the site of photosynthesis, a process where light energy is converted into chemical
energy, fueling the organism’s activities. It contains the pigment called chlorophyll.
Vacuoles:
They are membrane-bound sacs found within the cell cytoplasm. The vacuole sac has a single
membrane surrounding it known as a tonoplast and this membrane resembles the plasma
membrane. Vacuoles store food, water, and other waste materials in the cell. They also remove
toxic substances and waste materials from the cell as a protection strategy.
Structure of Plant cell and Animal cell
Types of cells:
Cells are primarily classified into two types, namely Prokaryotic cells and Eukaryotic cells.
Prokaryotic cells have no nucleus. Instead, some prokaryotes such as bacteria have a region
within the cell where the genetic material is freely suspended. This region is called the nucleoid.
They all are single-celled microorganisms. Examples include archaea, bacteria, and cyanobacteria.
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 4
Eukaryotic cells are characterized by a true nucleus. This broad category involves plants, fungi,
protozoans, and animals. The plasma membrane is responsible for monitoring the transport of
nutrients and electrolytes in and out of the cells. There are some contrasting features between
plant and animal cells. For e.g., the plant cell contains chloroplast, central vacuoles, and other
plastids, whereas the animal cells do not.

Structure of Prokaryotic cell and Eukaryotic cell
Functions of cell:
A cell performs major functions essential for the growth and development of an organism.
1. Metabolism: Chemical processes that sustain life, including energy production,
biosynthesis of molecules and nutrient breakdown.
2. Protein synthesis: Involves transcription of DNA into mRNA in the nucleus, followed by
translation of mRNA into proteins on ribosomes.
3. Provides Support and Structure: The cell wall and the cell membrane provide support
and structure to the organism. For e.g., the skin is made up of a large number of cells.
Xylem present in the vascular plants provide structural support to the plants.
4. Facilitate Growth of Mitosis: In the process of mitosis, the parent cell divides into the
daughter cells I.e. multiply and facilitate the growth in an organism.
5. Allows Transport of Substances: Various nutrients are imported by the cells to carry out
various chemical processes going on inside the cells. The waste produced by the chemical
processes is eliminated from the cells by active and passive transport.
6. Energy Production: Cells require energy to carry out various chemical processes. This
energy is produced by the cells through a process called photosynthesis in plants and
respiration in animals.
7. Reproduction: Cells also helps in reproduction.
Stem cells and their application:
“Stem cells are special human cells that can develop into many different types of cells, from
muscle cells to brain cells.” Stem cells also have the ability to repair damaged cells. These cells
have strong healing power. They can evolve into any type of cell. Research on stem cells is going
on, and it is believed that stem cell therapies can cure ailments like paralysis and Alzheimer’s as
well. Let us have a detailed look at stem cells, their types and their functions.
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 5
Stem cells
Types of cells:
Stem cells are of the following different types
1. Embryonic Stem Cells: The fertilized egg begins to divide immediately. All the cells in the
young embryo are totipotent cells. These cells form a hollow structure within a few days. Cells
in one region group together to form the inner cell mass. This contains pluripotent cells that
make up the developing foetus. The embryonic stem cells can be further classified as:
a. Totipotent Stem Cells: These can differentiate into all possible types of stem cells.
b. Pluripotent Stem Cells: These are the cells from an early embryo and can differentiate
into any cell type.
c. Multipotent Stem Cells: These differentiate into a closely related cell type. E.g., the
hematopoietic stem cells differentiate into red blood cells and white blood cells.
d. Oligopotent Stem Cells: Adult lymphoid or myeloid cells are oligopotent. They can
differentiate into a few different types of cells
e. Unipotent Stem Cells: They can produce cells only of their own type. Since they have the
ability to renew themselves, they are known as unipotent stem cells. E.g., Muscle stem
cells.
2. Adult Stem Cells: These stem cells are obtained from developed organs and tissues. They can
repair and replace the damaged tissues in the region where they are located. For eg.,
hematopoietic stem cells are found in the bone marrow. These stem cells are used in bone
marrow transplants to treat specific types of cancers.
3. Induced Pluripotent Stem Cells: These cells have been tested and arranged by converting
tissue-specific cells into embryonic cells in the lab. These cells are accepted as an important
tool to learn about the normal development, onset and progression of the disease and are also
helpful in testing various drugs. These stem cells share the same characteristics as embryonic
cells do. They also have the potential to give rise to all the different types of cells in the human
body.
4. Mesenchymal stem cells: These cells are mainly formed from the connective tissues
surrounding other tissues and organs, known as the stroma. These mesenchymal stem cells are
accurately called stromal cells. The first mesenchymal stem cells were found in the bone
marrow that is capable of developing bones, fat cells, and cartilage.
Applications of Stem Cells:
Following are the important applications of stem cells:
1. Tissue Regeneration:
This is the most important application of stem cells. The stem cells can be used to grow a
specific type of tissue or organ. This can be helpful in kidney and liver transplants. The doctors
have already used the stem cells from beneath the epidermis to develop skin tissue that can
repair severe burns or other injuries by tissue grafting.
2. Treatment of Cardiovascular Disease:
A team of researchers have developed blood vessels in mice using human stem cells. Within
two weeks of implantation, the blood vessels formed their network and were as efficient as the
natural vessels.
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 6
3. Treatment of Brain Diseases:
Stem cells can also treat diseases such as Parkinson’s disease and Alzheimer’s. These can help
to replenish the damaged brain cells. Researchers have tried to differentiate embryonic stem
cells into these types of cells and make it possible to treat diseases.
4. Blood Disease Treatment:
The adult hematopoietic stem cells are used to treat cancers, sickle cell anaemia, and other
immunodeficiency diseases. These stem cells can be used to produce red blood cells and white
blood cells in the body.
Biomolecules:
Biomolecules are the most essential organic molecules, which are found in living organisms and
involved in the maintenance and metabolic processes of living organisms. Biomolecules are the
building blocks of life and perform important functions in living organisms. Biomolecules have a
wide range of sizes and structures.
Examples; Carbohydrates, Proteins, Nucleic acids and Lipids, Enzymes, Vitamins, Hormones.
Biomolecules
Carbohydrates:
Introduction: Carbohydrates are macronutrients and are one of the three main ways by which our
body obtains its energy. They are called carbohydrates as they
contain carbon, hydrogen and oxygen at their chemical level. Carbohydrates are essential
nutrients which include sugars, fibers and starches. They are found in grains, vegetables, fruits
and in milk and other dairy products. They are the basic food groups which play an important role
in a healthy life.
Carbohydrates are chemically defined as polyhydroxy aldehydes or ketones or compounds which
produce them on hydrolysis. They are collectively called as saccharides (Greek: sakcharon =
sugar). Depending on the number of constituting sugar units obtained upon hydrolysis, they are
classified as monosaccharides (1 unit), oligosaccharides (2-10 units) and polysaccharides (more
than 10 units). They have multiple functions’ viz. they’re the most abundant dietary source of
energy; they are structurally very important for many living organisms as they form a major
structural component, e.g. Cellulose is an important structural fibre for plants.
Properties of Carbohydrates:
1. Stereoisomerism: Compound shaving the same structural formula but they differ in spatial
configuration. Example: Glucose has two isomers with respect to the penultimate carbon atom.
They are D-glucose and L-glucose.
2. Optical Activity: It is the rotation of plane-polarized light forming (+) glucose and (-) glucose.
3. Diastereo isomers: It the configurational changes with regard to C2, C3, or C4 in glucose.
Example: Mannose, galactose.
4. Annomerism: It is the spatial configuration with respect to the first carbon atom in aldoses and
the second carbon atom in ketoses.
5. Osazone formation: Osazone are carbohydrate derivatives when sugars are reacted with an
excess of phenylhydrazine. e.g. Glucosazone
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 7
6. Benedict’s test: Reducing sugars when heated in the presence of an alkali gets converted to
powerful reducing species known as enediols. When Benedict’s reagent solution and reducing
sugars are heated together, the solution changes its color to orange-red/ brick red.
7. Oxidation: Monosaccharides are reducing sugars if their carbonyl groups oxidize to give
carboxylic acids. In Benedict’s test, D-glucose is oxidized to D-gluconic acid thus, glucose is
considered a reducing sugar.
8. Reduction to alcohols: The C=O groups in open-chain forms of carbohydrates can be reduced
to alcohols by sodium borohydride, NaBH4, or catalytic hydrogenation (H2, Ni, EtOH/H2O).
The products are known as “alditols”.
Functions of Carbohydrates:
Carbohydrates are widely distributed molecules in plant and animal tissues. In plants and
arthropods, carbohydrates from the skeletal structures, they also serve as food reserves in plants
and animals. They are important energy sources required for various metabolic activities; the
energy is derived by oxidation.
Some of their major functions include
1. Carbohydrates are helpful in performing many functions such as breakdown of protein
molecules, dehydration as well as eliminating ketosis.
2. Carbohydrates serve as primary energy sources.
3. Carbohydrates provide energy.
4. Carbohydrates help in the regulation of blood glucose.
5. Carbohydrates provide the carbon skeleton for the synthesis of some non-essential amino
acids. Carbohydrates are intermediates in the biosynthesis of fats and proteins.
6. Carbohydrates aid in the regulation of nerve tissue and is the energy source for the brain.
7. Carbohydrates get associated with lipids and proteins to form surface antigens, receptor
molecules, vitamins, and antibiotics.
8. Formation of the structural framework of RNA and DNA (ribonucleic acid and
deoxyribonucleic acid).
9. Carbohydrates that are rich in fiber content help to prevent constipation.
Nucleic acids:
Introduction: Nucleic acids are long-chain polymeric molecules, the monomer (the repeating
unit) is known as the nucleotides and hence sometimes nucleic acids are referred to as
polynucleotides. Deoxyribonucleic acid (DNA) and ribonucleic acid (RNA) are two major types
of nucleic acids. DNA and RNA are responsible for the inheritance and transmission of specific
characteristics from one generation to the other. There are prominently two types of nucleic acids
known to us.
Nucleic acids
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 8
Properties of Nucleic acids:
1. The basic nucleic acid structure is similar to a chain of molecules composed of identical series
of nucleotides.
2. Single nucleotide, the base property of nucleic acid, comprises a nitrogen-containing fragrant
base affixed to a five-carbon sugar connected to a phosphate group.
3. Every nucleic acid encompasses four of five possible nitrogen-containing bases, which are,
uracil (U), adenine (A), thymine (T), guanine (G), and cytosine (C).
4. Among these nitrogen-containing bases, C, U, and T are classified as pyrimidines and A and G
are classified as purines.
5. An artificially synthesized polymer is also named Peptide Nucleic Acid (PNA), similar to DNA
or RNA. Peptide Nucleic Acid might be similar to DNA and RNA. Its function varies from that
of both.
6. Generally, all nucleic acids contain the bases G, A, and C. But T is specifically found in DNA
while U is in RNA.
Functions of Nucleic acids:
The basic function of nucleic acid is mentioned below:
1. Stores Information: These acids are responsible for both carrying and transmitting
information in the human body. Both copying and reading the information stored in DNA
relies on base pairing between two nucleic acids.
2. Protects Information: Apart from storing these molecules, it also protects the transmitted
information. It protects the information from being lost by storing in a safer place.
3. Determination of inherited characteristics: These acids are responsible for DNA in a human
being and eventually determines their inherited characteristics from one generation to another.
4. DNA fingerprinting: It is a method used by forensic experts to determine paternity. It is also
used for the identification of criminals.
5. In research: It has also played a major role in studies regarding biological evolution and
genetics.
Proteins:
Introduction: Proteins are macromolecules made up of monomers called amino acids. Amino
acids are the building block of all proteins. An amino acid is a simple organic compound
consisting of a basic group (-NH2), an acidic group (-COOH), and an organic R group that is
unique to each amino acid. The term amino acid is short for alpha-amino carboxylic acid. Each
molecule has a central carbon atom, called the α-carbon to which both the groups are attached.
The remaining two bonds for the central carbon are satisfied by the hydrogen atom and an organic
R group. The organic R group can be as simple as a hydrogen atom (H) or a methyl group (- CH3)
or a more sophisticated group. Thus, the α -carbon in all the amino acids is asymmetric except in
glycine where the α -carbon is symmetric with a hydrogen atom as an R group. Because of this
asymmetry, the amino acids (except glycine) exist in two optically active forms: those having -
NH2 group to the right are designated as Dforms, and those having -NH2 group to the left
as L-forms. The property to exist in two
optically different forms is termed as chirality.
Amino acids are amphoteric compounds with
both acidic and alkaline groups. These also
always exist as ions except at the isoelectric
point.
 Empirical structure of amino acids
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 9
Properties of Proteins:
1. Solubility in water: The relationship of proteins with water is complex. The secondary
structure of proteins depends largely on the interaction of peptide bonds with water through
hydrogen bonds. Hydrogen bonds are also formed between protein (alpha and beta structures)
and water. The protein-rich static ball is more soluble than the helical structures. At the tertiary
structure, water causes the orientation of the chains and hydrophilic radicals to the outside of
the molecule, while the hydrophobic chains and radicals tend to react with each other within
the molecule (hydrophobic effect).
2. Denaturation: Partial or complete unfolding of the native (natural) conformation of the
polypeptide chain is known as denaturation. This is caused by heat, acids, alkalies, alcohol,
acetone, urea, beta- mercaptoethanol.
3. Coagulation: When proteins are denatured by heat, they form insoluble aggregates known as
coagulum. All the proteins are not heat coagulable, only a few like the albumins, globulins are
heat coagulable.
4. Isoelectric pH (pH): The pH at which a protein has equal number of positive and negative
charges is known as isoelectric pH. When subjected to an electric field the proteins do not
move either towards anode or cathode, hence this property is used to isolate proteins.
5. Molecular Weights of Proteins: Different proteins have different amino acid composition and
hence their molecular weights differ. The average molecular weight of an amino acid is taken
to be 110. The total number of amino acids in a protein multiplied by 110 gives the
approximate molecular weight of that protein.
Functions of Proteins:
1. Digestion: The digestive enzymes, which are primarily proteinaceous in origin, carry out
digestion.
2. Movement: Muscles include a protein called myosin, which helps muscles contract, allowing
for movement.
3. Structure and Support: The structural protein known as keratin is what gives humans and
other animals hair, nails, and horns.
4. Cellular communication: Through receptors on their surface, cells can communicate with
other cells and the outside world. These receptors are made of proteins.
5. Act as a messenger: These proteins serve as chemical messengers that facilitate
communication among cells, tissues, and organs.
Lipids:
Introduction: “Lipids are organic compounds that contain hydrogen, carbon and oxygen atoms,
which form the framework for the structure and function of living cells.” These organic
compounds are nonpolar molecules, which are soluble only in nonpolar solvents and insoluble in
water because water is a polar molecule. In the human body, these molecules can be synthesized
in the liver and are found in oil, butter, whole milk, cheese, fried foods and also in some red
meats. Lipids are the polymers of fatty acids that contain a long, non-polar hydrocarbon chain
with a small polar region containing oxygen.
Lipid bilayer structure
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 10
Properties of Lipids:
1. Lipids are oily or greasy nonpolar molecules, stored in the adipose tissue of the body.
2. Lipids are a heterogeneous group of compounds, mainly composed of hydrocarbon chains.
3. Lipids are energy-rich organic molecules, which provide energy for different life processes.
4. Lipids are a class of compounds characterized by their solubility in nonpolar solvents and
insolubility in water.
5. Lipids are significant in biological systems as they form a mechanical barrier dividing a cell
from the external environment known as the cell membrane.
6. Lipids are generally hydrophobic, meaning they repel water and do not dissolve in it.
Functions of Lipids:
1. Lipids, like adipose tissue, act as insulators and help to maintain body temperature by reducing
heat loss.
2. Lipids, especially triglycerides, act as energy storage in organisms, providing a reserve of
metabolic fuel.
3. Lipids protect the plant leaves from direct heat and drying.
4. Steroid hormones, derived from cholesterol, play vital roles in regulating various physiological
processes, including metabolism, growth, and reproduction.
5. In plants, lipids can be stored as oils in seeds, providing a source of energy for germination and
early growth.
6. Lipids form waterproofing structures, such as the waxy cuticle on plant leaves or the oil on the
feathers of water birds.
7. It provides color to many fruits and vegetables with the presence of carotenoid pigment.
8. Lipids serve as signalling molecules; They are catalysts of electrical impulse activity within the
brain. Nerve response in myelinated neurons (right) propagate faster than in unmyelinated
neurons (left). Myelin is a mixture of proteins and phospholipids that insulates nerves. The
myelin coating is ~70% lipids.
Enzymes:
Introduction: “Enzymes can be defined as biological polymers that catalyse biochemical
reactions.” The majority of enzymes are proteins with catalytic capabilities crucial to perform
different processes. Metabolic processes and other chemical reactions in the cell are carried out by
a set of enzymes that are necessary to sustain life. The initial stage of metabolic process depends
upon the enzymes, which react with a molecule and is called the substrate. Enzymes convert the
substrates into other distinct molecules, which are known as products. Enzymes are found in all
tissues and fluids of the body.
Enzyme action
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 11
Properties of Enzymes:
1. Enzymes are complex macromolecules with high molecular weight.
2. They catalyse biochemical reactions in a cell.
3. They help in the breakdown of large molecules into smaller molecules or bring together two
smaller molecules to form a larger molecule.
4. Enzymes do not start a reaction. However, they help in accelerating it.
5. Enzymes affect the rate of biochemical reaction and not the direction.
6. Most of the enzymes have a high turnover number. Turnover number of an enzyme is the
number of molecules of a substance that is acted upon by an enzyme per minute.
7. High turnover number of enzymes increases the efficiency of the reaction.
8. Enzymatic activity decreases with increase in temperature.
9. They show maximum activity at an optimum pH of 6 – 8.
Functions of Enzymes:
1. Enzymes like kinases & phosphatases are important for cell regulation & signal transmission.
2. The activation and inhibition of enzymes resulting in a negative feedback mechanism adjust
the rate of synthesis of intermediate metabolites.
3. They catalyse post-translational modifications involving phosphorylation, glycosylation, and
cleavage of the polypeptide chain.
4. Some enzymes are also involved in the regulation of enzyme levels by changing the rate of
enzyme degradation.
5. Since a tight regulation of enzymes is essential for homeostasis, any changes in the enzyme
structure and production might result in diseases.
6. Enzymes synthesized in various organisms are also utilized in various industries for wine
production, cheese production, bread whitening, and designing fabrics.
Vitamins:
Introduction: Vitamins are chemical compounds that are required in small amounts with our
regular diet in order to carry out certain biological functions and for the maintenance of our
growth. There are 13 essential vitamins. This means that these vitamins are required for the body
to work properly. Vitamins are generally classified as water-soluble vitamins and fat-soluble
vitamins.
1. Fat-Soluble Vitamins:
Vitamin A, D, E and K are fat-soluble. These are stored in adipose tissues and hence are called
fat-soluble vitamins.
2. Water-Soluble Vitamins:
Vitamins in B-group and vitamin C are water-soluble and cannot be stored in our bodies as they
pass with the water in urine. These vitamins must be supplied to our bodies with regular diets.
Molecular structure of vitamin C
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 12
Properties of Vitamins:
1. The vitamins are organic, low molecular weight substances that have key roles in metabolism.
2. Few are single substances; most are families of chemically-related substances sharing
biological activities.
3. The vitamers comprising a vitamin family may vary in biopotency.
4. Otherwise, vitamin families are chemically heterogeneous; therefore, it is convenient to
classify the vitamins according to their physical properties.
5. Some vitamins are fat-soluble; the others are water-soluble.
6. The water-soluble vitamins (C, thiamin, riboflavin, pyridoxine, biotin, pantothenic acid, folate,
B12) tend to have one or more polar or ionizable groups, whereas the fat-soluble vitamins (A,
D, E, and K) have predominantly aromatic and aliphatic characters.
7. These traits determine the nature of their absorption, transport, tissue distribution, and
metabolic function. Vitamins function as antioxidants, affectors of gene transcription, H + / e −
donors/acceptors, hormones, and coenzymes.
Functions of Vitamins:
Each of the vitamins listed below has an important job in the body. A vitamin deficiency occurs
when you do not get enough of a certain vitamin. Vitamin deficiency can cause health problems.
1. Vitamin B6 is also called pyridoxine. Vitamin B6 helps form red blood cells and maintain
brain function. This vitamin also plays an important role in the proteins that are part of many
chemical reactions in the body. The more protein you eat the more pyridoxine your body
requires.
2. Vitamin B12, like the other B vitamins, is important for metabolism. It also helps form red
blood cells and maintain the central and peripheral nervous systems.
3. Vitamin C, also called ascorbic acid, is an antioxidant that promotes healthy teeth and gums. It
helps the body absorb iron and maintain healthy tissue. It is also essential for wound healing.
4. Vitamin D is also known as the "sunshine vitamin," since it is made by the body after being in
the sun. Ten to 15 minutes of sunshine 3 times a week is enough to produce the body's
requirement of vitamin D for most people at most latitudes.
5. Vitamin E is an antioxidant also known as tocopherol. It helps the body form red blood cells
and use vitamin K.
6. Vitamin K is needed because without it blood would not coagulate normally. Some studies
suggest that it is important for bone health.
7. Niacin is a B vitamin that helps maintain healthy skin and nerves. It also has triglyceridelowering effects at higher doses.
Hormones:
Introduction: These are chemicals that coordinate different functions in your body by carrying
messages through your blood to our organs, skin, muscles and other tissues. These signals tell our
body what to do and when to do it. Hormones are essential for life. As stated above, hormones are
chemicals that essentially function as messengers. These chemicals are secreted by special glands
known as the endocrine glands. These endocrine glands are distributed throughout the body.
These messengers control many physiological functions as well as psychological health. They are
also quite important in maintaining homeostasis in the body.
Properties of Hormones:
➢ The significant properties of hormones are –
➢ They have a low molecular weight; thus, they can easily pass through capillaries.
➢ Hormones always act in low concentration.
Biology for Engineers 21BE45
Department of Chemistry, Sai Vidya Institute of Technology Page 13
➢ They are soluble in water so that they can be transported via blood.
➢ The importance of hormones is that they are non-antigenic.
➢ They are organic catalysts. Hormones act as coenzymes of other enzymes in the human body.
➢ Hormones, in their first action, cause a limited number of reactions and do not influence any
metabolic activities of a cell directly.
➢ A significant characteristic of hormones is that, after their function is over, they are readily
destroyed, excreted or inactivated.
➢ Hormonal activities are not hereditary.
Functions of Hormones:
different hormones have different functions.
Hormones are created by glands, which are part of the endocrine system. The main hormoneproducing glands are:
1. Hypothalamus: The hypothalamus is responsible for body temperature, hunger, moods and
the release of hormones from other glands; and also controls thirst, sleep and sex drive.
2. Parathyroid: This gland controls the amount of calcium in the body.
3. Thymus: This gland plays a role in the function of the adaptive immune system and the
maturity of the thymus, and produces T-cells.
4. Pancreas: This gland produces the insulin that helps control blood sugar levels.
5. Thyroid: The thyroid produces hormones associated with calorie burning and heart rate.
6. Adrenal: Adrenal glands produce the hormones that control sex drive and cortisol, the stress
hormone.
7. Pituitary: Considered the "master control gland," the pituitary gland controls other glands
and makes the hormones that trigger growth.
8. Pineal: Also called the thalamus, this gland produces serotonin derivatives of melatonin,
which affects sleep.
9. Ovaries: Only in women, the ovaries secrete estrogen, testosterone and progesterone, the
female sex hormones.
10. Testes: Only in men, the testes produce the male sex hormone, testosterone, and produce
sperm.
Important questions
1. Explain any five cell organelles.
2. Explain the functions of a cell.
3. Explain differences between Prokaryotic cells and Eukaryotic cells.
4. What are stem cells? Explain any four functions of stem cells.
5. Explain the any five functions of Proteins.
6. What are lipids? Explain any five properties of Lipids.
7. What are Carbohydrates? Explain the properties of Carbohydrates.
8. Explain any five functions of Vitamins.
9. What are Hormones? Explain the properties of Hormones.
10. What are biomolecules? Mention the properties of Nucleic acids.
What are enzymes? Explain the functions of Enzymes.
"""



question = """
list down the inmportant concepts mentioned in this text in the below format.
Make sure that you don't repeat the topics/concepts twice or more.
1. Tom
2. Jerry
3. Bob
without any additional text
"""
response = chat_session.send_message(text + question)
print(f"{response.text}")