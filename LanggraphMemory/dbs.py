from LanggraphMemory.vectorDB import CreateVectorDB

# Memory database configurations
MEMORY_CONFIGS = {
    "sensory_buffer": {
        "name": "sensory_buffer",
        "description": """Brain's instant snapshot of the world through senses - automatically and unconsciously records raw sensory information for hundreds of milliseconds. Each sense has its own buffer (iconic memory for vision, echoic memory for hearing) creating fleeting 'echo' or 'afterimage' of stimuli. Like waving a sparkler in darkness and seeing light trails that aren't really there - visual sensory memory holding the image for split seconds. The brain's first stop for incoming data before conscious processing decides importance. Operates in primary sensory cortices as fragile but immediate record of current perceptual moment.""",
        "ttl_seconds": 300,  # Extended for testing - 5 minutes instead of 1 second
        "when_to_retrieve": "by immediate attention selection - if something grabs focus (bright flash, loud noise, meaningful trigger), brain flags it for short-term processing. Must happen instantly or memory fades irretrievably. Like suddenly realizing someone asked a question and still 'hearing' the tail end to respond. Retrieval is selecting what's noteworthy from sea of fleeting impressions before they vanish.",
        "when_to_store": "continuously and automatically every time sensory input hits receptors - opening eyes, hearing sounds, touching objects. Brain's sensory areas create immediate but fragile record without conscious effort. Only holds recent milliseconds of image or couple seconds of sound before decay. No deliberate memorization needed - just the natural lingering of stimulus traces in sensory registers."
    },
    "short_term_memory": {
        "name": "short_term_memory",
        "description": """Brain's 'mental notepad' powered by prefrontal cortex acting as traffic controller for active information. Limited capacity workspace holding 5-7 items for 15-30 seconds without rehearsal. Used for mental math, remembering phone numbers just long enough to dial, tracking conversation flow. Not just storage but active manipulation space - mixing, comparing, transforming information like calculating 23+47 or formulating sentences while remembering key points. Volatile memory requiring constant refreshing through repetition or focused attention.""",
        "ttl_seconds": 7200,  # Extended for testing - 2 hours instead of 1 hour
        "when_to_retrieve": "by continued use or conscious refocusing on actively held information. Since working memory contains what you're thinking about, retrieval is directing attention back to mental notepad contents. If distracted, items slip away like walking into room and forgetting why. May attempt reconstruction but often information is truly lost unless stored elsewhere. Immediate and conscious access to current cognitive workspace.",
        "when_to_store": "any time actively focusing on information deemed immediately relevant for current goals. Concentration on tasks, thoughts, reading sentences, holding questions in mind triggers active storage. Information stays only as long as maintained through attention. Repetition or 'refreshing' (like silently repeating names) extends duration or helps transfer to long-term storage."
    },
    "episodic_memory": {
        "name": "episodic_memory",
        "description": """Brain's personal diary storing rich 'what-where-when' experiences for mental time travel. Hippocampus acts as memory indexer linking sights, sounds, emotions, places into coherent episodes. Enables re-experiencing past events - recalling birthday parties with room appearance, friends singing, cake taste. Fallible and subjective (two people remember same event differently) but crucial for learning from experience and personal identity construction. Prefrontal cortex organizes information and context for later ordered retrieval.""",
        "ttl_seconds": 604800,  # 1 week - events fade over time
        "when_to_retrieve": "when consciously recalling past experiences (deliberate mental scrapbook access) or involuntarily triggered by environmental cues. Smells, songs, locations can instantly evoke specific memories. Hippocampus and networks reconstruct events by pulling together stored pieces for vivid whole-scene recollection. Sometimes feels like 'mental time travel' - re-living moments. Context-dependent: right cue needed to access relevant past episodes.",
        "when_to_store": "whenever experiencing noteworthy events requiring attention or having significance. Encoding process activated by unusual, important, or emotional happenings. Novelty and emotion are key factors - new experiences or strong feelings get stronger episodic encoding. Routine events often don't 'stick'. Hippocampus rapidly binds event details during experience, then consolidates through reflection or importance assessment for cortical long-term storage."
    },
    "semantic_memory": {
        "name": "semantic_memory",
        "description": """Mental encyclopedia of general knowledge, facts, concepts, and meanings stored across widespread cortical networks in temporal and parietal lobes. Impersonal factual knowledge (Paris is capital of France, zebras have stripes, 2+2=4) detached from specific learning moments. Deals with vocabulary, historical dates, scientific facts, and world knowledge. Temporal-parietal junction especially important for word meanings and factual information. Unlike episodic memory, entries aren't tied to particular time/place - you just 'know' it.""",
        "ttl_seconds": 2592000,  # 30 days - facts persist longer
        "when_to_retrieve": "when recalling general knowledge unconnected to specific personal experiences. Quick conscious query to mental database triggered by questions, conversations requiring word meanings, trivia, explanations. Often automatic when needed - checking internal dictionary for uncommon words, recognizing objects and their properties. Frontal cortex initiates search, temporal lobe areas provide stored knowledge brought to conscious awareness.",
        "when_to_store": "through gradual learning over time via repetition and exposure. School lessons, reading, informative media, life experience building knowledge networks. Unlike episodic single-experience storage, semantic memory forms through multiple exposures until facts become 'obvious'. Brain organizes information into meaning networks, connecting new facts to existing knowledge structures. Solidification occurs through use and conceptual integration."
    },
    "procedural_memory": {
        "name": "procedural_memory",
        "description": """'Muscle memory' storing skills and habits through basal ganglia and cerebellum coordination. Enables automatic performance of learned routines - bike riding, shoe tying, typing, musical instruments - without conscious step-by-step thinking. Implicit memory operating below awareness, difficult to verbalize. Once skills are ingrained through practice, they become unconscious and durable, often lasting years without decay. Brain literally re-wires circuits to optimize task performance through repetition.""",
        "ttl_seconds": 7776000,  # 90 days - skills are stable
        "when_to_retrieve": "when performing learned skills automatically without conscious step-by-step recall. Retrieval embedded in execution - sitting in car triggers driving sequence, holding guitar activates playing routine. Memory directs actions implicitly once cue initiates routine. Conscious interference can actually disrupt automatic performance. Hands 'know' shoe-tying even when verbal description struggles.",
        "when_to_store": "gradually through repetition and practice until movements become smooth and unconscious. Starts with effortful conscious thought (beginner pianist thinking each note), progresses to automatic execution through multiple trials. Cerebellum and basal ganglia fine-tune motions and feedback during practice sessions. Often stored without awareness - suddenly finding you can perform instinctively after sufficient repetition."
    },
    "personalization_memory": {
        "name": "personalization_memory",
        "description": """Ventral medial prefrontal cortex (vmPFC) anchored system integrating personal identity, preferences, and traits from memory blend. Self-reference effect makes self-related information more easily recalled. Contains personal profile elements ('I prefer tea over coffee', 'grew up in Texas') that started as episodes but crystallized into identity markers. Knits together cohesive sense of self and understanding of others' unique characteristics. Dynamic system updating with new experiences and changing preferences.""",
        "ttl_seconds": 31536000,  # 1 year - very stable personal traits
        "when_to_retrieve": "when making choices reflecting personal identity or recalling others' characteristics. Restaurant ordering consults taste preferences, gift-buying retrieves friend's likes. Any situation requiring personal adaptation ('What would I enjoy?', 'What would they prefer?') accesses this knowledge. VmPFC and related networks activate when thinking about self or close others. Autobiographical questioning triggers identity memory compilation.",
        "when_to_store": "through meaningful interactions and experiences shaping identity or revealing preferences. New discoveries ('I love sushi!'), personal milestones ('won award'), learned details about others ('sister's favorite color'). Originates from episodic experiences then distills into general traits. Hippocampus encodes specific incidents, cortex integrates into broader self/other understanding. Updates dynamically with taste changes and new experiences."
    },
    "emotional_memory": {
        "name": "emotional_memory",
        "description": """Amygdala-tagged memory system binding experiences with emotional significance and valence. Emotions act as memory highlighter - intense events become vivid 'flashbulb memories' lasting years. Includes learned emotional reactions (phobias, fondness) and affective associations (cookies-baking warmth, hospital-disinfectant anxiety). Amygdala works with hippocampus during emotional events, releasing stress hormones that strengthen memory encoding. Sensory elements can trigger powerful emotional recall through direct olfactory-amygdala connections.""",
        "ttl_seconds": 2592000,  # 30 days - emotions have lasting impact
        "when_to_retrieve": "when memories with emotional significance are recalled, often re-experiencing original feeling echoes. Sometimes emotion retrieves first - sudden anxiety before conscious memory identification. Environmental cues (songs, smells, contexts) can involuntarily trigger affective memories. Amygdala activation during retrieval can cause physical stress responses. Guides decision-making through 'gut feelings' about past emotional lessons.",
        "when_to_store": "whenever experiencing feelings during events, especially strong emotions signaling importance ('remember this!'). Evolutionary priority for survival-relevant emotional experiences. Amygdala releases neurotransmitters strengthening hippocampal encoding during emotional events. Even mild emotions enhance storage. Forms associations linking sensations with feelings through limbic system connections. Affective significance acts as memory consolidation trigger."
    },
    "social_memory": {
        "name": "social_memory",
        "description": """Specialized memory system for people and relationships utilizing fusiform face area for recognition and hippocampus for distinguishing individuals. Enhanced by oxytocin hormone boosting social encoding and retrieval. Stores faces, voices, names, relationship dynamics, interaction history, and person-specific knowledge. Keeps separate 'friend folders' preventing memory confusion between individuals. Includes emotional coloring (trust levels, likability) via amygdala contribution and contextual details of meetings and conversations.""",
        "ttl_seconds": 7776000,  # 90 days - relationships are relatively stable
        "when_to_retrieve": "when encountering people or thinking about relationships - automatic face/voice recognition triggering identity and relevant facts. Context cues help (high school reunion activates school memories with person). Hippocampus provides episodic details, temporal lobes supply semantic person information. Emotional relevance affects retrieval - loved ones activate warm circuits, difficult people trigger frustration responses.",
        "when_to_store": "when meeting new people or having new interactions adding to person-specific knowledge. First meetings establish initial social memory (face, name, impressions). Subsequent interactions accumulate personality details, preferences, relationship dynamics. Emotional impact and repetition strengthen encoding. Amygdala adds emotional coloring, hippocampus encodes meeting contexts. Oxytocin-enhanced system separates similar individuals and prevents social memory confusion."
    },
    "planning_memory": {
        "name": "planning_memory",
        "description": """Prospective memory system for future intentions and goal achievement utilizing prefrontal cortex for plan formulation and hippocampus for contextual cueing. Brain's internal calendar and GPS combined - remembers what to do, when to do it, and monitors progress. Handles both short-term intentions ('send email after call') and long-term goals ('save for vacation'). Works through conscious strategies (reminders, self-prompts) and unconscious monitoring. Fragile system requiring cues or active checking to trigger timely retrieval.""",
        "ttl_seconds": 1209600,  # 2 weeks - plans need regular updates
        "when_to_retrieve": "when it's time to act on intentions or during agenda review. Time-based goals ideally pop up at right moment ('8 PM - call Mom'). External cues trigger recall (grocery store reminds of milk-buying plan). Active monitoring involves periodic mental to-do list checking. Prefrontal cortex provides monitoring function, hippocampus enables spontaneous contextual recall. System imperfect - retrieval can fail causing 'forgot to mail letter' experiences.",
        "when_to_store": "at moment of intention setting or plan formation. Thinking 'I need to do X later' or 'My goal is Y' encodes prospective memory. Prefrontal cortex encodes intention and strategizes execution. Often supported by external cues, visualization, or environmental aids. Brain may rehearse plans (reinforcing memory) or associate with triggers ('water plants when seeing kitchen light'). Both conscious formulation and unconscious need-arising can create planning memories."
    }
}

