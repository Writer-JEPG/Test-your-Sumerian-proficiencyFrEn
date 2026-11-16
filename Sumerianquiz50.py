import streamlit as st

# ---------------------------------------------------------
# Sumerian Knowledge Quiz
# Created by Rami Ibrahim
# 50 questions – English / French
# ---------------------------------------------------------

st.set_page_config(
    page_title="Test Your Sumerian Knowledge",
    page_icon="📜",
    layout="wide"
)

# ---------------------------------------------------------
# LANGUAGE SETTINGS
# ---------------------------------------------------------

LANGUAGES = {
    "English": {
        "title": "📜 Test Your Sumerian Knowledge",
        "subtitle": "This quiz intends to test your knowledge about Mesopotamian ancient cultures, languages, and the textile industry. This quiz was created by Rami Ibrahim, a linguist and the founder of the Museum of the Archaeology and Craftsmanship of Textiles.",
        "instructions": "Select one answer for each question, then click **Submit my answers**.",
        "submit": "Submit my answers",
        "score": "Your score",
        "out_of": "out of",
        "excellent": "Excellent! You have a very strong knowledge of Sumerian civilisation.",
        "good": "Very good! You have a good understanding of Sumerian civilisation.",
        "average": "Good effort! There is still more to discover about Sumer.",
        "beginner": "Keep learning! Sumerian civilisation has a fascinating history.",
        "review": "Answer review",
        "your_answer": "Your answer",
        "correct_answer": "Correct answer",
        "explanation": "Explanation",
        "not_answered": "Not answered",
        "restart": "Restart the quiz",
        "creator": "Created by Rami Ibrahim",
        "references": "Research references",
        "references_note": "These resources are useful for further research into Sumerian language, cuneiform and Mesopotamian history.",
        "question": "Question",
        "select_answer": "Choose an answer",
        "complete": "You have answered all 50 questions.",
        "incomplete": "You have not answered all the questions. Unanswered questions will be counted as incorrect."
    },
    "Français": {
        "title": "📜 Testez vos connaissances sur les Sumériens",
        "subtitle": "Un quiz de 50 questions sur l’histoire, la langue, l’écriture, la religion et la culture sumériennes.",
        "choose_language": "Choisissez votre langue",
        "instructions": "Sélectionnez une réponse pour chaque question, puis cliquez sur **Soumettre mes réponses**.",
        "submit": "Soumettre mes réponses",
        "score": "Votre score",
        "out_of": "sur",
        "excellent": "Excellent ! Vous possédez de très solides connaissances sur la civilisation sumérienne.",
        "good": "Très bien ! Vous avez une bonne compréhension de la civilisation sumérienne.",
        "average": "Bon travail ! Il vous reste encore beaucoup à découvrir sur Sumer.",
        "beginner": "Continuez à apprendre ! La civilisation sumérienne possède une histoire fascinante.",
        "review": "Correction des réponses",
        "your_answer": "Votre réponse",
        "correct_answer": "Bonne réponse",
        "explanation": "Explication",
        "not_answered": "Sans réponse",
        "restart": "Recommencer le quiz",
        "creator": "Créé par Rami Ibrahim",
        "references": "Références scientifiques",
        "references_note": "Ces ressources permettent d’approfondir les recherches sur la langue sumérienne, l’écriture cunéiforme et l’histoire mésopotamienne.",
        "question": "Question",
        "select_answer": "Choisissez une réponse",
        "complete": "Vous avez répondu aux 50 questions.",
        "incomplete": "Vous n’avez pas répondu à toutes les questions. Les questions sans réponse seront considérées comme incorrectes."
    }
}

# ---------------------------------------------------------
# QUESTION FORMAT
# ---------------------------------------------------------

def Q(en, fr, options_en, options_fr, answer, explanation_en, explanation_fr):
    return {
        "en": en,
        "fr": fr,
        "options_en": options_en,
        "options_fr": options_fr,
        "answer": answer,
        "explanation_en": explanation_en,
        "explanation_fr": explanation_fr
    }


# ---------------------------------------------------------
# 50 QUESTIONS
# The answer is the zero-based index of the correct option.
# ---------------------------------------------------------

