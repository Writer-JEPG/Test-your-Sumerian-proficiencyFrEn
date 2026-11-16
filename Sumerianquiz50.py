
import streamlit as st

st.set_page_config(
    page_title="Sumerian Knowledge Quiz",
    page_icon="𒀭",
    layout="wide"
)

# ---------------------------------------------------------
# LANGUAGE SETTINGS
# ---------------------------------------------------------

translations = {
    "English": {
        "title": "𒀭 Sumerian Knowledge Quiz",
        "subtitle": "Test your knowledge of the Sumerian language, cuneiform writing and civilization.",
        "language": "Select your language",
        "instructions": "Answer the 50 questions below. Select one answer for each question, then submit your quiz.",
        "question": "Question",
        "submit": "Submit Quiz",
        "score": "Your Score",
        "excellent": "Excellent! You have an outstanding knowledge of Sumerian.",
        "very_good": "Very good! You have a solid understanding of Sumerian.",
        "good": "Good effort! Keep studying and improving your knowledge.",
        "keep_learning": "Keep learning! There is much more to discover about Sumerian.",
        "correct": "Correct answer",
        "your_answer": "Your answer",
        "explanation": "Explanation",
        "result": "Quiz Results",
        "restart": "Restart Quiz",
        "not_answered": "Not answered",
        "all_questions": "Total questions",
        "percentage": "Percentage",
        "creator": "Created by Rami Ibrahim",
        "sources": "Recommended academic resources",
        "source_intro": "These resources can help you verify Sumerian words, signs and readings.",
        "footer": "Sumerian language and cuneiform knowledge quiz"
    },
    "Français": {
        "title": "𒀭 Quiz de connaissances sur le sumérien",
        "subtitle": "Testez vos connaissances de la langue sumérienne, de l’écriture cunéiforme et de la civilisation sumérienne.",
        "language": "Choisissez votre langue",
        "instructions": "Répondez aux 50 questions ci-dessous. Sélectionnez une réponse pour chaque question, puis soumettez votre quiz.",
        "question": "Question",
        "submit": "Soumettre le quiz",
        "score": "Votre score",
        "excellent": "Excellent ! Vous avez une connaissance remarquable du sumérien.",
        "very_good": "Très bien ! Vous avez une bonne maîtrise des connaissances sur le sumérien.",
        "good": "Bon travail ! Continuez à approfondir vos connaissances.",
        "keep_learning": "Continuez à apprendre ! Il reste beaucoup à découvrir sur le sumérien.",
        "correct": "Bonne réponse",
        "your_answer": "Votre réponse",
        "explanation": "Explication",
        "result": "Résultats du quiz",
        "restart": "Recommencer le quiz",
        "not_answered": "Sans réponse",
        "all_questions": "Nombre total de questions",
        "percentage": "Pourcentage",
        "creator": "Créé par Rami Ibrahim",
        "sources": "Ressources académiques recommandées",
        "source_intro": "Ces ressources permettent de vérifier les mots, les signes et les lectures du sumérien.",
        "footer": "Quiz de connaissances sur la langue sumérienne et l’écriture cunéiforme"
    }
}

# ---------------------------------------------------------
# QUESTION BANK
# Format:
# (English question, French question,
#  English options, French options,
#  correct answer index,
#  English explanation, French explanation)
# ---------------------------------------------------------