# Cache for initialized databases
_memory_instances = {}

def get_memory_db(memory_name: str) -> CreateVectorDB:
    """Get or create a memory database instance with lazy initialization."""
    if memory_name not in _memory_instances:
        if memory_name not in MEMORY_CONFIGS:
            raise ValueError(f"Unknown memory type: {memory_name}")
        
        config = MEMORY_CONFIGS[memory_name]
        _memory_instances[memory_name] = CreateVectorDB(**config)
    
    return _memory_instances[memory_name]

# Create a lazy proxy class that initializes databases on first access
class LazyMemoryDB:
    def __init__(self, memory_name: str):
        self._memory_name = memory_name
        self._instance = None
    
    def _get_instance(self):
        if self._instance is None:
            self._instance = get_memory_db(self._memory_name)
        return self._instance
    
    def __getattr__(self, name):
        # Delegate all attribute access to the actual database instance
        return getattr(self._get_instance(), name)

# Create lazy instances for each memory type
sensory_buffer = LazyMemoryDB("sensory_buffer")
short_term_memory = LazyMemoryDB("short_term_memory")
episodic_memory = LazyMemoryDB("episodic_memory")
semantic_memory = LazyMemoryDB("semantic_memory")
procedural_memory = LazyMemoryDB("procedural_memory")
personalization_memory = LazyMemoryDB("personalization_memory")
emotional_memory = LazyMemoryDB("emotional_memory")
social_memory = LazyMemoryDB("social_memory")
planning_memory = LazyMemoryDB("planning_memory")
