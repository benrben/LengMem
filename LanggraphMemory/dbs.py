from LanggraphMemory.vectorDB import CreateVectorDB

# Sensory Buffer - Millisecond-level store for raw perceptual input
sensory_buffer = CreateVectorDB(
    name="sensory_buffer", 
    description="Millisecond-level store for raw perceptual input including ASR text, OCR results, telemetry data, and immediate sensor readings. Acts as the first stage of perception before filtering and processing.",
    ttl_seconds=1  # Very short TTL - 1 second
)

# Working / Short-Term Memory - Currently active information during reasoning
short_term_memory = CreateVectorDB(
    name="short_term_memory", 
    description="Actively attended information used during the current reasoning step. Contains conversation context, current task variables, and temporary working data. Lasts seconds to minutes.",
    ttl_seconds=3600  # 1 hour
)

# Episodic Memory - Time-stamped autobiographical events
episodic_memory = CreateVectorDB(
    name="episodic_memory", 
    description="Time-stamped 'what-happened-when' autobiographical events. Stores specific experiences, conversations, and interactions with detailed temporal context and situational details.",
    ttl_seconds=604800  # 1 week - events fade over time
)

# Semantic Memory - Aggregated facts and concepts
semantic_memory = CreateVectorDB(
    name="semantic_memory", 
    description="Aggregated facts, concepts, and general knowledge distilled from many episodes. Contains learned patterns, abstractions, and consolidated understanding independent of specific experiences.",
    ttl_seconds=2592000  # 30 days - facts persist longer
)

# Procedural Memory - Skills and how-to knowledge
procedural_memory = CreateVectorDB(
    name="procedural_memory", 
    description="How-to skills, multistep procedures, and behavioral patterns. Stores learned sequences, habits, and muscle memory for both cognitive and motor tasks.",
    ttl_seconds=7776000  # 90 days - skills are stable
)

# Personalization Memory - Stable user preferences and identity
personalization_memory = CreateVectorDB(
    name="personalization_memory", 
    description="Stable user preferences, identity markers, personal goals, and consistent behavioral patterns. Maintains long-term understanding of individual characteristics and customization settings.",
    ttl_seconds=31536000  # 1 year - very stable personal traits
)

# Emotional / Affective Memory - Emotional associations and valence
emotional_memory = CreateVectorDB(
    name="emotional_memory", 
    description="Stores emotional valence of events, affective associations, and sentiment patterns to guide future responses. Enables empathy, emotional intelligence, and safety through emotional learning.",
    ttl_seconds=2592000  # 30 days - emotions have lasting impact
)

# Social / Relationship Memory - Interpersonal connections and dynamics
social_memory = CreateVectorDB(
    name="social_memory", 
    description="Tracks interpersonal relationships, social dynamics, communication patterns, commitments, and relationship strength. Maintains understanding of who is who and social context.",
    ttl_seconds=7776000  # 90 days - relationships are relatively stable
)

# Planning & Goal Memory - Objectives and strategic planning
planning_memory = CreateVectorDB(
    name="planning_memory", 
    description="Active and long-range objectives, sub-tasks, deadlines, and strategic plans. Maintains goal hierarchies, progress tracking, and future-oriented decision making.",
    ttl_seconds=1209600  # 2 weeks - plans need regular updates
)