questions = [

(
"What does the Sumerian word DINGIR generally mean?",
"Que signifie généralement le mot sumérien DINGIR ?",
["God or deity", "King", "Temple", "Water"],
["Dieu ou divinité", "Roi", "Temple", "Eau"],
0,
"DINGIR is the Sumerian word for a god or deity. It can also function as a divine determinative in writing.",
"DINGIR désigne un dieu ou une divinité. Il peut également fonctionner comme déterminatif divin dans l’écriture."
),

(
"Which cuneiform sign represents AN?",
"Quel signe cunéiforme représente AN ?",
["𒀭", "𒈗", "𒌓", "𒆳"],
["𒀭", "𒈗", "𒌓", "𒆳"],
0,
"The sign 𒀭 is read AN and is associated with heaven and the god An.",
"Le signe 𒀭 se lit AN et est associé au ciel et au dieu An."
),

(
"What does É mean in Sumerian?",
"Que signifie É en sumérien ?",
["House or temple", "Mountain", "Field", "River"],
["Maison ou temple", "Montagne", "Champ", "Rivière"],
0,
"É means house or temple in Sumerian.",
"É signifie maison ou temple en sumérien."
),

(
"Which sign represents LUGAL?",
"Quel signe représente LUGAL ?",
["𒈗", "𒊩", "𒌉", "𒅗"],
["𒈗", "𒊩", "𒌉", "𒅗"],
0,
"The cuneiform sign 𒈗 is read LUGAL, meaning king.",
"Le signe cunéiforme 𒈗 se lit LUGAL, qui signifie roi."
),

(
"What is a common meaning of KI?",
"Quel est un sens courant de KI ?",
["Earth or place", "Water", "Fire", "King"],
["Terre ou lieu", "Eau", "Feu", "Roi"],
0,
"KI commonly means earth, ground or place, depending on context.",
"KI signifie couramment terre, sol ou lieu, selon le contexte."
),

(
"Which cuneiform sign represents UD?",
"Quel signe cunéiforme représente UD ?",
["𒌓", "𒀀", "𒄑", "𒈬"],
["𒌓", "𒀀", "𒄑", "𒈬"],
0,
"The sign 𒌓 has the reading UD and is associated with day or sunlight.",
"Le signe 𒌓 possède notamment la lecture UD et est associé au jour ou à la lumière solaire."
),

(
"What does LUGAL mean?",
"Que signifie LUGAL ?",
["King", "Queen", "Priest", "Scribe"],
["Roi", "Reine", "Prêtre", "Scribe"],
0,
"LUGAL is the Sumerian word for king.",
"LUGAL est le mot sumérien désignant le roi."
),

(
"Which cuneiform sign represents A?",
"Quel signe cunéiforme représente A ?",
["𒀀", "𒀭", "𒈗", "𒆳"],
["𒀀", "𒀭", "𒈗", "𒆳"],
0,
"The sign 𒀀 is commonly read A and can represent water in appropriate contexts.",
"Le signe 𒀀 se lit couramment A et peut représenter l’eau dans certains contextes."
),

(
"What does AMA mean?",
"Que signifie AMA ?",
["Mother", "Father", "Son", "Daughter"],
["Mère", "Père", "Fils", "Fille"],
0,
"AMA is the Sumerian word for mother.",
"AMA est le mot sumérien pour mère."
),

(
"Which sign represents DUMU?",
"Quel signe représente DUMU ?",
["𒌉", "𒊩", "𒅗", "𒄑"],
["𒌉", "𒊩", "𒅗", "𒄑"],
0,
"The sign 𒌉 is read DUMU and means child or son in many contexts.",
"Le signe 𒌉 se lit DUMU et signifie enfant ou fils dans de nombreux contextes."
),

(
"What does MUNUS mean?",
"Que signifie MUNUS ?",
["Woman or female", "Man or male", "Child", "God"],
["Femme ou féminin", "Homme ou masculin", "Enfant", "Dieu"],
0,
"MUNUS is a Sumerian word and sign associated with woman or the female gender.",
"MUNUS est un mot et un signe sumériens associés à la femme ou au féminin."
),

(
"Which sign is commonly read MUNUS?",
"Quel signe se lit couramment MUNUS ?",
["𒊩", "𒈗", "𒌓", "𒀀"],
["𒊩", "𒈗", "𒌓", "𒀀"],
0,
"The sign 𒊩 is read MUNUS and is associated with woman or female.",
"Le signe 𒊩 se lit MUNUS et est associé à la femme ou au féminin."
),

(
"What is the Unicode name of the cuneiform character 𒐕?",
"Quel est le nom Unicode du caractère cunéiforme 𒐕 ?",
["ONE GESH2", "ONE DISH", "TWO GESH2", "THREE DISH"],
["ONE GESH2", "ONE DISH", "TWO GESH2", "THREE DISH"],
0,
"The Unicode character U+12415 is named CUNEIFORM NUMERIC SIGN ONE GESH2.",
"Le caractère Unicode U+12415 porte le nom CUNEIFORM NUMERIC SIGN ONE GESH2."
),

(
"Which readings are associated with the signs in 𒀭𒈗, when read separately?",
"Quelles lectures sont associées aux signes de 𒀭𒈗, lorsqu’ils sont lus séparément ?",
["AN and LUGAL", "KI and UD", "A and AMA", "DUMU and MUNUS"],
["AN et LUGAL", "KI et UD", "A et AMA", "DUMU et MUNUS"],
0,
"The first sign is AN and the second is LUGAL.",
"Le premier signe est AN et le second est LUGAL."
),

(
"Which writing system was used to record Sumerian?",
"Quel système d’écriture était utilisé pour noter le sumérien ?",
["Cuneiform", "Hieroglyphic alphabet", "Latin alphabet", "Greek alphabet"],
["L’écriture cunéiforme", "L’alphabet hiéroglyphique", "L’alphabet latin", "L’alphabet grec"],
0,
"Sumerian was written using cuneiform, a writing system developed in ancient Mesopotamia.",
"Le sumérien était écrit en cunéiforme, un système d’écriture développé dans l’ancienne Mésopotamie."
),

(
"What can KUR mean in Sumerian?",
"Que peut signifier KUR en sumérien ?",
["Mountain or land", "Water or river", "House or temple", "Mother or woman"],
["Montagne ou pays", "Eau ou rivière", "Maison ou temple", "Mère ou femme"],
0,
"KUR can mean mountain, land or foreign country, depending on context.",
"KUR peut signifier montagne, pays ou territoire étranger, selon le contexte."
),

(
"Which sign represents KUR?",
"Quel signe représente KUR ?",
["𒆳", "𒀭", "𒅗", "𒌉"],
["𒆳", "𒀭", "𒅗", "𒌉"],
0,
"The cuneiform sign 𒆳 is commonly read KUR.",
"Le signe cunéiforme 𒆳 se lit couramment KUR."
),

(
"What does GIS commonly refer to?",
"À quoi GIS fait-il généralement référence ?",
["Tree or wood", "Water", "Sky", "King"],
["Arbre ou bois", "Eau", "Ciel", "Roi"],
0,
"GIS is associated with tree or wood and also appears in the writing of words related to wooden objects.",
"GIS est associé à l’arbre ou au bois et apparaît également dans l’écriture de mots liés aux objets en bois."
),

(
"Which sign is commonly read GIS?",
"Quel signe se lit couramment GIS ?",
["𒄑", "𒈗", "𒌓", "𒈬"],
["𒄑", "𒈗", "𒌓", "𒈬"],
0,
"The sign 𒄑 is commonly read GIS and is associated with wood.",
"Le signe 𒄑 se lit couramment GIS et est associé au bois."
),

(
"What does KA mean?",
"Que signifie KA ?",
["Mouth", "Hand", "Foot", "Eye"],
["Bouche", "Main", "Pied", "Œil"],
0,
"KA is the Sumerian word for mouth.",
"KA est le mot sumérien pour bouche."
),

(
"Which sign represents KA?",
"Quel signe représente KA ?",
["𒅗", "𒊩", "𒆳", "𒀀"],
["𒅗", "𒊩", "𒆳", "𒀀"],
0,
"The cuneiform sign 𒅗 is read KA.",
"Le signe cunéiforme 𒅗 se lit KA."
),

(
"What does MU commonly mean?",
"Que signifie couramment MU ?",
["Name", "Mountain", "House", "Woman"],
["Nom", "Montagne", "Maison", "Femme"],
0,
"MU commonly means name, although the sign has other readings and meanings in different contexts.",
"MU signifie couramment nom, bien que le signe possède d’autres lectures et significations selon le contexte."
),

(
"Which sign represents MU?",
"Quel signe représente MU ?",
["𒈬", "𒌓", "𒄑", "𒌉"],
["𒈬", "𒌓", "𒄑", "𒌉"],
0,
"The sign 𒈬 is commonly read MU.",
"Le signe 𒈬 se lit couramment MU."
),

(
"What does GAL mean?",
"Que signifie GAL ?",
["Great or big", "Small", "Old", "Young"],
["Grand ou important", "Petit", "Vieux", "Jeune"],
0,
"GAL means great, big or large.",
"GAL signifie grand, important ou de grande taille."
),

(
"Which sign represents GAL?",
"Quel signe représente GAL ?",
["𒃲", "𒅗", "𒀭", "𒊩"],
["𒃲", "𒅗", "𒀭", "𒊩"],
0,
"The cuneiform sign 𒃲 is read GAL.",
"Le signe cunéiforme 𒃲 se lit GAL."
),

(
"What is the usual basic word order in a Sumerian verbal clause?",
"Quel est généralement l’ordre des mots de base dans une proposition verbale sumérienne ?",
["Subject–Object–Verb", "Subject–Verb–Object", "Verb–Subject–Object", "Object–Verb–Subject"],
["Sujet–Objet–Verbe", "Sujet–Verbe–Objet", "Verbe–Sujet–Objet", "Objet–Verbe–Sujet"],
0,
"Sumerian generally follows Subject–Object–Verb order, although information structure and other constructions can affect word order.",
"Le sumérien suit généralement l’ordre Sujet–Objet–Verbe, même si la structure informationnelle et certaines constructions peuvent modifier cet ordre."
),

(
"How is Sumerian generally classified linguistically?",
"Comment le sumérien est-il généralement classé sur le plan linguistique ?",
["Language isolate", "Semitic language", "Indo-European language", "Turkic language"],
["Langue isolée", "Langue sémitique", "Langue indo-européenne", "Langue turcique"],
0,
"Sumerian is generally considered a language isolate because no genetic relationship with another language family has been demonstrated.",
"Le sumérien est généralement considéré comme une langue isolée, car aucune parenté génétique avec une autre famille linguistique n’a été démontrée."
),

(
"What does the term cuneiform literally refer to?",
"À quoi le terme « cunéiforme » fait-il littéralement référence ?",
["Wedge-shaped", "Circular writing", "Picture writing", "Alphabetic writing"],
["En forme de coin", "Écriture circulaire", "Écriture pictographique", "Écriture alphabétique"],
0,
"The term cuneiform comes from a word meaning wedge-shaped, referring to the characteristic marks.",
"Le terme cunéiforme vient d’un mot signifiant « en forme de coin », en référence aux marques caractéristiques."
),

(
"What does the Sumerian word NIN commonly mean?",
"Que signifie couramment le mot sumérien NIN ?",
["Lady or mistress", "King", "Servant", "Farmer"],
["Dame ou maîtresse", "Roi", "Serviteur", "Agriculteur"],
0,
"NIN is commonly used for lady, mistress or a female authority figure.",
"NIN est couramment utilisé pour désigner une dame, une maîtresse ou une figure féminine d’autorité."
),

(
"What does EN commonly mean in Sumerian titles?",
"Que signifie couramment EN dans les titres sumériens ?",
["Lord or high priest", "Farmer", "Merchant", "Soldier"],
["Seigneur ou grand prêtre", "Agriculteur", "Marchand", "Soldat"],
0,
"EN can mean lord and is also used in certain religious and political titles.",
"EN peut signifier seigneur et est également utilisé dans certains titres religieux et politiques."
),

(
"What does NINDA mean?",
"Que signifie NINDA ?",
["Bread or food", "Water", "Wood", "Cloth"],
["Pain ou nourriture", "Eau", "Bois", "Tissu"],
0,
"NINDA is a Sumerian word associated with bread and food.",
"NINDA est un mot sumérien associé au pain et à la nourriture."
),

(
"What does AŠ mean in Sumerian numeration?",
"Que représente AŠ dans la numération sumérienne ?",
["One", "Two", "Five", "Ten"],
["Un", "Deux", "Cinq", "Dix"],
0,
"AŠ is a basic Sumerian numerical term meaning one.",
"AŠ est un terme numérique sumérien de base qui signifie un."
),

(
"What does MIN mean in Sumerian numeration?",
"Que représente MIN dans la numération sumérienne ?",
["Two", "One", "Three", "Four"],
["Deux", "Un", "Trois", "Quatre"],
0,
"MIN is the Sumerian numerical term for two.",
"MIN est le terme numérique sumérien pour deux."
),

(
"What does EŠE mean in Sumerian numeration?",
"Que représente EŠE dans la numération sumérienne ?",
["Three", "Two", "Four", "Five"],
["Trois", "Deux", "Quatre", "Cinq"],
0,
"EŠE is a Sumerian numerical term meaning three.",
"EŠE est un terme numérique sumérien qui signifie trois."
),

(
"What was the principal writing material for many Mesopotamian cuneiform documents?",
"Quel était le principal support d’écriture de nombreux documents cunéiformes mésopotamiens ?",
["Clay tablets", "Papyrus scrolls", "Silk sheets", "Wooden books"],
["Tablettes d’argile", "Rouleaux de papyrus", "Feuilles de soie", "Livres en bois"],
0,
"Many Mesopotamian texts were written on clay tablets using a stylus.",
"De nombreux textes mésopotamiens étaient écrits sur des tablettes d’argile à l’aide d’un stylet."
),

(
"Which tool was commonly used to impress cuneiform signs into clay?",
"Quel outil était couramment utilisé pour imprimer les signes cunéiformes dans l’argile ?",
["A reed stylus", "A metal brush", "A feather quill", "A stone chisel"],
["Un stylet en roseau", "Un pinceau métallique", "Une plume", "Un ciseau en pierre"],
0,
"A reed stylus was commonly pressed into soft clay to create cuneiform impressions.",
"Un stylet en roseau était couramment pressé dans l’argile humide pour produire les empreintes cunéiformes."
),

(
"Which ancient city was a major centre of Sumerian culture?",
"Quelle ancienne ville était un centre majeur de la culture sumérienne ?",
["Uruk", "Athens", "Rome", "Alexandria"],
["Uruk", "Athènes", "Rome", "Alexandrie"],
0,
"Uruk was one of the most important early urban centres in southern Mesopotamia.",
"Uruk était l’un des centres urbains les plus importants de la Mésopotamie méridionale ancienne."
),

(
"Which archaeological site is associated with the famous Royal Cemetery?",
"Quel site archéologique est associé au célèbre cimetière royal ?",
["Ur", "Nineveh", "Persepolis", "Hattusa"],
["Ur", "Ninive", "Persépolis", "Hattusa"],
0,
"The Royal Cemetery of Ur is famous for its rich burials and archaeological finds.",
"Le cimetière royal d’Ur est célèbre pour ses sépultures riches et ses découvertes archéologiques."
),

(
"Which Sumerian ruler is associated with the famous law collection known as the Code of Ur-Nammu?",
"Quel souverain sumérien est associé au célèbre recueil de lois appelé Code d’Ur-Nammu ?",
["Ur-Nammu", "Sargon of Akkad", "Hammurabi", "Ashurbanipal"],
["Ur-Nammu", "Sargon d’Akkad", "Hammurabi", "Assurbanipal"],
0,
"Ur-Nammu is associated with one of the earliest known surviving law collections.",
"Ur-Nammu est associé à l’un des plus anciens recueils de lois conservés."
),

(
"Which language was closely related to Sumerian in the region but belongs to the Semitic family?",
"Quelle langue, présente dans la région et en contact étroit avec le sumérien, appartient à la famille sémitique ?",
["Akkadian", "Elamite", "Hurrian", "Hattic"],
["L’akkadien", "L’élamite", "Le hourrite", "Le hattique"],
0,
"Akkadian is a Semitic language that coexisted and interacted with Sumerian.",
"L’akkadien est une langue sémitique qui a coexisté et interagi avec le sumérien."
),

(
"What is a characteristic of an agglutinative language such as Sumerian?",
"Quelle est une caractéristique d’une langue agglutinante comme le sumérien ?",
["Grammatical elements are added in sequences", "Words never change form", "Only word order expresses grammar", "It has no suffixes"],
["Les éléments grammaticaux sont ajoutés en séquence", "Les mots ne changent jamais de forme", "Seul l’ordre des mots exprime la grammaire", "La langue ne possède aucun suffixe"],
0,
"Sumerian is agglutinative: grammatical elements are attached to a base in sequences.",
"Le sumérien est une langue agglutinante : des éléments grammaticaux sont ajoutés successivement à une base."
),

(
"What is a ziggurat?",
"Qu’est-ce qu’une ziggourat ?",
["A monumental stepped temple structure", "A royal crown", "A type of boat", "A writing instrument"],
["Une construction monumentale à étages servant de temple", "Une couronne royale", "Un type de bateau", "Un instrument d’écriture"],
0,
"A ziggurat is a monumental stepped structure associated with religious architecture in Mesopotamia.",
"Une ziggourat est une construction monumentale à étages associée à l’architecture religieuse de Mésopotamie."
),

(
"Which material was commonly used to make cylinder seals in Mesopotamia?",
"Quel matériau était couramment utilisé pour fabriquer les sceaux-cylindres en Mésopotamie ?",
["Stone", "Paper", "Glass fibre", "Cotton"],
["La pierre", "Le papier", "La fibre de verre", "Le coton"],
0,
"Cylinder seals were commonly carved from stone and rolled over clay to create impressions.",
"Les sceaux-cylindres étaient souvent gravés dans la pierre puis roulés sur l’argile pour y laisser une empreinte."
),

(
"What was one important function of cylinder seals?",
"Quelle était l’une des fonctions importantes des sceaux-cylindres ?",
["Authentication and administration", "Measuring temperature", "Making textiles", "Producing metal tools"],
["L’authentification et l’administration", "La mesure de la température", "La fabrication de textiles", "La production d’outils métalliques"],
0,
"Cylinder seals could identify individuals, authenticate documents and secure goods.",
"Les sceaux-cylindres pouvaient identifier des personnes, authentifier des documents et sécuriser des biens."
),

(
"Which natural fibre was widely used in ancient Mesopotamian textile production?",
"Quelle fibre naturelle était largement utilisée dans la production textile de l’ancienne Mésopotamie ?",
["Flax", "Nylon", "Polyester", "Acrylic"],
["Le lin", "Le nylon", "Le polyester", "L’acrylique"],
0,
"Flax was an important source of linen fibre in the ancient Near East, including Mesopotamia.",
"Le lin était une source importante de fibres textiles dans le Proche-Orient ancien, notamment en Mésopotamie."
),

(
"What is the main product obtained from flax stems for textile production?",
"Quel est le principal produit obtenu à partir des tiges de lin pour la production textile ?",
["Bast fibres", "Metal threads", "Animal hair", "Mineral crystals"],
["Des fibres libériennes", "Des fils métalliques", "Des poils d’animaux", "Des cristaux minéraux"],
0,
"Flax stems contain bast fibres that can be processed into linen yarn and fabric.",
"Les tiges de lin contiennent des fibres libériennes qui peuvent être transformées en fils et en tissus de lin."
),

(
"What is the purpose of spinning in textile production?",
"Quel est le but du filage dans la production textile ?",
["To make fibres into yarn", "To dye finished fabric", "To cut garments", "To weave a basket"],
["Transformer les fibres en fil", "Teindre le tissu fini", "Couper les vêtements", "Tisser un panier"],
0,
"Spinning twists fibres together to produce yarn.",
"Le filage consiste à tordre les fibres ensemble pour produire du fil."
),

(
"What is the main function of a loom?",
"Quelle est la fonction principale d’un métier à tisser ?",
["To interlace warp and weft yarns", "To spin raw fibres", "To extract flax seeds", "To carve stone"],
["Entrecroiser les fils de chaîne et de trame", "Filer les fibres brutes", "Extraire les graines de lin", "Tailler la pierre"],
0,
"A loom holds the warp threads and allows weft threads to be interlaced with them.",
"Un métier à tisser maintient les fils de chaîne et permet d’entrecroiser les fils de trame."
),

(
"What is the warp in weaving?",
"Qu’est-ce que la chaîne dans le tissage ?",
["The lengthwise threads", "The crosswise threads", "The finished fabric edge", "The spinning spindle"],
["Les fils longitudinaux", "Les fils transversaux", "Le bord du tissu fini", "Le fuseau de filage"],
0,
"The warp consists of the lengthwise threads held under tension on a loom.",
"La chaîne est constituée des fils longitudinaux maintenus sous tension sur le métier à tisser."
),

(
"What is the weft in weaving?",
"Qu’est-ce que la trame dans le tissage ?",
["The crosswise threads", "The lengthwise threads", "The loom frame", "The finished garment"],
["Les fils transversaux", "Les fils longitudinaux", "Le cadre du métier", "Le vêtement fini"],
0,
"The weft threads pass across the warp to form the woven fabric.",
"Les fils de trame passent transversalement à travers la chaîne pour former le tissu."
),

(
"What is a spindle used for?",
"À quoi sert un fuseau ?",
["Spinning fibres into yarn", "Cutting stone", "Writing on clay", "Dyeing leather"],
["À filer les fibres pour produire du fil", "À tailler la pierre", "À écrire sur l’argile", "À teindre le cuir"],
0,
"A spindle is a tool used to twist fibres into yarn.",
"Le fuseau est un outil utilisé pour tordre les fibres et produire du fil."
),

(
"What is a spindle whorl?",
"Qu’est-ce qu’un fusaïole ?",
["A weighted component fitted to a spindle", "A type of loom", "A woven textile", "A clay tablet"],
["Un élément lesté placé sur un fuseau", "Un type de métier à tisser", "Un textile tissé", "Une tablette d’argile"],
0,
"A spindle whorl adds weight and helps maintain the rotation of a spindle.",
"Une fusaïole ajoute du poids et aide à maintenir la rotation du fuseau."
),

(
"What does the term 'textile archaeology' primarily investigate?",
"Que cherche principalement à étudier l’archéologie du textile ?",
["Evidence of ancient fibres, yarns, fabrics and textile production", "Only ancient architecture", "Only royal inscriptions", "Modern fashion trends"],
["Les traces de fibres, fils, tissus et techniques textiles anciens", "Uniquement l’architecture ancienne", "Uniquement les inscriptions royales", "Les tendances de la mode actuelle"],
0,
"Textile archaeology studies material evidence and technologies related to the production and use of textiles in the past.",
"L’archéologie du textile étudie les traces matérielles et les techniques liées à la production et à l’utilisation des textiles dans le passé."
),

(
"Why are textile impressions sometimes found on ancient pottery?",
"Pourquoi trouve-t-on parfois des empreintes textiles sur des poteries anciennes ?",
["Wet clay can preserve impressions from woven materials", "Textiles were always painted on pottery", "Pottery was made from cloth", "Textile impressions are modern decorations"],
["L’argile humide peut conserver les empreintes de matériaux tissés", "Les textiles étaient toujours peints sur les poteries", "La poterie était fabriquée en tissu", "Les empreintes textiles sont des décorations modernes"],
0,
"Textile impressions can survive when fabric or cordage is pressed into wet clay before firing.",
"Les empreintes textiles peuvent être conservées lorsqu’un tissu ou une corde est pressé dans l’argile humide avant la cuisson."
),

(
"What is the main purpose of a textile dye?",
"Quel est le rôle principal d’un colorant textile ?",
["To impart colour to fibres or fabrics", "To spin fibres", "To weave threads", "To harden clay"],
["Donner une couleur aux fibres ou aux tissus", "Filer les fibres", "Tisser les fils", "Durcir l’argile"],
0,
"Dyes are substances used to impart colour to textile materials.",
"Les colorants sont des substances utilisées pour donner une couleur aux matériaux textiles."
),

(
"Which of the following is an example of a plant-based textile fibre?",
"Lequel des éléments suivants est un exemple de fibre textile d’origine végétale ?",
["Flax", "Wool", "Silk", "Leather"],
["Le lin", "La laine", "La soie", "Le cuir"],
0,
"Flax is a plant fibre; wool and silk are animal fibres.",
"Le lin est une fibre végétale ; la laine et la soie sont des fibres animales."
)

]

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