questions = [

    Q(
        "Where was the heartland of ancient Sumer located?",
        "Où se trouvait le cœur de l’ancien pays de Sumer ?",
        ["Southern Mesopotamia", "Northern Egypt", "The Indus Valley", "Central Anatolia"],
        ["Dans le sud de la Mésopotamie", "Dans le nord de l’Égypte", "Dans la vallée de l’Indus", "En Anatolie centrale"],
        0,
        "Sumer was located in southern Mesopotamia, mainly in the southern part of present-day Iraq.",
        "Sumer se trouvait dans le sud de la Mésopotamie, principalement dans la partie méridionale de l’actuel Irak."
    ),

    Q(
        "Which two rivers were central to Mesopotamian civilisation?",
        "Quels sont les deux fleuves qui ont joué un rôle central dans la civilisation mésopotamienne ?",
        ["Nile and Jordan", "Tigris and Euphrates", "Indus and Ganges", "Danube and Rhine"],
        ["Le Nil et le Jourdain", "Le Tigre et l’Euphrate", "L’Indus et le Gange", "Le Danube et le Rhin"],
        1,
        "The Tigris and Euphrates rivers shaped the landscape, agriculture and settlement patterns of Mesopotamia.",
        "Le Tigre et l’Euphrate ont façonné le paysage, l’agriculture et les modes d’établissement de la Mésopotamie."
    ),

    Q(
        "Which city is often associated with the earliest development of urban civilisation in Sumer?",
        "Quelle ville est souvent associée aux premières formes de civilisation urbaine à Sumer ?",
        ["Uruk", "Babylon", "Nineveh", "Persepolis"],
        ["Uruk", "Babylone", "Ninive", "Persépolis"],
        0,
        "Uruk was one of the earliest major cities in southern Mesopotamia and played a central role in early urban development.",
        "Uruk fut l’une des premières grandes villes du sud de la Mésopotamie et joua un rôle central dans le développement urbain ancien."
    ),

    Q(
        "What type of writing system did the Sumerians develop?",
        "Quel type de système d’écriture les Sumériens ont-ils développé ?",
        ["Alphabetic writing", "Cuneiform writing", "Hieroglyphic writing", "Runic writing"],
        ["L’écriture alphabétique", "L’écriture cunéiforme", "L’écriture hiéroglyphique", "L’écriture runique"],
        1,
        "Sumerian scribes used cuneiform, a writing system characterised by wedge-shaped impressions.",
        "Les scribes sumériens utilisaient l’écriture cunéiforme, un système caractérisé par des impressions en forme de coins."
    ),

    Q(
        "What material was commonly used for Sumerian writing tablets?",
        "Quel matériau était couramment utilisé pour les tablettes d’écriture sumériennes ?",
        ["Papyrus", "Clay", "Parchment", "Wood"],
        ["Le papyrus", "L’argile", "Le parchemin", "Le bois"],
        1,
        "Clay was widely used because it was abundant in Mesopotamia and could preserve written records when baked or dried.",
        "L’argile était largement utilisée, car elle était abondante en Mésopotamie et pouvait conserver les textes lorsqu’elle était séchée ou cuite."
    ),

    Q(
        "Which tool was commonly used to make impressions on clay tablets?",
        "Quel outil était couramment utilisé pour faire des impressions sur les tablettes d’argile ?",
        ["A reed stylus", "A metal pen", "A brush", "A stone chisel"],
        ["Un stylet en roseau", "Une plume métallique", "Un pinceau", "Un ciseau en pierre"],
        0,
        "Scribes commonly used a cut reed stylus to press signs into soft clay.",
        "Les scribes utilisaient généralement un stylet taillé dans un roseau pour imprimer les signes dans l’argile molle."
    ),

    Q(
        "What does the word 'cuneiform' refer to?",
        "À quoi le terme « cunéiforme » fait-il référence ?",
        ["Circular shapes", "Wedge-shaped forms", "Bird-shaped signs", "Painted symbols"],
        ["Des formes circulaires", "Des formes en coin", "Des signes en forme d’oiseau", "Des symboles peints"],
        1,
        "The term comes from the Latin words cuneus (wedge) and forma (shape).",
        "Le terme vient des mots latins cuneus (coin) et forma (forme)."
    ),

    Q(
        "What was one of the earliest important uses of writing in Mesopotamia?",
        "Quel était l’un des premiers usages importants de l’écriture en Mésopotamie ?",
        ["Recording economic transactions", "Writing novels", "Printing newspapers", "Recording musical performances"],
        ["L’enregistrement des transactions économiques", "L’écriture de romans", "L’impression de journaux", "L’enregistrement de représentations musicales"],
        0,
        "Early written documents often recorded goods, labour, agricultural products and administrative transactions.",
        "Les premiers documents écrits enregistraient souvent des marchandises, du travail, des produits agricoles et des transactions administratives."
    ),

    Q(
        "Which statement best describes the Sumerian language?",
        "Quelle affirmation décrit le mieux la langue sumérienne ?",
        ["It is a Semitic language", "It is generally considered a language isolate", "It is an Indo-European language", "It is a Turkic language"],
        ["C’est une langue sémitique", "Elle est généralement considérée comme une langue isolée", "C’est une langue indo-européenne", "C’est une langue turcique"],
        1,
        "Sumerian is generally classified as a language isolate because no generally accepted genetic relationship with another language has been established.",
        "Le sumérien est généralement classé comme une langue isolée, car aucune parenté génétique généralement acceptée avec une autre langue n’a été établie."
    ),

    Q(
        "Which language was widely used alongside Sumerian in ancient Mesopotamia?",
        "Quelle langue était largement utilisée aux côtés du sumérien dans l’ancienne Mésopotamie ?",
        ["Akkadian", "Latin", "Ancient Greek", "Coptic"],
        ["L’akkadien", "Le latin", "Le grec ancien", "Le copte"],
        0,
        "Akkadian, a Semitic language, coexisted with Sumerian and eventually became dominant in many areas of Mesopotamia.",
        "L’akkadien, une langue sémitique, a coexisté avec le sumérien et est finalement devenu dominant dans de nombreuses régions de Mésopotamie."
    ),

    Q(
        "What does the Sumerian sign E₂ commonly mean?",
        "Que signifie généralement le signe sumérien E₂ ?",
        ["House", "Water", "King", "Mountain"],
        ["Maison", "Eau", "Roi", "Montagne"],
        0,
        "E₂ is commonly read as 'house' and can refer to a building or institution, depending on context.",
        "E₂ se lit généralement « maison » et peut désigner un bâtiment ou une institution selon le contexte."
    ),

    Q(
        "What does the Sumerian word GAL commonly mean?",
        "Que signifie généralement le mot sumérien GAL ?",
        ["Small", "Great or big", "Water", "Earth"],
        ["Petit", "Grand ou important", "Eau", "Terre"],
        1,
        "GAL commonly means 'big' or 'great' in Sumerian.",
        "GAL signifie généralement « grand » ou « important » en sumérien."
    ),

    Q(
        "What does the compound E₂-GAL mean?",
        "Que signifie le composé E₂-GAL ?",
        ["Palace", "Canal", "Field", "Workshop"],
        ["Palais", "Canal", "Champ", "Atelier"],
        0,
        "E₂-GAL means 'palace'. It combines E₂ (house) and GAL (great or big).",
        "E₂-GAL signifie « palais ». Le composé associe E₂ (maison) et GAL (grand ou important)."
    ),

    Q(
        "What does the Sumerian word LUGAL mean?",
        "Que signifie le mot sumérien LUGAL ?",
        ["King", "Scribe", "Farmer", "Priestess"],
        ["Roi", "Scribe", "Agriculteur", "Prêtresse"],
        0,
        "LUGAL is the Sumerian word commonly translated as 'king'.",
        "LUGAL est le mot sumérien généralement traduit par « roi »."
    ),

    Q(
        "What was a DUB-SAR?",
        "Qu’était un DUB-SAR ?",
        ["A scribe", "A soldier", "A farmer", "A merchant ship"],
        ["Un scribe", "Un soldat", "Un agriculteur", "Un navire marchand"],
        0,
        "DUB-SAR refers to a scribe, literally associated with writing on tablets.",
        "DUB-SAR désigne un scribe, littéralement associé à l’écriture sur des tablettes."
    ),

    Q(
        "What was a ziggurat?",
        "Qu’était une ziggourat ?",
        ["A stepped monumental structure", "A royal boat", "A type of textile", "A military weapon"],
        ["Une construction monumentale à étages", "Un bateau royal", "Un type de textile", "Une arme militaire"],
        0,
        "A ziggurat was a monumental stepped structure associated with religious and temple complexes.",
        "Une ziggourat était une construction monumentale à étages associée aux complexes religieux et aux temples."
    ),

    Q(
        "Which Sumerian city is famous for its well-known ziggurat?",
        "Quelle ville sumérienne est célèbre pour sa ziggourat ?",
        ["Ur", "Memphis", "Athens", "Carthage"],
        ["Ur", "Memphis", "Athènes", "Carthage"],
        0,
        "The ziggurat of Ur, associated with the moon god Nanna, is one of the best-known surviving monuments of ancient Mesopotamia.",
        "La ziggourat d’Ur, associée au dieu-lune Nanna, est l’un des monuments les plus connus de l’ancienne Mésopotamie."
    ),

    Q(
        "Which goddess was especially associated with love, sexuality and warfare?",
        "Quelle déesse était particulièrement associée à l’amour, à la sexualité et à la guerre ?",
        ["Inanna", "Nisaba", "Ninhursag", "Ereshkigal"],
        ["Inanna", "Nisaba", "Ninhursag", "Ereshkigal"],
        0,
        "Inanna was a major Sumerian goddess associated with love, sexuality, political power and warfare.",
        "Inanna était une grande déesse sumérienne associée à l’amour, à la sexualité, au pouvoir politique et à la guerre."
    ),

    Q(
        "Which god was associated with wisdom and freshwater?",
        "Quel dieu était associé à la sagesse et à l’eau douce ?",
        ["Enki", "Nanna", "Utu", "Nergal"],
        ["Enki", "Nanna", "Utu", "Nergal"],
        0,
        "Enki, also known in Akkadian as Ea, was associated with wisdom, freshwater and the subterranean waters known as the Apsu.",
        "Enki, également connu sous le nom akkadien d’Ea, était associé à la sagesse, à l’eau douce et aux eaux souterraines appelées Apsu."
    ),

    Q(
        "Which god was associated with the moon?",
        "Quel dieu était associé à la Lune ?",
        ["Nanna", "Utu", "Enlil", "Enki"],
        ["Nanna", "Utu", "Enlil", "Enki"],
        0,
        "Nanna, also called Suen, was the Sumerian moon god.",
        "Nanna, également appelé Suen, était le dieu-lune sumérien."
    ),

    Q(
        "Which god was associated with the sun?",
        "Quel dieu était associé au Soleil ?",
        ["Utu", "Nanna", "Enki", "Dumuzi"],
        ["Utu", "Nanna", "Enki", "Dumuzi"],
        0,
        "Utu was the Sumerian sun god, associated with justice and judgement.",
        "Utu était le dieu solaire sumérien, associé à la justice et au jugement."
    ),

    Q(
        "Which goddess was associated with writing and grain?",
        "Quelle déesse était associée à l’écriture et aux céréales ?",
        ["Nisaba", "Inanna", "Ereshkigal", "Geshtinanna"],
        ["Nisaba", "Inanna", "Ereshkigal", "Geshtinanna"],
        0,
        "Nisaba was associated with grain, accounting and scribal learning.",
        "Nisaba était associée aux céréales, à la comptabilité et au savoir des scribes."
    ),

    Q(
        "Who was Enlil?",
        "Qui était Enlil ?",
        ["A major god associated with air and authority", "A Sumerian king", "A famous scribe", "A goddess of weaving"],
        ["Un grand dieu associé à l’air et à l’autorité", "Un roi sumérien", "Un célèbre scribe", "Une déesse du tissage"],
        0,
        "Enlil was one of the most important Mesopotamian gods and was associated with authority, wind and the atmosphere.",
        "Enlil était l’un des dieux les plus importants de Mésopotamie. Il était associé à l’autorité, au vent et à l’atmosphère."
    ),

    Q(
        "Who was Ereshkigal?",
        "Qui était Ereshkigal ?",
        ["Goddess of the underworld", "Goddess of the moon", "Goddess of weaving", "Goddess of the harvest"],
        ["La déesse des Enfers", "La déesse de la Lune", "La déesse du tissage", "La déesse des récoltes"],
        0,
        "Ereshkigal was the goddess who ruled the underworld in Mesopotamian mythology.",
        "Ereshkigal était la déesse qui régnait sur les Enfers dans la mythologie mésopotamienne."
    ),

    Q(
        "Which goddess is often described as a mother goddess associated with mountains and fertility?",
        "Quelle déesse est souvent décrite comme une déesse mère associée aux montagnes et à la fertilité ?",
        ["Ninhursag", "Inanna", "Nisaba", "Ereshkigal"],
        ["Ninhursag", "Inanna", "Nisaba", "Ereshkigal"],
        0,
        "Ninhursag was a major mother goddess associated with fertility and the creation of life.",
        "Ninhursag était une grande déesse mère associée à la fertilité et à la création de la vie."
    ),

    Q(
        "Who was Dumuzi?",
        "Qui était Dumuzi ?",
        ["A god associated with shepherds and vegetation", "A god of the moon", "A Sumerian lawgiver", "A city governor"],
        ["Un dieu associé aux bergers et à la végétation", "Un dieu de la Lune", "Un législateur sumérien", "Un gouverneur de ville"],
        0,
        "Dumuzi was a shepherd deity associated with vegetation and seasonal cycles.",
        "Dumuzi était une divinité pastorale associée à la végétation et aux cycles saisonniers."
    ),

    Q(
        "Which city was traditionally associated with the goddess Inanna?",
        "Quelle ville était traditionnellement associée à la déesse Inanna ?",
        ["Uruk", "Mari", "Hattusa", "Byblos"],
        ["Uruk", "Mari", "Hattusa", "Byblos"],
        0,
        "Inanna had a major sanctuary in Uruk, particularly in the Eanna temple district.",
        "Inanna possédait un sanctuaire important à Uruk, notamment dans le quartier du temple Eanna."
    ),

    Q(
        "Who was Gilgamesh in Mesopotamian tradition?",
        "Qui était Gilgamesh dans la tradition mésopotamienne ?",
        ["A king of Uruk", "A god of writing", "A Babylonian law code", "A Sumerian textile worker"],
        ["Un roi d’Uruk", "Un dieu de l’écriture", "Un code de lois babylonien", "Un artisan textile sumérien"],
        0,
        "Gilgamesh was remembered as a king of Uruk and became the central figure of an important literary tradition.",
        "Gilgamesh était considéré comme un roi d’Uruk et devint le personnage central d’une importante tradition littéraire."
    ),

    Q(
        "What is the Epic of Gilgamesh?",
        "Qu’est-ce que l’Épopée de Gilgamesh ?",
        ["A Mesopotamian literary epic", "A Sumerian tax register", "A royal building", "A type of cylinder seal"],
        ["Une épopée littéraire mésopotamienne", "Un registre fiscal sumérien", "Un bâtiment royal", "Un type de sceau-cylindre"],
        0,
        "The Epic of Gilgamesh is a major Mesopotamian literary work, preserved principally in Akkadian versions, with earlier Sumerian poems about Gilgamesh.",
        "L’Épopée de Gilgamesh est une œuvre majeure de la littérature mésopotamienne, principalement conservée dans des versions akkadiennes, avec des poèmes sumériens plus anciens consacrés à Gilgamesh."
    ),

    Q(
        "Who was Enheduanna?",
        "Qui était Enheduanna ?",
        ["A high priestess and literary author", "A military commander", "A Babylonian architect", "A goddess of the underworld"],
        ["Une grande prêtresse et autrice", "Une commandante militaire", "Une architecte babylonienne", "Une déesse des Enfers"],
        0,
        "Enheduanna was a high priestess of the moon god at Ur and is widely regarded as the earliest known author identified by name.",
        "Enheduanna était une grande prêtresse du dieu-lune à Ur. Elle est largement considérée comme la plus ancienne autrice connue identifiée par son nom."
    ),

    Q(
        "Which ruler founded the Third Dynasty of Ur?",
        "Quel souverain a fondé la troisième dynastie d’Ur ?",
        ["Ur-Nammu", "Sargon of Akkad", "Hammurabi", "Nebuchadnezzar II"],
        ["Ur-Nammu", "Sargon d’Akkad", "Hammurabi", "Nabuchodonosor II"],
        0,
        "Ur-Nammu founded the Third Dynasty of Ur, also known as the Ur III period.",
        "Ur-Nammu fonda la troisième dynastie d’Ur, également appelée période d’Ur III."
    ),

    Q(
        "Which ruler is associated with the law code of Ur-Nammu?",
        "Quel souverain est associé au code de lois d’Ur-Nammu ?",
        ["Ur-Nammu", "Gudea", "Gilgamesh", "Sargon II"],
        ["Ur-Nammu", "Gudea", "Gilgamesh", "Sargon II"],
        0,
        "The Code of Ur-Nammu is associated with the founder of the Third Dynasty of Ur and is among the earliest surviving law collections.",
        "Le Code d’Ur-Nammu est associé au fondateur de la troisième dynastie d’Ur et figure parmi les plus anciennes collections de lois conservées."
    ),

    Q(
        "Who was Gudea?",
        "Qui était Gudea ?",
        ["A ruler of Lagash", "A king of Egypt", "A Hittite general", "A Babylonian goddess"],
        ["Un souverain de Lagash", "Un roi d’Égypte", "Un général hittite", "Une déesse babylonienne"],
        0,
        "Gudea was a ruler of the city-state of Lagash, known especially for inscriptions and statues.",
        "Gudea était un souverain de la cité-État de Lagash, particulièrement connu pour ses inscriptions et ses statues."
    ),

    Q(
        "What was a cylinder seal used for?",
        "À quoi servait un sceau-cylindre ?",
        ["Identifying and authenticating documents or property", "Cutting textiles", "Measuring rainfall", "Lighting temples"],
        ["À identifier et authentifier des documents ou des biens", "À couper des textiles", "À mesurer les précipitations", "À éclairer les temples"],
        0,
        "A cylinder seal was rolled over clay to create a distinctive impression used for identification and authentication.",
        "Un sceau-cylindre était roulé sur l’argile afin de produire une empreinte distinctive utilisée pour l’identification et l’authentification."
    ),

    Q(
        "What was one important use of cylinder seals in Mesopotamia?",
        "Quel était l’un des usages importants des sceaux-cylindres en Mésopotamie ?",
        ["Sealing containers and administrative documents", "Weaving wool", "Writing on papyrus", "Making bronze weapons"],
        ["Sceller des récipients et des documents administratifs", "Tisser la laine", "Écrire sur du papyrus", "Fabriquer des armes en bronze"],
        0,
        "Cylinder seals could be rolled over clay sealings to secure containers, doors and administrative records.",
        "Les sceaux-cylindres pouvaient être roulés sur des scellements d’argile afin de sécuriser des récipients, des portes et des documents administratifs."
    ),

    Q(
        "Which numbering system was important in Mesopotamian mathematics?",
        "Quel système de numération était important dans les mathématiques mésopotamiennes ?",
        ["Sexagesimal (base 60)", "Decimal (base 10) only", "Binary (base 2)", "Vigesimal (base 20)"],
        ["Le système sexagésimal (base 60)", "Le système décimal (base 10) uniquement", "Le système binaire (base 2)", "Le système vigésimal (base 20)"],
        0,
        "Mesopotamian mathematical traditions made extensive use of a sexagesimal system based on 60.",
        "Les traditions mathématiques mésopotamiennes utilisaient largement un système sexagésimal fondé sur 60."
    ),

    Q(
        "Which modern measurement still reflects the Mesopotamian base-60 tradition?",
        "Quelle mesure moderne reflète encore la tradition mésopotamienne de la base 60 ?",
        ["60 seconds in a minute", "10 centimetres in a decimetre", "100 years in a century", "7 days in a week"],
        ["60 secondes dans une minute", "10 centimètres dans un décimètre", "100 ans dans un siècle", "7 jours dans une semaine"],
        0,
        "The division of an hour into 60 minutes and a minute into 60 seconds reflects the long history of sexagesimal mathematics.",
        "La division d’une heure en 60 minutes et d’une minute en 60 secondes reflète la longue histoire des mathématiques sexagésimales."
    ),

    Q(
        "What was a common agricultural crop in ancient southern Mesopotamia?",
        "Quelle culture agricole était courante dans le sud de l’ancienne Mésopotamie ?",
        ["Barley", "Coffee", "Potatoes", "Maize"],
        ["L’orge", "Le café", "Les pommes de terre", "Le maïs"],
        0,
        "Barley was a major crop in Mesopotamia and was important for food, payments and administration.",
        "L’orge était une culture majeure en Mésopotamie et jouait un rôle important dans l’alimentation, les paiements et l’administration."
    ),

    Q(
        "Why were irrigation systems important in Sumer?",
        "Pourquoi les systèmes d’irrigation étaient-ils importants à Sumer ?",
        ["They supplied water to agricultural land", "They provided electricity", "They protected against earthquakes", "They produced metal"],
        ["Ils apportaient de l’eau aux terres agricoles", "Ils produisaient de l’électricité", "Ils protégeaient contre les tremblements de terre", "Ils produisaient du métal"],
        0,
        "Canals and irrigation works helped bring river water to fields in the relatively dry southern Mesopotamian environment.",
        "Les canaux et les ouvrages d’irrigation permettaient d’apporter l’eau des fleuves aux champs dans l’environnement relativement aride du sud mésopotamien."
    ),

    Q(
        "Which material was widely used for making textiles in ancient Mesopotamia?",
        "Quel matériau était largement utilisé pour fabriquer des textiles dans l’ancienne Mésopotamie ?",
        ["Wool", "Nylon", "Polyester", "Synthetic acrylic"],
        ["La laine", "Le nylon", "Le polyester", "L’acrylique synthétique"],
        0,
        "Sheep's wool was a major textile material in Mesopotamia. Flax linen was also known and used.",
        "La laine de mouton était une matière textile majeure en Mésopotamie. Le lin était également connu et utilisé."
    ),

    Q(
        "Which plant was the source of linen fibres in the ancient world?",
        "Quelle plante était la source des fibres de lin dans le monde ancien ?",
        ["Flax", "Cotton", "Papyrus", "Hemp"],
        ["Le lin", "Le coton", "Le papyrus", "Le chanvre"],
        0,
        "Linen fibres are obtained from the flax plant, Linum usitatissimum.",
        "Les fibres de lin sont obtenues à partir de la plante de lin, Linum usitatissimum."
    ),

    Q(
        "What is spinning in textile production?",
        "Qu’est-ce que le filage dans la production textile ?",
        ["Turning fibres into yarn", "Dyeing finished cloth", "Cutting a garment", "Printing patterns on fabric"],
        ["Transformer les fibres en fil", "Teindre un tissu terminé", "Couper un vêtement", "Imprimer des motifs sur un tissu"],
        0,
        "Spinning is the process of drawing out and twisting fibres to create yarn.",
        "Le filage consiste à étirer et à tordre des fibres afin de produire du fil."
    ),

    Q(
        "What is weaving?",
        "Qu’est-ce que le tissage ?",
        ["Interlacing warp and weft yarns", "Twisting fibres into yarn", "Carving wood", "Dyeing wool"],
        ["L’entrecroisement des fils de chaîne et de trame", "La torsion des fibres pour produire du fil", "La sculpture du bois", "La teinture de la laine"],
        0,
        "Weaving creates fabric by interlacing two sets of yarns: the warp and the weft.",
        "Le tissage produit un tissu en entrecroisant deux séries de fils : la chaîne et la trame."
    ),

    Q(
        "What is the warp in a woven textile?",
        "Qu’est-ce que la chaîne dans un textile tissé ?",
        ["The lengthwise yarns held under tension", "The crosswise yarns", "The finished fringe", "The dye applied to the fabric"],
        ["Les fils longitudinaux maintenus sous tension", "Les fils transversaux", "Les franges du tissu terminé", "La teinture appliquée au tissu"],
        0,
        "The warp consists of the lengthwise yarns arranged on the loom and held under tension.",
        "La chaîne est constituée des fils longitudinaux disposés sur le métier à tisser et maintenus sous tension."
    ),

    Q(
        "What is the weft in a woven textile?",
        "Qu’est-ce que la trame dans un textile tissé ?",
        ["The crosswise yarns passing through the warp", "The lengthwise yarns", "The loom frame", "The finished textile edge"],
        ["Les fils transversaux passant à travers la chaîne", "Les fils longitudinaux", "Le cadre du métier à tisser", "Le bord du textile terminé"],
        0,
        "The weft is inserted across the warp to form the woven structure.",
        "La trame est insérée transversalement à travers la chaîne afin de former la structure du tissu."
    ),

    Q(
        "What does the term 'archaeological textile' refer to?",
        "À quoi fait référence le terme « textile archéologique » ?",
        ["A textile preserved from an archaeological context", "A modern textile inspired by antiquity", "A drawing of a garment", "A textile made only for decoration"],
        ["Un textile conservé dans un contexte archéologique", "Un textile moderne inspiré de l’Antiquité", "Un dessin de vêtement", "Un textile fabriqué uniquement à des fins décoratives"],
        0,
        "An archaeological textile is a textile or textile fragment recovered from an archaeological context.",
        "Un textile archéologique est un textile ou un fragment textile provenant d’un contexte archéologique."
    ),

    Q(
        "Which city is particularly associated with the ancient kingdom of Mari?",
        "Quelle ville est particulièrement associée à l’ancien royaume de Mari ?",
        ["Mari, on the Euphrates", "Uruk, on the Nile", "Athens, on the Tigris", "Memphis, on the Euphrates"],
        ["Mari, sur l’Euphrate", "Uruk, sur le Nil", "Athènes, sur le Tigre", "Memphis, sur l’Euphrate"],
        0,
        "Mari was an important ancient city on the middle Euphrates, in present-day Syria.",
        "Mari était une importante ville ancienne située sur le moyen Euphrate, dans l’actuelle Syrie."
    ),

    Q(
        "Which archaeological site is associated with the ancient Hurrian city of Urkesh?",
        "Quel site archéologique est associé à l’ancienne cité hourrite d’Urkesh ?",
        ["Tell Mozan", "Tell Brak", "Ur", "Eridu"],
        ["Tell Mozan", "Tell Brak", "Ur", "Eridu"],
        0,
        "Tell Mozan in northeastern Syria is identified with ancient Urkesh, an important Hurrian centre.",
        "Tell Mozan, dans le nord-est de la Syrie, est identifié à l’ancienne Urkesh, un important centre hourrite."
    ),

    Q(
        "Which language is associated with the Hurrians?",
        "Quelle langue est associée aux Hourrites ?",
        ["Hurrian", "Latin", "Old Persian", "Ancient Egyptian"],
        ["Le hourrite", "Le latin", "Le vieux perse", "L’égyptien ancien"],
        0,
        "The Hurrians spoke Hurrian, a language distinct from Sumerian and Akkadian.",
        "Les Hourrites parlaient le hourrite, une langue distincte du sumérien et de l’akkadien."
    ),

    Q(
        "Which empire was founded by Sargon of Akkad?",
        "Quel empire fut fondé par Sargon d’Akkad ?",
        ["The Akkadian Empire", "The Neo-Assyrian Empire", "The Persian Empire", "The Roman Empire"],
        ["L’Empire akkadien", "L’Empire néo-assyrien", "L’Empire perse", "L’Empire romain"],
        0,
        "Sargon of Akkad established the Akkadian Empire in the third millennium BCE.",
        "Sargon d’Akkad établit l’Empire akkadien au troisième millénaire avant notre ère."
    ),

    Q(
        "Which statement about cuneiform is correct?",
        "Quelle affirmation concernant l’écriture cunéiforme est correcte ?",
        ["It was used to write several ancient languages", "It was used only for Sumerian", "It was an alphabet with 26 letters", "It was invented in ancient Rome"],
        ["Elle servait à écrire plusieurs langues anciennes", "Elle servait uniquement à écrire le sumérien", "C’était un alphabet de 26 lettres", "Elle fut inventée dans la Rome antique"],
        0,
        "Cuneiform was adapted to write several languages, including Sumerian and Akkadian, and later languages such as Hittite.",
        "L’écriture cunéiforme fut adaptée à plusieurs langues, notamment le sumérien et l’akkadien, puis des langues comme le hittite."
    ),

    Q(
        "What is a determinative in cuneiform writing?",
        "Qu’est-ce qu’un déterminatif dans l’écriture cunéiforme ?",
        ["A sign that helps classify the meaning of a word", "A punctuation mark used at the end of every sentence", "A number representing a king", "A type of clay tablet"],
        ["Un signe qui aide à classer le sens d’un mot", "Un signe de ponctuation placé à la fin de chaque phrase", "Un nombre représentant un roi", "Un type de tablette d’argile"],
        0,
        "A determinative is a sign used to indicate the semantic category of a word, often without being pronounced.",
        "Un déterminatif est un signe qui indique la catégorie sémantique d’un mot, sans être nécessairement prononcé."
    ),

    Q(
        "What is the main purpose of a museum catalogue for archaeological objects?",
        "Quel est l’objectif principal d’un catalogue de musée consacré aux objets archéologiques ?",
        ["To document and describe objects systematically", "To replace the objects", "To provide entertainment only", "To establish the age of every object without research"],
        ["Documenter et décrire les objets de manière systématique", "Remplacer les objets", "Fournir uniquement un divertissement", "Déterminer l’âge de chaque objet sans recherche"],
        0,
        "A catalogue records information such as an object's description, materials, dimensions, provenance and interpretation.",
        "Un catalogue rassemble des informations telles que la description, les matériaux, les dimensions, la provenance et l’interprétation d’un objet."
    ),

    Q(
        "Why is archaeological context important when studying an ancient object?",
        "Pourquoi le contexte archéologique est-il important pour étudier un objet ancien ?",
        ["It helps interpret the object's date, use and significance", "It always reveals the object's owner's name", "It makes scientific analysis unnecessary", "It proves that every object was religious"],
        ["Il aide à interpréter la date, l’usage et l’importance de l’objet", "Il révèle toujours le nom du propriétaire de l’objet", "Il rend toute analyse scientifique inutile", "Il prouve que chaque objet était religieux"],
        0,
        "The object's location and association with other finds can provide essential evidence for interpretation.",
        "L’emplacement de l’objet et ses associations avec d’autres découvertes peuvent fournir des éléments essentiels à son interprétation."
    ),

    Q(
        "Which modern country contains most of the territory of ancient Sumer?",
        "Quel pays actuel comprend la majeure partie du territoire de l’ancien Sumer ?",
        ["Iraq", "Egypt", "Turkey", "Greece"],
        ["L’Irak", "L’Égypte", "La Turquie", "La Grèce"],
        0,
        "The main cities of ancient Sumer were located in what is now southern Iraq.",
        "Les principales villes de l’ancien Sumer se trouvaient dans ce qui est aujourd’hui le sud de l’Irak."
    )

]

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

