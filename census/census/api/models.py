from typing import Any, Dict, List, Set


class GeographyClauses:
    forClause: str = ""
    inClauses: List[str] = []

    def __init__(self, forClause: str, inClauses: List[str]) -> None:
        self.forClause = forClause
        self.inClauses = inClauses

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def __hash__(self) -> int:
        return self.forClause.__hash__() + sum(
            [item.__hash__() for item in self.inClauses]
        )


class GeographyItem:
    name: str
    hierarchy: str
    clauses: List[GeographyClauses] = []

    def __init__(
        self, name: str, hierarchy: str, clauses: Set[GeographyClauses]
    ) -> None:
        self.name = name
        self.hierarchy = hierarchy
        self.clauses = list(clauses)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def __hash__(self) -> int:
        return (
            self.name.__hash__()
            + self.hierarchy.__hash__()
            + sum([clause.__hash__() for clause in self.clauses])
        )


class GeographyResponseItem:
    name: str
    geoLevelDisplay: str
    referenceData: str
    requires: List[str] = []
    wildcard: List[str] = []
    optionalWithWCFor: str = ""

    def __init__(self, jsonRes: Any) -> None:
        self.__dict__ = jsonRes

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False


class GeographyResponse:
    fips: List[GeographyResponseItem] = []

    def __init__(self, fips: List[dict], **_) -> None:  # type: ignore
        for fip in fips:
            self.fips.append(GeographyResponseItem(fip))  # type: ignore

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False


class Group:
    name: str
    description: str
    variables: str

    def __init__(self, jsonRes: Dict[str, str]) -> None:
        self.__dict__ = jsonRes

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False


class GroupVariable:
    code: str
    groupCode: str
    groupConcept: str
    name: str
    limit: int
    predicateOnly: bool
    predicateType: str

    def __init__(self, code: str, jsonData: dict) -> None:  # type: ignore
        self.code = code
        self.groupCode = jsonData["group"]
        self.groupConcept = jsonData["concept"]
        self.name = jsonData["label"]
        self.limit = jsonData["limit"]
        self.predicateOnly = jsonData["predicateOnly"]
        self.predicateType = jsonData["predicateType"]

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.__dict__ == o.__dict__
        return False