assert len(questions) == 50, f"Expected 50 questions, found {len(questions)}"

for question in questions:
    assert len(question[2]) == 4
    assert len(question[3]) == 4
    assert 0 <= question[4] < 4

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.markdown("## 𒀭 Sumerian Quiz")

language = st.sidebar.radio(
    translations["English"]["language"] + " / " +
    translations["Français"]["language"],
    ["English", "Français"],
    index=0
)

t = translations[language]

st.sidebar.divider()
st.sidebar.markdown(f"**{t['creator']}**")

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {t['sources']}")
st.sidebar.write(t["source_intro"])

st.sidebar.markdown(
    "[Oracc Sign List](https://oracc.museum.upenn.edu/osl/)"
)
st.sidebar.markdown(
    "[Electronic Pennsylvania Sumerian Dictionary](https://oracc.museum.upenn.edu/epsd2/)"
)
st.sidebar.markdown(
    "[Unicode Cuneiform Chart](https://unicode.org/charts/PDF/U12000.pdf)"
)
st.sidebar.markdown(
    "[Unicode Cuneiform Numbers Chart](https://unicode.org/charts/PDF/U12400.pdf)"
)

# ---------------------------------------------------------
# MAIN PAGE
# ---------------------------------------------------------

st.title(t["title"])
st.subheader(t["subtitle"])
st.markdown("---")
st.info(t["instructions"])