for number, question in enumerate(questions, start=1):
    assert len(question["options_en"]) == 4, (
        f"Question {number} must have exactly 4 English options."
    )
    assert len(question["options_fr"]) == 4, (
        f"Question {number} must have exactly 4 French options."
    )
    assert 0 <= question["answer"] < 4, (
        f"Question {number} has an invalid correct-answer index."
    )

# ---------------------------------------------------------
# APPLICATION INTERFACE
# ---------------------------------------------------------

st.sidebar.title("⚙️ Settings")

language = st.sidebar.radio(
    "Choose your language / Choisissez votre langue",
    ["English", "Français"],
    index=0
)

t = LANGUAGES[language]
lang = "en" if language == "English" else "fr"

st.title(t["title"])
st.subheader(t["subtitle"])

st.markdown("---")

st.info(t["instructions"])

# Progress display
st.write(f"**{len(questions)} questions**")

# ---------------------------------------------------------
# QUIZ FORM
# ---------------------------------------------------------

with st.form("sumerian_quiz_form"):

    user_answers = []

    for i, question in enumerate(questions):

        question_text = question[lang]
        options = (
            question["options_en"]
            if lang == "en"
            else question["options_fr"]
        )

        st.markdown(f"### {i + 1}. {question_text}")

        selected_answer = st.radio(
            label=f"{t['question']} {i + 1}",
            options=options,
            index=None,
            key=f"question_{i}",
            label_visibility="collapsed"
        )

        user_answers.append(selected_answer)

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

    for i, selected in enumerate(user_answers):
        options = (
            questions[i]["options_en"]
            if lang == "en"
            else questions[i]["options_fr"]
        )

        correct_option = options[questions[i]["answer"]]

        if selected == correct_option:
            score += 1

    percentage = (score / len(questions)) * 100

    st.markdown("---")
    st.header(t["score"])

    st.metric(
        label=t["score"],
        value=f"{score} / {len(questions)}",
        delta=f"{percentage:.1f}%"
    )

    st.progress(score / len(questions))

    # Feedback according to score
    if percentage >= 85:
        st.success(t["excellent"])
    elif percentage >= 65:
        st.success(t["good"])
    elif percentage >= 40:
        st.warning(t["average"])
    else:
        st.info(t["beginner"])

    unanswered = sum(answer is None for answer in user_answers)

    if unanswered == 0:
        st.write(t["complete"])
    else:
        st.warning(
            f"{t['incomplete']} "
            f"({unanswered} unanswered)"
        )

    # -----------------------------------------------------
    # ANSWER REVIEW
    # -----------------------------------------------------

    st.markdown("---")
    st.header(t["review"])

    for i, question in enumerate(questions):

        options = (
            question["options_en"]
            if lang == "en"
            else question["options_fr"]
        )

        correct_option = options[question["answer"]]
        selected = user_answers[i]

        explanation = (
            question["explanation_en"]
            if lang == "en"
            else question["explanation_fr"]
        )

        question_text = question[lang]

        with st.expander(f"{i + 1}. {question_text}"):

            st.write(f"**{t['your_answer']}:**")

            if selected is None:
                st.write(f"— {t['not_answered']}")
            else:
                st.write(selected)

            st.write(f"**{t['correct_answer']}:** {correct_option}")

            if selected == correct_option:
                st.success("✓ Correct!" if lang == "en" else "✓ Correct !")
            else:
                st.error("✗ Incorrect" if lang == "en" else "✗ Incorrect")

            st.write(f"**{t['explanation']}:**")
            st.write(explanation)

    # -----------------------------------------------------
    # RESTART BUTTON
    # -----------------------------------------------------

    if st.button(t["restart"], use_container_width=True):
        st.rerun()

# ---------------------------------------------------------
# SIDEBAR REFERENCES
# ---------------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader(t["references"])
st.sidebar.write(t["references_note"])

st.sidebar.markdown(
    "- [ORACC Sign List](https://oracc.museum.upenn.edu/osl/)"
)

st.sidebar.markdown(
    "- [Electronic Pennsylvania Sumerian Dictionary (ePSD2)]"
    "(https://oracc.museum.upenn.edu/epsd2/)"
)

st.sidebar.markdown(
    "- [Unicode Cuneiform Chart](https://unicode.org/charts/PDF/U12000.pdf)"
)

st.sidebar.markdown(
    "- [Unicode Cuneiform Numbers Chart]"
    "(https://unicode.org/charts/PDF/U12400.pdf)"
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    f"<div style='text-align: center; color: gray;'>"
    f"{t['creator']}<br>"
    f"Sumerian Knowledge Quiz – 50 Questions"
    f"</div>",
    unsafe_allow_html=True
)
