from dataclasses import dataclass


@dataclass
class CanMsg:
    msg: str


@dataclass
class CanOutput:
    msg: str


@dataclass
class CanTemp:
    msg: str