st.write(f"**{t['all_questions']}:** {len(questions)}")

# ---------------------------------------------------------
# QUIZ FORM
# ---------------------------------------------------------

with st.form("sumerian_quiz_form"):

    answers = []

    for i, q in enumerate(questions):

        question_text = q[0] if language == "English" else q[1]
        options = q[2] if language == "English" else q[3]

        st.markdown(f"### {t['question']} {i + 1}")
        st.write(question_text)

        answer = st.radio(
            label=f"Answer {i + 1}",
            options=options,
            key=f"question_{i}",
            index=None,
            label_visibility="collapsed"
        )

        answers.append(answer)

        st.markdown("---")

    submitted = st.form_submit_button(
        t["submit"],
        use_container_width=True
    )

# ---------------------------------------------------------
# RESULTS
# ---------------------------------------------------------

if submitted:

    score = 0

    for i, q in enumerate(questions):

        options = q[2] if language == "English" else q[3]
        correct_index = q[4]
        correct_answer = options[correct_index]

        if answers[i] == correct_answer:
            score += 1

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    st.markdown("---")
    st.header(t["result"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            t["score"],
            f"{score}/{total_questions}"
        )

    with col2:
        st.metric(
            t["percentage"],
            f"{percentage:.1f}%"
        )

    with col3:
        st.metric(
            t["all_questions"],
            total_questions
        )

    st.progress(percentage / 100)

    if percentage >= 90:
        st.success(t["excellent"])
    elif percentage >= 70:
        st.success(t["very_good"])
    elif percentage >= 50:
        st.warning(t["good"])
    else:
        st.error(t["keep_learning"])

    # Detailed answer review
    st.markdown("---")
    st.header("Answer Review" if language == "English" else "Correction des réponses")

    for i, q in enumerate(questions):

        question_text = q[0] if language == "English" else q[1]
        options = q[2] if language == "English" else q[3]
        explanation = q[5] if language == "English" else q[6]

        correct_answer = options[q[4]]
        user_answer = answers[i]

        st.markdown(f"### {t['question']} {i + 1}")
        st.write(question_text)

        if user_answer is None:
            st.warning(
                f"{t['your_answer']}: {t['not_answered']}"
            )
        else:
            st.write(f"**{t['your_answer']}:** {user_answer}")

        if user_answer == correct_answer:
            st.success(f"{t['correct']}: {correct_answer}")
        else:
            st.error(f"{t['correct']}: {correct_answer}")

        st.info(f"**{t['explanation']}:** {explanation}")

        st.markdown("---")

    if st.button(t["restart"], use_container_width=True):
        st.rerun()

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")
st.caption(t["footer"])
st.markdown(
    f"<div style='text-align:center; color:gray;'>"
    f"<b>{t['creator']}</b></div>",
    unsafe_allow_html=True
)
