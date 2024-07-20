import os
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2
load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.0,        # Lower temperature reduces randomness
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
instruction = """"""

# def pdf_to_text(pdf_path):
#     text = ""
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
        
#         # Loop through each page
#         for page_num in range(len(reader.pages)):
#             page = reader.pages[page_num]
            
#             # Extract text from the page, handling cases where text extraction fails
#             try:
#                 text += page.extract_text()
#             except TypeError:
#                 # Handle TypeError exceptions if the page contains non-text elements
#                 pass
            
#     return text
# pdf_path = "D:\BIOPDF.pdf"
text="""Biology for Engineers 21BE45
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
"""


question = "list out the main topics in this text. {text}"
response = chat_session.send_message(instruction + question)