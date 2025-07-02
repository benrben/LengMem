from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage


class SensoryBufferState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class ShortTermMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class EpisodicMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class SemanticMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class ProceduralMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class PersonalizationMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class EmotionalMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class SocialMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class PlanningMemoryState(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class SearchInMemory(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)


class GetFromMemory(BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list) 